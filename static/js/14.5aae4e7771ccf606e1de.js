webpackJsonp([14],{"/GXu":function(t,i,a){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var e=a("woOf"),o=a.n(e),s=a("SKcX"),c=a("Y43X"),n=a("e81K"),r=a("P9l9"),l=a("mtWM"),d=a.n(l),h=a("Au9i"),m=a("CaOM"),u=a("iO08"),g={name:"activityContent",data:function(){return{baid:"",banner:"",activity_list:[],icon_list:[{src:"icon-like",name:"收藏",url:"icon-like"},{src:"icon-share",name:"转发",url:"icon-share"}],show_fixed:!1,tnid:"5ed4e908-a6db-11e8-b2ff-0cd292f93404",isScroll:!0,total_count:0,count:5,bottom_show:!1,code_src:"",components_src:"",shareParams:{media:[],product:{}},bigImg:"",show_big_img:!1}},components:{mFooter:s.a,ctx:c.a,share:n.a,attention:u.a},methods:{closeModal:function(t){this[t]=!1},touchMove:function(){var t=m.a.getScrollTop(),i=m.a.getScrollHeight();t+m.a.getClientHeight()>=i-10&&this.isScroll&&(this.isScroll=!1,this.activity_list.length==this.total_count?this.bottom_show=!0:this.loadBottom())},getActivity:function(t,i){var a=this;d.a.get(r.a.get_bigactivity+"?token="+localStorage.getItem("token"),{params:{page_num:t||1,page_size:i||this.count,baid:this.baid}}).then(function(i){if(200==i.data.status){a.isScroll=!0,a.total_count=i.data.data.total_count,a.banner=i.data.data.banner,t?(a.activity_list=a.activity_list.concat(i.data.data.activity),a.activity_list.length==a.total_count&&(a.isScroll=!1)):a.activity_list=i.data.data.activity;for(var e=[].concat(a.activity_list),o=0;o<e.length;o++){var s=[{src:"icon-like",name:"123123",url:"icon-like"},{src:"icon-share",name:"转发",url:"icon-share"}];s[0].name=e[o].likenum,s[0].alreadylike=e[o].alreadylike,e[o].actext.length>92&&(e[o].show_text=!0),e[o].icon=[].concat(s)}a.activity_list=[].concat(e)}else Object(h.Toast)({message:i.data.message,className:"m-toast-fail"})})},loadTop:function(){this.getActivity(),this.$refs.loadmore.onTopLoaded()},loadBottom:function(){this.getActivity(this.activity_list.length,this.count)},iconClick:function(t,i){switch(t){case 0:this.changeLike(i);break;case 1:this.show_fixed=!0}},shareDone:function(t){this.getEr(this.activity_list[t].acskiptype,t)},changeRoute:function(t,i,a){var e="";if(a){switch(t){case 0:return!1;case 1:e=this.title+"activityContent?openid="+localStorage.getItem("openid")+"&baid="+(a?this.activity_list[i].baid:i);break;case 3:e=this.title+"productDetail?openid="+localStorage.getItem("openid")+"&prid="+(a?this.activity_list[i].prid:i);break;case 2:e=this.title+"discover/index?openid="+localStorage.getItem("openid")+"&acid="+(a?this.activity_list[i].acid:i)+"&name=赚钱学院";break;case 4:e=this.title+"discover/index/index?openid="+localStorage.getItem("openid")+"&acid="+(a?this.activity_list[i].acid:i)+"&name=公告"}return e}switch(t){case 0:return!1;case 1:this.$router.push({path:"/activityContent",query:{openid:localStorage.getItem("openid"),baid:i}});break;case 2:this.$router.push({path:"/productDetail",query:{openid:localStorage.getItem("openid"),prid:i}});break;case 3:this.$router.push({path:"/discover",query:{openid:localStorage.getItem("openid"),acid:i,name:"赚钱学院"}});break;case 4:this.$router.push({path:"/discover",query:{openid:localStorage.getItem("openid"),acid:i,name:"公告"}})}},getEr:function(t,i){var a,e=this;a=this.changeRoute(t,i,"活动"),d.a.post(r.a.share_qrcode+"?token="+localStorage.getItem("token"),{dataurl:a}).then(function(t){200==t.data.status&&(e.code_src=t.data.qrcodeurl,e.components_src=t.data.components,e.shareParams.product=e.activity_list[i].product,e.shareParams.media=e.activity_list[i].media,e.show_fixed=!0)})},changeLike:function(t){var i=this.activity_list[t].icon[0];d.a.post(r.a.ac_like+"?token="+localStorage.getItem("token"),{acid:this.activity_list[t].acid}).then(function(t){200==t.data.status?i.alreadylike?(i.name-=1,i.alreadylike=!1,Object(h.Toast)({message:t.data.message,className:"m-toast-warning"})):i.alreadylike||(i.name=Number(i.name)+1,i.alreadylike=!0,Object(h.Toast)({message:t.data.message,className:"m-toast-success"})):Object(h.Toast)({message:t.data.message,className:"m-toast-fail"})})},showMoreText:function(t,i){var a=[].concat(this.activity_list);a[i]=o()({},a[i],{show_text:t}),this.activity_list=[].concat(a)}},mounted:function(){this.baid=this.$route.query.baid,this.getActivity(),this.$route.query.baimage&&(this.bigImg=this.$route.query.baimage)}},v={render:function(){var t=this,i=t.$createElement,a=t._self._c||i;return a("div",{on:{touchmove:t.touchMove}},[t.show_big_img?a("div",{staticClass:"m-big-img"},[a("img",{staticClass:"activity-img",attrs:{src:t.bigImg}})]):a("div",[a("img",{staticClass:"activity-img",attrs:{src:t.banner}}),t._v(" "),a("mt-loadmore",{ref:"loadmore",attrs:{"top-method":t.loadTop}},[a("div",{staticClass:"m-index-section"},[t._l(t.activity_list,function(i,e){return[a("ctx",{attrs:{icon:t.icon_list,list:i,index:e},on:{iconClick:t.iconClick,showMoreText:t.showMoreText}})]})],2)]),t._v(" "),t.show_fixed?a("attention",{on:{closeModal:function(i){t.closeModal("show_fixed")}}}):t._e(),t._v(" "),t.bottom_show?a("div",{staticClass:"bottom-prompt"},[a("div",{staticClass:"bottom-line"}),t._v(" "),a("div",{staticClass:"m-grey-color"},[t._v("我是有底线的")]),t._v(" "),a("div",{staticClass:"bottom-line"})]):t._e()],1)])},staticRenderFns:[]};var _=a("VU/8")(g,v,!1,function(t){a("L4oC")},"data-v-fbc28eb4",null);i.default=_.exports},L4oC:function(t,i){}});
//# sourceMappingURL=14.5aae4e7771ccf606e1de.js.map