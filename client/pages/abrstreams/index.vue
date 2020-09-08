<template>
  <div>

<div class="container">
  <div class="shadow-lg p-3 mb-5 bg-white rounded" style="height: 700px">
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              aria-controls="abrstreams-table"
              size="sm"
          ></b-pagination>
        </div>
        <div style="margin-right: 20px">
          <nuxt-link to="/abrstreams/add" class="btn btn-sm btn-primary" style="width: 103px;">Добавить</nuxt-link>
          <button type="button" class="btn btn-sm btn-primary" @click="refreshData" style="width: 103px;">Обновить</button>
        </div>
     </div>
    </div>

        <b-table id="abrstreams-table" :items="abrstreams" :per-page="perPage" :current-page="currentPage" :fields="fields">

              <template slot="stream" slot-scope="item">
                /{{item.item.app}}/{{item.item.stream}}
              </template>

              <template slot="streams" slot-scope="item">
                <li  v-for="abrsource in item.item.streams">
                      /{{abrsource.app}}/{{abrsource.stream}}
                    </li>

              </template>

              <template slot="actions" slot-scope="item">
                       <nuxt-link :to="`/abrstreams/${item.item.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
                       <button @click="deleteAbrstream(item.item.id)"  class="btn btn-sm btn-danger">Delete</button>
              </template>
        </b-table>

      </div>

     </div>

</div>

</template>
<script>


export default {
  head() {
    return {
      title: "ABR Streams list",

    };
  },
  components: {},

  async asyncData({ $axios, params }) {
    // Получаем список объектов для отображения на странице
    try {
      let abrstreams = await $axios.$get(`/abrstreams/`);
      return { abrstreams };
    } catch (e) {
      return { abrstreams: [] };
    }
  },

  data() {
    return {
      abrstreams: [],
      perPage: 10,
      currentPage: 1,
      interval: null,
      fields: {
        id:{
          label: '#',
          sortable: true
        },
        stream:{
          label: 'Исходящий поток',
          sortable: true
        },
        streams:{
          label: 'Профили',
        },
        actions:{
          label: 'Действия',
        },
      }
    };
  },

  computed: {
    rows(){
      return this.abrstreams.length
    },
  },

  //created () {
  //  // Создаю таймер для выполнения периодической задачи
  //  this.interval = setInterval(this.refreshData, 5000)
  //},
  //beforeDestroy () {
  //  // Убиваю таймер по выходу со страницы
  //  clearInterval(this.interval)
  //  },

  methods: {
    async refreshData () {
      // Обновление данных
      try {
        let updatedAbrstreams = await this.$axios.$get("/abrstreams/");
        this.abrstreams = updatedAbrstreams;
      } catch (e) {
        console.log(e);
      }
    },

    async deleteAbrstream(abrstream_id) {
      // Удаляю объект и затем запрашиваю актуальный список объектов
      if (confirm('Вы уверены?')){
          try {
            await this.$axios.$delete(`/abrstreams/${abrstream_id}/`);
            let newAbrstreams = await this.$axios.$get("/abrstreams/");
            this.abrstreams = newAbrstreams;
          } catch (e) {
            console.log(e);
          }
      }
    },
  }
};
</script>

<style>

</style>
