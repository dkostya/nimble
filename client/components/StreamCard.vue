<template>


  <tr>
    <th scope="row">{{stream.id}}</th>
    <td>{{ stream.video }}</td>
    <td>{{stream.audio}}</td>
    <td>{{stream.vpid }}</td>
    <td>{{stream.apid }}</td>
    <td>{{stream.app }}</td>
    <td>{{stream.stream }}</td>
    <td>{{stream.bandwidth }}</td>
    <td>
        <nuxt-link :to="`/streams/${stream.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
        <button @click="onDelete(stream.id)"  class="btn btn-sm btn-danger">Delete</button>


    </td>
  </tr>

</template>
<script>
import NuxtLoading from "../.nuxt/components/nuxt-loading";
export default {
  components: {},
  props: ["stream", "onDelete"],
}
</script>
<style>
.stream-card {

}
.table{
  margin: 17px auto;
}
</style>
