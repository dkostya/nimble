<template v-if="$auth.$state.loggedIn">
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
              aria-controls="source-table"
              size="sm"
          ></b-pagination>
        </div>
        <div style="margin-right: 20px">
          <nuxt-link to="/sources/add" class="btn btn-sm btn-primary" style="width: 103px;">Добавить</nuxt-link>
          <button type="button" class="btn btn-sm btn-primary" @click="refreshData" style="width: 103px;">Обновить</button>
        </div>
     </div>
    </div>

        <b-table id="source-table" :items="sources" :per-page="perPage" :current-page="currentPage" :fields="fields">

              <template slot="stream" slot-scope="item">
                {{item.item.ip}}:{{item.item.port}}
              </template>

              <template slot="status" slot-scope="item">
                <div v-if="item.item.status"><span class="badge badge-success">online</span></div>
                <div v-else><span class="badge badge-danger">offline</span></div>
              </template>

              <template slot="bitrate" slot-scope="item">
                {{item.item.bitrate}} Mbps
              </template>

              <template slot="actions" slot-scope="item">
                <nuxt-link :to="`/sources/${item.item.id}/edit/`" class="btn btn-sm btn-primary">Править</nuxt-link>
                       <button @click="deleteSource(item.item.id)"  class="btn btn-sm btn-danger">Удалить</button>
              </template>
        </b-table>

      </div>

     </div>

</div>

</template>
<script>

import SourceCard from "../../components/SourceCard";

export default {

  head() {
    return {
      title: "Источники",

    };
  },
  components: {
    SourceCard,
  },

  async asyncData({ $axios, params }) {
    // Получаем список объектов для отображения на странице
    try {
      let sources = await $axios.$get(`/sources/`);
      return { sources };
    } catch (e) {
      return { sources: [] };
    }
  },

  data() {
    return {
      sources: [],
      perPage: 10,
      currentPage: 1,
      interval: null,
      fields: {
        id:{
          label: '#',
          sortable: true
        },
        name:{
          label: 'Имя потока'
        },
        status:{
          label: 'Статус',
          sortable: true
        },
        bitrate:{
          label: 'Битрейт',
          sortable: true
        },
        stream:{label: 'URL'},
        miface:{label: 'Интерфейс'},
        protocol:{label: 'Протокол'},
        actions:{label: 'Действия'},
        //show_details: {label: "Детали"}
      }
    };
  },

  computed: {
    rows(){
      return this.sources.length
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
        let updatedSources = await this.$axios.$get("/sources/");
        this.sources = updatedSources;
      } catch (e) {
        console.log(e);
      }
    },

    async deleteSource(source_id) {
      // Удаляю объект и затем запрашиваю актуальный список объектов
      if (confirm('Вы уверены?')) {
          try {
            await this.$axios.$delete(`/sources/${source_id}/`);
            let newSources = await this.$axios.$get("/sources/");
            this.sources = newSources;
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
