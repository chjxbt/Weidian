<template>
  <div class="m-search" @click.stop="searchClick">
    <input type="text" placeholder="" />
    <div class="m-search-text">
      <span class="m-search-icon"></span>
      <span >搜索商品、品牌</span>
    </div>
  </div>
</template>

<script>
    export default {
        name: "search",
      methods:{
        searchClick(){
          this.$emit('searchClick')
        }
      }
    }
</script>

<style lang="less" rel="stylesheet/less">
  .m-search{
    /*width: 100%;*/
    padding: 0 18px;
    position: relative;
    input{
      width: 94%;
      height: 72px;
      line-height: 72px;
      font-size: 26px;
      border: none;
      background-color: #f1f1f1;
      border-radius: 10px;
      padding: 0 20px;
      &::-webkit-input-placeholder{
        text-align: center;
      }
    }
    .m-search-text{
      position: absolute;
      top:0;
      left: 28px;
      height: 72px;
      line-height: 72px;
      text-align: center;
      color: #a4a4a4;
      font-size: 26px;
      display: flex;
      flex-flow: row;
      align-items: center;
      justify-content: center;
      width: 94%;
      .m-search-icon{
        display: inline-block;
        width: 34px;
        height: 34px;
        background: url("/static/images/icon-search.png") no-repeat;
        background-size: 100%;
        vertical-align: middle;
      }
    }
  }
</style>
