webpackJsonp([0],{"/GEb":function(t,e){},"1kS7":function(t,e){e.f=Object.getOwnPropertySymbols},C3lA:function(t,e,n){"use strict";var a=n("CaOM"),i={name:"navbar",data:function(){return{}},props:{list:{type:Array,default:null}},methods:{navClick:function(t){if(this.list[t].click)return!1;a.a.changeTitle(this.list[t].tnname),this.$emit("navClick",t)}},mounted:function(){}},s={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"m-navbar"},[n("ul",{staticClass:"ul-four"},t._l(t.list,function(e,a){return n("li",{class:e.click?"active":"",on:{click:function(e){t.navClick(a)}}},[n("span",{staticClass:"m-navbar-text"},[t._v(t._s(e.tnname))]),t._v(" "),e.dot?n("span",{staticClass:"m-dot"}):t._e()])}))])])},staticRenderFns:[]};var c=n("VU/8")(i,s,!1,function(t){n("D9YU")},"data-v-7a665900",null);e.a=c.exports},D9YU:function(t,e){},NpIQ:function(t,e){e.f={}.propertyIsEnumerable},P9l9:function(t,e,n){"use strict";var a="https://weidian.daaiti.cn",i={login:a+"/user/login",get_accesstoken:a+"/user/get_accesstoken",get_config:a+"/user/get_wx_config",get_all_banner:a+"/banner/get_all",get_home_banner:a+"/bigactivity/get_home_banner",get_all_hotmessage:a+"/hotmessage/get_all",get_all_activity:a+"/activity/get_all",get_home_topnav:a+"/topnav/get_home",ac_like:a+"/activitylike/ac_like",get_search:a+"/searchfield/get_search",get_dp_topnav:a+"//topnav/get_dp",get_info_recommend:a+"/recommend/get_info",get_all_recommendbanner:a+"/recommendbanner/get_all",get_discover_banner:a+"/bigactivity/get_discover_banner",re_like:a+"/recommendlike/re_like",add_comment:a+"/activitycomment/add_comment",get_list:a+"/activitycomment/get_list",share_qrcode:a+"/activity/share_qrcode",generate_poster:a+"/activity/generate_poster",get_order_count:a+"/order/get_count",get_more_order:a+"/order/get_more",get_list_order:a+"/order/get_list",get_info_mycenter:a+"/mycenter/get_info",get_account_info:a+"/mycenter/get_account_info",add_one_complain:a+"/complain/add_one",get_prlike_productlike:a+"/productlike/get_prlike",batch_del_productlike:a+"/productlike/batch_del",get_myimg_adimage:a+"/adimage/get_myimg",get_rule_mycenter:a+"/mycenter/get_rule",get_address:a+"/mycenter/get_address",add_address:a+"/mycenter/add_address",del_address:a+"/mycenter/del_address",update_address:a+"/mycenter/update_address",get_bank_list:a+"/mycenter/get_bank_list",add_bankcard:a+"/mycenter/add_bankcard",get_mybankcard:a+"/mycenter/get_mybankcard",get_province:a+"/mycenter/get_province",get_city:a+"/mycenter/get_city",get_area:a+"/mycenter/get_area",get_inforcode:a+"/mycenter/get_inforcode",verify_inforcode:a+"/mycenter/verify_inforcode",update_bankcard:a+"/mycenter/update_bankcard",del_bankcard:a+"/mycenter/del_bankcard",get_user_task:a+"/task/get_user_task",do_task:a+"/task/do_task",get_bigactivity:a+"/bigactivity/get_bigactivity",get_one_product:a+"/product/get_one"};e.a=i},QLTB:function(t,e,n){"use strict";var a={data:function(){return{select:""}},props:{slots:{type:Array,default:null},show_picker:{type:Boolean,default:!1},params:{type:String,default:""}},methods:{onValuesChange:function(t,e){this.select=e},pickerSave:function(t){this.$emit("pickerSave",t,this.select,this.params)},cancelSave:function(t){this.$emit("pickerSave",t)}}},i={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return t.show_picker?n("div",{staticClass:"m-picker-status"},[n("div",{staticClass:"m-picker-box"},[n("p",{staticClass:"m-picker-text"},[n("span",{staticClass:"cancel",on:{click:function(e){t.cancelSave(!1)}}},[t._v("取消")]),t._v(" "),n("span",{staticClass:"m-picker-btn",on:{click:function(e){t.pickerSave(!1)}}},[t._v("确定")])]),t._v(" "),n("mt-picker",{attrs:{slots:t.slots},on:{change:t.onValuesChange}})],1)]):t._e()},staticRenderFns:[]};var s=n("VU/8")(a,i,!1,function(t){n("w8RU")},"data-v-31a5a507",null);e.a=s.exports},R4wc:function(t,e,n){var a=n("kM2E");a(a.S+a.F,"Object",{assign:n("To3L")})},RCQN:function(t,e){},To3L:function(t,e,n){"use strict";var a=n("lktj"),i=n("1kS7"),s=n("NpIQ"),c=n("sB3e"),r=n("MU5D"),o=Object.assign;t.exports=!o||n("S82l")(function(){var t={},e={},n=Symbol(),a="abcdefghijklmnopqrst";return t[n]=7,a.split("").forEach(function(t){e[t]=t}),7!=o({},t)[n]||Object.keys(o({},e)).join("")!=a})?function(t,e){for(var n=c(t),o=arguments.length,l=1,u=i.f,m=s.f;o>l;)for(var d,g=r(arguments[l++]),f=u?a(g).concat(u(g)):a(g),_=f.length,p=0;_>p;)m.call(g,d=f[p++])&&(n[d]=g[d]);return n}:o},UNoc:function(t,e){},V3tA:function(t,e,n){n("R4wc"),t.exports=n("FeBl").Object.assign},Y43X:function(t,e,n){"use strict";var a={props:{name:{type:String,default:null}}},i={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"m-label"},[e("span",{staticClass:"m-triangle"}),this._v(" "),e("span",{staticClass:"m-text"},[this._v(this._s(this.name))])])},staticRenderFns:[]};var s=n("VU/8")(a,i,!1,function(t){n("rmNv")},"data-v-e8a42a90",null).exports,c=n("ug6D"),r=n("flXH"),o={mixins:[r.a],data:function(){return{}},props:{list:{type:Object,default:null},index:{type:Number,default:null}},components:{"m-label":s,"icon-list":c.a},mounted:function(){window.setInterval(this.getDJS,1e3)},methods:{bigImg:function(t,e){for(var n=[],a=0;a<e.length;a++)n.push(e[a].amimage);var i={current:n[t],urls:n};r.a.previewImage(i)},iconClick:function(t){this.$emit("iconClick",t,this.index)},showMoreText:function(t){this.$emit("showMoreText",t,this.index)},getDJS:function(){if(!this.list.acendtime)return!1;var t=new Date(this.list.acendtime.slice(0,4),this.list.acendtime.slice(4,6)-1,this.list.acendtime.slice(6,8),this.list.acendtime.slice(8,10),this.list.acendtime.slice(10,12),this.list.acendtime.slice(12)),e=new Date,n=t.getTime()-e.getTime();if(n>0){var a=Math.floor(n/1e3/60/60/24),i=Math.floor(n/1e3/60/60%24),s=Math.floor(n/1e3/60%60),c=[].concat(this.list.remaintime);c[0]=a,c[1]=i,c[2]=s,this.list.remaintime=[].concat(c)}},ctxClick:function(t){switch(t.acskiptype){case 1:0==t.bigactivity.type?this.$router.push({path:"/activityContent",query:{baid:t.aclinkvalue,baimage:bigactivity.baimage}}):this.$router.push({path:"/activityContent",query:{baid:t.aclinkvalue}});break;case 2:this.$router.push({path:"/productDetail",query:{prid:t.aclinkvalue}})}}}},l={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"m-section-one",on:{click:function(e){t.ctxClick(t.list)}}},[t.list.suuser&&t.list.suuser.suheader?n("img",{staticClass:"m-section-img",attrs:{src:t.list.suuser.suheader}}):t._e(),t._v(" "),n("div",{staticClass:"m-section-content"},[n("div",{staticClass:"m-section-title"},[t.list.suuser&&t.list.suuser.suname?n("span",{staticClass:"m-title"},[t._v(t._s(t.list.suuser.suname))]):t._e(),t._v(" "),t.list.soldnum?n("span",{staticClass:"m-sale"},[t._v("已售"+t._s(t.list.soldnum)+"件")]):t._e()]),t._v(" "),n("div",{staticClass:"m-section-text"},[n("p",{staticClass:"textP",class:t.list.show_text?"":"active"},[t._v("  "+t._s(t.list.actext))]),t._v(" "),t.list.show_text?n("span",{staticClass:"m-section-more",on:{click:function(e){e.stopPropagation(),t.showMoreText(!1)}}},[t._v("展开全文")]):t._e(),t._v(" "),t.list.actext.length>92&&!t.list.show_text?n("span",{staticClass:"m-section-more",on:{click:function(e){e.stopPropagation(),t.showMoreText(!0)}}},[t._v("收起全文")]):t._e(),t._v(" "),n("ul",{staticClass:"m-img-list"},[t._l(t.list.media,function(e,a){return[n("li",[e.amimage?n("img",{staticClass:"m-section-text-imgs",class:4==t.list.media.length?"active":"",attrs:{src:e.amimage},on:{click:function(e){e.stopPropagation(),t.bigImg(a,t.list.media)}}}):t._e()])]})],2),t._v(" "),n("div",{staticClass:"m-section-bottom"},[n("div",[t.list.product?n("div",[null!=t.list.product&&t.list.product.prprice?n("span",{staticClass:"m-price-unit"},[t._v("￥")]):t._e(),t._v(" "),null!=t.list.product&&t.list.product.prprice?n("span",{staticClass:"m-price "},[t._v(t._s(t.list.product.prprice))]):t._e(),t._v(" "),null!=t.list.product&&t.list.product.prsavemonty?n("span",{staticClass:"m-red m-ft-30"},[t._v("赚"+t._s(t.list.product.prsavemonty))]):t._e()]):t._e(),t._v(" "),n("div",{staticClass:"m-red m-ft-22"},[t._v("距活动结束仅剩"+t._s(t.list.remaintime[0]||"0")+"天"+t._s(t.list.remaintime[1]||"0")+"小时"),0==t.list.remaintime[0]?n("span",[t._v(t._s(t.list.remaintime[2]||"0")+"分钟")]):t._e()])]),t._v(" "),n("div",[n("ul",{staticClass:"m-icon-list"},t._l(t.list.icon,function(e,a){return n("li",{on:{click:function(e){e.stopPropagation(),t.iconClick(a)}}},[e.alreadylike?n("img",{staticClass:"m-icon",attrs:{src:"/static/images/"+e.src+"-active.png",alt:""}}):n("img",{staticClass:"m-icon",attrs:{src:"/static/images/"+e.src+".png",alt:""}}),t._v("\n              "+t._s(e.name)+"\n            ")])}))])])])]),t._v(" "),t.list.tags[0]?n("m-label",{attrs:{name:t.list.tags[0].atname}}):t._e()],1)},staticRenderFns:[]};var u=n("VU/8")(o,l,!1,function(t){n("UNoc")},"data-v-0bebf91a",null);e.a=u.exports},e81K:function(t,e,n){"use strict";var a={name:"share",data:function(){return{}},props:{num:{type:Number,default:3},item:{type:Object,default:{}}},methods:{fixedClick:function(){this.$emit("fixedClick")},share:function(t){this.$emit("share",t,this.item)}},mounted:function(){}},i={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"m-fixed",on:{click:t.fixedClick}},[n("div",{staticClass:"m-fixed-state"},[n("h3",[t._v("转发到")]),t._v(" "),n("ul",{staticClass:"m-share-list"},[3==t.num?n("li",{on:{click:function(e){e.stopPropagation(),t.share("appmessage")}}},[n("img",{staticClass:"m-share-icon",attrs:{src:"/static/images/icon-wei.png",alt:""}}),t._v("\n        转发到微信好友\n      ")]):t._e(),t._v(" "),n("li",{on:{click:function(e){e.stopPropagation(),t.share("line")}}},[n("img",{staticClass:"m-share-icon",attrs:{src:"/static/images/icon-peng.png",alt:""}}),t._v("\n        转发到朋友圈\n      ")]),t._v(" "),t._m(0)])])])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("li",[e("img",{staticClass:"m-share-icon",attrs:{src:"/static/images/icon-link.png",alt:""}}),this._v("\n        转发商品链接\n      ")])}]};var s=n("VU/8")(a,i,!1,function(t){n("hQp4")},"data-v-33f9e078",null);e.a=s.exports},flXH:function(t,e,n){"use strict";var a=n("fxnj"),i=n.n(a),s=n("mtWM"),c=n.n(s),r=n("P9l9"),o=n("Au9i"),l=(n.n(o),{isweixin:function(){return"micromessenger"==window.navigator.userAgent.toLowerCase().match(/MicroMessenger/i)||(this.$router.push({path:"/wxkj/isnotWechat"}),!1)},isWxAuth:function(){localStorage.getItem("localUid");if(!localStorage.getItem("localToken")){var t=this.$route.query.token,e=this.$route.query.uid;if(t)localStorage.setItem("localToken",t),localStorage.setItem("localUid",e);else{var n=encodeURIComponent(window.location.href);window.location.href=hostName+"/wxpl/oauth?forwardUrl="+n}}},wxRegister:function(t){c.a.get(r.a.get_config,{params:{url:window.location.href}}).then(function(t){200==t.data.status&&i.a.config({debug:!1,appId:t.data.data.appId,timestamp:Number(t.data.data.timestamp),nonceStr:t.data.data.noncestr,signature:t.data.data.sign,jsApiList:["onMenuShareTimeline","onMenuShareAppMessage","uploadImage","previewImage","chooseImage","downloadImage"]})}).catch(function(t){console.log(t,"1111")}),i.a.ready(function(t){i.a.onMenuShareTimeline({title:"微点",link:window.location.href+"?UPPerd="+localStorage.getItem("openid"),success:function(){Object(o.Toast)({message:"分享成功",className:"m-toast-success"})},cancel:function(){},error:function(){Object(o.Toast)({message:"分享失败，请稍后再试",className:"m-toast-fail"})}}),i.a.onMenuShareAppMessage({title:"微点",link:window.location.href+"?UPPerd="+localStorage.getItem("openid"),success:function(){Object(o.Toast)({message:"分享成功",className:"m-toast-success"})},cancel:function(){},error:function(){Object(o.Toast)({message:"分享失败，请稍后再试",className:"m-toast-fail"})}})})},ShareTimeline:function(t){i.a.ready(function(){i.a.onMenuShareAppMessage({title:t.title||"1111",link:t.link||"",imgUrl:t.imgUrl||"",success:function(){t.success()},cancel:function(){t.error()},error:function(){console.log("1112")}}),i.a.onMenuShareTimeline({title:t.title||"1111",link:t.link||"",imgUrl:t.imgUrl||"",success:function(){t.success()},cancel:function(){t.error()},error:function(){console.log("1112")}})})},ShareAppMessage:function(t){i.a.ready(function(e){i.a.onMenuShareAppMessage({title:t||"1111",link:t.link||"",imgUrl:t.imgUrl||"",success:function(){t.success()},cancel:function(){t.error()},error:function(){console.log("1112")}}),i.a.onMenuShareTimeline({title:t.title||"1111",link:t.link||"",imgUrl:t.imgUrl||"",success:function(){t.success()},cancel:function(){t.error()},error:function(){console.log("1112")}})})},previewImage:function(t){i.a.previewImage({current:t.current,urls:t.urls,success:function(){console.log("success",t)},failed:function(){console.log("failed",t)}})}});e.a=l},hQp4:function(t,e){},iO08:function(t,e,n){"use strict";var a=n("flXH"),i=n("mtWM"),s=n.n(i),c=n("P9l9"),r={mixins:[a.a],data:function(){return{name:"",wximg:localStorage.getItem("wximg"),is_sub:localStorage.getItem("subscribe")}},props:{src:{type:String,default:null},components_src:{type:String,default:null},show_fixed:{type:Boolean,default:!1},shareParams:{type:Object,default:null}},methods:{closeModal:function(){this.$emit("closeModal")},shareImg:function(){for(var t=this,e=[],n=0;n<t.shareParams.media.length;n++)e.push(t.shareParams.media[n].amimage);var a=document.createElement("canvas"),i=a.getContext("2d");a.height=1275,4==e.length?a.width=1525:6==e.length&&(a.width=2150),i.rect(0,0,a.width,a.height),i.fillStyle="#fff",i.fill(),i.fillStyle="#000000",i.font="30px PingFang-SC";var s=this.shareParams.product.prname;if(s.length<12||12==s.length)for(var c=0;c<s.length;c++)i.fillText(s[c],90+34*c,970);if(s.length>12)for(var r=12;r<23;r++)i.fillText(s[r],90+34*(r-12),1015),22==r&&i.fillText("...",90+34*(r-12+1),1015);var o=this.shareParams.product.prprice.split(".");i.fillStyle="#f43b51",i.font="bold 30px PingFang-SC",i.fillText("￥",90,1150),i.font="bold 58px PingFang-SC",i.fillText(o[0],120,1150),i.font="bold 30px PingFang-SC",i.fillText(". "+o[1],230,1150),i.fillStyle="#a4a4a4",i.font="30px PingFang-SC",i.fillText("原价：￥"+this.shareParams.product.prprice,90,1200);var l=new Image;l.crossOrigin="Anonymous",l.src="/static/images/share/bg_test.png",l.onload=function(){var n=new Image;n.crossOrigin="Anonymous",n.src="/static/images/share/sweep.png",n.onload=function(){i.drawImage(n,560,1190,260,60);var s=new Image;s.crossOrigin="Anonymous",s.src=t.src,s.onload=function(){i.drawImage(s,560,920,260,260);var n=new Image;n.crossOrigin="Anonymous",n.src=t.components_src,n.onload=function(){i.drawImage(n,50,825,800,55),console.log(n);var s=new Image;s.crossOrigin="Anonymous",s.src=e[0],s.onload=function(){i.drawImage(s,50,25,800,800),console.log(s);var n=new Image;n.crossOrigin="Anonymous",n.src=e[1],n.onload=function(){i.drawImage(n,875,25,600,600),console.log(n);var s=new Image;s.crossOrigin="Anonymous",s.src=e[2],s.onload=function(){i.drawImage(s,875,650,600,600),console.log(s);var n=new Image;n.crossOrigin="Anonymous",n.src="/static/images/share/delete.png",n.onload=function(){if(i.drawImage(n,175,1180,150,20),console.log(n),6==e.length){var s=new Image;s.crossOrigin="Anonymous",s.src=e[3],s.onload=function(){i.drawImage(s,1500,25,600,600);var n=new Image;n.crossOrigin="Anonymous",n.src=e[4],n.onload=function(){i.drawImage(n,1500,650,600,600);var e=a.toDataURL("image/png");document.getElementById("avatar").setAttribute("src",e),t.postImg(e)}}}if(4==e.length){var c=a.toDataURL("image/png");document.getElementById("avatar").setAttribute("src",c),t.postImg(c)}}}}}}}}}},postImg:function(t){s.a.post(c.a.generate_poster+"?token="+localStorage.getItem("token"),{baseimg:t}).then(function(t){})},dataURItoBlob:function(t){var e;e=t.split(",")[0].indexOf("base64")>=0?atob(t.split(",")[1]):unescape(t.split(",")[1]);for(var n=t.split(",")[0].split(":")[1].split(";")[0],a=new Uint8Array(e.length),i=0;i<e.length;i++)a[i]=e.charCodeAt(i);return new Blob([a],{type:n})}},mounted:function(){this.shareImg()},created:function(){}},o={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"m-modal m-share"},[n("div",{staticClass:"m-modal-state"},[n("div",{staticClass:"m-modal-head"},[n("span",{staticClass:"m-close",on:{click:function(e){t.closeModal("show_fixed")}}},[t._v(" x ")])]),t._v(" "),t.is_sub?t._e():n("div",{staticClass:"m-modal-content"},[n("h3",{staticClass:"h3-text"},[t._v("还差一步就可以转发内容啦")]),t._v(" "),n("div",[n("img",{staticClass:"m-share-img",attrs:{src:t.wximg,alt:""}}),t._v(" "),n("p",{staticClass:"grey-text"},[t._v("关注公众号获取")])])]),t._v(" "),t.is_sub?n("div",{staticClass:"m-modal-content"},[n("img",{staticClass:"canvas-img",attrs:{id:"avatar"}}),t._v(" "),n("p",{staticClass:"grey-text"},[t._v("长按图片分享您的专属二维码")])]):t._e()])])},staticRenderFns:[]};var l=n("VU/8")(r,o,!1,function(t){n("oY/4")},"data-v-5279a129",null);e.a=l.exports},"oY/4":function(t,e){},rmNv:function(t,e){},ug6D:function(t,e,n){"use strict";var a={data:function(){return{}},props:{list:{type:Array,default:[{src:"icon-like",name:"1",url:"icon-like"},{src:"icon-share",name:"转发",url:"icon-share"}]},index:{type:Number,default:0}},methods:{iconClick:function(t){this.$emit("iconClick",t,this.index)}}},i={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("ul",{staticClass:"m-icon-list"},t._l(t.list,function(e,a){return n("li",{on:{click:function(e){t.iconClick(a)}}},[n("img",{staticClass:"m-icon",attrs:{src:"/static/images/"+e.src+".png",alt:""}}),t._v("\n    "+t._s(e.name)+"\n  ")])}))},staticRenderFns:[]};var s=n("VU/8")(a,i,!1,function(t){n("/GEb")},"data-v-ea3f305c",null);e.a=s.exports},w8RU:function(t,e){},woOf:function(t,e,n){t.exports={default:n("V3tA"),__esModule:!0}},"zpT/":function(t,e,n){"use strict";var a={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"nav-span"},t._l(t.sub,function(e,a){return n("span",{staticClass:"nav-span-box"},[n("span",{staticClass:"nav-span-text m-ft-20 tc",class:a==t.subClick?"active":"",on:{click:function(n){t.changeSubClick(e,a)}}},[t._v(t._s(e))])])}))])},staticRenderFns:[]};var i=n("VU/8")({name:"differentDays",data:function(){return{sub:["今天","7天","15天","30天"],subClick:0}},methods:{changeSubClick:function(t,e){this.subClick=e}}},a,!1,function(t){n("RCQN")},null,null);e.a=i.exports}});
//# sourceMappingURL=0.debfdaa88d58e3d27292.js.map