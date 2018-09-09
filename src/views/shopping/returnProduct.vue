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
      <div class="reason-choose-text m-ft-28 m-grey">请选择&nbsp;&nbsp;&nbsp;></div>
    </div>

    <div class="m-modal" v-if="choose_show">
      <div class="m-modal-state">
        <div class="modal-row-one">
          <div class="row-one-text m-grey tl" @click="choose_show = false">取消</div>
          <div class="row-one-text tr" @click="reasonDone">确定</div>
        </div>
        <mt-picker :slots="slots" @change="onValuesChange"></mt-picker>
      </div>
    </div>

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
  import { Picker } from 'mint-ui';

  export default {
    name: "returnProduct",
    data() {
      return {
        value: "",
        choose_show: false,
        slots: [
          { values: ["七天无理由", "质量差", "衣服质量差", "上身效果差", "不值"] }
        ],
        reason: ""
      }
    },
    methods: {
      // 退货原因选择器-确定
      reasonDone() {
        this.choose_show = false;
        console.log(this.reason);
      },
      // 监听退货原因选择器
      onValuesChange(picker, values) {
        this.reason = values[0];
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
  @import "../../common/css/modal";

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
      margin: 0 0 0 60%;
    }
  }
  .m-modal {
    .m-modal-state {
      width: 100%;
      height: 500px;
      position: absolute;
      top: 75%;
      .modal-row-one {
        width: 100%;
        display: flex;
        .row-one-text {
          flex: 1;
          font-size: 30px;
          margin: 15px 30px;
        }
      }
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
