<template>
    <div class="m-bankCard">
      <div class="m-bankCard-box">
        <div class="m-one-card">
          <div class="m-bankCard-name">{{bank_info.bcbankname}}</div>
          <div class="m-bankCard-type">储蓄卡</div>
          <div class="m-bankCard-num">******* ***** ***** ***{{bank_info.bcnumber.substring(bank_info.bcnumber.length-3)}}</div>
          <span class="m-bankCard-cancel" @click="changeModal(true,0)">修改</span>
        </div>
      </div>
      <div class="m-bank-btn">
        <span @click="changeModal(true,1)">解除绑定</span>
      </div>

      <div class="m-modal " v-if="show_modal">
        <div class="m-modal-state m-bank-modal-state">
          <div class="m-modal-head m-bank">
            <p >输入验证码</p>
            <span class="m-close" @click="changeModal(false)"> x </span>
          </div>
          <div class="m-modal-content m-bank-modal">
            <div class="m-bank-tel">
              <span>{{tel}}</span>
              <span class="m-bank-time" v-if="count >0">{{count}}秒</span>
              <span class="m-bank-time" v-else @click="sendCode">重发</span>
            </div>
            <ul class="m-bank-input-box">
              <template v-for="(item,i) in code_box">
                <li>
                  <!--<input type="number" maxlength="1" v-model="code_box[i]">-->
                  <input type="number" v-model="code_box[i]" oninput="if(value.length>1)value=value.slice(0,1)">
                </li>
              </template>
            </ul>
            <div class="m-bank-modal-btn">
              <span @click="updateCard(true)" v-if="isDel">修改银行卡</span>
              <span @click="updateCard(false)" v-else>修改银行卡</span>
            </div>
          </div>

        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                bank_info:{
                  bcaddress: "",
                  bcbankname: "",
                  bcid: "",
                  bcnumber: "",
                  bcusername: ""
                },
              show_modal:false,
              code_box:[
                '','','','','',''
              ],
              count:0,
              isDel:true,
              tel:''
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
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
          sendCode(){
            const TIME_COUNT = 60;
            axios.post(api.get_inforcode +'?token=' + localStorage.getItem('token')).then(res => {
              if(res.data.status == 200){
                Toast({ message: res.data.message, className: 'm-toast-success' });
                this.tel = res.data.usphone;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
                return false;
              }
            });
            if (!this.timer) {
              this.count = TIME_COUNT;
              this.timer = setInterval(() => {
                if (this.count > 0 && this.count <= TIME_COUNT) {
                  this.count--;
                } else {
                  this.show = true;
                  clearInterval(this.timer);
                  this.timer = null;
                }
              }, 1000)
            }
          },
          changeModal(v,s){
            this.show_modal = v;
            if(s === 0 || s===1){
              this.isDel = Boolean(s);
              this.sendCode();
            }
          },
          updateCard(v){
            if(this.code_box.join('').length <6){
              return false;
            }
            axios.post(api.verify_inforcode+'?token=' + localStorage.getItem('token'),{
              ICcode:this.code_box.join('')
            }).then(res => {
              if(res.data.status ==200){
                if(v){
                  axios.post(api.del_bankcard +'?token='+localStorage.getItem('token'),{
                    BCid:this.bank_info.bcid
                  }).then(res => {
                    Toast({ message: res.data.message, className: 'm-toast-success' });
                    this.$router.push({path:'/setUp',query:this.bank_info})
                  })
                }else{
                  this.$router.push({path:'/addBankCard',query:this.bank_info})
                }

              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/modal";
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
.m-bank-tel{
  color: #a4a4a4;
  font-size: 20px;
  margin-top: 40px;
  .m-bank-time{
    display: inline-block;
    width: 90px;
    height: 32px;
    line-height: 32px;
    border: 1px solid #a4a4a4;
    margin-left: 10px;
  }
}
  .m-bank-input-box{
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: space-around;
    margin: 40px 0;
    input{
      display: block;
      width: 66px;
      height: 66px;
      border: 1px solid #a4a4a4;
      box-shadow: 0.8px 0.5px 1px 0 rgba(66, 66, 66, 0.55);
      text-align: center;
      font-size: 30px;
    }

  }
.m-bank-modal-btn{
  span{
    display: inline-block;
    width: 160px;
    height: 46px;
    border: 1px solid #a4a4a4;
    border-radius: 10px;
    line-height: 46px;
  }
}
</style>
