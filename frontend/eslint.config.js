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
      // Existing catch-and-wrap patterns in this codebase omit Error.cause.
      'preserve-caught-error': 'off',
    },
  },
];
