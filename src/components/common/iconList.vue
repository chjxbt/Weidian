<template>
  <ul class="m-icon-list">
    <li>
      <img src="/static/images/icon-like.jpg" class="m-icon" alt="">
      1219
    </li>
    <li >
      <img src="/static/images/icon-lian.jpg" class="m-icon" alt="">
      复制链接
    </li>
    <li>
      <img src="/static/images/icon-share.jpg" class="m-icon" alt="">
      转发
    </li>
  </ul>
</template>

<script>
    export default {
        name: "icon-list"
    }
</script>

<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";
  .m-icon-list{
    .flex-row(flex-end);
    li{
      margin-left: 10px;
      .flex-col(center);
      font-size: 22px;
      .m-icon{
        display: block;
        width: 40px;
        height: 40px;
        background-color: #666666;
      }
    }

  }
</style>
