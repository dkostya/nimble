<template>
  <main class="container my-5">
    <div class="row">


      <div class="col-md-4">
        <form @submit.prevent="submitSource">
          <div class="form-group">
            <label for>Source NAme</label>
            <input type="text" class="form-control"  v-model="source.name">
          </div>
          <div class="form-group">
                <label for>Miface</label>
                <select v-model="source.miface" type="text" class="form-control">
                  <option v-for="iface in ifaces" v-if="iface.iface_ip != '127.0.0.1'">{{iface.iface_ip}}</option>
                </select>

          </div>

          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
            <label for>IP</label>
            <input v-model="source.ip" type="text" class="form-control">

              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  Source port
                </label>
                <input v-model="source.port" type="text" class="form-control" placeholder="1234">
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>source protocol</label>
            <select v-model="source.protocol" class="form-control">
              <option v-for="option in options">{{option.value}}</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "Add Source"
    };
  },
  async asyncData({ $axios, params }) {
  try {
    let ifaces = await $axios.$get(`/ifaces/`);
    return { ifaces };
  } catch (e) {
    return { ifaces: [] };
  }
},
  data() {
    return {
      source: {
        name: "",
        ip: "",
        port: "",
        miface: "",
        protocol: "",
        ifaces: [],


      },
      options: [
        {value: 'udp'},
        {value: 'http'},
        {value: 'rtmp'}
      ],
      preview: ""
    };
  },
  methods: {

    async submitSource() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.source) {
        formData.append(data, this.source[data]);
      }
      try {
        let response = await this.$axios.$post("/sources/", formData, config);
        this.$router.push("/sources/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>
