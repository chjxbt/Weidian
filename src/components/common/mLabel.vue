<template>
  <div class="m-label">
    <span class="m-triangle"></span>
    <span class="m-text">新品</span>
  </div>
</template>

<script>
  export default {
    name: "m-label"
  }
</script>

<style lang="less" rel="stylesheet/less" >
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
      top: 8px;
      right: 6px;
      color: #fff;
    }
    .m-triangle{
      position: absolute;
      top:0;
      right: 0;
      width: 70px;
      height: 70px;
      background: url("/static/images/icon-label.jpg");
    }
  }
</style>
