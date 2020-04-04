<template>
  <div>
    <my-header/>
    <label-list-board contentName="热门站点" :labelList="labelList"></label-list-board>
    <label-list-board contentName="猜你喜欢" :labelList="labelList"></label-list-board>
    <my-footer/>
  </div>
</template>

<script>
  import MyHeader from '@/components/MyHeader'
  import MyFooter from '@/components/MyFooter'
  import LabelListBoard from '@/components/LabelListBoard'

  export default {
    name: 'Hot',
    components: {
      MyHeader,
      MyFooter,
      LabelListBoard
    },
    data() {
      return {
        labelList: [
          {
            'id': 1,
            'name': '博客园',
            'hotPoint': 999999999
          },
          {
            'id': 2,
            'name': 'CSDN',
            'hotPoint': 99999999
          },
          {
            'id': 3,
            'name': '掘金',
            'hotPoint': 9999999
          },
          {
            'id': 4,
            'name': 'Java',
            'hotPoint': 999999
          },
          {
            'id': 5,
            'name': 'Spring',
            'hotPoint': 99999
          },
          {
            'id': 6,
            'name': '微服务',
            'hotPoint': 9999
          }
        ]
      }
    }
  }
</script>

<style lang="less" scoped>

</style>
