webpackJsonp([0],{"Ks+q":function(t,e){},W2Q3:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});i("mtWM"),i("CaOM");var n={data:function(){return{name:""}},components:{},methods:{isWeiXin:function(){var t=window.navigator.userAgent.toLowerCase();return console.log(t),"micromessenger"==t.match(/MicroMessenger/i)},login:function(){window.location.href="https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxe8e8f6b9351d3587&redirect_uri="+encodeURIComponent("https://daaiti.cn/WeiDian/#/login")+"&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect"}},mounted:function(){this.isWeiXin()&&this.$route.query.code&&(window.localStorage.setItem("code",this.$route.query.code),this.$router.push("/index/index"))},created:function(){}},s={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"m-login"},[e("img",{staticClass:"m-login-logo",attrs:{src:"",alt:""}}),this._v(" "),e("div",{staticClass:"m-login-btn"},[e("span",{on:{click:this.login}},[this._v("微信登录")])]),this._v(" "),this._m(0)])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"m-login-bottom"},[e("span",{staticClass:"m-login-check-box"},[e("span",{staticClass:"m-login-check"}),this._v(" "),e("span",[this._v("我已阅读并同意《用户使用协议》")])])])}]};var o=i("VU/8")(n,s,!1,function(t){i("Ks+q")},null,null);e.default=o.exports}});
//# sourceMappingURL=0.ffe5615fec9ed689f09c.js.map