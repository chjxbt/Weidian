webpackJsonp([14],{AapP:function(t,s){},u9if:function(t,s,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var e={data:function(){return{slider_index:1,slider_list:[{src:"",url:"",name:1},{src:"",url:"",name:2},{src:"",url:"",name:3},{src:"",url:"",name:4}],startX:0,endX:0,interval:""}},components:{},mounted:function(){this.interval=window.setInterval(this.animation,3e3)},methods:{animation:function(t){t=t||1,this.slider_index==this.slider_list.length-1?this.slider_index=0:0==this.slider_index&&-1==t?this.slider_index=this.slider_list.length-1:this.slider_index=this.slider_index+t},touchStart:function(t){(t=t||event).preventDefault(),1==t.touches.length&&(this.startX=t.touches[0].clientX);window.clearInterval(this.interval)},touchEnd:function(t){(t=t||event).preventDefault(),1==t.changedTouches.length&&(this.endX=t.changedTouches[0].clientX),this.endX<this.startX?this.animation(1):this.animation(-1);this.interval=window.setInterval(this.animation,3e3)}},created:function(){}},n={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"m-poster"},[i("span",{staticClass:"m-poster-close"},[t._v("X")]),t._v(" "),i("h3",[t._v("选择海报")]),t._v(" "),i("div",{staticClass:"m-slider-box"},[i("ul",{staticStyle:{"margin-left":"0px"},attrs:{id:"m-slider-ul"},on:{touchstart:t.touchStart,touchend:t.touchEnd}},[t._l(t.slider_list,function(s,e){return[i("li",{class:e==t.slider_index-1||0==t.slider_index&&e==t.slider_list.length-1?"m-slider-left m-slider-side":e==t.slider_index?"m-slider-in":e==t.slider_index+1||t.slider_list.length-1==t.slider_index&&0==e?"m-slider-right m-slider-side":""},[i("img",{staticClass:"m-slider-img",attrs:{src:"",alt:""}}),t._v(" "),t._m(0,!0)])]})],2),t._v(" "),i("span",{staticClass:"m-slider-index"},[t._v(t._s(t.slider_index+1)+"/"+t._s(t.slider_list.length))])]),t._v(" "),t._m(1)])},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"m-poster-content"},[s("div",{staticClass:"m-headPortrait-name"},[s("span",{staticClass:"m-head-name"},[this._v("xxccccx")]),this._v(" "),s("img",{staticClass:"m-head-portrait",attrs:{src:""}})]),this._v(" "),s("div",{staticClass:"m-poster-bottom"},[s("div",{staticClass:"m-poster-code"},[s("span",{staticClass:"m-code"},[this._v("邀请码: 872420")]),this._v(" "),s("img",{staticClass:"m-poster-logo",attrs:{src:"",alt:""}})]),this._v(" "),s("img",{staticClass:"m-poster-er",attrs:{src:"",alt:""}})])])},function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"m-poster-btn"},[s("div",{staticClass:"m-btn"},[s("span",{staticClass:"m-poster-btn-icon"}),this._v(" "),s("p",[this._v("保存图片")])])])}]};var a=i("VU/8")(e,n,!1,function(t){i("AapP")},null,null);s.default=a.exports}});
//# sourceMappingURL=14.36f07f624bfedcc70ef2.js.map