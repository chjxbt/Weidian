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

      <div class="m-myOrder-content" @touchmove="touchMove" >

        <div class="m-myOrder-list">
          <template v-for="(items,index) in order_list">
            <one-order :item="items"></one-order>
          </template>

        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import oneOrder from './components/oneOrder';
  import axios from 'axios';
  import api from '../../../api/api';
  import common from '../../../common/js/common';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                name: '',
              order_list:[],
              page_size:3,
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
                token:localStorage.getItem('token'),
                sell:this.isSell
              }
            }).then(res => {
              if(res.data.status == 200){
                this.order_num = [].concat(res.data.data);
                for(let i=0;i<this.order_num.length;i++){
                  this.order_num[i].click = false;
                }
                this.order_num[0].click = true;
                this.getOrder();
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
                status = this.order_num[a].statusnum
              }
            }
            axios.get(api.get_list_order,{
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
                this.total_count = res.data.totalcount;
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
            if(this.sell == v){
              return false;
            }
            this.isSell = v;
            this.getOrderNum();
            this.getOrder();
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
            this.getOrder();
          },
          /*加载更多*/
          touchMove(){
            let scrollTop = common.getScrollTop();
            let scrollHeight = common.getScrollHeight();
            let ClientHeight = common.getClientHeight()
            if (scrollTop + ClientHeight >= scrollHeight) {
              if(this.isScroll){
                this.isScroll = false;
                if(this.order_list.length == this.total_count){
                  Toast({ message: '数据已加载完', className: 'm-toast-warning' });
                }else{
                  this.page_num = this.page_num +1;
                  this.getOrder(this.page_num);
                }
              }
            }
          },        },
        created() {

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
