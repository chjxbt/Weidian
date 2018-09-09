<template>
  <div class="logistics-info">
    <div style="height: 10px"></div>
    <div class="product-info">
      <img src="/static/images/product1.png" class="product-img">
      <div class="product-name m-ft-28 m-grey-color">2018早秋新款大码女装修身新款大码女装修身新款大码女装修身新款大码女装修身新款大码女装修身</div>
    </div>
    <div class="logistics-info-text m-bg-main-color tl">
      <div class="logistics-status m-ft-30">已发货</div>
      <div class="logistics-text m-ft-26">预计明天送达</div>
    </div>
    <div class="got-product">
      <div class="got-product-info tl">
        <div class="info-name m-ft-28">百世快递</div>
        <div class="info-no m-ft-24">运单号：5121522461454145</div>
      </div>
      <div class="info-status m-ft-26">已签收</div>
    </div>
    <div class="got-product">
      <div class="got-product-info tl">
        <div class="info-name m-ft-28">百世快递</div>
        <div class="info-no m-ft-24">运单号：5121522461454145</div>
      </div>
      <div class="info-status m-ft-26 m-red" @click="show_modal = true">换 货</div>
    </div>

    <div class="m-modal" v-if="show_modal">
      <div class="m-modal-state" v-if="!submit_done">
        <div class="m-modal-head m-ft-34 m-black">请 选 择</div>
        <div class="m-modal-cancel m-grey" @click="closeModal">X</div>
        <div class="m-modal-content">
          <div class="content-row">
            <div class="row-left">退</div>
            <div class="row-middle" @click="returnProduct('退')">
              <div class="row-middle-top">退货退款</div>
              <div class="row-middle-bottom">已收到货，需要退回已收到的货</div>
            </div>
            <div class="row-right">></div>
          </div>
          <div class="content-row">
            <div class="row-left">换</div>
            <div class="row-middle" @click="returnProduct('换')">
              <div class="row-middle-top" @click="show_modal = true">换货</div>
              <div class="row-middle-bottom">已收到货，需要更换已收到的货</div>
            </div>
            <div class="row-right">></div>
          </div>
        </div>
      </div>
      <div class="m-modal-state" v-if="submit_done">
        <img class="one-img" src="/static/images/icon-result-personal.png">
        <div class="m-modal-cancel-one m-grey" @click="closeModal">X</div>
        <div class="m-ft-28 m-black m-ft-b">提交成功</div>
        <div class="three-text m-ft-20 m-grey">我们将在3个工作日内完成审核，请及时关注退货状态</div>
        <div class="four-text m-ft-28 m-bg-main-color m-ft-b" @click="closeModal">我知道了</div>
      </div>
    </div>

    <div class="logistics-detail">
      <div class="shipping-address">
        <img src="/static/images/send-ok.png" class="shipping-address-img">
        <div class="shipping-address-text m-ft-24 tl">[收货地址] 浙江省杭州市滨江区 浦沿街道 东信大道1077号 碧水豪园47-2-802</div>
      </div>
      <div class="line-one"></div>
      <ul>
        <li class="detail-row">
          <div class="row-time tr">
            <div class="m-ft-26">08-26</div>
            <div class="m-ft-20">15:04</div>
          </div>
          <div class="row-line-img">
            <img src="/static/images/send-ok.png" class="row-img">
            <!--<div class="line-two"></div>-->
          </div>
          <div class="row-text tl">
            <div class="row-text-title m-ft-26">已发货</div>
            <div class="row-text-content m-ft-24">包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收</div>
          </div>
        </li>
        <div class="see-more" v-if="!moreVisible" @click="seeMore">
          <span class="see-more-text m-ft-20 m-grey tr">查看详细物流信息</span>
          <img src="/static/images/icon-list-down.png" class="see-more-img">
        </div>
      </ul>
      <ul v-if="moreVisible" v-for="item in list">
        <li class="detail-row">
          <div class="row-time tr">
            <div class="m-ft-22 m-grey">{{item.date}}</div>
            <div class="m-ft-22 m-grey">{{item.time}}</div>
          </div>
          <div class="row-line-img">
            <div class="line-two"></div>
            <img src="/static/images/send-ok.png" class="row-img">
          </div>
          <div class="row-text tl">
            <div class="row-text-title m-ft-26 m-grey">{{item.status}}</div>
            <div class="row-text-content m-ft-24 m-grey">{{item.address}}</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  Event = new Vue();
  export default {
    data() {
      return {
        name: "logisticsInfo",
        order: {},
        moreVisible: false,
        show_modal: false,
        submit_done: false,
        list: [
          { date: "08-26", time: "15:04", status: "已发货", address: "包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收" },
          { date: "08-26", time: "15:04", status: "已发货", address: "包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收" },
          { date: "08-26", time: "15:04", status: "已发货", address: "包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收" },
          { date: "08-26", time: "15:04", status: "已发货", address: "包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收" },
          { date: "08-26", time: "15:04", status: "已发货", address: "包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收包裹正在等待揽收" },
        ]
      }
    },
    components: {  },
    methods: {
      // 查看更多物流信息
      seeMore() {
        this.moreVisible = true;
      },
      // 关闭modal
      closeModal() {
        this.show_modal = false;
        this.submit_done = false;
      },
      returnProduct(way) {
        let type = way;
        this.$router.push({path: "/returnProduct", query: { type }});
      },
      // returnProduct页面吃退款信息提交成功后调用
      submitDone() {
        this.show_modal = true;
        this.submit_done = true;
      }
    },
    mounted() {

    },
    created() {
      this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/modal";

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
        margin: 20px 0 0 100px;
        padding-bottom: 20px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
    }
    .logistics-info-text {
      width: 710px;
      margin-left: 20px;
      /*text-align: left;*/
      background-color: @mainColor;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
     .logistics-status {
       padding: 20px 0 10px 40px;
     }
      .logistics-text {
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
        .info-name {
          margin: 30px 0 20px 30px;
        }
        .info-no {
          margin: 0 0 30px 30px;
        }
      }
      .info-status {
        margin: 55px;
      }
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
      opacity: 0.5;
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
          width: 430px;
        }
        .see-more-img {
          width: 20px;
          height: 20px;
          margin: 5px 0 40px 10px;
        }
      }
    }
    .m-modal{
      .m-modal-state{
        height: 460px;
        .m-modal-head{
          display: block;
          padding: 35px 0 25px 0;
        }
        .m-modal-cancel {
          font-size: 30px;
          text-align: right;
          margin: -100px 20px 90px 0;
        }
        .m-modal-content{
          padding: 0;
          .content-row {
            width: 100%;
            display: flex;
            padding: 30px 0;
            border-top: 2px @grey solid;
            .row-left {
              width: 45px;
              height: 40px;
              margin: 30px 30px 0 50px;
              color: @mainColor;
              font-size: 26px;
              border-radius: 50%;
              border: 2px @mainColor solid;
            }
            .row-middle {
              flex: 1;
              .row-middle-top {
                color: @black;
                font-size: 28px;
                text-align: left;
                font-weight: bold;
                margin: 10px 0;
              }
              .row-middle-bottom {
                color: @grey;
                text-align: left;
              }
            }
            .row-right {
              margin: 30px 50px 0 0;
              font-size: 30px;
              color: @greyColor;
            }
          }
        }
        .one-img {
          width: 89px;
          height: 90px;
          margin: 49px 0 25px 0;
        }
        .m-modal-cancel-one {
          font-size: 30px;
          text-align: right;
          margin: -150px 20px 110px 0;
        }
        .three-text {
          width: 60%;
          margin: 30px 20%;
          line-height: 40px;
        }
        .four-text {
          width: 40%;
          padding: 17px 0;
          margin-left: 30%;
          border-radius: 50px;
          background-color: @mainColor;
        }
      }
    }
  }
</style>
