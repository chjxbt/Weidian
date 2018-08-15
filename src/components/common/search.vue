<template>
  <div class="m-search">
    <input type="text" placeholder="搜索商品、品牌" />
  </div>
</template>

<script>
    export default {
        name: "search"
    }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  .m-search{
    width: 100%;
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
  }
</style>
