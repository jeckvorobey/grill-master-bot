module.exports = {
  tabWidth: 2,
  jsxSingleQuote: true,
  printWidth: 100,
  singleQuote: true,
  trailingComma: 'none',
  proseWrap: 'always',
  semi: false,
  overrides: [
    {
      files: '*.json',
      options: {
        printWidth: 200
      }
    }
  ]
}
