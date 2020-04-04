<template>
  <div>
    <my-header/>
    <div id="container">
      <p>body</p>
    </div>
    <my-footer/>
  </div>
</template>

<script>
    import MyHeader from '@/components/MyHeader'
    import MyFooter from '@/components/MyFooter'

    export default {
        name: 'Index',
        components: {
            MyHeader,
            MyFooter
        }
    }
</script>

<style scoped lang="less">
  #container {
    background-color: gray;
    height: 256px;
  }
</style>
