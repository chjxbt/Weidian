webpackJsonp([15],{EEGG:function(t,e){},mbxE:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={render:function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("img",{staticClass:"m-ok-img",attrs:{src:"/static/images/order_pay_OK.png"}}),t._v(" "),r("p",{staticClass:"m-ft-40 m-black m-ft-b"},[t._v("订单支付成功")]),t._v(" "),t._m(0),t._v(" "),r("p",{staticClass:"order-text m-ft-30 m-grey"},[t._v("仓库正为您备货中")]),t._v(" "),r("div",{staticClass:"m-btn"},[r("div",{staticClass:"m-btn-text m-ft-28 m-grey-color",on:{click:t.orderDetail}},[t._v("查看订单")]),t._v(" "),r("div",{staticClass:"m-btn-text m-ft-28 m-grey-color",on:{click:t.returnHome}},[t._v("返回首页")])])])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("p",{staticClass:"price-text m-black m-ft-b"},[this._v("￥"),e("span",{staticClass:"m-ft-34"},[this._v("159.00")])])}]};var a=r("VU/8")({data:function(){return{name:"orderPayOK",order:{}}},methods:{orderDetail:function(){var t=this.order;this.$router.push({path:"/orderStatus",query:{order:t}})},returnHome:function(){this.$router.push("/index")}},created:function(){this.order=this.$route.query.order}},s,!1,function(t){r("EEGG")},"data-v-a4401030",null);e.default=a.exports}});
//# sourceMappingURL=15.9a8012e0c07330ef6775.js.map