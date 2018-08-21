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
    top: 0.8rem;
    right: 0;
    width: 0.9rem;
    height: 0.9rem;
    .m-triangle{
      border-top: 0.8rem solid red;
      border-left: 0.9rem solid transparent;
    }
    .m-text{
      z-index: 100;
      position: absolute;
      top: -0.75rem;
      right: 0.05rem;
      color: #fff;
      transform: rotate(40deg);
    }
  }
</style>
