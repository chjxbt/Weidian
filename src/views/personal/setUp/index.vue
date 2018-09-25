<template>
    <div class="m-setUp">
      <div class="m-setUp-logo">
        <img :src="form.usheader" class="m-logo" alt="">
      </div>
      <div class="m-setUp-form">
        <div class="m-row">
          <span class="m-form-label">昵称</span>
          <!--<input type="text" v-model="form.usname" class="m-setUp-input" placeholder="小居居">-->
          <span class="m-setUp-input">{{form.usname}}</span>
        </div>
        <div class="m-row">
          <span class="m-form-label">微信号</span>
          <!--<input type="text" class="m-setUp-input" placeholder="xiaojujuxiaokeai2018">-->
          <span class="m-setUp-input">{{form.wxnum}}</span>
        </div>
        <div class="m-row">
          <span class="m-form-label">手机号</span>
          <!--<input type="text" class="m-setUp-input" placeholder="12345678912">-->
          <span class="m-setUp-input">{{form.usphone}}</span>
        </div>
        <div class="m-row" >
          <span class="m-form-label">地址</span>
          <!--<input type="text" class="m-setUp-input" placeholder="杭州市萧山区宁围镇XX号">-->
          <span class="m-setUp-input">{{form.address}}</span>
          <span class="m-row-btn" @click="addressClick">编辑</span>
        </div>
        <div class="m-row">
          <span class="m-form-label">银行卡</span>
          <!--<input type="text" class="m-setUp-input" placeholder="6222222222222222222">-->
          <span class="m-setUp-input">{{form.bankcard}}</span>
          <!--<router-link to="/bankCard" tag="span">-->
            <span class="m-row-btn" @click="barkChange" v-if="form.bankcard">更换</span>
          <span class="m-row-btn" @click="addChange" v-else>绑定</span>
          <!--</router-link>-->
        </div>
      </div>

      <div class="m-setUp-btn">
        <span>退出登录</span>

      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
  import common from '../../../common/js/common';
    export default {
        data() {
            return {
                form:{
                  usheader:'',
                  usname:'',
                  usphone:'',
                  wxnum:'',
                  bankcard:'',
                  address:''
                }
            }
        },
        components: {},
      mounted(){
        common.changeTitle('账号设置');
      },
        methods: {
          getInfo(){
            axios.get(api.get_account_info,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.form.usheader = res.data.data.user.usheader;
                this.form.usname = res.data.data.user.usname;
                this.form.usphone = res.data.data.user.usphone;
                this.form.wxnum = res.data.data.user.wxnum;
                this.form.address = res.data.data.address;
                this.form.bankcard = res.data.data.bankcard;
              }
            })
          },
          addressClick(){
            this.$router.push('/receiverAddress');
          },
          addChange(){
            this.$router.push('/addBankCard');
            // this.$router.push('/bankCard');
          },
          barkChange(){
            this.$router.push('/bankCard');
            // this.$router.push('/addBankCard');
          }
        },
        created() {
          this.getInfo();
        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
@import "../../../common/css/index";
.m-setUp{
  .m-setUp-logo{
    width: 100%;
    padding: 76px 0;
    text-align: center;
    .m-logo{
      display: inline-block;
      width: 200px;
      height: 200px;
      border-radius: 50%;
      background-color: #a3a3a3;
    }
  }
  .m-setUp-form{
    margin-top: 30px;
    .m-row{
      .flex-row(flex-start);
      border-bottom: 1px solid @borderColor;
      padding: 20px 0;
      font-size: 24px;
      line-height: 32px;
      .m-form-label{
        width: 145px;
        display: inline-block;
        text-align: right;
        color: #c1c1c1;
        margin-right: 45px;
      }
      .m-setUp-input{
        border: none;
        font-size: 24px;
        width: 400px;
        text-align: left;
        &:focus{
          border: none;
        }
      }
      .m-row-btn{
        display: inline-block;
        height: 40px;
        line-height: 40px;
        width: 120px;
        text-align: center;
        background-color: @mainColor;
        color: #fff;
      }
    }
  }
  .m-setUp-btn{
    margin-top: 225px;
    span{
      display: inline-block;
      width: 690px;
      height: 80px;
      line-height: 80px;
      background-color: @mainColor;
      color: #fff;
      font-size: 30px;
    }

  }
}
</style>
