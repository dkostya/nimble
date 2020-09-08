<template>
<div class="row">


  <div class="shadow-lg p-3 mb-5 bg-white rounded" style="margin-left: 10px; width: 280px">
      <b-list-group>
          <b-list-group-item class="d-flex justify-content-between align-items-center">
          Сервер:
          <b-badge variant="primary" >{{server.servername}}</b-badge>
        </b-list-group-item>
        <b-list-group-item class="d-flex justify-content-between align-items-center">
          Подключений:
          <b-badge variant="primary" pill>{{server.connection}}</b-badge>
        </b-list-group-item>

        <b-list-group-item class="d-flex justify-content-between align-items-center">
          Битрейт:
          <b-badge variant="primary" pill>{{server.outrate}}</b-badge>
        </b-list-group-item>

        <b-list-group-item class="d-flex justify-content-between align-items-center">
          Процессоры:
          <b-badge variant="primary" pill>{{server.ap}}</b-badge>
        </b-list-group-item>

      </b-list-group>

  </div>


  <div class="shadow-lg p-3 mb-5 bg-white rounded" style="margin-left: 10px; width: 280px">
    <h5>Ресурсы</h5>
    <div>
    <p>Память</p>
    <b-progress :max="max_mem" >
      <b-progress-bar :value="value_mem">
        {{value_mem}}/{{max_mem}}
      </b-progress-bar>
    </b-progress>
     </div>
    <p class="mt-3">Процессор</p>
    <b-progress :max="max_cpu" >
      <b-progress-bar :value="value_cpu">
        {{value_cpu}}/{{max_cpu}}
      </b-progress-bar>
    </b-progress>
    <p class="mt-3">SWAP</p>
    <b-progress :max="max_swap">
      <b-progress-bar :value="value_swap">
        {{value_swap}}/{{max_swap}}
      </b-progress-bar>
    </b-progress>

  </div>



</div>
</template>

<script>
    export default {
      name: "ServerCard",
      props: ["server"],


      data(){
        return{
          value_mem: (this.server.tpms - this.server.fpms),
          max_mem: this.server.tpms,
          value_cpu: this.server.scl,
          max_cpu: 100,
          value_swap: (this.server.tsss - this.server.fsss),
          max_swap: this.server.tsss,
        }
      },
    }
</script>

<style scoped>

</style>


<style>
</style>
