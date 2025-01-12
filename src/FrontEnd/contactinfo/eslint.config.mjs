// @ts-check
export default [
    {
        ignores: ['**/build/*']
    },
    {
        rules: {
            'quotes': ['error', 'single'],
            'max-len': [
                'error',
                {
                    code: 120,
                    tabWidth: 4,
                    ignoreUrls: true,
                    ignoreStrings: true,
                    ignoreTemplateLiterals: true,
                },
            ],
            'indent': ['error', 4]
        }
    }
];