<template>
    <div class="m-myOrder">
      <div class="m-order-top">
        <div class="m-myOrder-nav" v-if="isOpen">
          <span :class="isSell?'active':''" @click="sellClick(true)">销售订单</span>
          <span :class="!isSell?'active':''" @click="sellClick(false)">自买订单</span>
        </div>
        <div class="m-myOrder-nav m-one" v-else>
          <span class="active">自买订单</span>
        </div>
        <ul class="m-myOrder-content-nav">
          <template v-for="(item,index) in order_num">
            <li :class="item.click?'active':''" @click="statusClick(index)">
              {{item.status}}({{item.count}})
            </li>
          </template>
        </ul>
      </div>

      <div class="m-myOrder-content">

        <div class="m-myOrder-list">
          <one-order></one-order>
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span class="m-order-btn active">确认收货</span>
                </p>
              </div>
            </div>
            <ul class="m-one-order-money">
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
            </ul>
            <p class="m-order-time">2018-08-08 16:49:07  创建</p>
          </div>
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span class="m-red">确认收货</span>
                </p>
              </div>
            </div>
            <ul class="m-one-order-money">
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
            </ul>
            <p class="m-order-time">2018-08-08 16:49:07  创建</p>
          </div>
          <div class="m-one-order">
            <div class="m-one-order-top">
              <img src="" class="m-product-img" alt="">
              <div class="m-product-info">
                <p class="m-product-name">商品名称商品名称商品名称商品名称
                  商品名称商品名称商品名称</p>
                <p>投诉处理中..</p>
                <p class="m-order-code">
                  <span>订单号：123456789000</span>
                  <span >确认收货</span>
                </p>
              </div>
            </div>
            <ul class="m-one-order-money">
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
              <li>
                <span>付款金额</span>
                <span class="m-red m-ft-b">￥29.36</span>
              </li>
            </ul>
            <p class="m-order-time">2018-08-08 16:49:07  创建</p>
          </div>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import oneOrder from './components/oneOrder';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                name: '',
              order_list:[],
              page_size:10,
              page_num:1,
              total_count:0,
              isScroll:true,
              order_num:[],
              isOpen:false,
              isSell:true
            }
        },
        components: {
          oneOrder
        },
      mounted(){
          this.isOpen = localStorage.getItem('level') == 'partner'? true:false;
      },
        methods: {
          getOrderNum(){
            axios.get(api.get_order_count,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.order_num = [].concat(res.data.data);
                for(let i=0;i<this.order_num.length;i++){
                  this.order_num[i].click = false;
                }
                this.order_num[0].click = true;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          getOrder(page){
            let status ='';
            for(let a=0;a<this.order_num.length;a++){
              if(this.order_num[a].click){
                status = this.order_num[a].status
              }
            }
            axios.get(api.get_more_order,{
              params:{
                token: localStorage.getItem('token'),
                page_num: page || 1,
                page_size:this.page_size || 10,
                sell:this.isSell,
                paystatus:status
              }
            }).then(res => {
              if(res.data.status == 200){
                for(let i=0;i<res.data.data.length;i++){
                  res.data.data[i].click = false;
                }
                this.total_count = res.data.count;
                if(page){
                  this.order_list = this.order_list.concat(res.data.data);
                }else{
                  this.order_list = [].concat(res.data.data);
                }

              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          sellClick(v){
            this.isSell = v;
          },
          statusClick(i){
            if(this.order_num[i].click)
              return false;
            let arr =[].concat(this.order_num);
            for (let a=0;a<arr.length;a++){
              arr[a].click = false;
            }
            arr[i].click = true;
            this.order_num = [].concat(arr);
          }
        },
        created() {
          this.getOrder();
          this.getOrderNum();
        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
  .m-myOrder{
    padding-bottom: 40px;
    position: relative;
    .m-order-top{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 100;
      background-color: #fff;
      .m-myOrder-nav{
        .flex-row(flex-start);
        &.m-one{
          span{
            width: 100%;
          }
        }
        span{
          display: block;
          width: 50%;
          box-sizing: border-box;
          height: 46px;
          line-height: 46px;
          border: 2px solid @mainColor;
          color: #c1c1c1;
          font-size: 24px;
          text-align: center;
          &.active{
            background-color: @mainColor;
            color: #fff;
          }
        }
      }
      .m-myOrder-content-nav{
        .flex-row(space-around);
        font-size: 21px;
        color: #666;
        margin: 20px 0;
        li.active{
          color: #000;
        }
      }
    }

    .m-myOrder-content{
       padding-top: 100px;
      .m-myOrder-list{
        padding: 0 10px;
      }
    }
  }

</style>
