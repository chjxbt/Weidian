<template>
    <div class="m-bankCard">
      <div class="m-bankCard-box">
        <div class="m-one-card">
          <div class="m-bankCard-name">{{bank_info.bcbankname}}</div>
          <div class="m-bankCard-type">储蓄卡</div>
          <div class="m-bankCard-num">******* ***** ***** ***{{bank_info.bcnumber.substring(bank_info.bcnumber.length-3)}}</div>
          <span class="m-bankCard-cancel" @click="changeBank">修改</span>
        </div>
      </div>
      <div class="m-bank-btn">
        <span>解除绑定</span>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
    export default {
        data() {
            return {
                bank_info:{
                  bcaddress: "",
                  bcbankname: "",
                  bcid: "",
                  bcnumber: "",
                  bcusername: ""
                }
            }
        },
        components: {},
      mounted(){
        this.getInfo();
      },
        methods: {
          getInfo(){
            axios.get(api.get_mybankcard,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                  this.bank_info = res.data.data;
              }
            })
          },
          changeBank(){
            this.$router.push({path:'/addBankCard',query:this.bank_info})
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
.m-bankCard{
  background-color: #f2f5f7;
  height: 100%;
  padding: 0 35px;
  .m-bankCard-box{
    padding: 40px 0;
    .m-one-card{
      width: 680px;
      height: 207px;
      border-radius: 10px;
      padding: 20px 0;
      background-image: linear-gradient(to right, #37df8e, #12cca2);
      box-shadow: 0 5px 13px 0 rgba(66, 66, 66, 0.43);
      color: #fff;
      position: relative;
      div{
        padding: 0 33px;
        text-align: left;
        line-height: 29px;
        &.m-bankCard-name{
          font-size: 26px;
        }
        &.m-bankCard-type{
          font-size: 18px;
          margin: 10px 0;
        }
        &.m-bankCard-num{
          font-size: 30px;
        }
      }
      .m-bankCard-cancel{
        position: absolute;
        right: 26px;
        bottom: 20px;
        border: 1px solid #fff;
        padding: 5px 20px;
      }
    }
  }
  .m-bank-btn{
    margin-top: 30px;
    span{
      display: inline-block;
      width: 640px;
      background-color: #e68b8b;
      color: #fff;
      font-size: 28px;
      border-radius: 6px;
      height: 70px;
      line-height: 70px;
    }
  }
}
</style>
