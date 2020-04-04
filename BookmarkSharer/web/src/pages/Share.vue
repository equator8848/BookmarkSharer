<template>
  <div>
    <my-header/>
    <div id="container">
      <p>share</p>
    </div>
    <my-footer/>
  </div>
</template>

<script>
  import MyHeader from '@/components/MyHeader'
  import MyFooter from '@/components/MyFooter'

  export default {
    name: 'Share',
    components: {
      MyHeader,
      MyFooter
    }
  }
</script>

<style scoped>

</style>
