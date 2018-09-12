<template>
  <div class="m-one-order">
    <div class="m-one-order-top">
      <img :src="item.productinfo.opiproductimages" class="m-product-img" alt="">
      <div class="m-product-info">
        <p class="m-product-name">{{item.productinfo.opiproductname}}</p>
        <p class="m-complain-p">投诉处理中..</p>
        <p class="m-order-code">
          <span>订单号：{{item.oisn}}</span>
          <span  :class="item.oipaystatus == 0?'m-order-btn' : (item.oipaystatus == 7?'m-order-btn active': ( item.oipaystatus == 2 || item.oipaystatus == 3 ||item.oipaystatus == 10) ?'':'m-red')">{{item.oipaystatus}}</span>
        </p>
      </div>
    </div>
    <ul class="m-one-order-money">
      <li>
        <span>付款金额</span>
        <span class="m-red m-ft-b">￥29.36</span>
      </li>
      <li>
        <span>成交预估收入</span>
        <span class="m-red m-ft-b">￥29.36</span>
      </li>
      <li>
        <span>收入来源</span>
        <span class="m-red m-ft-b">省钱了29.36</span>
      </li>
    </ul>
    <p class="m-order-time">{{item.oicreatetime.slice(0,4)}}-{{item.oicreatetime.slice(4,6)}}-{{item.oicreatetime.slice(6,8)}} {{item.oicreatetime.slice(8,10)}}:{{item.oicreatetime.slice(10,12)}}:{{item.oicreatetime.slice(12,14)}}  创建</p>
  </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        props: {
          item:{
            type:Object,
            default:null
          }
        },
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
        .m-complain-p{
          color: #333;
          font-weight: bold;
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
        width: 30%;
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
