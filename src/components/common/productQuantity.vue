<template>
  <div class="product-quantity">
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
        // quantity: 1,
        inputValue: 1
      }
    },
    props:{
      quantity:{
        type: Number,
        default: 1
      }
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
          inputPattern:/^[0-9]/,    //正则条件
          inputErrorMessage:'数量必须为数字',
          showInput:true
        }).then(({ value, action }) => {
          if(action == "confirm") {
            console.log(value);
          }
        }).catch(MessageBox.noop);
 /*       /!*MessageBox({
          title: '修改购买数量',
          message: ' ',
          showCancelButton: true,
          showInput: true,
          inputType: Number,
          inputValue: this.quantity
        }).then(action => {
          if(action == "confirm") {
            console.log(this.inputValue);
          }
        });*!/

        MessageBox.prompt("修改购买数量", {
          inputValidator: (val) => {
            if(val == null) {
              return true;
            }
            /!*if(val != null) {
              console.log(isNaN(val.value));
              return true;
            }*!/
            // return (isNaN(val.value))
          },inputErrorMessage: '数量必须为数字'
        }).then((val) => {
            console.log(val.value)
          }, () => {
          console.info('cancel')
        })*/

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
  @import "../../common/css/_variate";
  @import "../../common/css/_remint";

  .product-quantity {
    width: 100%;
    display: flex;
    font-size: 24px;
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
