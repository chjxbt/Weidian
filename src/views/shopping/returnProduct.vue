<template>
  <div class="m-return-content">
    <div class="product-info" v-if="product_info">
      <img class="product-img" :src="product_info.opiproductimages">
      <div class="product-info-right">
        <div class="product-name m-ft-26 tl">{{product_info.opiproductname}}</div>
        <div class="product-params m-grey tl">
          <template v-for="(i,j) in product_info.pskproperkey">
          <span>{{i.key}}: {{i.value}}  </span>
        </template>
        </div>
      </div>
    </div>
    <div class="return-address">
      <div class="m-ft-30 m-black tl">退货地址：</div>
      <div class="address-two">
        <div class="address-people address-text">收货人：<input type="text" class="m-input" placeholder="请输入收件人姓名"></div>
        <div class="address-phone address-text">电话：<input type="text" class="m-input" placeholder="请输入收件人电话"></div>
      </div>
      <div class="address-text">地址：<input type="text" class="m-input-l" placeholder="请输入收件人地址"></div>
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
      <div class="input-box m-ft-28">
        <input class="money-input m-red" :class="value != ''?'active':''" type="text" v-model="value" placeholder="请输入退款金额" />
      </div>
    </div>
    <div class="return-text-box">
      <div class="m-ft-24 m-grey tl">最多￥21.90</div>
      <div class="text-two">
        <div class="m-ft-26 tl">如未收到货，请联系客服退款</div>
        <div class="text-right m-ft-26 m-bg-main-color" @click="service">！</div>
      </div>
    </div>
    <div class="return-memo">
      <div class="m-ft-28 m-black tl">退款说明：</div>
      <div class="input-box m-ft-28">
        <input class="money-input" type="text" v-model="memo" placeholder="选填" />
      </div>
    </div>

    <div class="upload-picture">
      <div class="m-ft-28 tl">上传凭证</div>
      <input class="picture-file" type="file">
      <div class="choose-picture">
        <img class="picture-logo" src="/static/images/product1.png" alt="">
        <div class="m-grey">上传凭证</div>
        <div class="m-grey">(最多6张)</div>
      </div>
    </div>

    <div class="return-memo">
      <div class="m-ft-28 m-black tl">快递公司：</div>
      <div class="input-box m-ft-28">
        <input class="money-input" type="text" v-model="courierCompany" placeholder="请填写退货快递公司" />
      </div>
    </div>
    <div class="return-memo margin-bottom">
      <div class="m-ft-28 m-black tl">快递单号：</div>
      <div class="input-box m-ft-28">
        <input class="money-input" type="text" v-model="courierNo" placeholder="请填写退货快递单号" />
      </div>
    </div>
    <div class="submit-text m-ft-36 m-bg-main-color" @click="submitReturn">提交</div>
  </div>
</template>

<script>
  // import { Picker } from 'mint-ui';
 import axios from 'axios';
 import api from '../../api/api'
  export default {
    name: "returnProduct",
    data() {
      return {
        value: "",
        choose_show: false,
        slots: [
          { values: ["七天无理由", "质量差", "衣服质量差", "上身效果差", "不值"] }
        ],
        reason: "",
        memo: "",
        courierCompany: "",
        courierNo: "",
        product_info:null,
        address_info:null
      }
    },
    mounted(){
      this.getOrderInfo()
    },
    methods: {
      //获取订单详情
      getOrderInfo(){
        axios.get(api.get_order_info,{
          params:{
            token: localStorage.getItem('token'),
            oiid: this.$route.query.oiid
          }
        }).then(res => {
          if(res.data.status == 200){
            for(let i=0;i<res.data.data.productinfo.length;i++){
              if(res.data.data.productinfo[i].prid == this.$route.query.prid){
                this.product_info = res.data.data.productinfo[i]
              }
            }
            this.address_info = res.data.data;
          }
        })
      },
      // 退货原因选择器-确定
      reasonDone() {
        this.choose_show = false;
        console.log(this.reason);
      },
      // 监听退货原因选择器
      onValuesChange(picker, values) {
        this.reason = values[0];
      },
      // 退款说明的感叹号
      service() {
        console.log();
      },
      // 提交
      submitReturn() {
        this.$router.go(-1);
      }
    },
    created() {
      let type = this.$route.query.type;
      // console.log("type", type);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/modal";

  input::-webkit-input-placeholder {
    font-size: 24px;
    line-height: 28px;
  }
.m-return-content{
  width: 100%;
  overflow-x: hidden;
}
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
      .flex-row(flex-start);
      input{
        width: 200px;
        &.m-input-l{
          width: 560px;
          display: inline-block;
        }
      }
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
  }
  .input-box {
    width: 350px;
    height: 40px;
    margin-left: 10px;
    border-radius: 10px;
    // border: 2px @grey solid;
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
  .return-text-box {
    padding: 20px 30px;
    background-color: #f3f3f3;
    .text-two {
      width: 100%;
      display: flex;
      margin: 10px 0;
      .text-right {
        width: 25px;
        height: 35px;
        border-radius: 50%;
        padding-left: 10px;
        margin-left: 20px;
        background-color: @mainColor;
      }
    }
  }
  .return-memo {
    width: 100%;
    display: flex;
    padding: 20px 30px 20px 30px;
  }
  .upload-picture {
    padding: 30px;
    border-top: 16px #f3f3f3 solid;
    border-bottom: 16px #f3f3f3 solid;
    .choose-picture {
      width: 18%;
      padding: 30px;
      margin-top: 20px;
      border:2px @grey dashed;
      .picture-logo {
        width: 60px;
        height: 50px;
      }
    }
    .picture-file {
      position: absolute;
      overflow: hidden;
      left: 30px;
      top: 918px;
      width: 25%;
      height: 180px;
      opacity: 0;
    }
  }
  .margin-bottom {
    margin-bottom: 100px;
  }
  .submit-text {
    position: fixed;
    bottom: 0;
    width: 100%;
    padding: 20px 0;
    letter-spacing: 30px;
    background-color: @mainColor;
  }
</style>
