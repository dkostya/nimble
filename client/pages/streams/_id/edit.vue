<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitStream">
          <div class="form-group">
            <label for>Stream Video</label>
            <select type="text" class="form-control"  v-model="stream.video">
              <option v-for="obj in sources" v-bind:value="obj.name">{{obj.name}} - {{obj.ip}}:{{obj.port}}</option>
            </select>
          </div>
          <div class="form-group">
            <label for>Video PID</label>
            <input type="text" v-model="stream.vpid" class="form-control" >
          </div>
          <div class="form-group">
            <label for>Stream Audio</label>
            <select type="text" class="form-control"  v-model="stream.audio">
              <option v-for="obj in sources" v-bind:value="obj.name">{{obj.name}} - {{obj.ip}}:{{obj.port}}</option>
            </select>
          </div>
          <div class="form-group">
            <label for>Stream Apid</label>
            <input type="text" v-model="stream.apid" class="form-control"  >
          </div>
          <div class="form-group">
            <label for>Stream App</label>
            <input type="text" v-model="stream.app" class="form-control"  >
          </div>
          <div class="form-group">
            <label for>Stream</label>
            <input type="text" v-model="stream.stream" class="form-control"  >
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
        title: "Edit Stream"
      }
    },
  async asyncData({ $axios, params }) {
    try {
      let stream = await $axios.$get(`/streams/${params.id}`);
      let sources = await $axios.$get(`/sources/`);
      return { stream: stream, sources };
    } catch (e) {
      return { stream: [], sources: [] };
    }
  },
  data() {
    return {
      stream: {
        video: "",
        audio: "",
        apid: "",
        vpid: "",
        name: "",
        stream: "",
        sources: []
      },

    };
  },
  methods: {
    async submitStream() {
      let editedStream = this.stream;
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedStream) {
        formData.append(data, editedStream[data]);
      }
      try {
        let response = await this.$axios.$patch(`/streams/${editedStream.id}/`, formData, config);
        this.$router.push("/streams/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
