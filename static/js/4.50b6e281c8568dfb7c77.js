webpackJsonp([4],{AMDm:function(t,s,i){"use strict";var e=i("Au9i"),a=(i("mtWM"),i("P9l9"),{data:function(){return{name:"productQuantity",quantitys:this.quantity,inputValue:1}},props:{quantity:{type:Number,default:1},id:{type:String,default:null},item:{type:Number,default:null}},methods:{postQuantity:function(){null!=this.item?this.$emit("changeNum",this.quantitys,this.item):this.$emit("changeNum",this.quantitys)},deductQuantity:function(){this.quantitys>1&&(this.quantitys-=1,this.postQuantity())},changeQuantity:function(){var t=this;Object(e.MessageBox)({$type:"prompt",title:"修改购买数量",message:" ",inputPattern:/^[0-9]/,inputErrorMessage:"数量必须为数字",showInput:!0}).then(function(s){s.value;"confirm"==s.action&&t.postQuantity()})},addQuantity:function(){this.quantitys+=1,this.postQuantity()}},created:function(){this.inputValue=this.quantitys}}),o={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"product-quantity m-ft-24"},[i("div",{staticClass:"deduct-add",on:{click:t.deductQuantity}},[t._v("-")]),t._v(" "),i("div",{staticClass:"quantity",on:{click:t.changeQuantity}},[t._v(t._s(t.quantitys))]),t._v(" "),i("div",{staticClass:"deduct-add",on:{click:t.addQuantity}},[t._v("+")])])},staticRenderFns:[]};var r=i("VU/8")(a,o,!1,function(t){i("hH3G")},null,null);s.a=r.exports},HQIK:function(t,s,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var e=i("aJjY"),a=i("AMDm"),o=i("Au9i"),r=i("mtWM"),c=i.n(r),u=i("P9l9"),n={data:function(){return{name:"",items:[{title:"你的名字",href:"http://baidu.com",url:"http://d6.yihaodianimg.com/N03/M02/1E/8B/CgQCs1Kyi3yABkF6AAEMkxApUWk35400.jpg"},{title:"你的名字",href:"http://baidu.com",url:"http://img006.hc360.cn/m1/M03/91/1F/wKhQb1RRIZuEaFdwAAAAAKhAlYA086.jpg"}],orderList:[{storeName:"衣衣旗舰店",productSend:"已免运费",reduceTitle:"满 300 减 30",reduceNumber:"还差 30 元",toReduce:"去凑单 >",productList:[],failureList:[]}],guessProductList:[{productImg:"/static/images/product1.png",productName:"商品名称商品名称商品名称商品名称商品名称",productPrice:"199"},{productImg:"/static/images/product1.png",productName:"商品名称商品名称商品名称商品名称商品名称",productPrice:"199"}],ifChooseAll:!1,totalPrice:0,order:[],sku:[{key:"颜色",values:[{vid:349,value:"灰色"},{vid:1,value:"绿色"},{vid:2,value:"红色"},{vid:3,value:"蓝色"}]},{key:"尺寸",values:[{vid:0,value:"S"},{vid:1,value:"M"},{vid:261,value:"L"},{vid:3,value:"XL"},{vid:4,value:"2XL"},{vid:5,value:"3XL"}]}]}},components:{productParams:e.a,productQuantity:a.a},mounted:function(){this.getShop()},methods:{postCar:function(t,s,i){var e=this;c.a.post(u.a.update_shoppingcart+"?token="+localStorage.getItem("token"),{pskid:t,num:s,scid:i}).then(function(t){200==t.data.status&&(e.click_add=!1,Toast({message:"已添加到购物车",className:"m-toast-success"}))})},getShop:function(){var t=this;c.a.get(u.a.get_list_shoppingcart+"?token="+localStorage.getItem("token")).then(function(s){if(200==s.data.status){for(var i=[],e=[],a=0;a<s.data.data.cart.length;a++)s.data.data.cart[a].choose=!1,1==s.data.data.cart[a].prstatus?i.push(s.data.data.cart[a]):e.push(s.data.data.cart[a]);t.orderList[0].productList=[].concat(i),t.orderList[0].failureList=[].concat(e),t.orderList[0].storeName=s.data.name,t.orderList[0].productSend=s.data.postfee}})},chooseProduct:function(t){if(t.choose)t.choose=!1,this.totalPrice=0,this.order=[];else if(!t.choose){t.choose=!0;for(var s=0;s<this.orderList.length;s++)for(var i=0;i<this.orderList[s].productList.length;i++)this.orderList[s].productList[i].choose&&(this.order.push(this.orderList[s].productList[i]),this.totalPrice=this.orderList[s].productList[i].current_sku.pskprice*this.orderList[s].productList[i].scnums)}},chooseAll:function(){var t=void 0,s=void 0;if(this.ifChooseAll){this.ifChooseAll=!1,this.totalPrice=0;for(var i=0;i<this.orderList.length;i++)for(var e=0;e<this.orderList[i].productList.length;e++)this.orderList[i].productList[e].choose=!1,this.order=[]}else if(!this.ifChooseAll){this.ifChooseAll=!0;for(var a=0;a<this.orderList.length;a++)for(var o=0;o<this.orderList[a].productList.length;o++)this.orderList[a].productList[o].choose=!0,t=parseFloat(this.orderList[a].productList[o].current_sku.pskprice),s=parseInt(this.orderList[a].productList[o].scnums),this.totalPrice=this.totalPrice+t*s,this.order.push(this.orderList[a].productList[o])}},deleteProduct:function(t){var s=this;Object(o.MessageBox)({title:"提示",message:"确定删除该商品？",showCancelButton:!0}).then(function(i){"confirm"==i&&c.a.post(u.a.delete_shoppingcart+"?token="+localStorage.getItem("token"),{scid:t.scid}).then(function(t){200==t.data.status&&s.getShop()})})},toDetail:function(t){var s=t.prid;this.$router.push({path:"/productDetail",query:{prid:s}})},toOrder:function(){var t=this.order;this.$router.push({path:"/submitOrder",query:{order:t}})},changeNum:function(t,s){this.orderList[0].productList[s].scnums=t,this.postCar(this.orderList[0].productList[s].current_sku.pskid,t)},carChoose:function(t,s,i){this.orderList[0].productList[i].scnums=s,this.orderList[0].productList[i].current_sku=t[0],this.postCar(this.orderList[0].productList[i].current_sku.pskid,s,this.orderList[0].productList[i].scid)}},created:function(){}},l={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticStyle:{"margin-bottom":"115px"}},[t._l(t.orderList,function(s){return i("div",{key:s.id,staticClass:"m-store-order"},[i("div",{staticClass:"m-store-name"},[i("img",{staticClass:"store-img",attrs:{src:"/static/images/store-img.png"}}),t._v(" "),i("div",{staticClass:"store-name m-ft-28 tl"},[t._v(t._s(s.storeName))]),t._v(" "),i("div",{staticClass:"product-send m-ft-28"},[t._v(t._s(s.productSend))])]),t._v(" "),i("div",{staticClass:"m-order-product"},t._l(s.productList,function(s,e){return i("div",{key:s.id,staticClass:"one-product"},[s.choose?i("img",{staticClass:"check-box-img",attrs:{src:"/static/images/check_box_on.png"},on:{click:function(i){t.chooseProduct(s)}}}):t._e(),t._v(" "),s.choose?t._e():i("img",{staticClass:"check-box-img",attrs:{src:"/static/images/check_box_un.png"},on:{click:function(i){t.chooseProduct(s)}}}),t._v(" "),i("img",{staticClass:"product-img",attrs:{src:s.primage},on:{click:function(i){t.toDetail(s)}}}),t._v(" "),i("div",{staticClass:"one-product-three"},[i("div",{staticClass:"product-name m-ft-24 tl m-ft-b",on:{click:function(i){t.toDetail(s)}}},[t._v(t._s(s.prtitle))]),t._v(" "),i("product-params",{attrs:{item:e,selects:s.current_sku.pskproperkey,number:s.current_sku.pskproductnum,price:s.current_sku.pskprice,options:s.sku_value.psvpropervalue,sku:s.sku,quantity:s.scnums},on:{carChoose:t.carChoose}}),t._v(" "),i("product-quantity",{attrs:{item:e,quantity:s.scnums},on:{changeNum:t.changeNum}})],1),t._v(" "),i("div",{staticClass:"one-product-four"},[i("p",{staticClass:"one-product-price m-red m-ft-20 m-ft-b"},[t._v("￥"),i("span",{staticClass:"product-price-number"},[t._v(t._s(s.current_sku.pskprice))])]),t._v(" "),i("div",{staticClass:"product-failure m-ft-24 m-grey"}),t._v(" "),i("img",{staticClass:"delete-product-img",attrs:{src:"/static/images/delete.png"},on:{click:function(i){t.deleteProduct(s)}}})])])})),t._v(" "),i("div",{staticClass:"failure-product"},t._l(s.failureList,function(s){return i("div",{key:s.id,staticClass:"one-product"},[i("img",{staticClass:"check-box-img",attrs:{src:"/static/images/check_box_disabled.png"}}),t._v(" "),i("img",{staticClass:"product-img",attrs:{src:s.primage}}),t._v(" "),i("div",{staticClass:"one-product-three"},[i("div",{staticClass:"product-name m-ft-24 tl m-ft-b"},[t._v(t._s(s.prtitle))]),t._v(" "),i("div",{staticClass:"product-params-text m-ft-26 m-grey tl m-ml-0"},[t._l(s.current_sku.pskproperkey,function(s,e){return[i("span",{staticClass:"product-params-detail  m-grey"},[t._v(t._s(s.key)+":"+t._s(s.value)+" ")])]})],2)]),t._v(" "),i("div",{staticClass:"one-product-four"},[i("p",{staticClass:"one-product-price m-red m-ft-20 m-ft-b"},[t._v("￥"),i("span",{staticClass:"product-price-number"},[t._v(t._s(s.current_sku.pskprice))])]),t._v(" "),i("div",{staticClass:"product-failure m-ft-24 m-grey"},[t._v("失效")]),t._v(" "),i("img",{staticClass:"delete-product-img",attrs:{src:"/static/images/delete.png"}})])])}))])}),t._v(" "),i("div",{staticClass:"pay-price"},[t.ifChooseAll?i("img",{staticClass:"choose-all-img",attrs:{src:"/static/images/check_box_on.png"},on:{click:function(s){t.chooseAll()}}}):t._e(),t._v(" "),t.ifChooseAll?t._e():i("img",{staticClass:"choose-all-img",attrs:{src:"/static/images/check_box_un.png"},on:{click:function(s){t.chooseAll()}}}),t._v(" "),i("div",{staticClass:"choose-all-text m-ft-30",on:{click:function(s){t.chooseAll()}}},[t._v("全 选")]),t._v(" "),i("div",{staticClass:"pay-price-detail tr"},[i("p",{staticClass:"pay-price-text m-ft-30"},[t._v("总 价：\n        "),i("span",{staticClass:"m-ft-20 m-red m-ft-b"},[t._v("￥")]),t._v(" "),i("span",{staticClass:"m-ft-34 m-red"},[t._v(t._s(t.totalPrice))])])]),t._v(" "),i("div",{staticClass:"to-pay m-ft-34 m-bg-main-color",on:{click:t.toOrder}},[t._v("去结算")])])],2)},staticRenderFns:[]};var p=i("VU/8")(n,l,!1,function(t){i("nF2n")},"data-v-31820ff7",null);s.default=p.exports},aJjY:function(t,s,i){"use strict";var e={data:function(){return{name:"productParams",popupVisible:this.choose,prompt:"请选择规格",sel:[],colorSizeList:[],id:"",all_sku:null,surplus_value:null,select_num:this.quantity,option:null,num:null,show_num:!1}},components:{productQuantity:i("AMDm").a},props:{choose:{type:Boolean,default:!1},size:{type:String,default:null},color:{type:String,default:null},quantity:{type:Number,default:1},options:{type:Array,default:[]},selects:{type:Array,default:null},sku:{type:Array,default:null},price:{type:Number,default:null},item:{type:Number,default:null},number:{type:Number,default:null}},watch:{choose:function(t,s){this.popupVisible=t}},mounted:function(){for(var t=this.options,s=0;s<t.length;s++)for(var i=0;i<t[s].values.length;i++)t[s].values[i].active=!0;this.option=[].concat(t),this.number&&(this.num=this.number,this.show_num=!0),this.selects?this.colorSizeList=[].concat(this.selects):this.colorSizeList=new Array(this.option.length);for(var e=this.sku,a=0;a<e.length;a++){for(var o="",r=0;r<e[a].pskproperkey.length;r++)o+=e[a].pskproperkey[r].vid;e[a].id_arr=o}this.surplus_value=[].concat(e),this.all_sku=[].concat(e),this.selects&&this.clickSku(0,this.selects[0].vid,!0)},methods:{closeModal:function(){this.popupVisible=!1,this.$emit("closeModal")},productParams:function(){if(this.popupVisible)this.popupVisible=!1;else if(!this.popupVisible){if(this.popupVisible=!0,this.selects)for(var t=0;t<this.selects.length;t++)for(var s=0;s<this.option[t].values.length;s++)this.option[t].values[s].vid!=this.selects[t].vid||(this.sel[t]=s);this.changePrompt()}},select:function(t,s){this.sel[t]=s,this.sel=this.sel.concat([]),this.colorSizeList[t]=this.option[t].values[s],this.changePrompt(),this.clickSku(t,this.option[t].values[s],!1,this.option[t].kid)},changePrompt:function(){for(var t=0;t<this.colorSizeList.length;t++)if(!this.colorSizeList[t])return this.prompt="请选择 "+this.option[t].key,!1;for(var s="",i=0;i<this.colorSizeList.length;i++)s=s+" "+this.option[i].key+":"+this.colorSizeList[i].value;this.prompt=s},chooseDone:function(){for(var t=0;t<this.colorSizeList.length;t++)if(!this.colorSizeList[t])return!1;this.popupVisible=!1,null!=this.item?this.$emit("carChoose",this.surplus_value,this.select_num,this.item):this.$emit("carChoose",this.surplus_value,this.select_num)},clickSku:function(t,s,i,e){for(var a=[],o="",r=0;r<this.colorSizeList.length;r++)this.colorSizeList[r]&&(o+=this.colorSizeList[r].vid);for(var c=0;c<this.all_sku.length;c++)if(this.all_sku[c].id_arr.length==o.length&&this.all_sku[c].id_arr==o)a.push(this.all_sku[c]);else for(var u=0;u<this.all_sku[c].pskproperkey.length;u++)this.all_sku[c].pskproperkey[u].vid==o&&a.push(this.all_sku[c]);1==a.length&&(this.num=a[0].pskproductnum),console.log(a),this.surplus_value=[].concat(a)},changeNum:function(t,s){this.select_num=t}},created:function(){}},a={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"product-params"},[i("div",{staticClass:"product-params-choose",on:{click:t.productParams}},[t.selects?t._e():i("div",{staticClass:"product-params-text m-ft-26 m-grey tl"},[t._v(t._s(t.prompt))]),t._v(" "),t.selects?i("div",{staticClass:"product-params-text m-ft-26 m-grey tl m-ml-0"},[t._l(t.selects,function(s,e){return[i("span",{staticClass:"product-params-detail  m-grey"},[t._v(" "+t._s(s.key)+":"+t._s(s.value)+" ")])]})],2):t._e(),t._v(" "),i("img",{staticClass:"more-params",attrs:{src:"/static/images/icon-list-right.png"}})]),t._v(" "),i("mt-popup",{attrs:{position:"bottom"},model:{value:t.popupVisible,callback:function(s){t.popupVisible=s},expression:"popupVisible"}},[i("div",{staticClass:"product-params-content"},[i("img",{staticClass:"product-img",attrs:{src:"/static/images/product1.png"}}),t._v(" "),i("div",{staticClass:"product-params-center"},[t.surplus_value&&1==t.surplus_value.length?i("p",{staticClass:"product-price m-ft-20 m-red m-ft-b tl"},[t._v("￥"),i("span",{staticClass:"m-ft-34"},[t._v(t._s(t.surplus_value[0].pskprice))])]):i("p",{staticClass:"product-price m-ft-20 m-red m-ft-b tl"},[t._v("￥"),i("span",{staticClass:"m-ft-34"},[t._v(t._s(t.price))])]),t._v(" "),i("div",{staticClass:"choose-prompt m-ft-26 tl"},[t._v(t._s(t.prompt)+"   库存："+t._s(t.num))])]),t._v(" "),i("img",{staticClass:"close-popup",attrs:{src:"/static/images/delete.png"},on:{click:t.closeModal}})]),t._v(" "),i("div",{staticClass:"line"}),t._v(" "),t._l(t.option,function(s,e){return i("div",{staticClass:"product-size-color"},[i("p",{staticClass:"product-size-color-text m-ft-30 tl"},[t._v(t._s(s.key))]),t._v(" "),t._l(s.values,function(s,a){return[s.active?i("span",{class:{select:t.colorSizeList[e]&&t.colorSizeList[e].vid==s.vid},on:{click:function(s){t.select(e,a)}}},[t._v(t._s(s.value))]):i("span",{staticClass:"m-cancel"},[t._v(t._s(s.value))])]})],2)}),t._v(" "),i("div",{staticClass:"line"}),t._v(" "),i("div",{staticClass:"product-quantity"},[i("div",{staticClass:"product-quantity-text m-ft-30 tl"},[t._v("购买数量")]),t._v(" "),i("product-quantity",{staticClass:"product-quantity-edit",attrs:{quantity:t.quantity},on:{changeNum:t.changeNum}})],1),t._v(" "),t.num?i("div",{staticClass:"choose-done m-ft-28 m-bg-main-color",on:{click:t.chooseDone}},[t._v("确定")]):i("div",{staticClass:"choose-done m-ft-28 m-choose-cancel"},[t._v("确定")])],2)],1)},staticRenderFns:[]};var o=i("VU/8")(e,a,!1,function(t){i("sy9j")},null,null);s.a=o.exports},hH3G:function(t,s){},nF2n:function(t,s){},sy9j:function(t,s){}});
//# sourceMappingURL=4.50b6e281c8568dfb7c77.js.map