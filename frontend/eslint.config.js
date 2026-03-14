import js from '@eslint/js';
import globals from 'globals';

export default [
  {
    ignores: [
      'node_modules/',
      'dist/',
      'build/',
      'coverage/',
      '*.min.js',
      '../docs/',
      '.vite/',
      '.vite-cache/',
      '.eslintcache',
      'htmlcov/',
      '*.config.js',
    ],
  },
  js.configs.recommended,
  {
    files: ['**/*.{js,jsx}'],
    languageOptions: {
      ecmaVersion: 2024,
      sourceType: 'module',
      globals: {
        ...globals.browser,
        ...globals.es2021,
      },
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
      },
    },
    rules: {
      // React is often imported for consistency in JSX files.
      'no-unused-vars': ['error', { varsIgnorePattern: '^React$' }],
      // ESLint 10-compatible equivalent for fail-fast hook safety in callbacks/conditionals.
      'no-restricted-syntax': [
        'error',
        {
          selector: "CallExpression[callee.name='forEach'] CallExpression[callee.name=/^use[A-Z]/]",
          message: 'Do not call React hooks inside forEach callbacks.',
        },
        {
          selector: "CallExpression[callee.name='map'] CallExpression[callee.name=/^use[A-Z]/]",
          message: 'Do not call React hooks inside map callbacks.',
        },
        {
          selector: "CallExpression[callee.name='reduce'] CallExpression[callee.name=/^use[A-Z]/]",
          message: 'Do not call React hooks inside reduce callbacks.',
        },
        {
          selector: 'IfStatement CallExpression[callee.name=/^use[A-Z]/]',
          message: 'Do not call React hooks conditionally.',
        },
      ],
      // Existing catch-and-wrap patterns in this codebase omit Error.cause.
      'preserve-caught-error': 'off',
    },
  },
];
