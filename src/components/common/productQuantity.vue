<template>
  <div class="product-quantity m-ft-24">
    <div class="deduct-add" @click="deductQuantity">-</div>
    <div class="quantity" @click="changeQuantity">{{quantity}}</div>
    <div class="deduct-add" @click="addQuantity">+</div>
  </div>
</template>

<script>
  import { MessageBox } from 'mint-ui';

  export default {
    data() {
      return {
        name: 'productQuantity',
        quantity: 1,
        inputValue: 1
      }
    },
    props:{
      /*quantity:{
        type: Number,
        default: 1
      }*/
    },
    methods: {
      // 产品数量减 1
      deductQuantity() {
        if(this.quantity > 1) {
          this.quantity -= 1;
          console.log("数量", this.quantity);
        }
      },
      changeQuantity() {
        MessageBox({
          $type:'prompt',
          title:'修改购买数量',
          message:' ',
          // showCancelButton: true,
          // cancelButtonText: "我再想想",
          inputPattern:/^[0-9]/,
          inputErrorMessage:'数量必须为数字',
          showInput:true
        }).then(({ value, action }) => {
          if(action == "confirm") {
            console.log(value);
          }
        });
      },
      // 产品数量加 1
      addQuantity() {
        this.quantity += 1;
        console.log("数量", this.quantity);
      }
    },
    created() {
      this.inputValue = this.quantity;
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .product-quantity {
    width: 100%;
    display: flex;
    .deduct-add {
      height: 25px;
      padding: 5px 14px;
      border: 2px solid @grey;
    }
    .quantity {
      height: 25px;
      margin: 0 -2px;
      padding: 5px 25px;
      border: 2px solid @grey;
    }
  }
</style>
