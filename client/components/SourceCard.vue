<template>

              <tr>

                <th scope="row">{{source.id}}</th>
                <td>{{source.name}}</td>
                <td v-if="source.status"><span class="badge badge-success">online</span></td>
                <td v-else><span class="badge badge-danger">offline</span></td>
                <td >{{source.bitrate}} Mbps</td>
                <td>{{source.ip}}</td>
                <td>{{source.port}}</td>
                <td>{{source.miface}}</td>
                <td>{{source.protocol}}</td>
                <td>
                  <nuxt-link :to="`/sources/${source.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
                  <button @click="onDelete(source.id)"  class="btn btn-sm btn-danger">Delete</button>

                </td>
              </tr>


</template>
<script>
export default {
  props: ["source", "onDelete"],
};
</script>
<style>
.source-card {

}

</style>
