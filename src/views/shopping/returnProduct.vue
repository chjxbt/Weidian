<template>
  <div>
    <div class="product-info">
      <img class="product-img" src="/static/images/product1.png">
      <div class="product-info-right">
        <div class="product-name m-ft-26 tl">商品名称商品名称商品名称商品名称商品名称商品名称商品名称商品名称100商品名称商品名称商品名称商品名称商品名称商品名称商品名称商品名称商品名称商品名称</div>
        <div class="product-params m-grey tl">规格：M-中型</div>
      </div>
    </div>
    <div class="return-address">
      <div class="m-ft-30 m-black tl">退货地址：</div>
      <div class="address-two">
        <div class="address-people address-text">收货人：XXX</div>
        <div class="address-phone address-text">电话：12345678912</div>
      </div>
      <div class="address-text">地址：浙江省 杭州市 滨江区 浦沿街道新城路33号 只是控股 创客空间</div>
    </div>
    <div class="return-reason" @click="choose_show = true">
      <div class="m-ft-28 m-black tl">退款原因</div>
      <div class="reason-choose-text m-ft-28 m-grey">请选择</div>
      <div class="return-reason-choose m-ft-32 m-grey">></div>
    </div>
    <mt-actionsheet :actions="actions" v-model="choose_show"></mt-actionsheet>
    <div class="return-money">
      <div class="m-ft-28 m-black tl">退款金额：</div>
      <div class="m-ft-28 m-red">￥</div>
      <div class="input-box">
        <input class="money-input m-red" :class="value != ''?'active':''" type="text" v-model="value" placeholder="请输入退款金额" />
      </div>
    </div>
  </div>
</template>

<script>
  import { Actionsheet } from 'mint-ui';
  export default {
    name: "returnProduct",
    data() {
      return {
        value: "",
        actions: [
          { name: "质量差", method: "reason" }, { name: "七天无理由", method: "reason" }, { name: "衣服质量差", method: "reason" },
          { name: "上身效果差", method: "reason" }, { name: "不值", method: "reason" }
        ],
        choose_show: false
      }
    },
    methods: {
      reason(e) {
        console.log(e);
      }
    },
    created() {
      let type = this.$route.query.type;
      console.log("type", type);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .product-info {
    width: 100%;
    display: flex;
    padding: 30px;
    border-bottom: 2px #E5E5E5 solid;
    .product-img {
      width: 150px;
      height: 150px;
    }
    .product-info-right {
      flex: 1;
      .product-name {
        padding-right: 30px;
        margin: 0 30px 20px 30px;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
        overflow: hidden;
      }
      .product-params {
        margin-left: 30px;
      }
    }
  }
  .return-address {
    padding: 30px 50px;
    border-bottom: 16px #f3f3f3 solid;
    .address-two {
      width: 100%;
      display: flex;
      padding: 15px 0;
      .address-people {
        width: 50%;
      }
      .address-phone {
        width: 50%;
      }
    }
    .address-text {
      color: @black;
      font-size: 26px;
      text-align: left;
    }
  }
  .return-reason {
    width: 100%;
    display: flex;
    padding: 20px 30px;
    .reason-choose-text {
      margin: 0 20px 0 60%;
    }
  }
  .return-money {
    width: 100%;
    display: flex;
    padding: 10px 30px 20px 30px;
    .input-box {
      width: 350px;
      height: 40px;
      margin-left: 10px;
      border-radius: 10px;
      border: 2px @grey solid;
      .money-input {
        width: 330px;
        padding: 0 10px;
        line-height: 40px;
        &.active{
          font-size: 28px;
          color: @mainColor;
        }
      }
    }
  }
</style>
