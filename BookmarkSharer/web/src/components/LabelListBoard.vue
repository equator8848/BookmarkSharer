<template>
  <div id="container">
    <flower-title :title="this.contentName"></flower-title>
    <div id="labelBoard">
      <div v-for="(item,index) of labelList" :key="index">
        <router-link tag="h3" :to="'/siteList/'+item.id" class="labelItem">{{item.name}}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import FlowerTitle from '@/components/Title'
  export default {
    name: "LabelListBoard",
    components:{
      FlowerTitle
    },
    props: {
      contentName: String,
      labelList: Array
    }
  }
</script>

<style lang="less" scoped>
  #container {
    text-align: center;

    #labelBoard {
      border: 1px lightslategray solid;
      width: 80%;
      margin: 0 auto;

      .labelItem {
        background-color: lightblue;
        margin-top: 4px;
        cursor: pointer;
      }
    }
  }
</style>
