webpackJsonp([25],{"1ghh":function(t,a){},ctS4:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var i=s("mtWM"),e=s.n(i),n=s("P9l9"),o=s("Au9i"),c=s("CaOM"),l=s("zfeG"),r=s("flXH"),m={mixins:[r.a],data:function(){return{name:"",show_modal:!1,show_img:!1,img_src:"",bg_img:"",show_invite:!1}},components:{imgModal:l.a},mounted:function(){this.getRule(9),r.a.wxRegister(this.wxRegCallback),c.a.changeTitle("邀请专属粉丝")},methods:{fansClick:function(){this.$router.push("/fansManagement")},sharePoster:function(){this.$router.push("/poster")},wxRegCallback:function(){this.wxShare()},wxShare:function(){var t={title:"微点13213",link:window.location.origin+"/#/index?UPPerd="+localStorage.getItem("openid"),success:function(){alert("分享成功")},error:function(){alert("分享失败")}};r.a.ShareTimeline(t),this.show_invite=!0},share:function(){this.wxShare()},copyText:function(){var t=this;this.$copyText(window.location.origin+"/#/login").then(function(a){t.show_modal=!0},function(t){})},getRule:function(t){var a=this;e.a.get(n.a.get_image_by_aitype,{params:{token:localStorage.getItem("token"),aitype:t}}).then(function(s){200==s.data.status?9==t?a.bg_img=s.data.data.aiimage:(a.show_img=!0,a.img_src=s.data.data.aiimage):Object(o.Toast)({message:s.data.message,className:"m-toast-fail"})},function(t){Object(o.Toast)({message:t.data.message,className:"m-toast-fail"})})},closeModal:function(t){this[t]=!1}},created:function(){}},d={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"m-fans"},[t.show_modal?s("div",{staticClass:"m-modal m-copy-text"},[s("div",{staticClass:"m-modal-state"},[s("div",{staticClass:"m-modal-head"},[s("span",{staticClass:"m-close",on:{click:function(a){t.closeModal("show_modal")}}},[t._v(" x ")])]),t._v(" "),t._m(0)])]):t._e(),t._v(" "),s("img",{staticClass:"m-fans-bg",attrs:{src:t.bg_img,alt:""}}),t._v(" "),s("div",{staticClass:"m-fans-rule",on:{click:function(a){t.getRule(6)}}}),t._v(" "),s("div",{staticClass:"m-fans-details",on:{click:function(a){t.getRule(14)}}}),t._v(" "),s("div",{staticClass:"m-fans-fans-details",on:{click:t.fansClick}}),t._v(" "),s("div",{staticClass:"m-fans-share-poster",on:{click:t.sharePoster}}),t._v(" "),s("div",{staticClass:"m-fans-share-link",on:{click:t.share}}),t._v(" "),t.show_img?s("img-modal",{attrs:{src:t.img_src},on:{closeModal:t.closeModal}}):t._e(),t._v(" "),t.show_invite?s("img",{staticClass:"m-invite-course",attrs:{src:"/static/images/invite.png",alt:""},on:{click:function(a){a.stopPropagation(),t.closeModal("show_invite")}}}):t._e()],1)},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"m-modal-content"},[a("h3",[this._v("链接已经复制成功")]),this._v(" "),a("p",[this._v("您可以去分享给好友啦！\n        ")])])}]};var h=s("VU/8")(m,d,!1,function(t){s("1ghh")},"data-v-53d5d39e",null);a.default=h.exports}});
//# sourceMappingURL=25.346e26be14d625e9bbbd.js.map