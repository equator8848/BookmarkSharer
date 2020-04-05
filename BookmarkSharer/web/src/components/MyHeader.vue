<template>
  <div id="header">
    <router-link to="/" tag="div" id="logo">
      <img src="@/assets/images/logo.png">
    </router-link>
    <div id="navBar">
      <router-link to="/hot" tag="div" class="navItem"><h3>热门站点</h3></router-link>
      <router-link to="/share" tag="div" class="navItem"><h3>站点分析</h3></router-link>
      <router-link to="/search" tag="div" class="navItem"><h3>搜索</h3></router-link>
      <router-link to="/login" tag="div" class="navItem"><h3>登录</h3></router-link>
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

      .navItem {
        text-decoration: none;
        color: white;
        cursor: pointer;
      }
    }
  }
</style>
