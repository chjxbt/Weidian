<template>
    <div class="m-login">
      <img src="" class="m-login-logo" alt="">
      <div class="m-login-btn">
        <span @click="login">微信登录</span></div>
      <div class="m-login-bottom">
        <span class="m-login-check-box">
          <span class="m-login-check"></span>
          <span>我已阅读并同意《用户使用协议》</span>
        </span>
      </div>
    </div>


</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../api/api';
  import common from '../../common/js/common'
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {},
        methods: {
          isWeiXin() {
            let ua = window.navigator.userAgent.toLowerCase();
            console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
            if (ua.match(/MicroMessenger/i) == 'micromessenger') {
              return true;
            } else {
              return false;
            }

          },
          login() {
            const id = 'wxe8e8f6b9351d3587'
            const url = window.location.href;
            // const  url = 'https://daaiti.cn/WeiDian/#/login';

            window.location.href = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='
            +  id + '&redirect_uri='+ encodeURIComponent(url) + '&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect'

          }
        },
      mounted(){
        if(this.isWeiXin()){    //是来自微信内置浏览器
          // 获取微信信息，如果之前没有使用微信登陆过，将进行授权登录
          if(common.GetQueryString('code')){
            alert(common.GetQueryString('code'))
            window.localStorage.setItem("code",common.GetQueryString('code'));
            axios.get(api.get_accesstoken,{
              params:{
                code: common.GetQueryString('code')
              }
            }).then(res => {

            });
            this.$router.push('/index/index');
          }
        }
      },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
.m-login{
  background-color: #9fd0bf;
  min-height: 100%;
  .m-login-logo{
    display: inline-block;
    width: 400px;
    height: 200px;
    border: 1px solid #a4a4a4;
    margin: 300px 0;
  }
  .m-login-btn{
    margin-top: 150px;
    span{
      display: inline-block;
      width: 630px;
      height: 97px;
      line-height: 97px;
      color: #fff;
      font-size: 32px;
      border-radius: 48.5px;
      background-color: #09bb07;
      box-shadow: 0px 13px 22px 0 rgba(9, 187, 7, 0.35);
    }
  }
  .m-login-bottom{
    margin-top: 40px;
    font-size: 22px;
    color: #666;
    line-height: 25px;
    .m-login-check{
      display: inline-block;
      width: 23px;
      height: 23px;
      border: 1px solid #a4a4a4;
      vertical-align: bottom;

    }
  }
}
</style>
