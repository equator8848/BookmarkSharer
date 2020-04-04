<template>
  <div>
    <my-header/>
    <div id="container">
      <p>login</p>
    </div>
    <my-footer/>
  </div>
</template>

<script>
  import MyHeader from '@/components/MyHeader'
  import MyFooter from '@/components/MyFooter'

  export default {
    name: 'Login',
    components: {
      MyHeader,
      MyFooter
    }
  }
</script>

<style scoped>

</style>
