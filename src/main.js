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

// let token = "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzODI2MDU2OSwiaWF0IjoxNTM4MTg4NTY5fQ.eyJtb2RlbCI6IlVzZXIiLCJpZCI6ImVmYzk4OWVlLWMyZWUtMTFlOC04NmE1LTAwMTYzZTBjYzAyNCIsInRpbWUiOiIyMDE4LTA5LTI5IDEwOjM2OjA5In0.5HfsnyBqICr3TRiMShvL8SCb95SA5BNRTq8fn0i0_IM";
// localStorage.setItem('token', token);


// 点击预览图片
// document.getElementById('#app').on('click','img',function(){
//   console.log(this)
//   // var src = $(this).attr('src');
//   // var imgs = $(this).parent().parent().find('img');
//   // var list = new Array();
//   // for (var i = 0; i < imgs.length; i++) {
//   //   list.push($(imgs[i]).attr('src'));
//   // }
//   // wx.previewImage({
//   //   current: src, // 当前显示图片的http链接
//   //   urls: list // 需要预览的图片http链接列表
//   // });
// });


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
axios.interceptors.response.use(data => {// 响应成功关闭loading
  // loadinginstace.close()
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

//引入微信
import 'weixin-js-sdk';

import store from './vuex'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
