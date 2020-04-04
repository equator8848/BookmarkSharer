<template>
  <div class="container">
    <span class="iconfont icon-left">&#xe6b2;</span>
    <div class="title">{{this.title}}</div>
    <span class="iconfont icon-right">&#xe6b2;</span>
  </div>
</template>

<script>
  export default {
    name: "Title",
    props: {
      title: String
    }
  }
</script>

<style lang="less" scoped>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 16px 0;

    .title {
      font-size: 32px;
    }

    .icon-left, .icon-right {
      font-size: 64px;
    }

    .icon-right {
      transform: rotateY(180deg)
    }

  }
</style>
