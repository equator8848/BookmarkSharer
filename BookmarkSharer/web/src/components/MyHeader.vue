<template>
  <div id="header">
    <router-link to="/" tag="div" id="logo">
      <img src="@/assets/images/logo.png">
    </router-link>
    <div id="navBar">
      <!--      <router-link to="/search" tag="div" class="navItem"><h3>搜索</h3></router-link>-->
      <!--      <router-link to="/share" tag="div" class="navItem"><h3>分享</h3></router-link>-->
      将你的谷歌浏览器书签上传，生成有趣的词云~
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MyHeader',
  }
</script>

<style scoped lang="less">
  #header {
    background-color: lightslategray;
    height: 128px;
    display: flex;
    justify-content: space-around;

    #logo {
      img {
        width: 128px;
        height: 128px;
      }

      cursor: pointer;
    }

    #navBar {
      width: 60%;
      display: flex;
      justify-content: space-around;
      align-items: center;
      height: inherit;
      color: aliceblue;

      .navItem {
        text-decoration: none;
        color: white;
        cursor: pointer;
      }
    }
  }
</style>
