
<template >

<div>
<template>
<div class="container">
  <b-navbar class="shadow-lg  mb-2 bg-white navbar-fixed-top" style="height: 70px; margin-top: 5px" toggleable="lg" type="light" variant="light" >
    <b-navbar-brand href="#"><img src="/SSE.png" style="width: 100px; margin-bottom: 5px; margin-left: 10px"></b-navbar-brand>
    <i style="margin-top: 0px">v1.0</i>


    <b-collapse id="nav-collapse" is-nav >
<template v-if="$auth.$state.loggedIn">
      <b-navbar-nav   align="center">

        <b-nav-item  class="nav-link" :to="`/server/`">Сервер</b-nav-item>
        <b-nav-item  class="nav-link" :to="`/sources/`">Источники</b-nav-item>
        <b-nav-item  class="nav-link" :to="`/streams/`">Потоки</b-nav-item>
        <b-nav-item  class="nav-link" :to="`/abrstreams/`">ABR</b-nav-item>
        <b-nav-item  class="nav-link" :to="`/rtmpsettings/`">Настройки</b-nav-item>




      </b-navbar-nav>

      <b-button v-if="$auth.$state.loggedIn" variant="primary"  @click="writeConfig" style="margin-top: 2px">Записать конфигурацию</b-button>
</template>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">


          <template v-if="$auth.$state.loggedIn">
            <b-nav-item-dropdown right class="nav-link" :text="$auth.user" right>
              <b-dropdown-item @click="$auth.logout()">Выйти</b-dropdown-item>
            </b-nav-item-dropdown>

          </template>

      </b-navbar-nav>

    </b-collapse>


  </b-navbar>
</div>
</template>

 <nuxt/>
</div>




</template>

<style>

</style>
<script>

  import BNav from "bootstrap-vue/src/components/nav/nav";
  import BNavItem from "bootstrap-vue/src/components/nav/nav-item";
  export default {
    props: ['refreshData'],
    components: {BNavItem, BNav},

    methods: {
      async writeConfig() {
        const write = await this.$axios.$get('/write_config/')
          .then((response) => {
            alert("Конфигурация сохранена");
          }).catch((error) => {
            alert("Error")
          });
        this.write = write
      },

    }
  }
</script>
