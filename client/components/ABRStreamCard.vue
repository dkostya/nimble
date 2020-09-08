<template>

              <tr>
                <td>/{{abrstream.id}}</td>
                <td>/{{abrstream.app}}/{{abrstream.stream}}</td>
                <td>
                  <ul>
                    <li  v-for="abrsource in abrstream.streams">
                      /{{abrsource.app}}/{{abrsource.stream}}
                    </li>
                    </ul>
                </td>
                <td>
                  <nuxt-link :to="`/abrstreams/${abrstream.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
                  <button @click="onDelete(abrstream.id)"  class="btn btn-sm btn-danger">Delete</button>

                </td>



              </tr>




</template>
<script>
export default {
  props: ["abrstream", "onDelete"],
};
</script>
<style>
</style>

