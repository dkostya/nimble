<template>
  <div>
       <template v-for="rtmpsetting in rtmpsettings">
                        <rtmp-settings-card :rtmpsetting="rtmpsetting"></rtmp-settings-card>
       </template>
    </div>
</template>
<script>

import RtmpSettingsCard from "../../components/RtmpSettingsCard";

export default {
  head() {
    return {
      title: "RTMP Settings"
    };
  },
  components: {
    RtmpSettingsCard,
  },
  async asyncData({ $axios, params }) {
    try {
      let rtmpsettings = await $axios.$get(`/rtmpsettings/`);
      return { rtmpsettings };
    } catch (e) {
      return { rtmpsettings: [] };
    }
  },

  data() {
    return {
      rtmpsettings: [],
    };
  },

};
</script>
<style>
</style>
