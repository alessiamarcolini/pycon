import graphene

from django import forms

from decimal import Decimal

from django import forms
from django.utils.translation import ugettext_lazy as _

from graphene_form.forms import FormWithContext

from conferences.models import TicketFare, Ticket, Conference
from conferences.types import TicketType
from orders.models import Order, OrderItem

from .providers.stripe.types import Stripe3DValidationRequired
from .providers.stripe.errors import Stripe3DVerificationError

from .errors import PaymentError
from .fields import CartField
from .types import GenericPaymentError, TicketsPayment


class CommonPaymentItemsForm(FormWithContext):
    items = CartField()
    conference = forms.ModelChoiceField(
        Conference.objects.all(),
        to_field_name='code',
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()

        conference = cleaned_data.get('conference', None)

        if not conference:
            return

        items = cleaned_data.get('items', [])

        if not items:
            raise forms.ValidationError({
                'items': _('The cart is empty')
            })

        total_amount = Decimal(0)

        for item in items:
            item_id = item['id']

            try:
                fare = conference.ticket_fares.get(id=item_id)
            except TicketFare.DoesNotExist:
                raise forms.ValidationError({
                    'items': _('Ticket %(id)s does not exist') % {'id': item_id}
                })

            if not fare.is_available:
                raise forms.ValidationError({
                    'items': _('Ticket %(id)s is not available anymore') % {'id': item_id}
                })

            item['fare'] = fare
            total_amount = total_amount + fare.price * item['quantity']

        cleaned_data['items'] = items
        cleaned_data['total_amount'] = total_amount

        return cleaned_data

    def create_order(self, provider):
        user = self.context.user

        total_amount = self.cleaned_data.get('total_amount')

        order = Order(
            user=user,
            provider=provider,
            amount=total_amount
        )

        return order

    def save_order(self, order):
        items = self.cleaned_data.get('items')

        order.save()

        # todo: improve
        for item in items:
            OrderItem.objects.create(
                order=order,
                description=item['fare'].order_description,
                unit_price=item['fare'].price,
                quantity=item['quantity']
            )


class BuyTicketWithStripeForm(CommonPaymentItemsForm):
    payment_method_id = forms.CharField(required=False)
    payment_intent_id = forms.CharField(required=False)

    def save(self):
        order = self.create_order('stripe')

        payload = {
            'payment_method_id': self.cleaned_data.get('payment_method_id', None),
            'payment_intent_id': self.cleaned_data.get('payment_intent_id', None),
        }

        try:
            order.charge(payload)
        except Stripe3DVerificationError as e:
            return Stripe3DValidationRequired(client_secret=e.client_secret)
        except PaymentError as e:
            return GenericPaymentError(message=e.message)

        self.save_order(order)

        tickets = []

        # Payment confirmed
        # Creating the tickets here

        for item in self.cleaned_data.get('items'):
            fare = item['fare']

            for _ in range(0, item['quantity']):
                tickets.append(
                    Ticket.objects.create(
                        user=self.context.user,
                        ticket_fare=fare,
                        order=order
                    )
                )

        return TicketsPayment(
            tickets=tickets,
            order=order
        )
