const { defineConfig } = require("cypress");
const dotenvPlugin = require('cypress-dotenv');


module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
      config = dotenvPlugin(config)
      return config
    },
    viewportHeight: 1000,
    viewportWidth: 1100,
    baseUrl:'http://127.0.0.1:5000/',
    chromeWebSecurity:false,
    experimentalSessionAndOrigin: true,

  },
});
