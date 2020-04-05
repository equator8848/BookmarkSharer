<template>
  <div id="footer">
    <div id="footer-left">
      <img src="@/assets/images/qrcode.png">
    </div>
    <div id="footer-right">
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=50010802002723">
        <p>渝公网安备 50010802002723号</p>
      </a>
      <a target="_blank" href="http://beian.miit.gov.cn"><p>粤ICP备18122194号</p></a>
      <a target="_blank" href="#"><p>邮箱：841116931@qq.com</p></a>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MyFooter'
  }
</script>

<style scoped lang="less">
  #footer {
    height: 128px;
    padding: 16px;
    background-color: #dee1e6;
    color: #6c757d;
    display: flex;
    justify-content: space-around;
    align-items: center;
    a {
      text-decoration: none;
      color: lightseagreen;
    }

    #footer-left img {
      width: 128px;
      height: 128px;
    }
  }
</style>
