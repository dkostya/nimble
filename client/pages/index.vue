<template>
    <h1>Hello World</h1>
</template>

<script>

    export default {
      middleware: 'auth',
        name: "index",

  asyncData ({ redirect }) {
    return redirect('/server')
  }

    }
</script>

<style scoped>

</style>
