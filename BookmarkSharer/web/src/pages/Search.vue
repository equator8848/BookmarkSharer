<template>
  <div>
    <my-header/>
    <div id="searchBoard">
      <input type="text" id="searchInput">
      <input type="button" id="searchSubmit" value="搜索一下">
    </div>
    <label-list-board content-name="猜你喜欢"></label-list-board>
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
  #searchBoard {
    width: 40%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px gray solid;
    padding: 8px;

    #searchInput {
      width: 80%;
    }
  }
</style>
