<template>
  <div>
    <div class="page-title" v-if="list">
      <div>
        <template v-for="(item, index) in list">
          <span v-if="index > 0"> / </span>
          <span v-text="item.name" class="router-link" :class="item.active ? 'active' : ''" @click="routerClick(item)">工作模块管理</span>
          <span></span>
        </template>
      </div>
      <span class="m-page-fresh" @click="freshClick" v-if="fresh"></span>
    </div>

    <div class="m-page-title" v-else>
      <span v-text="title">工作模块管理</span>
      <span class="m-page-fresh" @click="freshClick" v-if="fresh"></span>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  export default {
    data() {
      return {}
    },
    props:{
      title:{ type: String, default: '' },
      list:{ type: Array, default: null },
      fresh:{ type: Boolean, default: false }
    },
    methods: {
      freshClick(){
        this.$emit('freshClick');
      },
      // 点击标题 - 跳转页面
      routerClick(item){
        this.$router.push(item.url);
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .page-title {
    color: #595757;
    font-size: 0.14rem;
    letter-spacing: 1.5px;
    padding: 0.1rem 0.3rem;
    background-color: #eeeeef;
    /*border-radius: 0.1rem 0.1rem 0 0;*/
    span{
      display: inline-block;
      padding: 0.05rem 0;
      line-height: 0.2rem;
      &.router-link{
        cursor: pointer;
        &.active {
          color: #719aab;
          font-weight: bold;
        }
      }
    }
  }

  .m-page-title{
    font-size: 0.14rem;
    background-color: #eeeeef;
    padding: 0.1rem 0.4rem;
    .flex-row(space-between);
    font-weight: 600;
    span{
      display: inline-block;
    }
    .m-page-fresh{
      width: 0.2rem;
      height: 0.18rem;
      background: url("../../common/images/icon-fresh.png");
      background-size: 100% 100%;
      cursor: pointer;
    }
  }
</style>
