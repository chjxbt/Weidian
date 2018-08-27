<template>
  <div class="logistics-info">
    <div style="height: 10px"></div>
    <div class="product-info">
      <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="product-img">
      <div class="product-name">2018早秋新款大码女装修身新款大码女装修身新款大码女装修身新款大码女装修身新款大码女装修身</div>
    </div>
    <div class="logistics-info-text">
      <div class="logistics-status">已发货</div>
      <div class="logistics-text">预计明天送达</div>
    </div>
    <div class="got-product">
      <div class="got-product-info">
        <div class="info-name">百世快递</div>
        <div class="info-no">运单号：5121522461454145</div>
      </div>
      <div class="info-status">已签收</div>
    </div>
    <div class="got-product">
      <div class="got-product-info">
        <div class="info-name">百世快递</div>
        <div class="info-no">运单号：5121522461454145</div>
      </div>
      <div class="info-status red">换货</div>
    </div>
    <div class="logistics-detail">

    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "logisticsInfo",
        order: {},

      }
    },
    components: {  },
    methods: {

    },
    created() {
      this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
  .logistics-info {
    background-color: #F2F2F2;
    .product-info {
      width: 710px;
      margin-left: 20px;
      border-top-left-radius: 20px;
      border-top-right-radius: 20px;
      background-color: @bgMainColor;
      .product-img {
        width: 180px;
        height: 180px;
        margin-top: 80px;
        border-radius: 15px;
      }
      .product-name {
        width: 510px;
        font-size: 28px;
        margin: 20px 0 0 100px;
        padding-bottom: 20px;
        color: @greyColor;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
    }
    .logistics-info-text {
      width: 710px;
      margin-left: 20px;
      text-align: left;
      color: @bgMainColor;
      background-color: @mainColor;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
     .logistics-status {
       font-size: 30px;
       padding: 20px 0 10px 40px;
     }
      .logistics-text {
        font-size: 26px;
        padding: 0 0 20px 40px;
      }
    }
    .got-product {
      width: 710px;
      display: flex;
      margin-top: 20px;
      margin-left: 20px;
      border-radius: 20px;
      background-color: @bgMainColor;
      .got-product-info {
        flex: 1;
        text-align: left;
        .info-name {
          font-size: 28px;
          margin: 30px 0 20px 30px;
        }
        .info-no {
          font-size: 24px;
          margin: 0 0 30px 30px;
        }
      }
      .info-status {
        font-size: 26px;
        margin: 55px;
      }
      .grey {
        color: @grey;
      }
      .red {
        color: @mainColor;
      }
    }
    .logistics-detail {

    }
  }
</style>
