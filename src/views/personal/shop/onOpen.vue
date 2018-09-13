<template>
    <div class="m-onOpen">
      <div>
        <div class="m-part-one">
         <cell :item="part_tilt_one" ></cell>
          <ul class="m-part-list">
            <li>
              <span>今日销售额</span>
              <span class="m-red m-num">1250</span>
            </li>
            <li>
              <span>今日赚</span>
              <span class="m-red m-num">250</span>
            </li>
            <li>
              <span>额外赚</span>
              <span class="m-red m-num">125</span>
            </li>
            <li>
              <span>新衣币</span>
              <span class="m-red m-num">234</span>
            </li>
          </ul>
          <p class="m-income-info">本月还差<span class="m-red m-ft-30">1520元</span>销售额即可获得奖励</p>
        </div>

        <div class="m-part-one">
          <div class="m-name">订单</div>
         <cell :item="part_tilt_two"  @cellNav="cellNav" ></cell>
          <ul class="m-part-list">
            <template v-for="(item,index) in order_list">
              <li>
                <img :src="item.src" class="m-part-list-icon" />
                <span>{{item.name}}
                  <span class="m-red">({{item.num}})</span>
                </span>
              </li>
            </template>
          </ul>
        </div>
      </div>

      <ul class="m-part-list">
        <template v-for="(item,index) in nav_list">
          <li @click="navClick(item)">
            <img :src="item.src" class="m-part-list-icon" />
            <span>{{item.name}}</span>
          </li>
        </template>
      </ul>

      <div class="m-short-bannar" v-if="short">
        <img :src="short.aiimage" class="m-short-img" alt="">
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import cell from '../../../components/common/cell';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                name: '',
              part_tilt_one:{
                name:'我的收益',
                value:'查看更多',
                url:'details'
              },
              part_tilt_two:{
                name:'',
                nav:[
                  {
                    name:'销售订单',
                    url:'',
                    click:true
                  },
                  {
                    name:'自买订单',
                    url:'',
                    click:false
                  }
                ],
                value:'查看更多',
                url:'order'
              },
              order_list:[
                {
                  name:'待支付',
                  src:'/static/images/icon-pay-personal.png',
                  value:'',
                  num:0
                },{
                  name:'待发货',
                  src:'/static/images/icon-wait-send-personal.png',
                  value:'',
                  num:0
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
                  num:0
                }
              ],
              nav_list:[
                {
                  name:'我的收藏',
                  src:'/static/images/icon-collect-personal.png',
                  url:'/collect'
                },{
                  name:'赚钱学院',
                  src:'/static/images/icon-make-money-personal.png',
                  url:''
                },
                {
                  name:'我的导师',
                  src:'/static/images/icon-teacher-personal.png',
                  url:''
                },
                {
                  name:'素材圈',
                  src:'/static/images/icon-material-personal.png',
                  url:''
                },
                {
                  name:'快速投诉',
                  src:'/static/images/icon-complain-personal.png',
                  url:'/complain'
                }
              ],
              short:null
            }
        },
        components: {
          cell
        },
        methods: {
          /*获取订单预览数*/
          getOrder(sell){
            axios.get(api.get_order_count,{
              params:{
                token:localStorage.getItem('token'),
                sell:sell
              }
            }).then(res => {
              if(res.data.status == 200){
                // this.person_info = res.data.data
                for(let i=0;i<res.data.data.length;i++){
                  switch (res.data.data[i].status){
                    case '待支付':
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
              Toast({ message: error.data.message, className: 'm-toast-fail' });
            })
          },
          /*获取底部图片*/
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
                }
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });
            })
          },
          /*订单类型切换*/
          cellNav(v){
            for(let i=0;i<this.part_tilt_two.nav.length;i++){
              this.part_tilt_two.nav[i].click = false;
            }
            this.part_tilt_two.nav[v].click = true;
            switch (v){
              case 0:
                this.getOrder(true);
                break;
              case 1:
                this.getOrder(false);
                break;
            }
          },

          /*底部图标点击*/
          navClick(v){
           if(v.url){
             this.$router.push(v.url);
           }
          },
          // 临时方法，去往二三级页面的会员中心
          toPage() {
            this.$router.push("/memberCenter");
          }
        },
        created() {
          this.getOrder(true);
          this.getImg();
        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-onOpen{
    color: #666;
    .m-shop-top{
      font-size: 26px;
      background: url("/static/images/icon-shop-back.png") no-repeat;
      background-size: 100%;
      color: #fff;
      .m-shop-top-box{
        padding: 28px;
        .m-shop{
          padding: 28px;
          .m-shop-top-img{
            display: block;
            width: 200px;
            height: 200px;
            background-color: #a4a4a4;
            border-radius: 50%;
            margin-right: 30px;
            border: 10px solid #fff;
          }
          .m-shop-content{
            height: 200px;
            text-align: left;
            p{
              line-height: 32px;
              font-size: 24px;
              margin-bottom: 10px;
            }
            h3{
              font-size: 40px;
              margin-bottom: 43px;
              margin-top: 20px;
              color: #fff;
            }
          }
        }
      }
      .m-invite-box{
        .flex-row(space-around);
        span{
          display: block;
          width: 50%;
          height: 140px;
          line-height: 140px;
          text-align: center;
          color: #fff;
          &.m-invite-fans{
            background: url("/static/images/icon-fans-back.png") no-repeat;
            background-size: 100%;
          }
          &.m-invite-store{
            background: url("/static/images/icon-store-back.png") no-repeat;
            background-size: 100%;
          }
        }
      }
    }

    .m-part-one{
      border-bottom: 1px solid @borderColor;
    }
    .m-cell{
      border-bottom: none;
    }
  }

</style>
