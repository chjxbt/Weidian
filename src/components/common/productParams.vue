<template>
  <div class="product-params">
    <div class="product-params-show" @click="productParams">
      <span class="product-params-detail">尺寸：{{size}}</span><span class="product-params-detail">颜色：{{color}}</span>
      <img v-if="popupVisible" src="../../../static/images/icon-list-down.png" class="list-right-down">
      <img v-if="!popupVisible" src="../../../static/images/icon-list-right.png" class="list-right-down">
    </div>
    <mt-popup v-model="popupVisible" position="bottom">
      <div class="product-params-content">
        <img src="/static/images/product1.png" class="product-img">
        <div class="product-params-center">
          <p class="product-price">￥<span class="product-price-number">160</span></p>
          <div class="choose-prompt">请选择颜色、尺码</div>
        </div>
        <img src="/static/images/delete.png" class="close-popup">
      </div>
      <div class="line"></div>
      <div class="product-size-color">
        <div class="product-size-color-text">颜色</div>
        <div class="product-choose-button" v-for="item in colorList" :key="item.id">{{item}}</div>
      </div>
      <div class="line"></div>
      <div class="product-size-color">
        <div class="product-size-color-text">尺码</div>
        <div class="product-choose-button" v-for="item in sizeList" :key="item.id">{{item}}</div>
      </div>
      <div class="line"></div>
      <div class="product-quantity">
        <div class="product-quantity-text">购买数量</div>
        <product-quantity :quantity="quantity" class="product-quantity-edit"></product-quantity>
      </div>
      <div class="choose-done">确定</div>
    </mt-popup>
  </div>
</template>

<script>
  import productQuantity from "../../components/common/productQuantity";
  export default {
    data() {
      return {
        name: 'productParams',
        popupVisible: false,
        sizeList: ["S", "M", "L", "XL", "XXL", "XXL"],
        colorList: ["黄色", "绿色", "红色"]
      }
    },
    components: { productQuantity },
    props:{
      size:{
        type: String,
        default: null
      },
      color:{
        type: String,
        default: null
      },
      quantity:{
        type: Number,
        default: 1
      }
    },
    methods: {
      productParams() {
        if(this.popupVisible) {
          this.popupVisible = false;
        }else if(!this.popupVisible) {
          this.popupVisible = true;
        }
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/_variate";

  .product-params {
    .product-params-show {
      .product-params-detail {
        float: left;
        color: @grey;
        font-size: 22px;
        margin: 8px 20px 10px 0;
      }
      .list-right-down {
        width: 22px;
        height: 22px;
        margin-top: 14px;
        margin-left: -60px;
      }
    }
    .product-params-content {
      width: 750px;
      height: 160px;
      display: flex;
      .product-img {
        width: 220px;
        height: 220px;
        margin: -90px 0 0 40px;
      }
      .product-params-center {
        flex: 1;
        margin: 15px 0 0 35px;
        .product-price {
          font-size: 20px;
          text-align: left;
          font-weight: bold;
          color: @mainColor;
          .product-price-number {
            font-size: 34px;
          }
        }
        .choose-prompt {
          font-size: 26px;
          text-align: left;
        }
      }
      .close-popup {
        width: 34px;
        height: 34px;
        margin: 22px 22px;
      }
    }
    .product-size-color {
      height: 150px;
      .product-size-color-text {
        padding: 0 0 30px 40px;
        font-size: 30px;
        text-align: left;
      }
      .product-choose-button {
        float: left;
        font-size: 26px;
        padding: 8px 20px;
        margin: 0 -20px 0 40px;
        border-radius: 10px;
        background-color: #f4f3f9;
      }
    }
    .line {
      height: 2px;
      width: 696px;
      margin: 0 30px 20px 40px;
      background-color: @grey;
    }
    .product-quantity {
      .product-quantity-text {
        width: 535px;
        font-size: 30px;
        text-align: left;
        margin: 20px 0 40px 40px;
      }
      .product-quantity-edit {
        width: 205px;
        margin-top: 20px;
      }
    }
    .choose-done {
      padding: 30px;
      font-size: 28px;
      color: @bgMainColor;
      letter-spacing: 10px;
      background-color: @mainColor;
    }
  }
</style>
