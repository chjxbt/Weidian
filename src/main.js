// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import 'lib-flexible'
Vue.config.productionTip = false

//mint-ui
import Mint from 'mint-ui';
Vue.use(Mint);
import 'mint-ui/lib/style.css'
import VueClipboard from 'vue-clipboard2'

import router from './router'
VueClipboard.config.autoSetContainer = true // add this line
Vue.use(VueClipboard)

/*点击事件延迟问题*/
import fastClick from 'fastclick'
fastClick.attach(document.body)
//视频播放
// import VideoPlayer from 'vue-video-player'
// require('video.js/dist/video-js.css')
// require('vue-video-player/src/custom-theme.css')
// Vue.use(VideoPlayer)

//处理移动端click事件300毫秒延迟。
import FastClick from 'fastclick'
FastClick.attach(document.body);

import promise from 'es6-promise';//解决axios在ie9下不生效的方法
promise.polyfill();
//
// // let token = "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzOTYwMjMyOCwiaWF0IjoxNTM5NTk1MTI4fQ.eyJtb2RlbCI6IlVzZXIiLCJpZCI6Impma3NhZGpmLWZkYXNsa2pmLTMyMTMtMzEyMzEiLCJ0aW1lIjoiMjAxOC0xMC0xNSAxNzoxODo0OCJ9.GPSNz79JnUbsXOQ3BwD-e-Q5_XFrqPE__X2PYQ9XMGc";
// let token = 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTU0MDIwNzI5MywiaWF0IjoxNTQwMjAwMDkzfQ.eyJtb2RlbCI6IlVzZXIiLCJpZCI6Impma3NhZGpmLWZkYXNsa2pmLTMyMTMtMzEyMzEiLCJ0aW1lIjoiMjAxOC0xMC0yMiAxNzoyMTozMyJ9.NntQ_8KXxrUT6FmnB3HUSKypSqvyEidOxnHD73otDlA'
// localStorage.setItem('token', token);



Vue.prototype.$http = axios;
//拦截器、
// import { Loading, Message, MessageBox  } from 'element-ui'
import { Indicator } from 'mint-ui';
// 超时时间
axios.defaults.timeout = 600000
//http请求拦截器
var loadinginstace
axios.interceptors.request.use(config => {
  // element ui Loading方法
  // loadinginstace = Loading.service({ fullscreen: true });
  // console.log(loadinginstace)
  Indicator.open({ text: '加载中...', spinnerType: 'fading-circle' });
  return config
}, error => {
  // Message({
  //   message:'加载超时',
  //   type:'warning'
  // });
  // loadinginstace.close()
  Indicator.close();
  return Promise.reject(error)
})
// http响应拦截器
import api from './api/api'
axios.interceptors.response.use(data => {// 响应成功关闭loading
  // loadinginstace.close()

  if(data.data.status_code == 403001 ){
    axios.get(api.get_config,{
      params:{
        url: window.location.href
      }
    } ).then((res) => {
      if(res.data.status == 200){
        const id = res.data.data.appId
        const url = window.location.origin + '/#/index/index';
        // const  url = 'https://daaiti.cn/WeiDian/#/login';
        window.location.href = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='
          +  id + '&redirect_uri='+ encodeURIComponent(url) + '&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect'
      }

    }).catch((error) => {
      console.log(error ,'1111')
    })
  }
  Indicator.close();
  return data
}, error => {
  // Message({
  //   message:'请求失败',
  //   type:'warning'
  // });
  // loadinginstace.close()
  Indicator.close();
  return Promise.reject(error)
})
import store from './vuex';

//引入微信
import 'weixin-js-sdk';


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
