<template>
  <div class="m-fans" >

    <div class="m-modal m-copy-text" v-if="show_modal">
      <div class="m-modal-state">
        <div class="m-modal-head">
          <span class="m-close" @click="closeModal('show_modal')"> x </span>
        </div>
        <div class="m-modal-content">
          <h3>链接已经复制成功</h3>
          <p>您可以去分享给好友啦！
          </p>
        </div>
        <!--<div class="m-modal-foot">-->
        <!--<span class="m-modal-foot-btn">复制文案</span>-->
        <!--</div>-->
      </div>
    </div>

    <img :src="bg_img" class="m-fans-bg" alt="">
    <div class="m-fans-rule" @click="getRule(6)"></div>
    <div class="m-fans-details" @click="getRule(14)"></div>
    <div class="m-fans-fans-details" @click="fansClick"></div>
    <div class="m-fans-share-poster" @click="sharePoster"></div>
    <div class="m-fans-share-link" @click="copyText"></div>

    <img-modal v-if="show_img" :src="img_src" @closeModal="closeModal"></img-modal>
  </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
  import common from '../../../common/js/common';
  import imgModal from '../../../components/common/imgModal';
  export default {
    data() {
      return {
        name: '',
        show_modal:false,
        show_img:false,
        img_src:'',
        bg_img:''
      }
    },
    components: {imgModal},
    mounted(){
      this.getRule(9);
    },
    methods: {
      fansClick(){
        this.$router.push('/fansManagement')
      },
      sharePoster(){
        this.$router.push('/poster')
      },
      copyText(){
        let that =this;
        this.$copyText(window.location.origin + '/#/login').then(function (e) {
          that.show_modal = true;
        }, function (e) {

        })
      },
      getRule(type){
        axios.get(api.get_image_by_aitype,{
          params:{
            token:localStorage.getItem('token'),
            aitype:type
          }
        }).then(res => {
          if(res.data.status == 200){
            if(type == 9){
              this.bg_img = res.data.data.aiimage;
            }else{
              this.show_img = true;
              this.img_src = res.data.data.aiimage;
            }

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
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  @import "../../../common/css/modal";
  .m-fans{
    .m-fans-bg{
      display: block;
      width: 100%;
      height: 2300px;
    }
    .m-fans-rule{
      position: absolute;
      top:15px;
      right:15px;
      width:48px;
      height: 30px;
      background-color: transparent;
    }
    .m-fans-details{
      position: absolute;
      top:530px;
      left:533px;
      width:140px;
      height: 36px;
      background-color: transparent;
    }
    .m-fans-fans-details{
      position: absolute;
      top:622px;
      left:284px;
      width:294px;
      height: 36px;
      background-color: transparent;
    }
    .m-fans-share-poster{
      position: absolute;
      top:893px;
      left:176px;
      width:168px;
      height: 44px;
      background-color: transparent;
    }
    .m-fans-share-link{
      position: absolute;
      top:893px;
      left:413px;
      width:168px;
      height: 44px;
      background-color: transparent;
    }
  }

  .m-fans{
    .m-modal{
      .m-modal-state{
        .m-modal-content{
          border-bottom: none!important;
        }
      }
    }
  }
</style>
