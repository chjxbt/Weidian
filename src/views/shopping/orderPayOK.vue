<template>
  <div>
    <img src="/static/images/order_pay_OK.png" class="m-ok-img">
    <p class="m-ft-40 m-black m-ft-b">订单支付成功</p>
    <p class="price-text m-black m-ft-b">￥<span class="m-ft-34">159.00</span></p>
    <p class="order-text m-ft-30 m-grey">仓库正为您备货中</p>
    <div class="m-btn">
      <div class="m-btn-text m-ft-28 m-grey-color" @click="orderDetail">查看订单</div>
      <div class="m-btn-text m-ft-28 m-grey-color" @click="returnHome">返回首页</div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "orderPayOK",
        order: {}
      }
    },
    // components: {  },
    methods: {
      // 查看订单
      orderDetail() {
        let order = this.order;
        this.$router.push({path: "/orderStatus", query: { order }});
      },
      // 返回首页
      returnHome() {
        this.$router.push('/index');
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

  .m-ok-img {
    width: 198px;
    height: 191px;
    margin: 260px 0 70px 0;
  }
  .price-text {
    margin-top: 60px;
  }
  .order-text {
    margin: 20px 0 80px 0;
  }
  .m-btn {
    display: flex;
    .m-btn-text {
      width: 115px;
      margin: 0 65px;
      padding: 26px 63px;
      border-radius: 4px;
      white-space: nowrap;
      border: 2px solid @grey;
    }
  }
</style>
