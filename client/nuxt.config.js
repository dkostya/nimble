import pkg from './package'

export default {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],

  /*
  ** Nuxt.js modules Token
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org/docs/
    'bootstrap-vue/nuxt',
    '@nuxtjs/auth',
    '@nuxtjs/axios'
  ],
  axios: {
    baseURL: "http://192.168.1.247/panel/api/"
  },

  router: {
    middleware: ['auth']
  },

  auth: {
    redirect:{
      login: '/login',
      logout: '/login',
      home: '/server'
    },

    strategies: {
      local: {
        endpoints: {
          login: {url: '/rest-auth/login/', method: 'post', propertyName: 'key'},
          logout: {url: '/rest-auth/logout/', method: 'post'},
          user: { url: '/rest-auth/user/', method: 'get', propertyName: 'username' },
        },
        tokenRequired: true,
        tokenType: 'Token',
        localStorage: {
          prefix: 'auth.'
          }
      },
    }
  },


  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
