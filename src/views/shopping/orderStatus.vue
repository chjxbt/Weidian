<template>
  <div>
    <!--待支付-->
    <div class="order-status-title" v-if="orderStatus == 1">
      <img src="/static/images/order_time.png" class="order-time-img">
      <div class="order-time">还有 48:00:00 自动关闭交易</div>
    </div>
    <!--付款成功-->
    <div class="order-status-title" v-if="orderStatus == 2">
      <img src="/static/images/pay_ok.png" class="pay-ok-img">
      <div class="order-text-box">
        <div class="pay-ok-text">付款成功</div>
        <div class="ok-title-text">您的包裹马上就去找您</div>
      </div>
    </div>
    <!--已发货-->
    <div class="order-status-title" v-if="orderStatus == 3">
      <div class="order-text-box" style="margin: 10px 40px 0 30px">
        <div class="pay-ok-text">卖家已发货</div>
        <div class="ok-title-text">包裹已在路上，请您耐心等待</div>
      </div>
      <img src="/static/images/send_ok.png" class="send-ok-img">
    </div>
    <!--查看物流-->
    <div class="logistics-page" v-if="orderStatus == 3" @click="checkLogistics">
      <img src="/static/images/truck.png" class="truck-img">
      <div class="logistics-info">
        <p class="logistics-text">包裹已签收，签收人[ 吴伟杰 ]</p>
        <p class="logistics-time">2016.6.28 11:30:10</p>
      </div>
      <img src="/static/images/icon-more.png" class="more-img">
    </div>
    <!--交易完成-->
    <div class="order-status-title" v-if="orderStatus == 4">
      <img src="/static/images/order_ok.png" class="order-ok-img">
      <div class="order-ok-text">交易成功</div>
    </div>
    <!--查看物流-->
    <div class="logistics-page" v-if="orderStatus == 4" @click="checkLogistics">
      <img src="/static/images/truck.png" class="truck-img">
      <div class="logistics-info">
        <p class="logistics-text">包裹已签收，签收人[ 吴伟杰 ]</p>
        <p class="logistics-time">2016.6.28 11:30:10</p>
      </div>
      <img src="/static/images/icon-more.png" class="more-img">
    </div>
    <div class="line"></div>

    <order-product></order-product>

    <div class="order-btns">
      <img src="/static/images/product_detail_service.png" class="service-img" @click="service">
      <div class="service-text" @click="service">客服</div>
      <div class="complaints-text" @click="complaints">投诉</div>

      <!--待支付-->
      <div v-if="orderStatus == 1" class="btn-box">
        <div class="cancel-order" @click="cancelOrder">取消订单</div>
        <div class="to-pay" @click="toPay">立即支付</div>
      </div>
      <!--已发货-->
      <div v-if="orderStatus == 3" class="btn-box">
        <div class="cancel-order" @click="delayReceiving">延迟收货</div>
        <div class="to-pay" @click="confirmReceiving">确认收货</div>
      </div>
      <!--交易完成-->
      <div v-if="orderStatus == 4" class="btn-box">
        <div class="cancel-order" @click="deleteOrder">删除订单</div>
        <div class="to-pay" @click="toEvaluation">评 价</div>
      </div>

    </div>

    <div class="line"></div>
    <div class="order-time-box" @click="change">
      <p class="order-time-text">订单交易时间</p>
      <div class="order-create-time" v-for="item in timeList">{{item}}</div>
    </div>
    <div class="line-three"></div>

  </div>
</template>

<script>
  import orderProduct from "../../components/common/orderProduct";

  export default {
    data() {
      return {
        name: "orderStatus",
        order: {},
        // 待支付：1，付款成功：2，已发货：3，交易完成：4
        orderStatus: 4,
        timeList: ["创建时间：2018-08-16 14:28:58", "付款时间：2018-08-16 18:28:58", "发货时间：2018-08-16 20:28:58"]
      }
    },
    components: { orderProduct },
    methods: {
      // 测试方法
      change() {
        if(this.orderStatus == 4) {
          this.orderStatus = 1;
        }else {
          this.orderStatus += 1;
        }
        console.log(this.orderStatus);
      },
      // 客服
      service() {

      },
      // 投诉
      complaints() {

      },
      // 取消订单
      cancelOrder() {

      },
      // 立即支付
      toPay() {

      },
      // 延迟收货
      delayReceiving() {

      },
      // 确认收货
      confirmReceiving() {

      },
      // 删除订单
      deleteOrder() {

      },
      // 评 价
      toEvaluation() {

      },
      // 查看物流
      checkLogistics() {

      }
    },
    created() {
      this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
  .order-status-title {
    display: flex;
    background-color: #f53b52;
    .order-time-img {
      width: 38px;
      height: 38px;
      padding: 21px 31px;
    }
    .order-time {
      font-size: 24px;
      color: @bgMainColor;
      margin-top: 22px;
    }
    .pay-ok-img {
      width: 50px;
      height: 50px;
      margin: 55px;
    }
    .order-text-box {
      color: @bgMainColor;
      text-align: left;
      .pay-ok-text {
        font-size: 36px;
        margin: 30px 0 15px 10px;
      }
      .ok-title-text {
        margin-left: 10px;
      }
    }
    .send-ok-img {
      width: 100px;
      height: 100px;
      margin: 50px;
    }
    .order-ok-img {
      width: 80px;
      height: 64px;
      margin: 70px 30px 0 220px;
    }
    .order-ok-text {
      font-size: 40px;
      margin: 75px 0;
      color: @bgMainColor;
    }
  }
  .logistics-page {
    display: flex;
    .truck-img {
      width: 45px;
      height: 33px;
      margin: 50px 30px;
    }
    .logistics-info {
      flex: 1;
      font-size: 26px;
      text-align: left;
      .logistics-text {
        margin: 20px 0 0 20px;
        color: #28C222;
      }
      .logistics-time {
        margin: 20px 0 10px 20px;
      }
    }
    .more-img {
      width: 21px;
      height: 35px;
      margin: 50px;
    }
  }
  .order-btns {
    display: flex;
    .service-img {
      width: 52px;
      height: 45px;
      margin: 28px 40px;
    }
    .service-text {
      color: #e12f24;
      font-size: 26px;
      font-weight: bold;
      margin: 28px -10px;
    }
    .complaints-text {
      width: 190px;
      color: @grey;
      font-size: 26px;
      font-weight: bold;
      margin-top: 28px;
    }
    .btn-box {
      display: flex;
      .cancel-order {
        color: @black;
        font-size: 24px;
        margin: 20px 10px;
        padding: 10px 36px;
        border-radius: 25.5px;
        border: solid 2px @greyColor;
      }
      .to-pay {
        font-size: 24px;
        color: @mainColor;
        margin: 20px 10px;
        padding: 10px 36px;
        border-radius: 25.5px;
        border: solid 2px @mainColor;
      }
    }
  }
  .line {
    height: 25px;
    background-color: #f2f5f7;
  }
  .line-three {
    width: 750px;
    height: 117px;
    background-color: #f2f5f7;
  }
  .order-time-box {
    font-size: 24px;
    text-align: left;
    margin: 30px 0 20px 40px;
    .order-time-text {
      color: @black;
      font-weight: bold;
      .order-create-time {
        color: @greyColor;
      }
    }
  }
</style>
