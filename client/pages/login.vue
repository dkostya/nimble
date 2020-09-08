<template>
<div>

  <hr>
  <b-alert v-if="error" show variant="danger">{{ error + '' }}</b-alert>
  <b-alert show v-if="$auth.$state.redirect">
    You have to login before accessing to <strong>{{ $auth.$state.redirect }}</strong>
  </b-alert>

  <div class="container">
<div class="shadow-lg p-3 mb-5 bg-white rounded">
  <b-row align-h="center" align-v="center">
    <b-col md="4">


        <form @keydown.enter="login">
        <b-form-group label="Имя пользователя:">
          <b-input v-model="username" placeholder="anything" ref="username" />
        </b-form-group>

        <b-form-group label="Пароль:">
          <b-input type="password" v-model="password" placeholder="123" />
        </b-form-group>

        <div class="text-center">
          <b-btn @click="login" variant="primary" block>Войти</b-btn>
        </div>
        </form>

    </b-col>

  </b-row>
  </div>
</div>
</div>
</template>

<style scoped>
.login-button {
  border: 0;
};
</style>

<script>

import busyOverlay from '../components/busy-overlay'

export default {
    head() {
    return {
      title: "Login",

    };
  },

  components: { busyOverlay },

  data() {
    return {
      username: 'admin',
      password: 'admin',
      error: null
    }
  },
  computed: {
    redirect() {
      return (
        this.$route.query.redirect &&
        decodeURIComponent(this.$route.query.redirect)
      )
    },
    isCallback() {
      return Boolean(this.$route.query.callback)
    }
  },
  methods: {
    async login() {
      this.error = null
      return this.$auth
        .loginWith('local', {
          data: {
            username: this.username,
            password: this.password,
          },

        })
        .catch(e => {
          this.error = e + ''
        })
    }
  }
}
</script>
