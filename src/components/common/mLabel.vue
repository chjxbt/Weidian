<template>
  <div class="m-label">
    <span class="m-triangle"></span>
    <span class="m-text">{{name}}</span>
  </div>
</template>

<script>
  export default {
    props:{
      name:{
        type:String,
        default:null
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  .m-label{
    position: absolute;
    top:0;
    right: 0;
    width: 70px;
    height: 70px;
    .m-text{
      font-size: 10px;
      z-index: 100;
      position: absolute;
      transform: rotate(40deg);
      top: 6px;
      right: 0;
      color: #fff;
    }
    .m-triangle{
      position: absolute;
      top:0;
      right: 0;
      width: 70px;
      height: 70px;
      background: url("/static/images/icon-label.png");
    }
  }
</style>
