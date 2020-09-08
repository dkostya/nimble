<template>
  <main class="container my-5">
    <div class="row">


      <div class="col-md-4">
        <form @submit.prevent="submitStream">
          <div class="form-group">
            <label for>Stream Video</label>
            <select type="text" class="form-control"  v-model="stream.video">
              <option v-for="obj in sources" v-bind:value="obj.name">{{obj.name}}-{{obj.ip}}:{{obj.port}}</option>
            </select>
          </div>
          <div class="form-group">
            <label for>Stream Audio</label>
            <select  type="text" class="form-control" v-model="stream.audio">
              <option v-for="obj in sources" v-model="obj.name" v-bind:value="obj.name">{{obj.name}}-{{obj.ip}}:{{obj.port}}</option>
            </select>
          </div>
          <div class="form-group">
            <label for>stream.vpid</label>
            <input  type="text" class="form-control" v-model="stream.vpid">
          </div>
          <div class="form-group">
            <label for>stream.apid</label>
            <input  type="text" class="form-control" v-model="stream.apid">
          </div>
          <div class="form-group">
            <label for>stream.app</label>
            <input  type="text" class="form-control" v-model="stream.app" placeholder="live">
          </div>
          <div class="form-group">
            <label for>stream.stream</label>
            <input  type="text" class="form-control" v-model="stream.stream">
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
      title: "Add Stream"
    };
  },
  async asyncData({ $axios, params }) {
  try {
    let sources = await $axios.$get(`/sources/`);
    return { sources };
  } catch (e) {
    return { sources: [] };
  }
},
  data() {
    return {
      stream: {
        audio: [],
        video: [],
        vpid: "",
        apid: "",
        app: "",
        stream: "",


      },
      sources: [],
      preview: ""
    };
  },
  methods: {

    async submitStream() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.stream) {
        formData.append(data, this.stream[data]);
      }
      try {
        let response = await this.$axios.$post("/streams/", formData, config);
        this.$router.push("/streams/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>
