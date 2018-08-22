<template>
    <div class="m-myOrder">
      <div class="m-myOrder-nav">
        <span class="active">销售订单</span>
        <span >自买订单</span>
      </div>
      <div class="m-myOrder-content">
        <ul class="m-myOrder-content-nav">
          <li>
            所有订单(17)
          </li>
          <li>
            待发货(1)
          </li>
          <li>
            已发货(1)
          </li>
          <li>
            退货(1)
          </li>
          <li>
            已失效(1)
          </li>
        </ul>
        <div class="m-myOrder-list">
          <one-order></one-order>
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span class="m-order-btn active">确认收货</span>
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
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span class="m-red">确认收货</span>
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
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span >确认收货</span>
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
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import oneOrder from './components/oneOrder';
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {
          oneOrder
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
  .m-myOrder{
    .m-myOrder-nav{
      .flex-row(flex-start);
      span{
        display: block;
        width: 50%;
        box-sizing: border-box;
        height: 46px;
        line-height: 46px;
        border: 2px solid @mainColor;
        color: #c1c1c1;
        font-size: 24px;
        text-align: center;
        &.active{
          background-color: @mainColor;
          color: #fff;
        }
      }
    }
    .m-myOrder-content{
      padding: 20px ;
      .m-myOrder-content-nav{
        .flex-row(space-around);
        font-size: 21px;
        color: #666;
        margin-bottom: 20px;
      }
      .m-myOrder-list{
        padding: 0 10px;


      }
    }
  }

</style>
