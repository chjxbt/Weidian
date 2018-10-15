<template>
    <div class="m-login">
      <img src="" class="m-login-logo" alt="">
      <div class="m-login-btn">
        <span @click="login">微信登录</span></div>
      <!--<div class="m-login-bottom">-->
        <!--<span class="m-login-check-box">-->
          <!--<span class="m-login-check" :class="check?'active':''" @click.stop="checkClick"></span>-->
          <!--&lt;!&ndash;<input type="checkbox" class="m-login-check">&ndash;&gt;-->
          <!--<span>我已阅读并同意《用户使用协议》</span>-->
        <!--</span>-->
      <!--</div>-->
    </div>


</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../api/api';
  import common from '../../common/js/common';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                name: '',
              check:true
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
            if(this.check){
              axios.get(api.get_config,{
                params:{
                  url: window.location.href
                }
              } ).then((res) => {
                if(res.data.status == 200){
                  const id = res.data.data.appId
                  const url = window.location.href;
                  // const  url = 'https://daaiti.cn/WeiDian/#/login';
                  window.location.href = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='
                    +  id + '&redirect_uri='+ encodeURIComponent(url) + '&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect'
                }

              }).catch((error) => {
                console.log(error ,'1111')
              })

            }else{

            }


          },
          checkClick(){
            this.check = !this.check;
          }
        },
      mounted(){
        common.changeTitle('登录');
        if(this.isWeiXin()){    //是来自微信内置浏览器
          // 获取微信信息，如果之前没有使用微信登陆过，将进行授权登录
          if(common.GetQueryString('code')){
            // alert(common.GetQueryString('code'))
            window.localStorage.setItem("code",common.GetQueryString('code'));
            axios.get(api.get_accesstoken,{
              params:{
                code: common.GetQueryString('code'),
                UPPerd:localStorage.getItem('UPPerd') || ''
              }
            }).then(res => {
              if(res.data.status == 200){
                window.localStorage.setItem("access_token",res.data.data.access_token);
                window.localStorage.setItem("token",res.data.data.token);
                window.localStorage.setItem("openid",res.data.data.openid);
                window.localStorage.setItem("is_first",String(res.data.data.is_first));
                window.localStorage.setItem("wximg",res.data.data.wximg);
                window.localStorage.setItem("subscribe",res.data.data.subscribe);
                window.localStorage.setItem("is_today_first",res.data.data.is_today_first);
                window.localStorage.setItem("user_level",res.data.data.user_level);
                this.$store.state.tabbar = res.data.data.icon;
                this.$store.state.tabbar_select = res.data.data.icon[0].name;
                this.$router.push('/index/index');
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            });
          }
        }
      },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
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
      box-shadow: 0 13px 22px 0 rgba(9, 187, 7, 0.35);
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
      background: url("/static/images/icon-check-personal.png") no-repeat center;
      background-size: 100% 100%;
      vertical-align: bottom;
      &.active{
        background: url("/static/images/icon-check-personal-active.png") no-repeat center;
        background-size: 100% 100%;
      }
    }
  }
}
</style>
