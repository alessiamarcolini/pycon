const path = require("path");

module.exports = {
    env: {
        browser: true,
        es6: true,
        node: true,
    },
    extends: [],
    rules: {
        "prettier/prettier": "error",
        "@typescript-eslint/adjacent-overload-signatures": "error",
        "@typescript-eslint/array-type": "error",
        "@typescript-eslint/ban-types": "error",
        "@typescript-eslint/class-name-casing": "error",
        "@typescript-eslint/explicit-member-accessibility": [
            "off",
            {
                overrides: {
                    constructors: "off",
                },
            },
        ],
        "@typescript-eslint/indent": "off",
        "@typescript-eslint/interface-name-prefix": "off",
        "@typescript-eslint/member-delimiter-style": "off",
        "@typescript-eslint/member-ordering": "off",
        "@typescript-eslint/no-angle-bracket-type-assertion": "error",
        "@typescript-eslint/no-empty-interface": "error",
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-misused-new": "error",
        "@typescript-eslint/no-namespace": "error",
        "@typescript-eslint/no-object-literal-type-assertion": "error",
        "@typescript-eslint/no-parameter-properties": "off",
        "@typescript-eslint/no-this-alias": "error",
        "@typescript-eslint/no-triple-slash-reference": "error",
        "@typescript-eslint/no-use-before-declare": "off",
        "@typescript-eslint/no-var-requires": "error",
        "@typescript-eslint/prefer-for-of": "error",
        "@typescript-eslint/prefer-function-type": "error",
        "@typescript-eslint/prefer-interface": "off",
        "@typescript-eslint/prefer-namespace-keyword": "error",
        "@typescript-eslint/type-annotation-spacing": "off",
        "@typescript-eslint/unified-signatures": "error",
        "arrow-body-style": "error",
        "arrow-parens": ["off", "as-needed"],
        complexity: "off",
        "constructor-super": "error",
        curly: "error",
        "dot-notation": "error",
        "eol-last": "off",
        "guard-for-in": "error",
        "linebreak-style": "off",
        "max-classes-per-file": ["error", 1],
        "new-parens": "off",
        "newline-per-chained-call": "off",
        "no-bitwise": "error",
        "no-caller": "error",
        "no-cond-assign": "error",
        "no-console": "off",
        "no-debugger": "error",
        "no-duplicate-case": "error",
        "no-empty": "error",
        "no-empty-function": "error",
        "no-eval": "error",
        "no-extra-bind": "error",
        "no-extra-semi": "off",
        "no-fallthrough": "off",
        "no-invalid-this": "off",
        "no-irregular-whitespace": "off",
        "no-multiple-empty-lines": "off",
        "no-new-func": "error",
        "no-new-wrappers": "error",
        "no-return-await": "error",
        "no-sequences": "error",
        "no-sparse-arrays": "error",
        "no-template-curly-in-string": "error",
        "no-throw-literal": "error",
        "no-undef-init": "error",
        "no-unsafe-finally": "error",
        "no-unused-labels": "error",
        "no-var": "error",
        "object-shorthand": "error",
        "one-var": "off",
        "prefer-const": "error",
        "prefer-object-spread": "error",
        "quote-props": "off",
        radix: "error",
        "space-before-function-paren": "off",
        "use-isnan": "error",
        "valid-typeof": "off",
        "@typescript-eslint/tslint/config": [
            "error",
            {
                rulesDirectory: [
                    path.join(__dirname, "node_modules/tslint-react/rules"),
                ],
                rules: {
                    "comment-format": [true, "check-space"],
                    "jsdoc-format": [true, "check-multiline-start"],
                    "jsx-boolean-value": true,
                    "jsx-key": true,
                    "jsx-no-bind": true,
                    "jsx-no-string-ref": true,
                    "jsx-self-close": true,
                    "no-duplicate-imports": true,
                    "no-duplicate-variable": [true, "check-parameters"],
                    "no-implicit-dependencies": true,
                    "no-reference-import": true,
                    "no-shadowed-variable": true,
                    "no-unused-expression": true,
                    "only-arrow-functions": [
                        true,
                        "allow-declarations",
                        "allow-named-functions",
                    ],
                    "ordered-imports": [
                        true,
                        {
                            "grouped-imports": true,
                            groups: ["^react"],
                        },
                    ],
                    "prefer-conditional-expression": true,
                    quotemark: [true, "double", "jsx-double"],
                    semicolon: [true, "always"],
                    "triple-equals": [true, "allow-null-check"],
                    "variable-name": [
                        true,
                        "ban-keywords",
                        "check-format",
                        "allow-pascal-case",
                    ],
                },
            },
        ],
    },
    globals: {
        Atomics: "readonly",
        SharedArrayBuffer: "readonly",
    },
    parser: "@typescript-eslint/parser",
    parserOptions: {
        project: path.join(__dirname, "tsconfig.json"),
        sourceType: "module",
    },
    plugins: ["prettier", "@typescript-eslint", "@typescript-eslint/tslint"],
    settings: {},
};
