<template>
  <div>
    <img src="/static/images/order_pay_OK.png" class="m-ok-img">
    <p class="pay-text">订单支付成功</p>
    <p class="price-text">￥<span class="price-number">159.00</span></p>
    <p class="order-text">仓库正为您备货中</p>
    <div class="m-btn">
      <div class="m-btn-text" @click="orderDetail">查看订单</div>
      <div class="m-btn-text" @click="returnHome">返回首页</div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "orderPayOK",
        order:{}
      }
    },
    // components: {  },
    methods: {
      // 查看订单
      orderDetail() {
        let order = this.order;
        this.$router.push({path: "/productDetail", query: { order }});
      },
      // 返回首页
      returnHome() {
        this.$router.push('/index');
      }
    },
    created() {
      this.order = this.$route.query.order;
      console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";

  .m-ok-img {
    width: 198px;
    height: 191px;
    margin: 260px 0 70px 0;
  }
  .pay-text {
    color: @black;
    font-size: 40px;
    font-weight: bold;
  }
  .price-text {
    color: @black;
    margin-top: 60px;
    font-weight: bold;
    .price-number {
      font-size: 34px;
    }
  }
  .order-text {
    color: @grey;
    font-size: 30px;
    margin: 20px 0 80px 0;
  }
  .m-btn {
    display: flex;
    .m-btn-text {
      width: 115px;
      font-size: 28px;
      color: @greyColor;
      margin: 0 65px;
      padding: 26px 63px;
      border-radius: 4px;
      white-space: nowrap;
      border: 2px solid @grey;
    }
  }
</style>
