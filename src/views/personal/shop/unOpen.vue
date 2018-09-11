<template>
    <div class="m-unOpen">
      <div class="m-shop-top">
        <div class="m-flex-between">
          <span>账号设置</span>
          <span>等级规则</span>
        </div>
        <div class="m-flex-start m-shop">
          <img :src="person_info.user.usheader" class="m-shop-top-img" alt="">
          <div class="m-shop-content">
            <h3>{{person_info.user.usname}}</h3>
            <div>
              <p class="m-red">￥{{person_info.myrewards}}</p>
              <p>新衣币</p>
            </div>
          </div>
        </div>
      </div>
      <div class="m-order-box">
        <div class="m-part-one">
         <cell :item="part_title" ></cell>
          <order :list="order_list"></order>
        </div>
      </div>

      <div class="m-cell-box">
        <template v-for="(item,index) in cell_list">
          <cell :item="item" ></cell>
        </template>

      </div>
      <div class="m-short-bannar">

      </div>
      <div class="m-high-bannar">

      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import cell from '../../../components/common/cell';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
  import order from './components/order';
    export default {
        data() {
            return {
                name: '',
              person_info:[

              ],
              part_title:{
                name:'我的订单',
                value:'更多',
                url:'order'
              },
                cell_list:[
                  {
                    name:'收藏夹',
                    value:'',
                    url:'collect'
                  },
                  {
                    name:'快速投诉通道',
                    value:'',
                    url:'complain'
                  },
                  {
                    name:'关注公众号',
                    value:'',
                    url:''
                  }
                ],
              order_list:[
                {
                  name:'待支付',
                  src:'/static/images/icon-pay-personal.png',
                  value:'',
                  num:1
                },{
                  name:'待发货',
                  src:'/static/images/icon-wait-send-personal.png',
                  value:'',
                  num:2
                },
                {
                  name:'已发货',
                  src:'/static/images/icon-sent-personal.png',
                  value:'',
                  num:0
                },
                {
                  name:'已取消',
                  src:'/static/images/icon-cancel-personal.png',
                  value:'',
                  num:3
                }
              ],
            }
        },
        components: {
          cell,
          order
        },
        methods: {
          getInfo(){
            axios.get(api.get_info_mycenter,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.person_info = res.data.data
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          getOrder(){
            axios.get(api.get_order_count,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                // this.person_info = res.data.data
                for(let i=0;i<res.data.data.length;i++){
                  switch (res.data.data[i].status){
                    case '待付款':
                      this.order_list[0].value = res.data.data[i].count;
                      break;
                    case '待发货':
                      this.order_list[1].value = res.data.data[i].count;
                      break;
                    case '已发货':
                      this.order_list[2].value = res.data.data[i].count;
                      break;
                    case '已取消':
                      this.order_list[3].value = res.data.data[i].count;
                      break;
                  }
                }
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          cellClick(v){

          }
        },
        created() {
          this.getInfo();
          this.getOrder();
        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-unOpen{
    .m-shop-top{
      padding: 28px;
      color: #a4a4a4;
      font-size: 26px;
      .m-shop{
        padding: 28px;
        .m-shop-top-img{
          display: block;
          width: 200px;
          height: 200px;
          background-color: #a4a4a4;
          border-radius: 50%;
          margin-right: 30px;
          /*border: 20px solid #fff;*/
        }
        .m-shop-content{
          height: 200px;
          text-align: left;
          p{
            line-height: 32px;
            font-size: 24px;
          }
          h3{
            font-size: 40px;
            margin-bottom: 43px;
            margin-top: 20px;
            color: #000;
          }
        }
      }
    }
    .m-order-box{
      background-color: #f2f5f7;
      padding: 10px 0;

    }
    .m-cell-box{
      padding: 20px 0;
    }
    .m-high-bannar{
      width: 100%;
      height: 400px;
      background-color: #a4a4a4;

    }

  }

</style>
