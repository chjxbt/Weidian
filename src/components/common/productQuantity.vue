<template>
  <div class="product-quantity">
    <div class="deduct-add" @click="deductQuantity">-</div>
    <div class="quantity">{{quantity}}</div>
    <div class="deduct-add" @click="addQuantity">+</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'productQuantity',
        quantity: 1
      }
    },
    // props:{
    //   quantity:{
    //     type: Number,
    //     default: 1
    //   }
    // },
    methods: {
      // 产品数量减 1
      deductQuantity() {
        if(this.quantity > 1) {
          this.quantity -= 1;
        }
      },
      // 产品数量加 1
      addQuantity() {
        this.quantity += 1;
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/_variate";

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
