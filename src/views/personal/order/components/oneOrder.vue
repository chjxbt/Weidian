<template>
  <div class="m-one-order">
    <div class="m-one-order-top">
      <img src="" class="m-product-img" alt="">
      <div class="m-product-info">
        <p class="m-product-name">商品名称商品名称商品名称商品名称
          商品名称商品名称商品名称</p>
        <p>投诉处理中..</p>
        <p class="m-order-code">
          <span>订单号：123456789000</span>
          <span class="m-order-btn">订单付款</span>
        </p>
      </div>
    </div>
    <ul class="m-one-order-money">
      <li>
        <span>付款金额</span>
        <span class="m-red m-ft-b">￥29.36</span>
      </li>
      <li>
        <span>付款金额</span>
        <span class="m-red m-ft-b">￥29.36</span>
      </li>
      <li>
        <span>付款金额</span>
        <span class="m-red m-ft-b">￥29.36</span>
      </li>
    </ul>
    <p class="m-order-time">2018-08-08 16:49:07  创建</p>
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
<style lang="less" rel="stylesheet/less">
  @import "../../../../common/css/index";
  .m-one-order{
    margin-top: 20px;
    padding: 20px;
    box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.16);
    color: #666;
    .m-one-order-top{
      .flex-row(flex-start);
      margin-bottom: 20px;
      .m-product-img{
        display: block;
        width: 175px;
        height: 175px;
        background-color: #f7f7f7;
        margin-right: 27px;
      }
      .m-product-info{
        height: 175px;
        width: 70%;
        text-align: left ;
        font-size: 24px;
        position: relative;
        .m-product-name{
          line-height: 32px;
          height: 64px;
          text-align: left;
        }
        .m-order-code{
          position: absolute;
          left: 0;
          bottom: 0;
          width: 100%;
          .flex-row(space-between);
          font-size: 20px;
          line-height: 28px;
          .m-order-btn{
            display: block;
            width: 148px;
            height: 50px;
            font-size: 20px;
            line-height: 50px;
            text-align: center;
            background-color: @mainColor;
            border: 2px solid @mainColor;
            color: #fff;
            border-radius: 30px;
            &.active{
              background-color: #fff;
              color: @mainColor;
            }
          }
        }
      }

    }
    .m-one-order-money{
      .flex-row(space-around);
      li{
        span{
          display: block;
          margin: 10px 0;
          font-size: 24px;
        }
      }
    }
    .m-order-time{
      font-size: 21px;
      color: #c1c1c1;
      text-align: left;
      padding-left: 58px;
      margin-top: 20px;
    }
  }
</style>
