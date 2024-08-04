

const path = require('path')

module.exports = {
  mode: 'development',
  entry: '/introduction/introduction/static/js/introduction.js',
  output: {
    filename: 'main.js',
    path: path.resolve(`${__dirname}/introduction/introduction/static/js/`, 'dist')
  },
  module: {
    rules: [
      {
        exclude: /node_modules/
      },
    ],
  },
  watch: true,
}