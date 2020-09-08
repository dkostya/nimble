<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitSource">
          <div class="form-group">
            <label for>Source Name</label>
            <input type="text" class="form-control" v-model="source.name" >
          </div>
          <div class="form-group">
            <label for>Source IP</label>
            <input type="text" v-model="source.ip" class="form-control" >
          </div>
          <div class="form-group">
            <label for>Source port</label>
            <input type="text" v-model="source.port" class="form-control"  >
          </div>
          <div>
            <select v-model="source.protocol" class="form-control">
              <option v-for="option in options">{{option.value}}</option>
            </select>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Miface</label>
                <select v-model="source.miface" type="text" class="form-control">
                  <option v-for="iface in ifaces">{{iface.iface_ip}}</option>
                </select>
              </div>
            </div>
          </div>

          <button type="submit" class="btn btn-success">Save</button>
        </form>
      </div>
    </div>



  </main>

</template>
<script>
export default {
  head(){
      return {
        title: "Edit Source"
      }
    },
  async asyncData({ $axios, params }) {
    try {
      let source = await $axios.$get(`/sources/${params.id}`);
      let ifaces = await $axios.$get(`/ifaces/`);
      return {source: source, ifaces: ifaces};
    } catch (e) {
      return {source: [], ifaces: []};
    }
  },



  data() {
    return {
      source: {
        name: "",
        ip: "",
        miface: "",
        port: "",
        ifaces: [],
      },
      options: [
        {value: 'udp'},
        {value: 'http'},
        {value: 'rtmp'}
      ],

    };
  },
  methods: {
    async submitSource() {
      let editedSource = this.source;
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedSource) {
        formData.append(data, editedSource[data]);
      }
      try {
        let response = await this.$axios.$patch(`/sources/${editedSource.id}/`, formData, config);
        this.$router.push("/sources/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
