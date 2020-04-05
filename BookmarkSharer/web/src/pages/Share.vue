<template>
  <div>
    <my-header/>
    <div id="container">
      <div id="introBoard">
        <div class="textBoard">
          <h3>如何导出书签？</h3>
          <p>1、打开谷歌浏览器</p>
          <p>2、点击右上角“自定义以及控制”</p>
          <p>3、点击“书签”</p>
          <p>4、点击“书签管理器”</p>
          <p>5、在“书签管理器”的新页面的右上角呼出操作栏</p>
          <p>6、点击“导出书签”保存到本地</p>
        </div>
        <div class="textBoard">
          <h3>上传我的书签会导致隐私泄露吗？</h3>
          <p>1、谷歌浏览器的书签只包含名称、链接以及图标，不涉及账密等信息</p>
          <p>2、一般来说，书签中保存的链接都是大家可以访问的，那些涉及隐私的其他人没有账号密码是无法登录的</p>
          <p>3、可以在上传书签的时候，选择不分享书签。那样你的站点将不会被保存，只用于自己生成词云图一乐</p>
        </div>
      </div>
      <div id="uploadBoard">
        <label><input type="checkbox" accept="text/html" id="isShareInput">分享我的书签</label>
        <input type="file" name="bookmark">
        <button>确认</button>
      </div>
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

<style scoped lang="less">
  #container {
    display: flex;
    justify-content: space-between;
    align-items: center;

    #introBoard {
      width: 40%;
      padding: 4px;

      .textBoard {
        padding: 8px;

        p {
          padding: 4px;
        }
      }
    }

    #uploadBoard {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      height: 256px;
      width: 30%;
      margin: 0 auto;
      border-radius: 8px;
      border: 1px grey solid;
      padding: 8px;
    }
  }
</style>
