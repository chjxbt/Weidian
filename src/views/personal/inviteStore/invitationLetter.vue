<template>
    <div class="m-invitation">
      <div class="m-invitation-img-box">
        <span class="m-rule">规则</span>
        <div class="m-logo-name">
          <img src="" class="m-logo-img" alt="">
          <span class="m-name">xxxxx</span>
        </div>
        <img src=""  class="m-invitation-img" alt="">
      </div>
      <div class="m-invitation-title">
        礼包标题
      </div>
      <div class="m-invitation-products">
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {},
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>

  .m-invitation{
    padding: 30px 51px;
    .m-invitation-img-box{
      width: 644px;
      height: 644px;
      position: relative;
      box-shadow: 5px 5px 5px 0 rgba(0, 0, 0, 0.16);
      img.m-invitation-img{
        display: block;
        width: 644px;
        height: 644px;
        background-color: #9fd0bf;
      }
      span.m-rule{
        position: absolute;
        top:27px;
        right: 27px;
        font-size: 21px;
        color: #666;
      }
      .m-logo-name{
        position: absolute;
        top: 0;
        left: 25px;
        display: flex;
        align-items: center;
        flex-flow: row;
        .m-logo-img{
          display: inline-block;
          width: 148px;
          height: 148px;
          border-radius: 50%;
          border: 2px solid #f53b52;
          z-index: 1000;
        }
        span{
          display: inline-block;
          padding: 15px 50px;
          background-color: #a4a4a4;
          vertical-align: middle;
          margin-left: -25px;
          border-radius: 50px;
          color: #f53b52;
        }
      }
    }
    .m-invitation-title{
      width: 643px;
      height: 153px;
      background-color: #e9e9e9;
      box-shadow: 5px 5px 5px 0 rgba(0, 0, 0, 0.16);
      margin: 30px 0;
      font-size: 30px;
      line-height: 153px;
    }
    .m-invitation-products{
      display: flex;
      flex-flow: row;
      flex-wrap: wrap;
      .m-one{
        position: relative;
        width: 309px;
        font-size: 24px;
        margin-top: 20px;
        &:nth-child(even){
          margin-left: 25px;
        }
        p{
          padding: 5px;
        }
        .m-points{
          font-weight: bold;
          overflow: hidden;
          text-overflow:ellipsis;
          white-space: nowrap;
        }
        img{
          display: block;
          width: 309px;
          height: 372px;
          background-color: #a3a3a3;
        }
        .m-red-border{
          padding: 5px 30px;
          display: inline-block;
          color: #f53b52;
          border: 1px solid #f53b52;
          border-radius: 30px;
        }

      }
    }
  }
</style>
