<template>
  <div >
    <!--待支付-->
    <div class="order-status-title" v-if="order.oipaystatus == 1">
      <img src="/static/images/order_time.png" class="order-time-img">
      <div class="order-time m-ft-24 m-bg-main-color">还有 {{remaintime}} 自动关闭交易</div>
    </div>
    <div class="order-status-title" v-if="order.oipaystatus == 3">
      <img src="/static/images/order_time.png" class="order-time-img">
      <div class="order-time m-ft-24 m-bg-main-color">交易关闭</div>
    </div>
    <!--付款成功-->
    <div class="order-status-title" v-if="order.oipaystatus == 2">
      <img src="/static/images/pay_ok.png" class="pay-ok-img">
      <div class="order-text-box m-bg-main-color tl">
        <div class="pay-ok-text m-ft-36">付款成功</div>
        <div class="ok-title-text">您的包裹马上就去找您</div>
      </div>
    </div>
    <!--已发货-->
    <div class="order-status-title" v-if="order.oipaystatus == 5">
      <div class="order-text-box m-bg-main-color tl" style="margin: 10px 40px 0 30px">
        <div class="pay-ok-text m-ft-36">卖家已发货</div>
        <div class="ok-title-text">包裹已在路上，请您耐心等待</div>
      </div>
      <img src="/static/images/send_ok.png" class="send-ok-img">
    </div>
    <!--查看物流-->
    <div class="logistics-page" v-if="order.oipaystatus == 5" @click="checkLogistics">
      <img src="/static/images/truck.png" class="truck-img">
      <div class="logistics-info m-ft-26 tl">
        <p class="logistics-text">包裹已签收，签收人[ 吴伟杰 ]</p>
        <p class="logistics-time">2016.6.28 11:30:10</p>
      </div>
      <img src="/static/images/icon-more.png" class="more-img">
    </div>
    <!--交易完成-->
    <div class="order-status-title" v-if="order.oipaystatus == 6 || order.oipaystatus == 9">
      <img src="/static/images/order_ok.png" class="order-ok-img">
      <div class="order-ok-text m-ft-40 m-bg-main-color">交易成功</div>
    </div>
    <!--查看物流-->
    <div class="logistics-page" v-if="order.oipaystatus == 6 || order.oipaystatus == 9" @click="checkLogistics">
      <img src="/static/images/truck.png" class="truck-img">
      <div class="logistics-info m-ft-26 tl">
        <p class="logistics-text">包裹已签收，签收人[ 吴伟杰 ]</p>
        <p class="logistics-time">2016.6.28 11:30:10</p>
      </div>
      <img src="/static/images/icon-more.png" class="more-img">
    </div>
    <div class="line"></div>

    <order-product :order="order"></order-product>

    <div class="order-btns">
      <img src="/static/images/product_detail_service.png" class="service-img" @click="service">
      <div class="service-text m-ft-26 m-ft-b" @click="service">客服</div>
      <div class="complaints-text m-ft-26 m-grey m-ft-b" @click="complaints" ><span v-if="order.oipaystatus != 1 && order.oipaystatus != 2 ">投诉</span></div>

      <!--待支付-->
      <div v-if="order.oipaystatus == 1" class="btn-box">
        <div class="cancel-order m-ft-24 m-black" @click="cancelOrder">取消订单</div>
        <div class="to-pay m-ft-24 m-red" @click="toPay">立即支付</div>
      </div>
      <div v-else-if="order.oipaystatus == 2 || order.oipaystatus == 4" class="btn-box">
        <div class="cancel-order m-ft-24 m-black" @click="cancelOrder">取消订单</div>
      </div>
      <!--已发货-->
      <div v-else-if="order.oipaystatus == 5" class="btn-box">
        <div class="cancel-order m-ft-24 m-black" @click="delayReceiving">延迟收货</div>
        <div class="to-pay m-ft-24 m-red" @click="confirmReceiving">确认收货</div>
      </div>
      <!--交易完成-->
      <div v-else-if="order.oipaystatus != 9 && order.oipaystatus != 6" class="btn-box">
        <div class="cancel-order m-ft-24 m-black" @click="deleteOrder">删除订单</div>
        <!--<div class="to-pay m-ft-24 m-red" @click="toEvaluation">评 价</div>-->
      </div>

    </div>

    <div class="line"></div>
    <div class="order-time-box m-ft-24 tl" @click="change">
      <p class="m-black m-ft-b">订单交易时间</p>
      <div class="m-grey-color" >订单备注：{{order.oileavetext}}</div>
      <div class="m-grey-color" >创建时间：{{createTime}}</div>
      <div class="m-grey-color" >付款时间：{{payTime}}</div>
      <div class="m-grey-color" >发货时间：{{sendTime}}</div>
    </div>
    <div class="line-three"></div>

  </div>
</template>

<script>
  import orderProduct from "../shopping/components/orderProduct";
  import { Toast } from 'mint-ui';
  import axios from 'axios';
  import api from '../../api/api'
  export default {
    data() {
      return {
        name: "orderStatus",
        order: {},
        // 待支付：1，付款成功：2，已发货：3，交易完成：4
        orderStatus: 1,
        timeList: ["创建时间：2018-08-16 14:28:58", "付款时间：2018-08-16 18:28:58", "发货时间：2018-08-16 20:28:58"],
        createTime:'',
        payTime:'',
        sendTime:'',
        remaintime:'',
        interval:''
      }
    },
    components: { orderProduct },
    mounted(){
      this.getOrderInfo();

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
              this.order = res.data.data;
              // this.order.oipaystatus = 5;
              this.createTime = res.data.data.oicreatetime.slice(0,4) + '-' +res.data.data.oicreatetime.slice(4,6) + '-' +res.data.data.oicreatetime.slice(6,8) + ' ' +res.data.data.oicreatetime.slice(8,10) + ':' +res.data.data.oicreatetime.slice(10,12) + ':' +res.data.data.oicreatetime.slice(12,14);
              if(res.data.data.oipaytime)
                 this.payTime = res.data.data.oipaytime.slice(0,4) + '-' +res.data.data.oipaytime.slice(4,6) + '-' +res.data.data.oipaytime.slice(6,8) + ' ' +res.data.data.oipaytime.slice(8,10) + ':' +res.data.data.oipaytime.slice(10,12) + ':' +res.data.data.oipaytime.slice(12,14);
              let that = this;
              if(this.order.oipaystatus == 1){
                that.interval = window.setInterval(that.getDJS,1000)
              }else{
                window.clearInterval(that.interval)
              }
            }
        })
      },
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
        this.$router.push({path:'/complain',query:{oiid:this.$route.query.oiid}});
      },
      // 取消订单
      cancelOrder() {
        axios.post(api.cancle_order+'?token=' + localStorage.getItem('token'),{
          oiid:this.$route.query.oiid
        }).then(res => {
          if(res.data.status == 200){
            this.$router.push('/order')
            Toast({ message: res.data.message,duration:800, className: 'm-toast-success' });
          }
        })
      },
      // 立即支付
      toPay() {

      },
      // 延迟收货
      delayReceiving() {

      },
      // 确认收货
      confirmReceiving() {
       axios.post(api.confim_order +'?token=' +localStorage.getItem('token'),{
         oiid:this.$route.query.oiid
       }).then(res => {
         if(res.data.status == 200){
           this.getOrderInfo();
         }else{
           Toast({ message: res.data.message,duration:800, className: 'm-toast-success' });
         }
       })
      },
      // 删除订单
      deleteOrder() {
        axios.post(api.delete_order+'?token=' + localStorage.getItem('token'),{
          oiid:this.$route.query.oiid
        }).then(res => {
          if(res.data.status == 200){
            this.$router.push('/order')
            Toast({ message: res.data.message,duration:800, className: 'm-toast-success' });
          }
        })
      },
      // 评 价
      toEvaluation() {

      },
      // 查看物流
      checkLogistics() {
        let order = this.order;
        this.$router.push({path: "/logisticsInfo", query: { order }});
      },
      getDJS(){
        let NowTime = new Date();
        let start = this.order.oicreatetime;
        let EndTime= new Date(start.slice(0,4),start.slice(4,6)-1,start.slice(6,8),start.slice(8,10),start.slice(10,12),start.slice(12));//初始化结束日期2016年12月31日23点59分59秒
        // let  EndTime= new Date(start.slice(0,4),9,20,start.slice(8,10),start.slice(10,12),start.slice(12));//初始化结束日期2016年12月31日23点59分59秒
        let t =EndTime.getTime() - NowTime.getTime();
        if(t <= 0){
          this.order.oipaystatus = 3;
          return false;
        }
        if(t>0){
          let d=Math.floor(t/1000/60/60/24);
          let h=Math.floor(t/1000/60/60%24);
          let m=Math.floor(t/1000/60%60);
          let s=Math.floor(t/1000%60);
          let arr = [];
          arr[0] = d ==1 ?24+h:h;
          arr[1] = m<10? '0' + m:m;
          arr[2] = s<10? '0'+s:s;
          this.remaintime =arr.join(':');
        }
      },
    },
    created() {
      // this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .order-status-title {
    display: flex;
    background-color: #f53b52;
    .order-time-img {
      width: 38px;
      height: 38px;
      padding: 21px 31px;
    }
    .order-time {
      margin-top: 22px;
    }
    .pay-ok-img {
      width: 50px;
      height: 50px;
      margin: 55px;
    }
    .order-text-box {
      .pay-ok-text {
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
      margin: 75px 0;
    }
  }
  .logistics-page {
    display: flex;
    .truck-img {
      width: 45px;
      height: 33px;
      margin: 50px 0 0 30px;
    }
    .logistics-info {
      flex: 1;
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
      margin: 28px -10px;
    }
    .complaints-text {
      width: 190px;
      margin-top: 28px;
    }
    .btn-box {
      display: flex;
      flex-flow: row;
      justify-content: flex-end;
      width: 390px;
      .cancel-order {
        width: 100px;
        line-height: 30px;
        margin: auto;
        padding: 10px 36px;
        border-radius: 25.5px;
        border: solid 2px @greyColor;
      }
      .to-pay {
        width: 100px;
        line-height: 30px;
        margin: auto;
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
    margin: 30px 0 20px 40px;
  }
</style>
