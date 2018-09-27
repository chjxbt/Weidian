<template>
    <div class="m-add-bankCard">
        <div class="m-add-bankCard-content">
          <p class="m-bank-alert">
            <span class="m-alert-icon"></span>
            <span>为了不影响提现，请绑定储蓄卡</span>
          </p>
          <ul class="m-add-bankCard-form">
            <li>
              <span class="m-bankCard-label">姓名</span>
              <span class="m-bankCard-input">
                <input type="text" v-model="form.BCusername" placeholder="输入姓名">
              </span>
            </li>
            <li>
              <span class="m-bankCard-label">卡号</span>
              <span class="m-bankCard-input">
                <input type="number" v-model="form.BCnumber" placeholder="输入卡号">
              </span>
            </li>
            <li>
              <span class="m-bankCard-label">银行</span>
              <span class="m-bankCard-select" @click="showPicker(true)">
                <input type="text" v-model="form.BCbankname" placeholder="请选择银行">
                <span class="m-more-icon"></span>
              </span>
            </li>
            <li>
              <span class="m-bankCard-label">开户网点</span>
              <span class="m-bankCard-input">
                <input type="text" v-model="form.BCaddress" placeholder="输入开户网点">
              </span>
            </li>
          </ul>
          <div class="m-bank-list">
            <span class="m-alert"></span>
            <ul>
              <li>农村信用社开户网点查询 可致电 114 查询；</li>
              <li>邮政储蓄开户网点查询 可致电 95580 查询；</li>
                <li>建设银行开户网点查询 可致电 95533 查询；</li>
                <li>中国银行开户网点查询 可致电 95566 查询；</li>
                <li>工商银行开户网点查询 可致电 95588 查询；</li>
                <li>农业银行开户网点查询 可致电 95599 查询。</li>
            </ul>
          </div>
          <div class="m-add-bankCard-btn">
            <span @click="addBankcard">下一步</span></div>
        </div>
      <picker :show_picker="show_picker" :slots="slots" @pickerSave="pickerSave"></picker>
    </div>

</template>

<script type="text/ecmascript-6">
  import { Picker } from 'mint-ui';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast,MessageBox} from 'mint-ui';
  import picker from '../../../components/common/picker';
  import common from '../../../common/js/common';
    export default {
        data() {
            return {
                name: '',
              show_picker:false,
              slots: [
                {
                  flex: 1,
                  values: [],
                  className: 'slot1',
                  textAlign: 'center'
                }
              ],
              form:{
                BCusername:'',
                BCnumber:'',
                BCbankname:'',
                BCaddress:''
              }
            }
        },
        components: {
          picker
        },
      mounted(){
        common.changeTitle('添加银行卡');
          this.getInfo();
          if(this.$route.query.bcid){
            this.getBankInfo();
          }

      },
        methods: {
          addBankcard(){
            // this.$router.push('/result');
            if(this.$route.query.bcid){
              axios.post(api.update_bankcard+'?token='+localStorage.getItem('token') +'&bcid=' +this.$route.query.bcid,this.form).then(res => {
                if(res.data.status == 200 ){
                  Toast({ message: res.data.message, className: 'm-toast-success' });
                  this.$router.push('/bankCard');
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-warning' });
                }
              })
            }else{
              axios.post(api.add_bankcard+'?token='+localStorage.getItem('token'),this.form).then(res => {
                if(res.data.status == 200 ){
                  Toast({ message: res.data.message, className: 'm-toast-success' });
                  this.$router.push('/bankCard');
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-warning' });
                }
              })
            }

          },
          /*获取银行名*/
          getInfo(){
            axios.get(api.get_bank_list,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                 let arr = [];
                 for(let x in res.data.data){
                   arr.push(res.data.data[x])
                 }
               this.slots[0].values = arr;
              }
            })
          },
          getBankInfo(){
            axios.get(api.get_mybankcard,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.form.BCusername = res.data.data.bcusername;
                this.form.BCnumber = res.data.data.bcnumber;
                this.form.BCbankname = res.data.data.bcbankname;
                this.form.BCaddress = res.data.data.bcaddress;
              }
            })
          },
          pickerSave(v,i){
            this.show_picker = v;
            this.form.BCbankname = i;
          },
          showPicker(v){
            this.show_picker = v;
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
@import "../../../common/css/index";
  .m-add-bankCard{
    background-color: #f2f5f7;
    height: 100%;
    width: 100%;
    .m-add-bankCard-content{
      /*padding-top: 20px;*/
      .m-bank-alert{
        height: 64px;
        line-height: 64px;
        text-align: left;
        .m-alert-icon{
          display: inline-block;
          width: 30px;
          height: 30px;
          background: url("/static/images/bank_alert.png") no-repeat;
          background-size: 100%;
          margin-left: 50px;
          vertical-align: text-bottom;
        }
      }
      .m-add-bankCard-form{
        padding-left: 36px;
        background-color: #fff;
        border-bottom: 1px solid @borderColor;
        border-top: 1px solid @borderColor;
        li{
          height: 100px;
          line-height: 100px;
          .flex-row(flex-start);
          border-bottom: 1px solid @borderColor;
          &:last-child{
            border: none;
          }
          .m-bankCard-label{
            display: block;
            width: 170px;
            text-align: left;
            font-size: 30px;
          }
          .m-bankCard-input{
            width: 544px;
            input{
              width: 100%;
              font-size: 30px;
              border: none;
              height: 90px;
            }
          }
          .m-bankCard-select{
            width: 544px;
            display: flex;
            flex-flow: row;
            justify-content: flex-end;
            align-items: center;
            color: @grey;
            font-size: 30px;
            .m-more-icon{
              display: inline-block;
              width: 16px;
              height: 31px;
              margin: 0 34px;
              background: url("/static/images/icon-more.png") no-repeat;
              background-size: 100%;
              vertical-align: middle;
            }
            input{
              display: inline-block;
              width: 480px;
              font-size: 30px;
              border: none;
              height: 90px;
              text-align: right;
              &::-webkit-input-placeholder {
                 text-align: right;
               }
            }
          }
        }
      }
      .m-bank-list{
        display: flex;
        flex-flow: row;
        justify-content: flex-start;
        color: #a4a4a4;
        padding-left: 36px;
        padding-top: 20px;
        .m-alert{
          display: block;
          width: 25px;
          height: 25px;
          background: url("/static/images/m-alert.png") no-repeat center;
          background-size: 100% 100%;
          margin: 5px ;
        }
        ul{
          li{
            line-height: 35px;
            font-size: 22px;
          }
        }
      }
      .m-add-bankCard-btn{
        text-align: center;
        span{
          display: inline-block;
          width: 706px;
          height: 97px;
          line-height: 97px;
          font-size: 36px;
          color: #fff;
          background-color: @mainColor;
          border-radius: 10px;
          margin-top: 300px;
        }
      }
    }
  }
</style>
