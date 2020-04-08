<template>
  <div id="container">
    <div id="canvasContainer">
      <canvas id="wordCloudBoard" ref="wordCloudBoard" width="1500px" height="700px"></canvas>
    </div>
  </div>
</template>

<script>
  import WordCloud from 'wordcloud'

  export default {
    name: "WordCloudDetails",
    data() {
      return {
        labels: []
      }
    }, methods: {
      getLabels() {
        this.$httpUtil.request.get('analysis/get_labels_by_page_id', {
          params: {
            pageId: this.$route.params.pageId
          }
        }).then(res => {
          let result = res.data
          if (result.status == this.$httpUtil.statusCode.SUCCESS) {
            this.labels = result.data
            console.log('数据：', this.labels.length);
            let wc = WordCloud(this.$refs.wordCloudBoard, {
              list: this.labels,
              gridSize: 16,
              weightFactor: 3,
              fontWeight: 'normal',
              color: 'random-dark',
              rotateRatio: 1,
              backgroundColor: 'aliceblue'
            })
          } else {
            console.log('没有获取到数据！');
          }
        })
      }
    },
    created() {
      console.log("created labels", this.labels)
    },
    // mounted 与 created 获取DOM不一样
    mounted() {
      this.getLabels()
      console.log("mounted labels", this.labels)
    }
  }
</script>

<style scoped lang="less">
  #canvasContainer {
    width: 1500px;
    margin: 16px auto;
  }
</style>
