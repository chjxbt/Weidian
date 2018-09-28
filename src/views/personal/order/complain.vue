<template>
    <div class="m-complain" @touchmove="touchMove">
      <div class="m-complain-form">
        <div class="m-complain-type">
          <span class="m-complain-type-btn">服务投诉</span>
          <span class="m-complain-type-btn">质量投诉</span>
        </div>
        <ul class="m-complain-checkbox">
          <template v-for="(item,index) in check_list">
            <li @click="checkClickForm(index)">
              <span class="m-checkbox" :class="item.click?'active':''"></span>
              <span>{{item.name}}</span>
            </li>
          </template>
        </ul>
        <div class="m-complain-textarea-box">
          <p><span>请详细描述您遇到的问题：</span><span class="m-complain">{{COcontent.length}}/100</span></p>
          <textarea name="" id="" v-model="COcontent" maxlength="100" class="m-complain-textarea" placeholder="我们会尽快与您联系！"></textarea>
        </div>
        <div class="m-complain-submit">
          <span @click="complainClick">提交</span>
        </div>
      </div>

      <div class="m-myOrder-nav" v-if="isOpen">
        <span :class="isSell?'active':''" @click="sellClick(true)">销售订单</span>
        <span :class="!isSell?'active':''" @click="sellClick(false)">自买订单</span>
      </div>
      <div class="m-myOrder-nav m-one" v-else>
        <span class="active">自买订单</span>
      </div>
      <div class="m-complain-order-list">
        <div class="m-no-complain-order" v-if="!have_order">
          尚无相关订单...
        </div>
        <div class="m-one-complain-order" v-else>
          <template v-for="(items,index) in order_list">
            <div class="m-one" v-if="items.complainstatus.cotreatstatus == 0">
              <span class="m-check" :class="items.click?'active':''" @click="checkClick(index)"></span>
              <one-order :item="items"></one-order>
            </div>
          </template>
        </div>
      </div>
      <div class="bottom-prompt" v-if="bottom_show">
        <div class="bottom-line"></div>
        <div class="m-grey-color">我是有底线的</div>
        <div class="bottom-line"></div>
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
              have_order:true,
              page_size:5,
              page_num:1,
              total_count:0,
              isScroll:true,
              isOpen:true,
              isSell:true,
              order_list:[],
              COcontent:'',
              check_list:[
                {
                  name:'客服态度差',
                  value:'201',
                  click:false
                },
                {
                  name:'商品质量问题',
                  value:'202',
                  click:false
                },
                {
                  name:'售后方案不合理',
                  value:'203',
                  click:false
                },
                {
                  name:'商品包装问题',
                  value:'204',
                  click:false
                }
              ],
              bottom_show:false
            }
        },
        components: {
          oneOrder
        },
      mounted(){
        this.isOpen = localStorage.getItem('level') == 'partner'? true:false;
        this.isSell = localStorage.getItem('level') == 'partner'? true:false;
        common.changeTitle('快速投诉通道');
      },
        methods: {
          /*获取订单*/
          getOrder(page){
            axios.get(api.get_list_order,{
              params:{
                token: localStorage.getItem('token'),
                page_num: page || 1,
                page_size:this.page_size || 10,
                sell:this.isSell,
                paystatus:20
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
          /*提交投诉*/
          complainClick(e){
            e.preventDefault();
            let id = '';
            for(let a=0;a<this.order_list.length;a++){
              if(this.order_list[a].click){
                id = this.order_list[a].oiid;
                break;
              }
            }
            if(id == ''){
              Toast({ message:'请先选择订单',className: 'm-toast-warning'  });
              return false;
            }

            let arr =[];
            for(let i=0;i<this.check_list.length;i++){
              if(this.check_list[i].click )
                arr.push(this.check_list[i].value)
            }
            if(arr.length == 0 && this.COcontent == ''){
              Toast({ message:'请填写投诉理由',className: 'm-toast-warning'  });
              return false;
            }
            axios.post(api.add_one_complain +'?token=' + localStorage.getItem('token'),{
              OIid:id,
              COcontent:this.COcontent,
              COtype:arr
            }).then(res => {
              if(res.data.status ==200){
                Toast({ message: res.data.message, className: 'm-toast-success' });
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }

            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });       })
          },
          /*nav切换*/
          sellClick(v){
            if(this.sell == v){
              return false;
            }
            this.isSell = v;
            this.getOrder();
          },
          /*选择切换*/
          checkClick(i){
            if(this.order_list[i].click)
              return false;
            for(let a=0;a<this.order_list.length;a++){
              this.order_list[a].click = false;
            }
            this.order_list[i].click = true;
          },
          /*加载更多*/
          touchMove(){
            let scrollTop = common.getScrollTop();
            let scrollHeight = common.getScrollHeight();
            let ClientHeight = common.getClientHeight();
            if (scrollTop + ClientHeight >= scrollHeight - 10) {
              if(this.isScroll){
                this.isScroll = false;
                if(this.order_list.length == this.total_count){
                  this.bottom_show = true;
                  // Toast({ message: '数据已加载完', className: 'm-toast-warning' });
                }else{
                  this.page_num = this.page_num +1;
                  this.getOrder(this.page_num);
                }
              }
            }
          },
          checkClickForm(i){
            this.check_list[i].click = !this.check_list[i].click;
          }
        },
        created() {
          this.getOrder();
        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
.m-complain{
  padding-bottom: 40px;
  .m-complain-form{
    padding: 20px 69px;
    .m-complain-type{
      .flex-row(space-between);
      .m-complain-type-btn{
        display: block;
        width: 264px;
        height: 60px;
        line-height: 60px;
        background-color: #666;
        color: #fff;
        font-size: 30px;
      }
    }
    .m-complain-checkbox{
      .flex-row(flex-start);
      flex-wrap: wrap;
      padding: 25px 0;
      li{
        width: 50%;
        font-size: 24px;
        color: #666;
        line-height: 32px;
        height: 41px;
        margin-bottom: 20px;
        &:nth-child(odd){
          text-align: left;
        }
        .m-checkbox{
          display: inline-block;
          width: 40px;
          height: 40px;
          background: url("/static/images/icon-check-personal.png") no-repeat center;
          background-size: 100% 100%;
          vertical-align: middle;
          margin-right: 30px;
          margin-left: 25px;
          &.active{
            background: url("/static/images/icon-check-personal-active.png") no-repeat center;
            background-size: 100% 100%;
          }
        }
      }
    }
    .m-complain-textarea-box{
      p{
        .flex-row(space-between);
        padding: 0 25px;
        font-size: 24px;
        .m-complain{
          color: #c1c1c1;
        }
      }
      .m-complain-textarea{
        margin: 14px 25px;
        width: 517px;
        height: 160px;
        border: 2px solid @borderColor;
        padding: 10px 20px;
        font-size: 21px;
      }
    }
    .m-complain-submit{
      padding: 0 25px;
      text-align: right;
      span{
        display: inline-block;
        width: 90px;
        /*height: 30px;*/
        padding: 0 10px;
        /*line-height: 35px;*/
        text-align: center;
        background-color: @mainColor;
        color: #fff;
        border-radius: 30px;
        font-size: 21px;
      }
    }
  }
  .m-complain-line{
    width: 100%;
    height: 46px;
    line-height: 46px;
    font-size: 24px;
    background-color: @mainColor;
    color: #fff;
    margin-bottom: 40px;
  }
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
  .m-complain-order-list{
    .m-no-complain-order{
      font-size: 30px;
      color: #c1c1c1;
      margin-top: 300px;
    }
    .m-one-complain-order{
      .m-one{
        .flex-row(flex-start);
        padding-right: 20px;
        .m-check{
          display: block;
          width: 40px;
          height: 40px;
          background: url("/static/images/icon-complain-check.png") no-repeat;
          background-size: 100%;
          margin: 0 20px;
          &.active{
            background: url("/static/images/icon-complain-check-active.png") no-repeat;
            background-size: 100%;
          }
        }
        .m-one-order{
          width: 630px;
        }
      }

    }
  }
  .bottom-prompt {
    background-color: #fff;
  }
}
  .m-complain-textarea::-webkit-input-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea:-moz-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea::-moz-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea:-ms-input-placeholder{
    color:#c1c1c1;
  }
</style>
