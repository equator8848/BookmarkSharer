<template>
  <div id="container">
    <my-header/>
    <div id="wordCloudBoard">
      <div class="boardTitle">
        <h3>热门站点</h3>
      </div>
      <div id="wordCloud">
        <word-cloud :data="hotLabels" nameKey="name" valueKey="hotPoint" color="Category10"
                    :wordClick="wordClickHandler"
                    :fontSize="wordFontSize" :margin="wordMargin" :wordPadding="3" :showTooltip="false"></word-cloud>
      </div>
    </div>
    <div id="shareBoard">
      <div class="boardTitle">
        <h3>上传书签</h3>
      </div>
      <div id="share">
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
            <p>3、可以在上传书签的时候，选择不分享书签。那样你的站点将不会被保存，只用于自己生成词云乐一乐</p>
          </div>
        </div>
        <div id="uploadBoard">
          <label><input type="checkbox" accept="text/html" v-model="isShareInput">分享我的书签</label>
          <input type="file" name="bookmark" ref="bookmarkFile" multiple="multiple">
          <button @click="uploadBookmarkHandler">确认</button>
        </div>
      </div>
    </div>
    <my-footer/>
  </div>
</template>

<script>
  import MyHeader from '@/components/MyHeader'
  import MyFooter from '@/components/MyFooter'
  import WordCloud from 'vue-wordcloud'

  export default {
    name: 'Index',
    components: {
      WordCloud,
      MyHeader,
      MyFooter
    },
    created() {
      this.getHotLabels()
    },
    data() {
      return {
        wordFontSize: [20, 80],
        wordMargin: {top: 32, right: 16, bottom: 32, left: 16},
        hotLabels: [],
        isShareInput: 0,
      }
    },
    methods: {
      getHotLabels() {
        this.$httpUtil.request.get('label/get_hot_label').then(res => {
          let result = res.data
          if (result.status == this.$httpUtil.statusCode.SUCCESS) {
            this.hotLabels = result.data
          } else {
            console.log('没有获取到数据！');
          }
        })
      },
      wordClickHandler(name, value, vm) {
        console.log('wordClickHandler', name, value, vm);
      },
      uploadBookmarkHandler() {
        console.log("点击了按钮...")
        let ref = this.$refs.bookmarkFile
        let file = ref.files[0]
        let formData = new FormData()
        formData.append('bookmark', file)
        formData.append('isShare', this.isShareInput)
        this.$httpUtil.request.post('/upload/upload_bookmark', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(res => {
          let result = res.data
          if (result.status == this.$httpUtil.statusCode.SUCCESS) {
            console.log(result.data)
            this.$router.push({
              path: `/wordCloudDetails/${result.data.pageId}`
            })
          } else {
            console.log('文件上传失败！');
          }
        })
      }
    }
  }
</script>

<style scoped lang="less">
  #container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 1600px;

    .boardTitle {
      height: 64px;
      background-color: floralwhite;
      padding: 16px;
      line-height: 64px;
    }

    #wordCloudBoard {
      #wordCloud {
        cursor: pointer;
        background-color: aliceblue;
      }
    }

    #shareBoard {
      #share {
        display: flex;
        justify-content: space-around;
        align-items: center;
        background-color: aliceblue;
        padding: 16px;

        #introBoard {
          width: 40%;
          border: 1px gray solid;
          border-radius: 8px;
          padding: 8px;
          background-color: #dee1e6;

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
          background-color: lightblue;
        }
      }
    }
  }
</style>
