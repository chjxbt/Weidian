<template>
  <div id="app">
    <!--<span class="m-return" @click.stop="returnClick">返回</span>-->
    <router-view/>
  </div>
</template>

<script>
  import common from './common/js/common';
  import axios from 'axios';
  import api from './api/api';
  import {Toast} from 'mint-ui';
export default {
  name: 'App',
  mounted(){
    alert(common.GetQueryString('code'))
    if(!localStorage.getItem('token')){
      this.login();
    }
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
            // this.$router.push('/index/index');
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        });
      }
    }
  },
  methods:{
    returnClick(){
      this.$router.go(-1);
    },
    login(){
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
    },
    isWeiXin() {
      let ua = window.navigator.userAgent.toLowerCase();
      console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
      if (ua.match(/MicroMessenger/i) == 'micromessenger') {
        return true;
      } else {
        return false;
      }

    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;

}
.m-return{
  position: fixed;
  left: 10px;
  top: 10px;
  width: 80px;
  height: 40px;
  line-height: 44px;
  border-radius: 15px;
  background-color: rgba(0,0,0,0.2);
  color: #f7f7f7;
  z-index: 10000;
}
</style>
