<template>
  <div class="m-navbar">
    <ul>
      <li  class="active">
        <span class="m-navbar-text">上新</span>
        <span class="m-dot"></span>
      </li>
      <li>
        <span class="m-navbar-text">上新</span>
        <span class="m-dot"></span>
      </li>
      <li>
        <span class="m-navbar-text">上新</span>
        <span class="m-dot"></span>
      </li>
      <li>
        <span class="m-navbar-text">上新</span>
        <span class="m-dot"></span>
      </li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: "navbar"
    }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
  .m-navbar{
    margin-top: 10px;
    ul{
      display: flex;
      flex-flow: row;
      align-items: center;
      font-size: 32px;
      li{
        padding: 10px 0;
        width: 25%;
        position: relative;
        span.m-navbar-text{
          padding: 10px 20px;
          font-weight: 600;
        }
        &.active{
          span.m-navbar-text{
            color: @mainColor;
            border-bottom: 3px solid @mainColor;
          }
        }
        .m-dot{
          position: absolute;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background-color: @mainColor;
        }
      }
    }
  }
</style>
