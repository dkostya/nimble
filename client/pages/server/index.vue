<template>
  <div class="container">
    <div class="shadow-lg p-3 mb-5 bg-white rounded" style="height: 700px">
    <div class="container">
      <div class="row">
        <div class="col-sm">

        </div>
        <div style="margin-right: 20px">
          <button type="button" class="btn btn-sm btn-primary " @click="refreshData" style="width: 103px;">Обновить</button>
        </div>
     </div>
    </div>
       <template v-for="server in servers">
                        <server-card :server="server"></server-card>
       </template>
    </div>

  </div>
</template>

<script>
  import ServerCard from "../../components/ServerCard";
  export default {
    head() {
      return {
        title: "Сервер",
      }
    },
    name: "server",
    components: {ServerCard},
    async asyncData({$axios, params}) {
      try {
        let servers = await $axios.$get(`/server/`);
        return {servers};
      } catch (e) {
        return {servers: []};
      }
    },

    data(){
      return {
        servers:[]
      }
    },


    methods: {
      async refreshData() {
        // Обновление данных
        try {
          let updatedServers = await this.$axios.$get("/server/");
          this.servers = updatedServers;
        } catch (e) {
          console.log(e);
        }
      },
    }
  }
</script>

<style scoped>

</style>
