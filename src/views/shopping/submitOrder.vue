<template>
  <div>
    <div class="line-one" v-if="hasAddress"></div>
    <div class="add-address" v-if="!hasAddress" @click="addAddress">
      <span class="add-address-text m-ft-36 m-bg-main-color">+ 添加地址</span>
      <span class="to-add-address m-ft-36 m-bg-main-color">></span>
    </div>
    <div class="order-address" v-if="hasAddress" @click="addAddress">
      <div class="consignee-info">
        <img src="/static/images/order_address.png" class="order-address-img">
        <div class="consignee-name m-ft-26 m-black">收货人： {{address.oirecvname}}</div>
        <div class="consignee-phone m-ft-26 m-black tr">{{address.oirecvphone}}</div>
      </div>
      <div class="consignee-address m-ft-26 m-black">收货地址：{{address.oiaddress}}</div>
    </div>
    <div class="line-one"></div>
    <div class="store-product">
      <div class="store-title">
        <img src="/static/images/store-img.png" class="store-img">
        <div class="store-name m-ft-28 m-black tl">衣百惠</div>
      </div>
      <div class="line-two"></div>
      <template v-for="(item,index) in order">
        <div class="order-product">
          <img :src="item.primage" class="product-img">
          <div class="product-info">
            <div class="product-name m-ft-24 m-black">{{item.prtitle}}</div>
            <div class="product-params m-ft-24 m-black tl">
              <template v-for="(i,j) in item.current_sku.pskproperkey">
                <span>{{i.key}}: {{i.value}}  </span>
              </template>
            </div>
            <span class="product-price m-ft-24 m-red tl">￥{{item.current_sku.pskprice}}</span>
            <span class="product-quantity m-ft-20 m-black">X{{item.scnums}}</span>
          </div>
        </div>
      </template>

      <div class="line-two"></div>
      <p class="user-new">
        <span class="user-new-title m-ft-26 m-grey">使用新衣币</span>
        <new-currency class="new-currency tr"></new-currency>
      </p>
      <div class="line-two"></div>
      <div class="wechat-pay">
        <img src="/static/images/wechat_pay.png" class="wechat-pay-img">
        <span class="wechat-pay-text m-ft-26 m-black tl">微信支付</span>
        <img src="/static/images/icon-radio-active.png" class="wechat-pay-active">
      </div>
      <div class="line-one"></div>
      <p class="order-amount m-ft-26">
        <span class="amount-title m-grey tl">支付金额</span>
        <span class="amount-text m-black">运费： 0</span>
        <span class="amount-text m-black">总计：</span>
        <span class="amount-number m-red">￥{{totalPrice}}</span>
      </p>
      <div class="line-two"></div>
      <div class="buyer-msg">
        <div class="msg-title m-ft-26 m-black tl">买家留言：</div>
        <textarea class="msg-input m-ft-26" v-model="address.oilleavetext" placeholder="选填：建议填写和卖家商量好的内容~" rows="3"></textarea>
      </div>
      <div class="order-pay-box">
        <div class="order-pay m-ft-36 m-bg-main-color" @click="payOrder">支付订单</div>
      </div>
    </div>
  </div>
</template>

<script>
  import newCurrency from "../shopping/components/newCurrency";
 import axios from 'axios';
 import api from '../../api/api';
  export default {
    data() {
      return {
        name: "submitOrder",
        hasAddress: false,
        address:{
          oiaddress: "",
          oirecvname: "",
          oirecvphone: "",
          oilleavetext: "",
        },
        order: {},
        totalPrice:0,
      }
    },
    components: { newCurrency },
    methods: {
      //获取地址
      getInfo(uaid){
        axios.get(api.get_one_address,{
          params:{
            token:localStorage.getItem('token'),
            uaid:uaid
          }
        }).then(res => {
          if(res.data.status == 200){
            if(res.data.data.length == 0){
              this.hasAddress = false;
              return false;
            }else{
              let _arr = res.data.data.addressinfo.reverse();
              let text = '';
              for(let i=0;i<_arr.length;i++){
                text = text + _arr[i].name;
              }
              this.address.oiaddress = text + res.data.data.uatext;
              this.address.oirecvname = res.data.data.uaname;
              this.address.oirecvphone = res.data.data.uaphone;
              this.hasAddress = true;
            }
          }
        })
      },
      // 添加新地址
      addAddress() {
        if(!this.hasAddress) {
          this.$router.push({path:'/editAddress',query:{linkUrl:'/submitOrder',order:this.$route.query.order}});
        }else{
          this.$router.push({path:'/receiverAddress',query:{linkUrl:'/submitOrder',order:this.$route.query.order}});
        }
      },
      // 支付订单
      payOrder() {
        let order = [];
        for(let i =0;i<this.order.length;i++){
          order.push({pskid:this.order[i].current_sku.pskid,num:this.order[i].scnums})
        }
        axios.post(api.create_order+'?token='+localStorage.getItem('token'),{
          oiaddress: this.address.oiaddress,
          oirecvname:  this.address.oirecvname,
          oirecvphone:  this.address.oirecvphone,
          oilleavetext:  this.address.oilleavetext,
          sku:order
        }).then(res => {
          if(res.data.status == 200){
            this.$router.push({path: "/orderPayOK", query: { oiid:res.data.data.oiid,price:this.totalPrice}});
          }
        })

      }
    },
    mounted() {
      this.order = JSON.parse(this.$route.query.order);
      for(let i = 0; i < this.order.length; i++) {
        // 计算单价商品的总价
        this.totalPrice =  this.order[i].current_sku.pskprice *  this.order[i].scnums;
      }
      this.getInfo(this.$route.query.UAid);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/discover";
  @import "../../common/css/index";
  .line-one {
    height: 15px;
    background-color: #f2f5f7;
  }
  .line-two {
    width: 750px;
    height: 2px;
    opacity: 0.3;
    background-color: @grey;
  }
  .add-address {
    height: 88px;
    background-color: #9c94c5;
    .add-address-text {
      line-height: 88px;
    }
    .to-add-address {
      float: right;
      margin: 22px 45px 0 -45px;
    }
  }
  .order-address {
    .consignee-info {
      width: 100%;
      display: flex;
      .order-address-img {
        width: 30px;
        height: 45px;
        margin: 25px 30px 25px 50px;
      }
      .consignee-name {
        margin: 30px -10px;
      }
      .consignee-phone {
        flex: 1;
        margin: 33px;
      }
    }
    .consignee-address {
      letter-spacing: 2px;
      margin: 0 33px 20px 40px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
      text-align: left;
    }
  }
  .store-product {
    .store-title {
      display: flex;
      .store-img {
        width: 40px;
        height: 41px;
        margin: 20px 30px;
      }
      .store-name {
        flex: 1;
        margin: 20px 0;
      }
    }
    .order-product {
      display: flex;
      .product-img {
        width: 160px;
        height: 160px;
        margin: 25px 30px 32px 40px;
      }
      .product-info {
        flex: 1;
        .product-name {
          width: 435px;
          margin: 30px 0 14px 0;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .product-params {
          margin-left: 10px;
        }
        .product-price {
          float: left;
          width: 200px;
          margin: 35px 0 0 5px;
        }
        .product-quantity {
          width: 130px;
          float: right;
          margin: 40px 0 0 30px;
        }
      }
    }
    .user-new {
      display: flex;
      .user-new-title {
        margin: 32px 35px;
      }
      .new-currency {
        flex: 1;
        margin: 30px;
      }
    }
    .wechat-pay {
      display: flex;
      .wechat-pay-img {
        width: 40px;
        height: 30px;
        margin: 38px 20px 40px 50px;
      }
      .wechat-pay-text {
        flex: 1;
        margin-top: 37px;
      }
      .wechat-pay-active {
        width: 35px;
        height: 35px;
        margin: 37px 40px;
      }
    }
    .order-amount {
      display: flex;
      .amount-title {
        flex: 1;
        margin: 32px 30px;
      }
      .amount-text {
        margin: 32px 0 0 20px;
      }
      .amount-number {
        margin: 32px 40px 0 10px;
      }
    }
    .buyer-msg {
      .msg-title {
        margin: 40px 30px;
      }
      .msg-input {
        width: 600px;
        margin-bottom: 230px;
        letter-spacing: 2.5px;
      }
    }
    .order-pay-box {
      bottom: 0;
      position: fixed;
      padding: 40px 25px;
      background-color: #f2f5f7;
      .order-pay {
        width: 140px;
        height: 48px;
        padding: 20px 280px;
        white-space: nowrap;
        letter-spacing: 3px;
        background-color: @mainColor;
      }
    }
  }
</style>
