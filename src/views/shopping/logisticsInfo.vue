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
      <div class="shipping-address">
        <img src="/static/images/send-ok.png" class="shipping-address-img">
        <div class="shipping-address-text">[收货地址] 浙江省杭州市滨江区 浦沿街道 东信大道1077号 碧水豪园47-2-802</div>
      </div>
      <div class="line-one"></div>
      <ul>
        <li class="detail-row">
          <div class="row-time">
            <div class="m-ft-26">08-26</div>
            <div class="m-ft-20">15:04</div>
          </div>
          <div class="row-line-img">
            <img src="/static/images/send-ok.png" class="row-img">
            <!--<div class="line-two"></div>-->
          </div>
          <div class="row-text">
            <div class="row-text-title m-ft-26">已发货</div>
            <div class="row-text-content m-ft-24">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
        <div class="see-more" v-if="!moreVisible" @click="seeMore">
          <span class="see-more-text m-ft-20 grey">查看详细物流信息</span>
          <img src="/static/images/icon-list-down.png" class="see-more-img">
        </div>
      </ul>
      <ul v-if="moreVisible">
        <li class="detail-row">
          <div class="row-time">
            <div class="m-ft-22 grey">08-26</div>
            <div class="m-ft-22 grey">15:04</div>
          </div>
          <div class="row-line-img">
            <div class="line-two"></div>
            <img src="/static/images/send-ok.png" class="row-img">
          </div>
          <div class="row-text">
            <div class="row-text-title m-ft-26 grey">已发货</div>
            <div class="row-text-content m-ft-24 grey">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
        <li class="detail-row">
          <div class="row-time">
            <div class="m-ft-22 grey">08-26</div>
            <div class="m-ft-22 grey">15:04</div>
          </div>
          <div class="row-line-img">
            <div class="line-two"></div>
            <img src="/static/images/send-ok.png" class="row-img">
          </div>
          <div class="row-text">
            <div class="row-text-title m-ft-26 grey">已发货</div>
            <div class="row-text-content m-ft-24 grey">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
        <li class="detail-row">
          <div class="row-time">
            <div class="m-ft-22 grey">08-26</div>
            <div class="m-ft-22 grey">15:04</div>
          </div>
          <div class="row-line-img">
            <div class="line-two"></div>
            <img src="/static/images/send-ok.png" class="row-img">
          </div>
          <div class="row-text">
            <div class="row-text-title m-ft-26 grey">已发货</div>
            <div class="row-text-content m-ft-24 grey">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
        <li class="detail-row">
          <div class="row-time">
            <div class="m-ft-22 grey">08-26</div>
            <div class="m-ft-22 grey">15:04</div>
          </div>
          <div class="row-line-img">
            <div class="line-two"></div>
            <img src="/static/images/send-ok.png" class="row-img">
          </div>
          <div class="row-text">
            <div class="row-text-title m-ft-26 grey">已发货</div>
            <div class="row-text-content m-ft-24 grey">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "logisticsInfo",
        order: {},
        moreVisible: false
      }
    },
    components: {  },
    methods: {
      // 查看更多物流信息
      seeMore() {
        this.moreVisible = true;
      }
    },
    created() {
      this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  .logistics-info {
    padding-bottom: 50px;
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
    }
    .grey {
      color: @grey;
    }
    .red {
      color: @mainColor;
    }
    .line-one {
      width: 10px;
      height: 60px;
      margin: -50px 0 2px 117px;
      border-left: 2px dashed @grey;
    }
    .line-two {
      width: 2px;
      height: 106px;
      background-color: @grey;
      margin: -110px 0 0 20px;
    }
    .logistics-detail {
      width: 710px;
      margin: 20px;
      border-radius: 20px;
      background-color: @bgMainColor;
      .shipping-address {
        display: flex;
        .shipping-address-img {
          width: 40px;
          height: 40px;
          margin: 50px 0 0 100px;
        }
        .shipping-address-text {
          flex: 1;
          margin: 40px 40px 40px 20px;
          font-size: 24px;
          text-align: left;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          overflow: hidden;
        }
      }
      .detail-row {
        display: flex;
        .row-time {
          width: 67px;
          text-align: right;
          margin: 0 10px 0 20px;
        }
        .row-line-img {
          .row-img {
            width: 40px;
            height: 40px;
          }
        }
        .row-text {
          flex: 1;
          margin: 0 40px 40px 20px;
          text-align: left;
          .row-text-title {
            margin-bottom: 10px;
          }
          .row-text-content {
            display: -webkit-box;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 2;
            overflow: hidden;
          }
        }
      }
      .see-more {
        display: flex;
        .see-more-text {
          width: 450px;
          text-align: right;
        }
        .see-more-img {
          width: 20px;
          height: 20px;
          margin: 5px 0 40px 10px;
        }
      }
    }
  }
</style>
