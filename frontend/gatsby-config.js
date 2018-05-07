const rupture = require("rupture");
const nib = require("nib");

module.exports = {
  siteMetadata: {
    title: 'Eastcoin',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    {
      resolve: "gatsby-plugin-stylus",
      options: {
        use: [nib(), rupture()],
      },
    },
  ],
};
