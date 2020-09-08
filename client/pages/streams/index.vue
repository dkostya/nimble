<template>
  <div>

<div class="container">
  <div class="shadow-lg p-3 mb-5 bg-white rounded" style="min-height: 700px;">
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              aria-controls="stream-table"
              size="sm"
          ></b-pagination>
        </div>
        <div div style="margin-right: 20px">
          <nuxt-link to="/streams/add" class="btn btn-sm btn-primary" style="width: 103px;">Добавить</nuxt-link>
          <button type="button" class="btn btn-sm btn-primary" @click="refreshData" style="width: 103px;">Обновить</button>
        </div>
     </div>
    </div>

        <b-table id="stream-table" :items="streams" :per-page="perPage" :current-page="currentPage" :fields="fields">

              <template slot="app" slot-scope="item">
                /{{item.item.app}}/{{item.item.stream}}
              </template>

              <template slot="actions" slot-scope="item">
                <nuxt-link :to="`/streams/${item.item.id}/edit/`" class="btn btn-sm btn-primary"> Править </nuxt-link>
                <button @click="deleteStream(item.item.id)"  class="btn btn-sm btn-danger">Удалить</button>
              </template>

                <template slot="show_details" slot-scope="row">
                  <b-button variant="secondary" size="sm" @click="row.toggleDetails" class="mr-2" style="width: 77px">
                    {{ row.detailsShowing ? 'Скрыть' : 'Показать'}}
                    </b-button>
                </template>



                 <template slot="row-details" slot-scope="item">
                  <b-card>

                    <div v-for="iface in ifaces" v-if="iface.iface_ip != '127.0.0.1'">
                      http://{{iface.iface_ip}}:8081/{{item.item.app}}/{{item.item.stream}}/playlist.m3u8
                    </div>

                  </b-card>
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
      title: "Исходящие потоки",

    };
  },
  components: {
    SourceCard,
  },

  async asyncData({ $axios, params }) {
    // Получаем список объектов для отображения на странице
    try {
      let streams = await $axios.$get(`/streams/`);
      let ifaces = await $axios.$get('/ifaces/');
      return { streams, ifaces };
    } catch (e) {
      return { streams: [], ifaces: [] };
    }
  },

  data() {
    return {
      streams: [],
      ifaces: [],
      perPage: 10,
      currentPage: 1,
      interval: null,
      fields: {
        id:{label: '#'},
        video:{label: 'Видео'},
        audio:{label: 'Аудио'},
        vpid:{label: 'PID видео'},
        apid:{label: 'PID аудио'},
        app:{label: '/app/stream'},
        bandwidth:{label: 'Битрейт'},
        actions: {label: 'Действия'},
        show_details: {label: "Детали"}
      }
    };
  },

  computed: {
    rows(){
      return this.streams.length
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
      // Периодическое обновление данных с помощью таймера
      try {
        let updatedStreams = await this.$axios.$get("/streams/");
        this.streams = updatedStreams;
      } catch (e) {
        console.log(e);
      }
    },

    async deleteStream(stream_id) {
      // Удаляю объект и затем запрашиваю актуальный список объектов
      if (confirm('Вы уверены?')){
          try {
            await this.$axios.$delete(`/streams/${stream_id}/`);
            let newStreams = await this.$axios.$get("/streams/");
            this.streams = newStreams;
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
