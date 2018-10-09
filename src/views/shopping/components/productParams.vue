<template>
  <div class="product-params">

    <div  class="product-params-choose" @click="productParams">
      <div class="product-params-text m-ft-26 m-grey tl" v-if="!selects">{{prompt}}</div>
      <div class="product-params-text m-ft-26 m-grey tl m-ml-0" v-if="selects">
        <template v-for="(item,index) in selects">
          <span class="product-params-detail  m-grey"> {{item.key}}:{{item.value}} </span>
        </template>
      </div>
      <img src="/static/images/icon-list-right.png" class="more-params">
    </div>

    <!--<div v-if="choose" class="product-params-show" @click="productParams">-->
      <!--<span class="product-params-detail m-ft-22 m-grey">尺寸：{{size}}</span><span class="product-params-detail">颜色：{{color}}</span>-->
      <!--<img v-if="popupVisible" src="/static/images/icon-list-down.png" class="list-right-down">-->
      <!--<img v-if="!popupVisible" src="/static/images/icon-list-right.png" class="list-right-down">-->
    <!--</div>-->

    <mt-popup v-model="popupVisible" position="bottom">
      <div class="product-params-content">
        <img src="/static/images/product1.png" class="product-img">
        <div class="product-params-center">
          <p class="product-price m-ft-20 m-red m-ft-b tl">￥<span class="m-ft-34">160</span></p>
          <div class="choose-prompt m-ft-26 tl">{{prompt}}</div>
        </div>
        <img src="/static/images/delete.png" class="close-popup" @click="productParams">
      </div>
      <div class="line"></div>
      <div class="product-size-color" v-for="(option, index) in options">
        <p class="product-size-color-text m-ft-30 tl">{{option.key}}</p>
        <span :class="{select: sel[index] == ind}" v-for="(item, ind) in option.values" @click="select(index, ind)">{{item.value}}</span>
      </div>
      <div class="line"></div>
      <div class="product-quantity">
        <div class="product-quantity-text m-ft-30 tl">购买数量</div>
        <product-quantity :quantity="quantity" class="product-quantity-edit" :id="id"></product-quantity>
      </div>
      <div class="choose-done m-ft-28 m-bg-main-color" @click="chooseDone">确定</div>
    </mt-popup>
  </div>
</template>

<script>
  import productQuantity from "../components/productQuantity";
  export default {
    data() {
      return {
        name: 'productParams',
        popupVisible: false,
        prompt: "请选择规格",
        sel: [],
        colorSizeList: new Array(this.options.length),
        // options: [ {name: "颜色", items: [{id: 0, msg: "黄色"}, {id: 1, msg: "绿色"}, {id: 2, msg: "红色"}, {id:3, msg: "蓝色"}]},
        //   {name: "尺寸", items: [{id: 0, msg: "S"}, {id: 1, msg: "M"}, {id: 2, msg: "L"}, {id: 3, msg: "XL"}, {id: 4, msg: "2XL"}, {id: 5, msg: "3XL"}]} ],
       id: ''
      }
    },
    components: { productQuantity },
    props:{
      choose:{
        type: Boolean,
        default: false
      },
      size:{
        type: String,
        default: null
      },
      color:{
        type: String,
        default: null
      },
      quantity:{
        type: Number,
        default: 1
      },
      options:{
        type:Array,
        default:[]
      },
      selects:{
        type:Array,
        default:null
      }
    },
    mounted(){
      // this.colorSizeList=new Array(this.options.length);
    },
    methods: {
      // 判断选择商品类型的下部弹框是否弹出
      productParams() {
        if(this.popupVisible) {
          this.popupVisible = false;
        }else if(!this.popupVisible) {
          this.popupVisible = true;

          // 从购物车中调用时选中已确定的颜色和尺寸
          // for(let i = 0; i < this.options.length; i ++) {
          //   for(let j = 0; j < this.options[i].values.length; j ++) {
          //     if(this.color == this.options[i].values[j].value) {
          //       this.sel[0] = this.options[i].values[j].id;
          //       this.colorSizeList[0] = this.color;
          //     }
          //     if(this.size == this.options[i].values[j].value) {
          //       this.sel[1] = this.options[i].values[j].id;
          //       this.colorSizeList[1] = this.size;
          //     }
          //   }
          // }
          this.changePrompt();
        }
      },
      select(index, ind) {
        this.sel[index] = ind;                  // 让数组sel的第index+1的元素的值等于ind
        this.sel = this.sel.concat([]);         // 因为数组是引用类型，对其中一个变量直接赋值不会影响到另一个变量（并未操作引用的对象），使用concat（操作了应用对象）
        this.colorSizeList[index] = this.options[index].values[ind].value;         // 获取选中的id
        this.changePrompt();
      },
      // 根据选择的商品参数来改变提示信息
      changePrompt() {
        for(let i=0;i<this.colorSizeList.length;i++){
          if(!this.colorSizeList[i]){
            this.prompt = "请选择 " + this.options[i].key;
            return false;
          }
        }
        let promptTemp = "";
        for(let i = 0; i < this.colorSizeList.length; i ++) {
          promptTemp = promptTemp + " " + this.options[i].key+':'+ this.colorSizeList[i];
        }
        this.prompt = promptTemp;

        // if(this.colorSizeList[0] == "" && this.colorSizeList[1] != "") {
        //   this.prompt = "请选择 颜色"
        // }else if(this.colorSizeList[1] == "" && this.colorSizeList[0] != "") {
        //   this.prompt = "请选择 尺寸"
        // }else if(this.colorSizeList[0] != "" && this.colorSizeList[1] != "") {
        //   let promptTemp = "";
        //   for(let i = 0; i < this.colorSizeList.length; i ++) {
        //     promptTemp = promptTemp + " " + this.colorSizeList[i];
        //   }
        //   this.prompt = "已选择 " + promptTemp;
        // }
      },
      chooseDone() {
        console.log(this.colorSizeList)
        for(let i=0;i<this.colorSizeList.length;i++){
          if(!this.colorSizeList[i] ){
            return false;
          }
        }
        this.popupVisible = false;
      }
    },
    created() {
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";

  .product-params {
    .product-params-choose {
      width: 100%;
      display: flex;
      .product-params-text {
        flex: 1;
        margin: 15px 0 25px 35px;
        &.m-ml-0{
          margin: 15px 0;
        }
      }
      .more-params {
        width: 22px;
        height: 22px;
        margin: 22px 25px;
      }
    }
    .product-params-show {
      .product-params-detail {
        float: left;
        margin: 8px 20px 10px 0;
      }
      .list-right-down {
        width: 22px;
        height: 22px;
        margin-top: 14px;
        margin-left: -60px;
      }
    }
    .product-params-content {
      width: 750px;
      height: 160px;
      display: flex;
      .product-img {
        width: 220px;
        height: 220px;
        margin: -90px 0 0 40px;
      }
      .product-params-center {
        flex: 1;
        margin: 15px 0 0 35px;
        .product-price {
          margin: 20px 0;
        }
      }
      .close-popup {
        width: 34px;
        height: 34px;
        margin: 22px 22px;
      }
    }
    .product-size-color {
      height: 150px;
      .product-size-color-text {
        padding-left: 40px;
        margin-bottom: 20px;
      }
      .select {
        color: @bgMainColor;
        background-color: @mainColor;
      }
      span {
        display: inline-block;
        width: 90px;
        float: left;
        padding: 8px 0;
        font-size: 26px;
        border-radius: 10px;
        margin: 0 -20px 0 40px;
        background-color: #f4f3f9;
      }
    }
    .line {
      height: 2px;
      width: 696px;
      margin: 0 30px 20px 40px;
      background-color: @grey;
    }
    .product-quantity {
      .product-quantity-text {
        width: 535px;
        margin: 20px 0 40px 40px;
      }
      .product-quantity-edit {
        width: 205px;
        margin-top: 20px;
      }
    }
    .choose-done {
      padding: 30px;
      letter-spacing: 10px;
      background-color: @mainColor;
    }
  }
</style>
