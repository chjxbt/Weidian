<template>
    <div class="m-weidian">
      <page-title :title="name" ></page-title>
      <div class="m-weidian-content">
        <ul class="m-weidian-tabbox">
          <li>
            <span class="m-tab-name active">高级合伙人</span>
            <span class="m-tab-line">/</span>
          </li>
          <li>
            <span class="m-tab-name ">中级合伙人</span>
            <span class="m-tab-line">/</span>
          </li>
          <li>
            <span class="m-tab-name">初级合伙人</span>
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
           name:'佣金管理'
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
