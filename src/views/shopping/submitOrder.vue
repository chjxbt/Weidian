<template>
  <div>
    <div class="line-one" v-if="hasAddress"></div>
    <div class="add-address" v-if="hasAddress" @click="addAddress">
      <span class="add-address-text m-ft-36 m-bg-main-color">+ 添加地址</span>
      <span class="to-add-address m-ft-36 m-bg-main-color">></span>
    </div>
    <div class="order-address" v-if="!hasAddress" @click="addAddress">
      <div class="consignee-info">
        <img src="/static/images/order_address.png" class="order-address-img">
        <div class="consignee-name m-ft-26 m-black">收货人： 茉莉</div>
        <div class="consignee-phone m-ft-26 m-black tr">13588718806</div>
      </div>
      <div class="consignee-address m-ft-26 m-black">收货地址：北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京</div>
    </div>
    <div class="line-one"></div>
    <div class="store-product">
      <div class="store-title">
        <img src="/static/images/store-img.png" class="store-img">
        <div class="store-name m-ft-28 m-black tl">衣衣旗舰店</div>
      </div>
      <div class="line-two"></div>
      <div class="order-product">
        <img src="http://img1.imgtn.bdimg.com/it/u=661395716,3070712851&fm=214&gp=0.jpg" class="product-img">
        <div class="product-info">
          <div class="product-name m-ft-24 m-black">2018早秋新款显瘦秋新款显瘦款显瘦瘦2018早秋新款显瘦秋新款显瘦款显瘦瘦</div>
          <div class="product-params m-ft-24 m-black tl">尺寸：L   颜色：红色</div>
          <span class="product-price m-ft-24 m-red tl">￥ 149</span>
          <span class="product-quantity m-ft-20 m-black">X1</span>
        </div>
      </div>
      <div class="line-two"></div>
      <p class="user-new">
        <span class="user-new-title m-ft-26 m-grey">使用新衣币</span>
        <new-currency class="new-currency tr"></new-currency>
      </p>
      <div class="line-two"></div>
      <div class="wechat-pay">
        <img src="/static/images/wechat_pay.png" class="wechat-pay-img">
        <span class="wechat-pay-text m-ft-26 m-black tl">微信支付</span>
        <img src="/static/images/icon-radio-active.png" class="wechat-pay-active">
      </div>
      <div class="line-one"></div>
      <p class="order-amount m-ft-26">
        <span class="amount-title m-grey tl">支付金额</span>
        <span class="amount-text m-black">运费： 0</span>
        <span class="amount-text m-black">总计：</span>
        <span class="amount-number m-red">￥149.00</span>
      </p>
      <div class="line-two"></div>
      <div class="buyer-msg">
        <div class="msg-title m-ft-26 m-black tl">买家留言：</div>
        <textarea class="msg-input m-ft-26" placeholder="选填：建议填写和卖家商量好的内容~" rows="3"></textarea>
      </div>
      <div class="order-pay-box">
        <div class="order-pay m-ft-36 m-bg-main-color" @click="payOrder">支付订单</div>
      </div>
    </div>
  </div>
</template>

<script>
  import newCurrency from "../shopping/components/newCurrency";

  export default {
    data() {
      return {
        name: "submitOrder",
        hasAddress: true,
        order: {}
      }
    },
    components: { newCurrency },
    methods: {
      // 添加新地址
      addAddress() {
        if(this.hasAddress) {
          this.hasAddress = false;
        }else if(!this.hasAddress) {
          this.hasAddress = true;
        }
      },
      // 支付订单
      payOrder() {
        let order = this.order;
        this.$router.push({path: "/orderPayOK", query: { order }});
      }
    },
    created() {
      this.order = this.$route.query.order;
      console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/discover";
  @import "../../common/css/index";
  .line-one {
    height: 15px;
    background-color: #f2f5f7;
  }
  .line-two {
    width: 750px;
    height: 2px;
    opacity: 0.3;
    background-color: @grey;
  }
  .add-address {
    height: 88px;
    background-color: #9c94c5;
    .add-address-text {
      line-height: 88px;
    }
    .to-add-address {
      float: right;
      margin: 22px 45px 0 -45px;
    }
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
      letter-spacing: 2px;
      margin: 0 33px 20px 40px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
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
          width: 435px;
          margin: 30px 0 14px 0;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .product-params {
          margin-left: 10px;
        }
        .product-price {
          float: left;
          width: 200px;
          margin: 35px 0 0 5px;
        }
        .product-quantity {
          width: 130px;
          float: right;
          margin: 40px 0 0 30px;
        }
      }
    }
    .user-new {
      display: flex;
      .user-new-title {
        margin: 32px 35px;
      }
      .new-currency {
        flex: 1;
        margin: 30px;
      }
    }
    .wechat-pay {
      display: flex;
      .wechat-pay-img {
        width: 40px;
        height: 30px;
        margin: 38px 20px 40px 50px;
      }
      .wechat-pay-text {
        flex: 1;
        margin-top: 37px;
      }
      .wechat-pay-active {
        width: 35px;
        height: 35px;
        margin: 37px 40px;
      }
    }
    .order-amount {
      display: flex;
      .amount-title {
        flex: 1;
        margin: 32px 30px;
      }
      .amount-text {
        margin: 32px 0 0 20px;
      }
      .amount-number {
        margin: 32px 40px 0 10px;
      }
    }
    .buyer-msg {
      .msg-title {
        margin: 40px 30px;
      }
      .msg-input {
        width: 600px;
        margin-bottom: 230px;
        letter-spacing: 2.5px;
      }
    }
    .order-pay-box {
      bottom: 0;
      position: fixed;
      padding: 40px 25px;
      background-color: #f2f5f7;
      .order-pay {
        width: 140px;
        height: 48px;
        padding: 20px 280px;
        white-space: nowrap;
        letter-spacing: 3px;
        background-color: @mainColor;
      }
    }
  }
</style>
