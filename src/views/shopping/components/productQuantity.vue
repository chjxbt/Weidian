<template>
  <div class="product-quantity m-ft-24">
    <div class="deduct-add" @click="deductQuantity">-</div>
    <div class="quantity" @click="changeQuantity">{{quantitys}}</div>
    <div class="deduct-add" @click="addQuantity">+</div>
  </div>
</template>

<script>
  import { MessageBox } from 'mint-ui';
  import axios from 'axios';
  import api from '../../../api/api'
  export default {
    data() {
      return {
        name: 'productQuantity',
        quantitys: this.quantity,
        inputValue: 1
      }
    },
    props:{
      quantity:{
        type: Number,
        default: 1
      },
      id:{
        type:String,
        default:null
      }
    },
    methods: {
      //修改购物车
      changeQuantity(){
        axios.post(api.update_shoppingcart + '?token=' + localStorage.getItem('token'),{
          pskid:this.id,
          changenum:this.quantitys
        }).then(res => {

        })
      },
      // 产品数量减 1
      deductQuantity() {
        if(this.quantitys > 1) {
          this.quantitys -= 1;
          this.changeQuantity();
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
            this.changeQuantity();
          }
        });
      },
      // 产品数量加 1
      addQuantity() {
        this.quantitys += 1;
        this.changeQuantity();
      }
    },
    created() {
      this.inputValue = this.quantitys;
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";

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
