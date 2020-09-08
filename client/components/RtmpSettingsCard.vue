<template>
      <div class="container">
            <div class="shadow-lg p-3 mb-5 bg-white rounded" style="height: 700px">
                    <ul class="list-group">

<!--
                      <li class="list-group-item">{{rtmpsetting.interfaces}}</li>
                      <li class="list-group-item">{{rtmpsetting.login}}</li>
                      <li class="list-group-item">{{rtmpsetting.password}}</li>
-->

                      <a>{{rtmpsetting.duration}}</a>
                      <a >{{rtmpsetting.chunk_count}}</a>
                      <a >{{rtmpsetting.dash_template}}</a>

                      <div class="row">
                        <div class="container">
                          <a>Протоколы вещания:</a>
                          <span class="badge badge-primary" style="margin-left: 5px" v-for="protocol in rtmpsetting.protocols">{{ protocol }}</span>
                          </div>
                      </div>
<!--
                      <li class="list-group-item">{{rtmpsetting.apps}}</li>
                      <li class="list-group-item">{{rtmpsetting.abr}}</li>
-->
                    </ul>

        <nuxt-link to="/rtmpsettings/edit" class="btn btn-sm btn-primary">Edit Settings</nuxt-link>
             </div>
       </div>

</template>
<script>
export default {
  props: ["rtmpsetting"],
};
</script>
<style>
</style>
