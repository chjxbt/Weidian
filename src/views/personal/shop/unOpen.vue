<template>
    <div class="m-unOpen">
      <div class="m-order-box">
        <div class="m-part-one">
         <cell :item="part_title"  ></cell>
          <!--<order :list="order_list"></order>-->
          <ul class="m-part-list">
            <template v-for="(item,index) in order_list">
              <li @click="orderIcon(item)">
                <img :src="item.src" class="m-part-list-icon" />
                <span>{{item.name}}
                  <span class="m-red">({{item.value}})</span>
                </span>
              </li>
            </template>
          </ul>
        </div>
      </div>

      <div class="m-cell-box">
        <template v-for="(item,index) in cell_list">
          <cell :item="item" ></cell>
        </template>

      </div>

        <div class="m-short-bannar" v-if="short">
          <img :src="short.aiimage" class="m-short-img" alt="">
        </div>
        <div class="m-high-bannar"  v-if="high">
          <img :src="high.aiimage" class="m-high-img" alt="">
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
                  name:'待付款',
                  src:'/static/images/icon-pay-personal.png',
                  value:'',
                  num:0
                },
                // {
                //   name:'待发货',
                //   src:'/static/images/icon-wait-send-personal.png',
                //   value:'',
                //   num:0
                // },
                {
                  name:'待收货',
                  src:'/static/images/icon-sent-personal.png',
                  value:'',
                  num:0
                },
                // {
                //   name:'待评价',
                //   src:'/static/images/icon-comment-personal.png',
                //   value:'',
                //   num:0
                // },
                {
                  name:'退换货',
                  src:'/static/images/icon-change-personal.png',
                  value:'',
                  num:0
                }
              ],
              short:null,
              high:null
            }
        },
        components: {
          cell,
          order
        },
        methods: {
          getOrder(){
            axios.get(api.get_order_count,{
              params:{
                token:localStorage.getItem('token'),
                sell:false
              }
            }).then(res => {
              if(res.data.status == 200){
                // this.person_info = res.data.data
                let _arr  = [].concat(this.order_list);
                for(let i=0;i<res.data.data.length;i++){

                  switch (res.data.data[i].status){
                    case '待付款':
                      _arr[0].value = res.data.data[i].count;
                      break;
                    // case '待发货':
                    //   this.order_list[1].value = res.data.data[i].count;
                    //   break;
                    case '待收货':
                      _arr[1].value = res.data.data[i].count;
                      break;
                    // case '待评价':
                    //   this.order_list[3].value = res.data.data[i].count;
                    //   break;
                    case '退换货':
                      _arr[2].value = res.data.data[i].count;
                      break;
                  }
                }
                this.order_list  = [].concat(_arr);
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          getImg(){
            axios.get(api.get_myimg_adimage,{
              params:{
                lasting:true,
                token:localStorage.getItem('token')
              }
            }).then(res => {
                if(res.data.status == 200){
                  for(let i=0;i<res.data.data.length;i++){
                    if(res.data.data[i].aisize == 1)
                      this.short = res.data.data[i];
                    else if(res.data.data[i].aisize == 2)
                      this.high = res.data.data[i];
                  }

                }else{
                  Toast({ message: res.data.message, className: 'm-toast-fail' });
                }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          cellClick(v){

          },
          orderIcon(i){
            this.$router.push({path:"/order",query:{name:i.name}});
          }
        },
        created() {
          this.getOrder();
          this.getImg();
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
     background-color: #fff;
      margin-top: 20px;
      .m-high-img{
        display: block;
        width: 100%;
        height: 400px;
      }
    }

  }

</style>
