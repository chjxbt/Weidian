<template>
  <div>
    <div class="order-no-box">
      <div class="order-no m-ft-26 m-black tl">订单号：{{order.oiid}}</div>
      <div class="copy-order-no m-ft-20 m-grey" @click="copyText">复制</div>
    </div>
    <div class="line-one"></div>
    <div class="order-address">
      <div class="consignee-info">
        <img src="/static/images/order_address.png" class="order-address-img">
        <div class="consignee-name m-ft-26 m-black">收货人： {{order.oirecvname}}</div>
        <div class="consignee-phone m-ft-26 m-black tr">{{order.oirecvphone}}</div>
      </div>
      <div class="consignee-address m-ft-26 m-black">收货地址：{{order.oiaddress}}</div>
    </div>
    <div class="line-two"></div>
    <div class="store-product">
      <div class="store-title">
        <img src="/static/images/store-img.png" class="store-img">
        <div class="store-name m-ft-28 m-black tl"><span>衣百惠</span><span class="m-red">{{order.order_status}}</span></div>
      </div>
      <div class="line-one"></div>
      <template v-for="(item,index) in order.productinfo">
        <div class="order-product">
          <img src="http://img1.imgtn.bdimg.com/it/u=661395716,3070712851&fm=214&gp=0.jpg" class="product-img">
          <div class="product-info">
            <div class="product-name m-ft-24 m-black">
              <span class="name">{{item.opiproductname}}</span>
              <span>退/换</span>
            </div>
            <div class="product-params m-ft-24 m-black tl">
              <template v-for="(i,j) in item.pskproperkey">
                <span>{{i.key}}: {{i.value}}  </span>
              </template>
            </div>
            <span class="product-price m-ft-24 m-red tl">￥ {{item.oiproductprice}}</span>
            <span class="product-quantity m-ft-20 m-black">X{{item.opiproductnum}}</span>
          </div>
        </div>
      </template>

      <div class="line-one"></div>
      <div class="price-detail">
        <p class="price-detail-box m-ft-26 m-grey">
          <span class="price-detail-text tl">商品总价</span>
          <span class="price-detail-number tr">￥{{order.oimount}}</span>
        </p>
        <!--<p class="price-detail-box m-ft-26 m-grey">-->
          <!--<span class="price-detail-text tl">使用新衣币</span>-->
          <!--<span class="price-detail-number tr">-￥3.00</span>-->
        <!--</p>-->
      </div>
      <div class="line-one"></div>
      <div class="total-price m-ft-22 m-grey-color">
        <div class="total-price-detail tl">总计￥{{order.oimount}} 运费￥0</div>
        <div class="total-price-total tr">共2件商品 合计￥{{order.oimount}}</div>
      </div>
      <div class="line-one"></div>
    </div>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui';
  export default {
    data() {
      return {
        name: "orderProduct",
      }
    },
    props:{
      order:{
        type:Object,
        default:null
      }
    },
    // components: {  },
    methods: {
      // 复制
      copyText() {
        let link = "订单号";
        this.$copyText(this.order.oiid).then(function (e) {
          Toast({ message: "复制成功", className: 'm-toast-success' });
        })
      }
    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  .order-no-box {
    display: flex;
    flex-flow: row;
    justify-content: space-between;
    padding: 0 20px;
    .order-no {
      margin: 35px 0 20px 0;
      white-space: nowrap;
    }
    .copy-order-no {
      width: 50px;
      height: 35px;
      padding: 5px 21px;
      white-space: nowrap;
      margin: 28px 0 0 25px;
      border-radius: 6px;
      border: solid 2px @grey;
    }
  }
  .line-one {
    width: 710px;
    height: 2px;
    opacity: 0.3;
    margin: 0 20px;
    background-color: @grey;
  }
  .line-two {
    height: 15px;
    background-color: #f2f5f7;
  }
  .order-address {
    .consignee-info {
      width: 100%;
      display: flex;
      .order-address-img {
        width: 30px;
        height: 45px;
        margin: 25px 30px 25px 50px;
      }
      .consignee-name {
        margin: 30px -10px;
      }
      .consignee-phone {
        flex: 1;
        margin: 33px;
      }
    }
    .consignee-address {
      letter-spacing: 1px;
      margin: 0 33px 20px 40px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
      text-align: left;
    }
  }
  .store-product {
    .store-title {
      display: flex;
      .store-img {
        width: 40px;
        height: 41px;
        margin: 20px 30px;
      }
      .store-name {
        flex: 1;
        margin: 20px 0;
        padding-right:20px;
        display: flex;
        flex-flow: row;
        justify-content: space-between;
      }
    }
    .order-product {
      display: flex;
      .product-img {
        width: 160px;
        height: 160px;
        margin: 25px 30px 32px 40px;
      }
      .product-info {
        flex: 1;
        .product-name {
          display: flex;
          flex-flow: row;
          justify-content: space-between;
          margin: 30px 0 14px 0;
          padding-right: 20px ;
          .name{
            width: 365px;
            text-align: left;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
          }
        }
        .product-params {
          /*margin-left: 10px;*/
        }
        .product-price {
          float: left;
          width: 200px;
          margin: 35px 0 0 0;
        }
        .product-quantity {
          width: 130px;
          float: right;
          margin: 40px 0 0 30px;
        }
      }
    }
    .price-detail {
      .price-detail-box {
        display: flex;
        margin: 20px 29px;
        .price-detail-number {
          flex: 1;
        }
      }
    }
    .total-price {
      .total-price-detail {
        margin: 30px;
      }
      .total-price-total {
        margin: 30px;
      }
    }
  }
</style>
