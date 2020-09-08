<template>
<div>
      <div class="container" @submit.prevent="submitRtmpsettings">
        <div class="shadow-lg p-3 mb-5 bg-white rounded">
                    <form class="list-group">

<!--
                      <li class="list-group-item"><input v-model="rtmpsettings.interfaces">interfaces</li>
                      <li class="list-group-item"><input v-model="rtmpsettings.login">login</li>
                      <li class="list-group-item"><input v-model="rtmpsettings.password">password</li>
-->
                      <div class="row">
                      <span class="list-group-item"><input v-model="rtmpsettings.duration"> Chunk Duration</span>
                      <span class="list-group-item"><input v-model="rtmpsettings.chunk_count"> Chunk Count</span>
                        </div>

<!--
                      <li class="list-group-item"><input v-model="rtmpsettings.dash_template">dash_template</li>
-->
                      <div class="row">
                        <label for="select_prtcls">Protocols</label>
                      <select id="select_prtcls" multiple class="form-control" name="protocol" v-model="rtmpsettings.protocols">
                        <option  v-for="obj in protocols_choices">{{obj.protocol}}</option>

                      </select>
                        </div>

<!--
                      <li class="list-group-item"><input v-model="rtmpsettings.apps">apps</li>
                      <li class="list-group-item"><input v-model="rtmpsettings.abr">abr</li>
-->
                       <button type="submit" class="btn btn-success">Save</button>

                    </form>
        </div>


      </div>
</div>
</template>

<script>

import Index from "../streams/_id/index";
export default {
  components: {Index},
  head(){
      return {
        title: "Edit Settings"
      }
    },
  async asyncData({ $axios, params }) {
    try {
      let rtmpsettings = await $axios.$get(`/rtmpsettings/1`);
      let protocols_choices = await $axios.$get(`/protocols/`);
      return {rtmpsettings: rtmpsettings, protocols_choices: protocols_choices};
    } catch (e) {
      return {rtmpsettings: [], protocols_choices: []};
    }
  },



  data() {
    return {
      rtmpsettings: {
        interfaces: "",
        login: "",
        password: "",
        duration: "",
        chunk_count: [],
        dash_template: "",
        protocols: [],
        apps: "",
        abr: "",

      },

      selected_protocol: [],


    };
  },
  methods: {
    async submitRtmpsettings() {

      let editedRtmpsettings = this.rtmpsettings;
      let selectedProtocol = this.rtmpsettings.protocols;


      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();

      for (let data in editedRtmpsettings) {
        formData.append(data, editedRtmpsettings[data]);
      }
      formData.delete('protocols');
      for (let data in selectedProtocol) {
        formData.append('protocols', selectedProtocol[data]);
      }




      try {
        let response = await this.$axios.$put(`/rtmpsettings/1/`, formData, config);
        this.$router.push("/rtmpsettings/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>


<style scoped>

</style>
