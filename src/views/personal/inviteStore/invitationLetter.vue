<template>
    <div class="m-invitation">
      <div class="m-invitation-img-box">
        <span class="m-rule" @click="getRule(13)">规则</span>
        <div class="m-logo-name">
          <img src="" class="m-logo-img" alt="">
          <span class="m-name">xxxxx</span>
        </div>
        <img src=""  class="m-invitation-img" alt="">
      </div>
      <div class="m-invitation-title">
        礼包标题
      </div>
      <div class="m-invitation-products">
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
        <div class="m-one">
          <img src="" alt="">
          <p class="m-points">商品名称商品名称商品名称名称</p>
          <p class="m-flex-between"> <span class="m-red">￥139</span><span class="m-red-border">购买</span></p>
        </div>
      </div>
      <!--<img-modal v-if="show_img" :src="img_src" @closeModal="closeModal"></img-modal>-->
      <div class="m-fans-img-modal" @click="closeFansModal" v-if="show_fans_img">
        <div class="m-modal-state" @click.stop="selectImg">
          <!--<span class="m-close" @click="closeModal">X</span>-->
          <!--<img :src="src"  alt="">-->
          <div class="m-headPortrait-name">
            <span class="m-head-name">xxccccx</span>
            <img src="" class="m-head-portrait" />
          </div>
          <mt-popup
            class="help-popup"
            v-model="helpPopupVisible"
            popup-transition="popup-fade">
            <img class="close-img" @click="closeFansModal" src="static/images/delete.png" alt="">
            <img style="width: 100%;height: 100%;" src="" alt="" >
          </mt-popup>
        </div>
      </div>
      <div class="m-fans-modal" v-if="show_fans" @click="closeModal('show_fans')">
        <div class="m-modal-state">
          <div class="m-modal-content">
            <p>86%的店主都收入过万了，
              您不试试吗？</p>
            <div class="m-fans-btn">
              <span @click="closeModal('show_fans')">残忍拒绝</span>
              <span class="active" @click="closeModal('show_fans')">好的</span>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
  import imgModal from '../../../components/common/imgModal';
    export default {
        data() {
            return {
                img_src:'',
              show_fans_img:false,
              show_fans:false,
              helpPopupVisible:false
            }
        },
        components: {imgModal},
      mounted(){
        this.show_fans_img =true;
        this.helpPopupVisible = true;
      },
        methods: {
          getRule(type){
            axios.get(api.get_image_by_aitype,{
              params:{
                token:localStorage.getItem('token'),
                aitype:type
              }
            }).then(res => {
              if(res.data.status == 200){
                this.show_img = true;
                this.img_src = res.data.data.aiimage;
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
          closeFansModal(){
            this.show_fans_img = false;
            this.helpPopupVisible =false;
            this.show_fans = true;
          },
          selectImg(){
            this.show_fans_img = false;
            this.helpPopupVisible =false;
            Toast({ message: '领取成功', duration: 800, className: 'm-toast-success' });
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>

  .m-invitation{
    padding: 30px 51px;
    .m-invitation-img-box{
      width: 644px;
      height: 644px;
      position: relative;
      box-shadow: 5px 5px 5px 0 rgba(0, 0, 0, 0.16);
      img.m-invitation-img{
        display: block;
        width: 644px;
        height: 644px;
        background-color: #9fd0bf;
      }
      span.m-rule{
        position: absolute;
        top:27px;
        right: 27px;
        font-size: 21px;
        color: #666;
      }
      .m-logo-name{
        position: absolute;
        top: 10px;
        left: 25px;
        display: flex;
        align-items: center;
        flex-flow: row;
        .m-logo-img{
          display: inline-block;
          width: 148px;
          height: 148px;
          border-radius: 50%;
          border: 2px solid #f53b52;
          z-index: 1000;
        }
        span{
          display: inline-block;
          padding: 15px 50px;
          background-color: #a4a4a4;
          vertical-align: middle;
          margin-left: -25px;
          border-radius: 50px;
          color: #f53b52;
        }
      }
    }
    .m-invitation-title{
      width: 643px;
      height: 153px;
      background-color: #e9e9e9;
      box-shadow: 5px 5px 5px 0 rgba(0, 0, 0, 0.16);
      margin: 30px 0;
      font-size: 30px;
      line-height: 153px;
    }
    .m-invitation-products{
      display: flex;
      flex-flow: row;
      flex-wrap: wrap;
      .m-one{
        position: relative;
        width: 309px;
        font-size: 24px;
        margin-top: 20px;
        &:nth-child(even){
          margin-left: 25px;
        }
        p{
          padding: 5px;
        }
        .m-points{
          font-weight: bold;
          overflow: hidden;
          text-overflow:ellipsis;
          white-space: nowrap;
        }
        img{
          display: block;
          width: 309px;
          height: 372px;
          background-color: #a3a3a3;
        }
        .m-red-border{
          padding: 5px 30px;
          display: inline-block;
          color: #f53b52;
          border: 1px solid #f53b52;
          border-radius: 30px;
        }

      }
    }
  }
  .m-fans-modal{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0,0,0,0.2);
    z-index: 1001;
    transition: opacity .5s;
    .m-modal-state{
      background-color: #fff;
      position: absolute;
      width: 500px;
      height: 279px;
      top: 0;
      left: 0;
      right:0;
      bottom:0;
      margin: auto;
      border: 1px solid #eeeeee;
      border-radius: 10px;
      -webkit-transition: height 0.88s;
      transition: height 0.88s;
      .m-modal-content{
        text-align: center;
        p{
          margin: 30px 50px 56px;
          font-size: 33px;
          color: #666;
          line-height: 1.39;
          letter-spacing: normal;
        }
        .m-fans-btn{
          display: flex;
          flex-flow: row;
          align-items: center;
          justify-content: space-around;
          span{
            display: block;
            width: 205px;
            height: 79px;
            color: #fff;
            background-color: #c6c6c6;
            line-height: 79px;
            border-radius: 4px;
            font-size: 28px;
            &.active{
              background-color: #f43b51;
            }
          }
        }
      }
    }
  }
  .m-fans-img-modal{
    position: fixed;
    top:0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0,0,0,0.4);
    z-index: 10001;
    .m-modal-state{
      position: absolute;
      width: 500px;
      height: 750px;
      top:50%;
      left: 50%;
      transform: translate(-250px,-375px);
      background-color: #fff;
      border-radius: 10px;
      .m-close{
        position: absolute;
        top: 20px;
        right: 20px;
      }
    }
  }
  .help-popup{
    height: 750px;
    width: 500px;
    border-radius: 10px;
    .close-img{
      position: absolute;
      top: 10px;
      right: 10px;
      width: 25px;
      height: 25px;
    }
    img{
      border-radius: 10px;
    }
  }
  .m-headPortrait-name{
    position: relative;
    top:-85px;
    left: -60px;
    .m-head-portrait{
      position: absolute;
      top:0;
      left:0;
      width: 95px;
      height: 95px;
      border: 2px solid #fff;
      border-radius: 50%;
      z-index: 200;
      background-color: #a4a4a4;
    }
    .m-head-name{
      position: absolute;
      top:22px;
      left:70px;
      z-index: 100;
      padding: 0 40px;
      height: 52px;
      line-height: 52px;
      background-color: #c3c3c3;
      border-radius: 25.3px;
      font-size: 26px;
    }
  }
</style>
