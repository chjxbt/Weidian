webpackJsonp([6],{A2Dw:function(t,a,s){"use strict";var e={name:"search",data:function(){return{value:""}},props:{search:{type:Boolean,default:!0}},methods:{inputClick:function(t){t.preventDefault(),this.$emit("inputClick")},searchClick:function(){this.$emit("searchClick",this.value)}}},i={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"m-search"},[t.search?s("div",{staticClass:"m-search-text",on:{click:t.inputClick}},[s("span",{staticClass:"m-search-icon",on:{click:t.inputClick}}),t._v(" "),s("span",{on:{click:t.inputClick}},[t._v("搜索商品、品牌")])]):t._e(),t._v(" "),t.search?t._e():s("div",{staticClass:"m-input"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.value,expression:"value"}],attrs:{type:"text",autofocus:"!search",placeholder:""},domProps:{value:t.value},on:{input:function(a){a.target.composing||(t.value=a.target.value)}}}),t._v(" "),s("span",{on:{click:function(a){return a.stopPropagation(),t.searchClick(a)}}},[t._v("搜索")])])])},staticRenderFns:[]};var o=s("VU/8")(e,i,!1,function(t){s("m1pt")},"data-v-5ae4b5ea",null);a.a=o.exports},JXTs:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=s("woOf"),i=s.n(e),o=s("C3lA"),n=s("A2Dw"),c=s("Y43X"),l=s("e81K"),r=s("P9l9"),d=s("mtWM"),h=s.n(d),u=s("Au9i"),m=s("flXH"),_=s("CaOM"),v=s("iO08"),p={name:"video",data:function(){return{playerOptions:{playbackRates:[.7,1,1.5,2],autoplay:!0,muted:!1,loop:!1,preload:"auto",language:"zh-CN",aspectRatio:"16:9",fluid:!0,sources:[{type:"",src:this.src}],poster:"",notSupportedMessage:"此视频暂无法播放，请稍后再试",controlBar:{timeDivider:!0,durationDisplay:!0,remainingTimeDisplay:!1,fullscreenToggle:!0}}}},props:{src:{type:String,default:null}},mounted:function(){},methods:{videoClose:function(){this.$emit("videoClose")}}},g={render:function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"m-modal m-video-modal"},[a("div",{staticClass:"m-video-box"},[a("video",{attrs:{src:this.src,controls:"controls",autoplay:"true","x5-playsinline":"true","x5-video-player-type":"h5","x5-video-player-fullscreen":"false"}}),this._v(" "),a("span",{staticClass:"m-close",on:{click:this.videoClose}},[this._v("X")])])])},staticRenderFns:[]};var f,k=s("VU/8")(p,g,!1,function(t){s("kjyc")},"data-v-0eacb010",null).exports,w=s("zfeG"),y=(s("fxnj"),{afterOpen:function(){f=document.scrollingElement.scrollTop||document.body.scrollTop,document.body.classList.add("scroll"),document.body.style.top=-f+"px"},beforeClose:function(){document.body.classList.remove("scroll"),document.scrollingElement.scrollTop=f,document.body.scrollTop=f}}),C={mixins:[m.a],data:function(){return{title:"https://weidianweb.daaiti.cn/#/",course:1,count:5,total_count:0,search:!0,show_course:!1,show_modal:!1,show_task:!1,show_fixed:!1,show_task_btn:!0,show_fen:!1,show_video:!1,show_img:!1,_fixed:null,swipe_items:[{title:"你的名字",href:"http://google.com",url:"http://www.baidu.com/img/bd_logo1.png"},{title:"我的名字",href:"http://baidu.com",url:"http://www.baidu.com/img/bd_logo1.png"}],hot_list:[],hot_index:0,interval:null,activity_list:[],nav_list:[{sub:[],tnid:"c3281b16-ab6b-11e8-97e2-00163e0cc024",tnname:"特卖",tntype:1,tsort:57}],icon_list:[{src:"icon-like",name:"123123",url:"icon-like"},{src:"icon-share",name:"转发",url:"icon-share"}],isScroll:!0,shareParams:{media:[],product:{}},bottom_show:!1,task_list:[],video_src:"",img_src:"",TArole:"",code_src:"",components_src:"",task_reward:null,is_vip:!0}},components:{navbar:o.a,search:n.a,ctx:c.a,share:l.a,attention:v.a,mVideo:k,imgModal:w.a},mounted:function(t){_.a.changeTitle("首页"),_.a.GetQueryString("UPPerd")&&(localStorage.setItem("UPPerd",_.a.GetQueryString("UPPerd")),alert(_.a.GetQueryString("UPPerd")),localStorage.getItem("token")&&this.$router.push("/login")),this.getSwipe(),this.getHot(),this.getTopnav(),"partner"==localStorage.getItem("level")?(this.is_vip=!0,this.getTask()):this.is_vip=!1,localStorage.getItem("is_first")&&(this.show_course=!0);this.interval=window.setInterval(this.animation,3e3),m.a.wxRegister(this.wxRegCallback)},watch:{show_task:function(t,a){t?y.afterOpen():y.beforeClose()}},methods:{touchStart:function(t){},touchMove:function(t){this.show_task_btn=!1,this.search=!0,this.show_fixed=!1;var a=_.a.getScrollTop(),s=_.a.getScrollHeight();a+_.a.getClientHeight()>=s-10&&this.isScroll&&(this.isScroll=!1,this.activity_list.length==this.total_count?this.bottom_show=!0:this.loadBottom())},touchEnd:function(){this.show_task_btn=!0},wxRegCallback:function(){this.wxShare()},wxShare:function(t,a){var s=window.location.href,e={title:"微点"+a.acid,link:s,success:function(){alert("分享成功")},error:function(){alert("分享失败")}};switch(t){case"appmessage":m.a.ShareTimeline(e),this.show_fen=!0;break;case"line":m.a.ShareAppMessage(e),this.show_fen=!0}},share:function(t){this.wxShare(t,this._fixed)},fenClick:function(){this.show_fen=!1},hotClick:function(t){this.changeRoute(t.hmskiptype,t.hmcontent)},changeRoute:function(t,a,s){var e="";if(s){switch(t){case 0:return!1;case 1:e=this.title+"activityContent?openid="+localStorage.getItem("openid")+"&baid="+(s?this.activity_list[a].aclinkvalue:a);break;case 2:e=this.title+"productDetail?openid="+localStorage.getItem("openid")+"&prid="+(s?this.activity_list[a].product.prid:a);break;case 3:e=this.title+"discover/index?openid="+localStorage.getItem("openid")+"&acid="+(s?this.activity_list[a].acid:a)+"&name=赚钱学院";break;case 4:e=this.title+"discover/index/index?openid="+localStorage.getItem("openid")+"&acid="+(s?this.activity_list[a].acid:a)+"&name=公告"}return e}switch(t){case 0:return!1;case 1:this.$router.push({path:"/activityContent",query:{openid:localStorage.getItem("openid"),baid:a}});break;case 2:this.$router.push({path:"/productDetail",query:{openid:localStorage.getItem("openid"),prid:a}});break;case 3:this.$router.push({path:"/discover",query:{openid:localStorage.getItem("openid"),acid:a,name:"赚钱学院"}});break;case 4:this.$router.push({path:"/discover",query:{openid:localStorage.getItem("openid"),acid:a,name:"公告"}})}},getEr:function(t,a){var s,e=this;s=this.changeRoute(t,a,"活动"),h.a.post(r.a.share_qrcode+"?token="+localStorage.getItem("token"),{dataurl:s}).then(function(t){200==t.data.status&&(e.code_src=t.data.qrcodeurl,e.components_src=t.data.components,e.shareParams.product=e.activity_list[a].product,e.shareParams.media=e.activity_list[a].media,e.show_fixed=!0)})},getTask:function(t){var a=this;h.a.get(r.a.get_user_task,{params:{token:localStorage.getItem("token")}}).then(function(t){200==t.data.status?(a.task_list=t.data.data,a.TArole=t.data.TArole,a.task_reward=t.data.RAward,1==localStorage.getItem("is_today_first")&&(a.show_task=!0,window.localStorage.setItem("is_today_first",0)),t.data.is_complate&&(a.img_src=t.data.TAcomplateNotifications,a.show_img=!0)):Object(u.Toast)({message:t.data.message,className:"m-toast-fail"})})},getTopnav:function(){var t=this;h.a.get(r.a.get_home_topnav).then(function(a){if(200==a.data.status){t.nav_list=[].concat(a.data.data);for(var s=0;s<t.nav_list.length;s++)t.nav_list[s].click=!1;t.nav_list[0].click=!0,t.getActivity(t.nav_list[0].tnid)}else Object(u.Toast)({message:a.data.message,className:"m-toast-fail"})})},getSwipe:function(){var t=this;h.a.get(r.a.get_home_banner+"?lasting=true&token="+localStorage.getItem("token")).then(function(a){200==a.data.status?t.swipe_items=a.data.data:Object(u.Toast)({message:a.data.message,className:"m-toast-fail"})})},getHot:function(){var t=this;h.a.get(r.a.get_all_hotmessage,{params:{lasting:!0,token:localStorage.getItem("token")}}).then(function(a){200==a.data.status?t.hot_list=a.data.data:Object(u.Toast)({message:a.data.message,className:"m-toast-fail"})})},getActivity:function(t,a,s){var e=this;h.a.get(r.a.get_all_activity+"?token="+localStorage.getItem("token"),{params:{lasting:!0,start:a||0,count:s||this.count,tnid:t}}).then(function(t){if(200==t.data.status){e.isScroll=!0,e.total_count=t.data.count,e.activity_list=a?e.activity_list.concat(t.data.data):t.data.data;for(var s=[].concat(e.activity_list),i=0;i<s.length;i++){var o=[{src:"icon-like",name:"123123",url:"icon-like"},{src:"icon-share",name:"转发",url:"icon-share"}];o[0].name=s[i].likenum,o[0].alreadylike=s[i].alreadylike,s[i].actext.length>92&&(s[i].show_text=!0),s[i].icon=[].concat(o)}e.activity_list=[].concat(s)}else Object(u.Toast)({message:t.data.message,className:"m-toast-fail"})})},animation:function(t){t=t||1,this.hot_index==this.hot_list.length-1?this.hot_index=0:this.hot_index=this.hot_index+t},changeLike:function(t,a){var s=this.activity_list[a].icon[0];h.a.post(r.a.ac_like+"?token="+localStorage.getItem("token"),{acid:t}).then(function(t){200==t.data.status?s.alreadylike?(s.name-=1,s.alreadylike=!1,Object(u.Toast)({message:t.data.message,duration:800,className:"m-toast-warning"})):s.alreadylike||(s.name=Number(s.name)+1,s.alreadylike=!0,Object(u.Toast)({message:t.data.message,duration:800,className:"m-toast-success"})):Object(u.Toast)({message:t.data.message,className:"m-toast-fail"})})},inputClick:function(){this.search=!1},searchClick:function(t){var a=this;h.a.get(r.a.get_search,{params:{token:localStorage.getItem("token"),PRname:t,page:1,start:0,count:this.count}}).then(function(t){if(200==t.data.status){t.data.data.length<1&&Object(u.Toast)({message:"无匹配内容",className:"m-toast-warning"}),a.activity_list=t.data.data;for(var s=0;s<a.activity_list.length;s++)a.activity_list[s].icon=a.icon_list,a.activity_list[s].icon[0].name=a.activity_list[s].likenum,a.activity_list[s].icon[0].alreadylike=a.activity_list[s].alreadylike,a.activity_list[s].actext.length>92&&(a.activity_list[s].show_text=!0)}else Object(u.Toast)({message:t.data.message,className:"m-toast-fail"})})},closeModal:function(t){this[t]=!1},videoClose:function(){this.show_video=!1},showModal:function(t){this[t]=!0,"show_task"==t&&this.getTask("two")},fixedClick:function(){this.show_fixed=!1},navClick:function(t){for(var a=this.nav_list,s=0;s<a.length;s++)a[s].click=!1;a[t].click=!0,this.nav_list=[].concat(a),this.activity_list=[],this.getActivity(this.nav_list[t].tnid)},iconClick:function(t,a){switch(t){case 0:this.changeLike(this.activity_list[a].acid,a);break;case 1:this.shareDone(a)}},download:function(t){var a=this;this.$copyText(window.location.href).then(function(t){a.show_modal=!0},function(t){})},showMoreText:function(t,a){var s=[].concat(this.activity_list);s[a]=i()({},s[a],{show_text:t}),this.activity_list=[].concat(s)},loadTop:function(){for(var t=0;t<this.nav_list.length;t++)this.nav_list[t].click&&this.getActivity(this.nav_list[t].tnid);this.$refs.loadmore.onTopLoaded()},loadBottom:function(){for(var t=0;t<this.nav_list.length;t++)this.nav_list[t].click&&this.getActivity(this.nav_list[t].tnid,this.activity_list.length)},courseClick:function(){this.course<3?this.course+=1:this.show_course=!1},shareDone:function(t){this.getEr(this.activity_list[t].acskiptype,t)},makeTask:function(t){var a=this;if(0!=this.task_list[t].tatype)return this.show_task=!1,!1;this.video_src=this.task_list[t].taurl,this.show_video=!0,h.a.post(r.a.do_task+"?token="+localStorage.getItem("token"),{TUid:this.task_list[t].tuid}).then(function(t){200==t.data.status&&a.getTask()})},toActivity:function(t){var a=t.baimage;this.$router.push({path:"/activityContent",query:{rbimage:a,baid:t.baid}})}}},b={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"m-index",on:{touchmove:function(a){return a.stopPropagation(),t.touchMove(a)},touchend:function(a){return a.stopPropagation(),t.touchEnd(a)},touchstart:function(a){return a.stopPropagation(),t.touchStart(a)}}},[t.is_vip?s("div",{staticClass:"m-suspend-btn ",class:t.show_task_btn?"":"active",attrs:{id:"m-suspend-btn"},on:{click:function(a){a.stopPropagation(),t.showModal("show_task")}}},[s("span",[t._v("开始转发")])]):t._e(),t._v(" "),s("mt-loadmore",{ref:"loadmore",attrs:{"top-method":t.loadTop,"bottom-all-loaded":!t.isScroll}},[s("div",{staticClass:"m-top"},[s("search",{attrs:{search:t.search},on:{searchClick:t.searchClick,inputClick:t.inputClick}}),t._v(" "),s("navbar",{attrs:{list:t.nav_list},on:{navClick:t.navClick}})],1),t._v(" "),s("mt-swipe",{attrs:{auto:2e3}},t._l(t.swipe_items,function(a){return s("mt-swipe-item",{key:a.baid},[s("a",{attrs:{href:a.href,rel:"external nofollow"}},[s("img",{staticClass:"img",attrs:{src:a.baimage},on:{click:function(s){t.toActivity(a)}}}),t._v(" "),s("span",{staticClass:"desc"})])])})),t._v(" "),s("div",{staticClass:"m-recommend"},[t._l(t.hot_list,function(a,e){return[s("div",{staticClass:"m-recommend-one",class:e==t.hot_index?"active":"",attrs:{keys:a.hmid},on:{click:function(s){t.hotClick(a)}}},[s("span",{staticClass:"m-recommend-span"},[s("span",{staticClass:"m-recommend-label"},[t._v("热文")]),t._v(" "),s("span",[t._v(t._s(a.hmtext))])])])]})],2),t._v(" "),s("div",{staticClass:"m-index-section"},[t._l(t.activity_list,function(a,e){return[s("ctx",{attrs:{icon:t.icon_list,list:a,index:e},on:{iconClick:t.iconClick,showMoreText:t.showMoreText}})]})],2)],1),t._v(" "),t.show_task?s("div",{staticClass:"m-modal",on:{click:function(a){a.stopPropagation(),t.closeModal("show_task")}}},[s("div",{staticClass:"m-modal-state"},[s("div",{staticClass:"m-modal-head"},[s("span",{staticClass:"m-close",on:{click:function(a){a.stopPropagation(),t.closeModal("show_task")}}},[t._v(" x ")])]),t._v(" "),s("div",{staticClass:"m-modal-content"},[s("h3",{staticClass:"m-modal-award-title"},[s("span",[t._v("奖励任务")]),t._v(" "),t.task_reward?s("span",{staticClass:"m-modal-award-info"},[t._v(t._s(t.task_reward.raward))]):t._e()]),t._v(" "),s("div",{staticClass:"m-scroll"},[s("ul",{staticClass:"m-modal-award-ul"},[t._l(t.task_list,function(a,e){return[s("li",[s("div",{staticClass:"m-modal-award-img-box"},[s("img",{staticClass:"m-modal-award-img",attrs:{src:a.tahead,alt:""}}),t._v(" "),s("div",[s("h3",[t._v(t._s(a.taname))]),t._v(" "),s("p",{staticClass:"m-modal-award-complete"},[0==a.tatype?s("span",[t._v("完成 "+t._s(a.tunumber)+"/1")]):s("span",[t._v("完成"+t._s(a.tunumber)+"/"+t._s(a.taurl))]),t._v(" "),a.tamessage?s("span",{staticClass:"m-red"},[t._v(t._s(a.tamessage))]):t._e()])])]),t._v(" "),1==a.tustatus?s("span",{staticClass:"m-modal-award-btn",class:a.tustatus>0?"active":""},[t._v("完 成")]):99==a.talevel?s("span",{staticClass:"m-modal-award-btn"},[t._v("额外奖励")]):s("span",{staticClass:"m-modal-award-btn",on:{click:function(a){a.stopPropagation(),t.makeTask(e)}}},[t._v("做任务")])])]})],2)]),t._v(" "),s("div",{staticClass:"m-modal-award-rule"},[s("h3",[t._v("规则")]),t._v(" "),s("p",{staticClass:"m-modal-award-rule-info"},[t._v("\n           "+t._s(t.TArole)+"\n          ")])])])])]):t._e(),t._v(" "),t.show_fixed?s("attention",{attrs:{src:t.code_src,components_src:t.components_src,shareParams:t.shareParams},on:{closeModal:function(a){t.closeModal("show_fixed")}}}):t._e(),t._v(" "),t.show_course?s("img",{staticClass:"m-course-img",attrs:{src:"/static/images/course/course-"+t.course+".png",alt:""},on:{click:function(a){return a.stopPropagation(),t.courseClick(a)}}}):t._e(),t._v(" "),t.show_video?s("m-video",{attrs:{src:t.video_src},on:{videoClose:t.videoClose}}):t._e(),t._v(" "),t.show_img?s("img-modal",{attrs:{src:t.img_src},on:{closeModal:t.closeModal}}):t._e(),t._v(" "),t.bottom_show?s("div",{staticClass:"bottom-prompt"},[s("div",{staticClass:"bottom-line"}),t._v(" "),s("div",{staticClass:"m-grey-color"},[t._v("我是有底线的")]),t._v(" "),s("div",{staticClass:"bottom-line"})]):t._e()],1)},staticRenderFns:[]};var x=s("VU/8")(C,b,!1,function(t){s("TJJp")},"data-v-7c38e84e",null);a.default=x.exports},TJJp:function(t,a){},kjyc:function(t,a){},m1pt:function(t,a){}});
//# sourceMappingURL=6.6655908aec38d12c8840.js.map