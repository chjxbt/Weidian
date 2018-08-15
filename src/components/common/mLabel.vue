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
    transform: rotate(40deg);
    width: 70px;
    height: 70px;
    .m-text{
      font-size: 14px;
     z-index: 100;
      position: absolute;
      top:0;
      right: 14px;
      color: #fff;
    }
    .m-triangle{
      position: absolute;
      top:0;
      right: 0;
      transform: rotate(-40deg);
      width: 70px;
      height: 70px;
      background: url("/static/images/icon-label.jpg");
    }
  }
</style>
