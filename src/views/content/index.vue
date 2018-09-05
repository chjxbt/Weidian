<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <ul class="m-weidian-tabbox">
        <li>
          <span>高级合伙人</span>
          <span class="m-tab-line">/</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  export default {
    data(){
      return{
        name:'首页管理'
      }
    },
    components:{
      pageTitle
    },
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";
</style>
