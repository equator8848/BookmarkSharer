<template>
  <div>
    <my-header/>
    <div id="container">
      <div id="entranceList">
        <a
          href="https://github.com/login/oauth/authorize?client_id=2032e483fa91b9e80921&redirect_uri=https://www.equator8848.xyz/bookmarkSharer/api/user/github_login_callback">Github登录</a>
      </div>
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

<style scoped lang="less">
  #container {
    min-height: 512px;
    #entranceList {
      width: 40%;
      margin: 8px auto;
      text-align: center;
      border: 1px gray solid;

      a {
        text-decoration: none;
        color: black;
      }
    }
  }
</style>
