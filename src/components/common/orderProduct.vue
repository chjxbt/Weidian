<template>
  <div>
    <div class="order-no-box">
      <div class="order-no">订单号：RRK65S6R332SD654S613DF65SAD5</div>
      <div class="copy-order-no">复制</div>
    </div>
    <div class="line-one"></div>
    <div class="order-address">
      <div class="consignee-info">
        <img src="/static/images/order_address.png" class="order-address-img">
        <div class="consignee-name">收货人： 茉莉</div>
        <div class="consignee-phone">13588718806</div>
      </div>
      <div class="consignee-address">收货地址：北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京北京北京大北京</div>
    </div>
    <div class="line-two"></div>
    <div class="store-product">
      <div class="store-title">
        <img src="/static/images/store-img.png" class="store-img">
        <div class="store-name">衣衣旗舰店</div>
      </div>
      <div class="line-one"></div>
      <div class="order-product">
        <img src="http://img1.imgtn.bdimg.com/it/u=661395716,3070712851&fm=214&gp=0.jpg" class="product-img">
        <div class="product-info">
          <div class="product-name">2018早秋新款显瘦秋新款显瘦款显瘦瘦2018早秋新款显瘦秋新款显瘦款显瘦瘦</div>
          <div class="product-params">尺寸：L   颜色：红色</div>
          <span class="product-price">￥ 149</span>
          <span class="product-quantity">X1</span>
        </div>
      </div>
      <div class="order-product">
        <img src="http://img1.imgtn.bdimg.com/it/u=661395716,3070712851&fm=214&gp=0.jpg" class="product-img">
        <div class="product-info">
          <div class="product-name">2018早秋新款显瘦秋新款显瘦款显瘦瘦2018早秋新款显瘦秋新款显瘦款显瘦瘦</div>
          <div class="product-params">尺寸：L   颜色：红色</div>
          <span class="product-price">￥ 149</span>
          <span class="product-quantity">X1</span>
        </div>
      </div>
      <div class="line-one"></div>
      <div class="price-detail">
        <p class="price-detail-box">
          <span class="price-detail-text">商品总价</span>
          <span class="price-detail-number">￥298.00</span>
        </p>
        <p class="price-detail-box">
          <span class="price-detail-text">使用新衣币</span>
          <span class="price-detail-number">-￥3.00</span>
        </p>
      </div>
      <div class="line-one"></div>
      <div class="total-price">
        <div class="total-price-detail">总计￥273 运费￥0</div>
        <div class="total-price-total">共2件商品 合计￥ 273</div>
      </div>
      <div class="line-one"></div>
    </div>
  </div>
</template>

<script>

  export default {
    data() {
      return {
        name: "orderProduct",
        order: {}
      }
    },
    // components: {  },
    methods: {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
  .order-no-box {
    display: flex;
    .order-no {
      color: @black;
      font-size: 26px;
      text-align: left;
      margin: 35px 23px 20px 23px;
      white-space: nowrap;
    }
    .copy-order-no {
      width: 50px;
      height: 35px;
      color: @grey;
      font-size: 20px;
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
        margin: 25px 50px;
      }
      .consignee-name {
        color: @black;
        font-size: 26px;
        margin: 30px -10px;
      }
      .consignee-phone {
        flex: 1;
        margin: 33px;
        color: @black;
        font-size: 26px;
        text-align: right;
      }
    }
    .consignee-address {
      color: @black;
      font-size: 26px;
      letter-spacing: 1px;
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
        color: @black;
        margin: 20px 0;
        font-size: 28px;
        text-align: left;
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
          color: @black;
          font-size: 24px;
          margin: 30px 0 14px 0;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .product-params {
          color: @black;
          font-size: 24px;
          text-align: left;
          margin-left: 10px;
        }
        .product-price {
          float: left;
          width: 200px;
          font-size: 24px;
          text-align: left;
          margin: 35px 0 0 5px;
          color: @mainColor;
        }
        .product-quantity {
          width: 130px;
          float: right;
          color: @black;
          font-size: 18px;
          margin: 40px 0 0 30px;
        }
      }
    }
    .price-detail {
      .price-detail-box {
        display: flex;
        color: @grey;
        font-size: 26px;
        margin: 20px 29px;
        .price-detail-text {
          text-align: left;
        }
        .price-detail-number {
          flex: 1;
          text-align: right;
        }
      }
    }
    .total-price {
      font-size: 22px;
      color: @greyColor;
      .total-price-detail {
        margin: 30px;
        text-align: left;
      }
      .total-price-total {
        margin: 30px;
        text-align: right;
      }
    }
  }
</style>
