<template>
  <div class="m-order-product">
    <div class="order-no-box">
      <div class="order-no m-ft-26 m-black tl">订单号：{{order.oiid}}</div>
      <div class="copy-order-no m-ft-20 m-grey" @click="copyText">复制</div>
    </div>
    <div class="line-one"></div>
    <div class="order-address">
      <div class="consignee-info">
        <img src="/static/images/order_address.png" class="order-address-img">
        <div class="consignee-name m-ft-26 m-black">收货人： {{order.oirecvname}}</div>
        <div class="consignee-phone m-ft-26 m-black tr">{{order.oirecvphone}}</div>
      </div>
      <div class="consignee-address m-ft-26 m-black">收货地址：{{order.oiaddress}}</div>
    </div>
    <div class="line-two"></div>
    <div class="store-product">
      <div class="store-title">
        <img src="/static/images/store-img.png" class="store-img">
        <div class="store-name m-ft-28 m-black tl"><span>衣百惠</span><span class="m-red">{{order.order_status}}</span></div>
      </div>
      <div class="line-one"></div>
      <template v-for="(item,index) in order.productinfo">
        <div class="order-product">
          <img src="http://img1.imgtn.bdimg.com/it/u=661395716,3070712851&fm=214&gp=0.jpg" class="product-img">
          <div class="product-info">
            <div class="product-name m-ft-24 m-black">
              <span class="name">{{item.opiproductname}}</span>
              <span @click.stop="changeProduct(index)">退/换</span>
            </div>
            <div class="product-params m-ft-24 m-black tl">
              <template v-for="(i,j) in item.pskproperkey">
                <span>{{i.key}}: {{i.value}}  </span>
              </template>
            </div>
            <span class="product-price m-ft-24 m-red tl">￥ {{item.oiproductprice}}</span>
            <span class="product-quantity m-ft-20 m-black">X{{item.opiproductnum}}</span>
          </div>
        </div>
      </template>

      <div class="line-one"></div>
      <div class="price-detail">
        <p class="price-detail-box m-ft-26 m-grey">
          <span class="price-detail-text tl">商品总价</span>
          <span class="price-detail-number tr">￥{{order.oimount}}</span>
        </p>
        <!--<p class="price-detail-box m-ft-26 m-grey">-->
          <!--<span class="price-detail-text tl">使用新衣币</span>-->
          <!--<span class="price-detail-number tr">-￥3.00</span>-->
        <!--</p>-->
      </div>
      <div class="line-one"></div>
      <div class="total-price m-ft-22 m-grey-color">
        <div class="total-price-detail tl">总计￥{{order.oimount}} 运费￥0</div>
        <div class="total-price-total tr">共2件商品 合计￥{{order.oimount}}</div>
      </div>
      <div class="line-one"></div>
    </div>
    <div class="m-change-modal" v-if="show_change" @click.stop="closeModel('show_change')">
      <div class="m-change-modal-state">
        <div class="m-change-modal-head">
          <span @click.stop="closeModel('show_change')">X</span>
        </div>
        <div class="m-change-modal-content">
          <p class="m-change-head">请选择</p>
          <ul class="m-change-ul">
            <li @click.stop="changeState">
              <span class="m-icon"></span>
              <div class="m-change-text">
                <p>退货退款</p>
                <p class="m-grey">已收到货，需要退掉已收到的货物</p>
              </div>
              <span class="m-icon-more"> </span>
            </li>
            <li>
              <span class="m-icon"></span>
              <div class="m-change-text">
                <p>换货</p>
                <p class="m-grey">已收到货，需要更换已收到的货物</p>
              </div>
              <span class="m-icon-more"> </span>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="m-modal" v-if="show_modal" @click.stop="closeModel('show_modal')">
      <div class="m-modal-state">
        <div class="m-modal-content">
          <img src="" class="m-apply-success" alt="">
          <p class="m-ft-30 m-ft-b">提交成功</p>
          <div class="m-apply-result-info">
            我们将在3个工作日内完成审核，
            请及时关注退货状态。
          </div>
          <div class="m-apply-result-btn">
            <span @click.stop="closeModel('show_modal')">我知道了</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui';
  export default {
    data() {
      return {
        name: "orderProduct",
        show_change:false,
        select:null,
        show_modal:false
      }
    },
    props:{
      order:{
        type:Object,
        default:null
      }
    },
    // components: {  },
    methods: {
      // 复制
      copyText() {
        let link = "订单号";
        this.$copyText(this.order.oiid).then(function (e) {
          Toast({ message: "复制成功", className: 'm-toast-success' });
        })
      },
      changeProduct(index){
        this.show_change =true;
        this.select = this.order.productinfo[index];
      },
      closeModel(v){
        this[v] =false;
        this.select = null
      },
      changeState(){
          // this.$router.push({path:'/returnProduct',query:{oiid:this.order.oiid,prid:this.select.prid}})
        this.show_change =false;
        this.show_modal =true
      }
    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  @import "../../../common/css/modal";
  .order-no-box {
    display: flex;
    flex-flow: row;
    justify-content: space-between;
    padding: 0 20px;
    .order-no {
      margin: 35px 0 20px 0;
      white-space: nowrap;
    }
    .copy-order-no {
      width: 50px;
      height: 35px;
      padding: 5px 21px;
      white-space: nowrap;
      margin: 28px 0 0 25px;
      border-radius: 6px;
      border: solid 2px @grey;
    }
  }
  .line-one {
    width: 710px;
    height: 2px;
    opacity: 0.3;
    margin: 0 20px;
    background-color: @grey;
  }
  .line-two {
    height: 15px;
    background-color: #f2f5f7;
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
      letter-spacing: 1px;
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
        padding-right:20px;
        display: flex;
        flex-flow: row;
        justify-content: space-between;
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
          display: flex;
          flex-flow: row;
          justify-content: space-between;
          margin: 30px 0 14px 0;
          padding-right: 20px ;
          .name{
            width: 365px;
            text-align: left;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
          }
        }
        .product-params {
          /*margin-left: 10px;*/
        }
        .product-price {
          float: left;
          width: 200px;
          margin: 35px 0 0 0;
        }
        .product-quantity {
          width: 130px;
          float: right;
          margin: 40px 0 0 30px;
        }
      }
    }
    .price-detail {
      .price-detail-box {
        display: flex;
        margin: 20px 29px;
        .price-detail-number {
          flex: 1;
        }
      }
    }
    .total-price {
      .total-price-detail {
        margin: 30px;
      }
      .total-price-total {
        margin: 30px;
      }
    }
  }
  .m-change-modal{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0,0,0,0.2);
    z-index: 1001;
    transition: opacity .5s;
    .m-change-modal-state{
      background-color: #fff;
      position: absolute;
      width: 600px;
      height: 415px;
      top: 0;
      left: 0;
      right:0;
      bottom:0;
      margin: auto;
      border: 1px solid @borderColor;
      border-radius: 10px;
      -webkit-transition: height 0.88s;
      transition: height 0.88s;
      .m-change-modal-head{
        padding: 10px 20px;
        width: 93%;
        margin: 0!important;
        text-align: right;
      }
      .m-change-head{
        font-size: 34px;
        margin-bottom: 40px;
      }
      .m-change-ul{
        width: 100%;
        li{
          padding: 20px 0;
          border-top: 1px solid @borderColor;
          .flex-row(flex-start);
          text-align: left;
          .m-icon{
            display: block;
            width: 35px;
            height: 35px;
            margin: 0 40px 30px;
            background: url("/static/images/back.png") no-repeat  center top;
            background-size: 100%;

          }
          .m-icon-more{
            display: block;
            width: 10px;
            height: 15px;
            margin: 0 20px;
            background: url("/static/images/icon-more.png") no-repeat  center;
            background-size: 100% 100%;
          }
          .m-change-text{
            width: 460px;
            line-height: 36px;
          }
        }
      }
    }
  }
  .m-order-product{
    .m-modal {
      .m-modal-state {
        width: 520px;
        height: 600px;
        border-radius: 30px;
        .m-modal-content {
          padding-top: 120px;
          p {
            color: #000;
          }
          .m-apply-success {
            display: inline-block;
            width: 85px;
            height: 85px;
            background: url("/static/images/icon-result-personal.png") no-repeat;
            background-size: 100%;
            margin-bottom: 36px;
          }
          .m-apply-result-info {
            margin: 40px 0;
            font-size: 24px;
            line-height: 35px;
          }
          .m-apply-result-btn {
            span {
              display: inline-block;
              width: 250px;
              height: 70px;
              line-height: 70px;
              background-color: @mainColor;
              color: #fff;
              border-radius: 50px;
              box-shadow: 2px 8px 8px 0 rgba(0, 0, 0, 0.16);
            }
          }
        }

      }
    }
  }
</style>
