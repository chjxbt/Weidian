<template>
    <div>
      <div class="m-shop-top" :class="isOpen?'active':''">
        <div class="m-shop-top-box">
          <div class="m-flex-between">
            <span @click="setClick">账号设置</span>
            <span @click="getRule()">等级规则</span>
          </div>
          <div class="m-flex-start m-shop">
            <img v-if="person_info.user" :src="person_info.user.usheader" class="m-shop-top-img" alt="">
            <div class="m-shop-content">
              <h3 v-if="person_info.user">{{person_info.user.usname}}</h3>
              <div v-if="!isOpen">
                <p class="m-red">￥{{person_info.myrewards}}</p>
                <p>新衣币</p>
              </div>
              <div v-if="person_info.show == 1 && isOpen">
                <p>您已成功超过 <span class="m-ft-30">{{person_info.myranking}}%</span> 的VIP</p>
                <p>离成功保级还差 <span class="m-ft-30">¥{{person_info.myrewards}}</span> 元</p>
              </div>
            </div>
          </div>
        </div>
        <div class="m-invite-box" v-if="isOpen">
          <span class="m-invite-fans" @click="invite('fans')">邀请专属粉丝</span>
          <span class="m-invite-store" @click="invite('store')">邀请购买开店大礼包</span>
        </div>
      </div>
      <on-open v-if="isOpen" @teacherClick="teacherClick"></on-open>
      <un-open v-else></un-open>

      <img-modal v-if="show_img" :src="rule" @closeModal="closeModal"></img-modal>
    </div>

</template>

<script type="text/ecmascript-6">
  import onOpen from './shop/onOpen';
  import unOpen from './shop/unOpen';
  import axios from 'axios';
  import api from '../../api/api';
  import {Toast} from 'mint-ui';
  import common from '../../common/js/common';
  import imgModal from '../../components/common/imgModal';
    export default {
        data() {
            return {
                isOpen: false,
              show_img:false,
              rule:'',
              person_info:[

              ],
            }
        },
        components: {
          onOpen,
          unOpen,
          imgModal
        },
      mounted(){
        common.changeTitle('我的');
        this.$store.state.tabbar_select = '我的';
      },
        methods: {
          getInfo(){
            axios.get(api.get_info_mycenter,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.person_info = res.data.data;
                localStorage.setItem('level',res.data.data.user.level)
                if(res.data.data.user.level == 'partner'){
                  this.isOpen = true;
                }else{
                  this.isOpen = false;
                }
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          getRule(type){
            axios.get(api.get_image_by_aitype,{
              params:{
                token:localStorage.getItem('token'),
                aitype:type
              }
            }).then(res => {
              if(res.data.status == 200){
                this.show_img= true;
                this.rule=res.data.data.aiimage;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          /*关闭模态框*/
          closeModal(v){
            this[v]  = false;
          },
          /*账号设置*/
          setClick(){
            this.$router.push('/setUp')
          },
          /*邀请粉丝/开店*/
          invite(v){
            if(v == 'fans'){
              this.$router.push('/inviteFans')
            }else if(v == 'store'){
              this.$router.push('/inviteStore')
            }
          },
          teacherClick(){
            this.getRule(0);
          }
        },
        created() {
          this.getInfo();

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";

  .m-shop-top{
    font-size: 26px;
    color: #a4a4a4;
    &.active{
      background: url("/static/images/icon-shop-back.png") no-repeat;
      background-size: 100%;
      color: #fff;
      .m-shop-top-box .m-shop .m-shop-content h3{
        color: #fff;
      }
    }
    .m-shop-top-box{
      padding: 20px;
      .m-shop{
        padding: 20px 20px 0;
        .m-shop-top-img{
          display: block;
          width: 136px;
          height: 136px;
          background-color: #a4a4a4;
          border-radius: 50%;
          margin:0 60px;
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
            margin-bottom: 30px;
            margin-top: 20px;
            /*color: #fff;*/
            color: #000;
          }
        }
      }
    }
    .m-invite-box{
      .flex-row(space-around);
      span{
        display: block;
        width: 50%;
        height: 120px;
        line-height: 120px;
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
    background-color: #fff;

    .m-name{
      text-align: left;
      font-size: 24px;
      line-height: 32px;
      margin-top: 20px;
      margin-left: 32px;
    }
    .m-income-info{
      padding-bottom: 30px;
      text-align: center;
    }
  }
  .m-part-list{
    .flex-row(space-around);
    padding: 20px 0;
    &.m-new{
      border-top: 10px solid #f3f5f8;
      border-bottom: 10px solid #f3f5f8;
    }
    li{
      .flex-col(center);
      .m-part-list-icon{
        display: block;
        width: 50px;
        height: 50px;
        margin-bottom: 15px;
      }
      .m-num{
        font-size: 40px;
        margin-top: 30px;
        /*line-height: 1.33;*/
        font-weight: bold;
      }
    }

  }
  .m-short-bannar{
    width: 100%;
    height: 120px;
    border-top: 10px solid  #f3f5f8;;
    background-color: #fff;
    .m-short-img{
      display: block;
      width: 100%;
      height: 120px;
    }
  }
</style>
