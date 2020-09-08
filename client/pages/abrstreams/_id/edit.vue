<template>

  <main class="container my-5">
    <div class="row">


      <div class="col-md-4">
        <form @submit.prevent="submitAbrstream">
          <div class="row">
            <div class="col">
            <label for>ABR App name</label>
            <input type="text" class="form-control"  v-model="abrstream.app">
              </div>
            <div class="col">
            <label for>ABR Stream name</label>
            <input type="text" class="form-control"  v-model="abrstream.stream">
            </div>
          </div>

              <div class="row">
                <label for>Streams</label>
                </div>
          <div class="row">
            <div class="col">
            <label for>App</label>
              <select type="text" class="form-control"  v-model="selected_streams.app">
                <option v-for="stream in source_streams">{{stream.app}}</option>
              </select>
          </div>
            <div class="col">
            <label for>Stream</label>
              <select type="text" class="form-control"  v-model="selected_streams.stream">
                <option v-for="stream in source_streams">{{stream.stream}}</option>
              </select>
          </div>
            <div class="row">
              <div >
                <button class="btn btn-primary" type="button" v-on:click="streamAdd">Add</button>
              </div>
            </div>


          </div>
          <div>
            <ul class="list-group list-group-flush" v-for="item in selected_streams">
              <li class="list-group-item">
                /{{item.app}}/{{item.stream}}
              </li>
            </ul>
          </div>
          <div>
          <button type="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
      </div>
    </div>
  </main>

</template>
<script>
export default {
  head() {
    return {
      title: "Edit AbrStream"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let abrstream = await $axios.$get(`/abrstreams/${params.id}`);
      let source_streams = await $axios.$get(`/streams/`);
      return { source_streams, abrstream };
    } catch (e) {
      return { source_streams: [], abrstream: [] };
    }
  },
  data() {
    return {
      abrstream: {
        app: "",
        stream: "",
        order: "desc",
        streams: [],
      },
      selected_streams: [],
      source_streams: []
    };
  },

  methods: {
    streamAdd: function(){
    this.selected_streams.push({app: this.selected_streams.app, stream: this.selected_streams.stream});

    },
    async submitAbrstream() {
      const config = {
        headers: { "content-type": "application/json" }
      };


      this.abrstream.streams = this.selected_streams;

      let formData = new FormData();
      for (let data in this.$data.abrstream) {
        formData.append(data, this.$data.abrstream[data]);
      }

      let object = {};

      formData.forEach((value, key) => {object[key] = value});

      object.streams = [];
      object.streams = this.abrstream.streams;
      let json = JSON.stringify(object);

      try {
        let response = await this.$axios.$patch(`/abrstreams/${this.abrstream.id}/`, json, config);
        console.log(response);
        this.$router.push("/abrstreams/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>
