module.exports = {
  entry: "./client/App.js",
  output: {
    filename: "client/static/bundle.js"
  },
  module: {
    loaders: [
      {test: /\.js$/, loader: 'jsx-loader'}
    ]
  }
};
