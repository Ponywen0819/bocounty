const path = require("path");

module.exports = {
  entry: "./src/jsx/enter_point.jsx",
  mode: "development",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "src/js"),
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [["@babel/preset-react", { targets: "defaults" }]],
          },
        },
      },
    ],
  },
};
