<template>
  <div class="product-params">
    <div class="product-params-show" @click="productParams">
      <span class="product-params-detail">尺寸：{{size}}</span><span class="product-params-detail">颜色：{{color}}</span>
      <img v-if="popupVisible" src="../../../static/images/icon-list-down.png" class="list-right-down">
      <img v-if="!popupVisible" src="../../../static/images/icon-list-right.png" class="list-right-down">
    </div>
    <mt-popup v-model="popupVisible" position="bottom">
      <div class="product-params-content">
        <img src="/static/images/product1.png" class="product-img">
        <div class="product-params-center">
          <p class="product-price">￥<span class="product-price-number">160</span></p>
          <div class="choose-prompt">{{prompt}}</div>
        </div>
        <img src="/static/images/delete.png" class="close-popup" @click="productParams">
      </div>
      <div class="line"></div>
      <div class="product-size-color" v-for="(option, index) in options">
        <p class="product-size-color-text">{{option.name}}</p>
        <span :class="{select: sel[index] == ind}" v-for="(item, ind) in option.items" @click="select(index, ind)">{{item.msg}}</span>
      </div>
      <div class="line"></div>
      <div class="product-quantity">
        <div class="product-quantity-text">购买数量</div>
        <product-quantity :quantity="quantity" class="product-quantity-edit"></product-quantity>
      </div>
      <div class="choose-done" @click="chooseDone">确定</div>
    </mt-popup>
  </div>
</template>

<script>
  import productQuantity from "../../components/common/productQuantity";
  export default {
    data() {
      return {
        name: 'productParams',
        popupVisible: false,
        prompt: "请选择颜色、尺码",
        sel: [],
        colorSizeList: ['', ''],
        options: [ {name: "颜色", items: [{id: 0, msg: "黄色"}, {id: 1, msg: "绿色"}, {id: 2, msg: "红色"}, {id:3, msg: "蓝色"}]},
                  {name: "尺寸", items: [{id: 0, msg: "S"}, {id: 1, msg: "M"}, {id: 2, msg: "L"}, {id: 3, msg: "XL"}, {id: 4, msg: "2XL"}, {id: 5, msg: "3XL"}]} ],
      }
    },
    components: { productQuantity },
    props:{
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
      }
    },
    methods: {
      // 判断选择商品类型的下部弹框是否弹出
      productParams() {
        if(this.popupVisible) {
          this.popupVisible = false;
        }else if(!this.popupVisible) {
          this.popupVisible = true;

          // 从购物车中调用时选中已确定的颜色和尺寸
          for(let i = 0; i < this.options.length; i ++) {
            for(let j = 0; j < this.options[i].items.length; j ++) {
              if(this.color == this.options[i].items[j].msg) {
                this.sel[0] = this.options[i].items[j].id;
                this.colorSizeList[0] = this.color;
              }
              if(this.size == this.options[i].items[j].msg) {
                this.sel[1] = this.options[i].items[j].id;
                this.colorSizeList[1] = this.size;
              }
            }
          }
          this.changePrompt();
        }
      },
      select(index, ind) {
        this.changePrompt();
        this.sel[index] = ind;                  // 让数组sel的第index+1的元素的值等于ind
        this.sel = this.sel.concat([]);         // 因为数组是引用类型，对其中一个变量直接赋值不会影响到另一个变量（并未操作引用的对象），使用concat（操作了应用对象）
        this.colorSizeList[index] = this.options[index].items[ind].msg;         // 获取选中的id
      },
      // 根据选择的商品参数来改变提示信息
      changePrompt() {
        if(this.colorSizeList[0] == "" && this.colorSizeList[1] != "") {
          this.prompt = "请选择 颜色"
        }else if(this.colorSizeList[1] == "" && this.colorSizeList[0] != "") {
          this.prompt = "请选择 尺寸"
        }else if(this.colorSizeList[0] != "" && this.colorSizeList[1] != "") {
          let promptTemp = "";
          for(let i = 0; i < this.colorSizeList.length; i ++) {
            promptTemp = promptTemp + " " + this.colorSizeList[i];
          }
          this.prompt = "已选择 " + promptTemp;
        }
      },
      chooseDone() {
        if(this.colorSizeList[0] != "" && this.colorSizeList[1] != "") {
          console.log(this.colorSizeList);
        }
      }
    },
    created() {
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/_variate";

  .product-params {
    .product-params-show {
      .product-params-detail {
        float: left;
        color: @grey;
        font-size: 22px;
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
          font-size: 20px;
          text-align: left;
          font-weight: bold;
          color: @mainColor;
          .product-price-number {
            font-size: 34px;
          }
        }
        .choose-prompt {
          font-size: 26px;
          text-align: left;
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
        font-size: 30px;
        text-align: left;
      }
      .select {
        color: #ffffff;
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
        font-size: 30px;
        text-align: left;
        margin: 20px 0 40px 40px;
      }
      .product-quantity-edit {
        width: 205px;
        margin-top: 20px;
      }
    }
    .choose-done {
      padding: 30px;
      font-size: 28px;
      color: @bgMainColor;
      letter-spacing: 10px;
      background-color: @mainColor;
    }
  }
</style>
