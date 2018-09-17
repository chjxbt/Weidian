<template>
    <div class="m-editAddress">
      <div class="m-editAddress-form">
        <div class="m-editAddress-row">
          <span class="m-editAddress-row-name">收货人</span>
          <div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="form.UAname" class="m-editAddress-input" placeholder="输入收货人姓名">
            </div>
             <div class="m-editAddress-input-box">
               <input type="text" v-model="form.UAphone" class="m-editAddress-input" placeholder="输入收货人联系方式">
             </div>
          </div>
        </div>
        <div class="m-editAddress-row">
          <span class="m-editAddress-row-name">收货地址</span>
          <div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="address" @click="pickerSave(true)" class="m-editAddress-input" placeholder="选择省、市、区（县）">
            </div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="form.UAtext" class="m-editAddress-input" placeholder="输入详情街道地址">
            </div>
          </div>
        </div>
      </div>
      <div class="m-editAddress-switch">
        <span>设为默认</span>
        <span class="m-radio" :class="form.UAdefault ? 'active':''" @click="radioChange"></span>
      </div>
      <div class="m-editAddress-switch" v-if="form.UAid" @click="delClick">
        <span class="m-red" >删除收货地址</span>
      </div>

      <div class="m-address-btn" @click="saveClick">保存</div>
      <div class="m-picker-box" v-if="show_picker">
        <span class="m-picker-btn" @click="pickerSave(false)">确定</span>
        <mt-picker :slots="slots"  @change="onValuesChange"></mt-picker>
      </div>

    </div>

</template>

<script type="text/ecmascript-6">
  import { Picker } from 'mint-ui';
  import Vue from 'vue';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast,MessageBox} from 'mint-ui';
  Vue.component(Picker.name, Picker);
    export default {
        data() {
            return {
                radio_select:true,
               form:{
                 UAdefault: false,
                 UAname:'',
                 UAphone:'',
                 UAtext:'',
                 UAid:''
               },
              show_picker:false,
              address:'',
              slots: [
                {
                  flex: 1,
                  values: ['浙江', '上海', '重庆', '四川', '安徽'],
                  className: 'slot1',
                  textAlign: 'right'
                }, {
                  divider: true,
                  content: '-',
                  className: 'slot2'
                }, {
                  flex: 1,
                  values: ['杭州', '湖州', '绍兴', '宁波', '台州'],
                  className: 'slot3',
                  textAlign: 'center'
                }, {
                  divider: true,
                  content: '-',
                  className: 'slot4'
                }, {
                  flex: 1,
                  values: ['杭州', '湖州', '绍兴', '宁波', '台州'],
                  className: 'slot5',
                  textAlign: 'left'
                }
              ]
            }
        },
        components: {},
        methods: {
          radioChange(){
            this.form.UAdefault = !this.form.UAdefault;
          },
          onValuesChange(picker, values) {
              this.address = values;
          },
          pickerSave(v){
            this.show_picker = v;
          },
          saveClick(){
            if(this.form.UAid){
              this.form.UAtext = this.address + this.form.UAtext;
              this.form.UAdefault = Boolean(this.form.UAdefault);
              axios.post(api.update_address +'?token='+localStorage.getItem('token') + '&uaid=' + this.form.UAid,this.form).then(res => {
                  if(res.data.status == 200 ){
                    Toast({ message: '修改成功', className: 'm-toast-success' });
                    this.$router.push('/receiverAddress');
                  }else{
                    Toast({ message: res.data.message, className: 'm-toast-warning' });
                  }
              })
            }else{
              this.form.UAtext = this.address + this.form.UAtext;
              this.form.UAdefault = Boolean(this.form.UAdefault);
              axios.post(api.add_address +'?token='+localStorage.getItem('token'),this.form).then(res => {
                if(res.data.status == 200 ){
                  Toast({ message: '添加成功', className: 'm-toast-success' });
                  this.$router.push('/receiverAddress');
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-warning' });
                }
              })
            }
          },
          delClick(){
            // MessageBox.confirm('确定执行此操作?').then(action => {
            //   if(action == 'confirm'){
                axios.post(api.del_address +'?token='+ localStorage.getItem('token'),{
                  UAid:this.form.UAid
                }).then(res => {
                  if(res.data.status ==200){
                    Toast({ message: '删除成功', className: 'm-toast-success' });
                    this.$router.push('/receiverAddress');
                  }else{
                    Toast({ message: res.data.message, className: 'm-toast-warning' });
                  }
                })
            //   }else{
            //   }
            // })

          }
        },
      mounted(){
          if(this.$route.query){
            this.form = this.$route.query;
          }
      },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
.m-editAddress{
  background-color: #f2f5f7;
  height: 100%;
  width: 100%;
  .m-editAddress-form{
    width: 100%;
    border-top: 20px solid #f2f5f7;
    .m-editAddress-row{
      background-color: #fff;
      display: flex;
      flex-flow: row;
      justify-content: flex-start;
      font-size: 30px;
      border-bottom: 2px solid @borderColor;
      &:last-child{
        border-bottom: none;
      }
      .m-editAddress-row-name{
        width: 190px;
        text-align: center;
        line-height: 85px;
      }
      .m-editAddress-input-box{
        width: 560px;
        border-bottom: 2px solid @borderColor;
        input{
          width: 100%;
          border: none;
          height: 85px;
          line-height: 85px;
          font-size: 30px;
        }
        &:last-child{
          border-bottom: none;
        }
      }
    }
  }
  .m-editAddress-switch{
    .flex-row(space-between);
    height: 80px;
    line-height: 80px;
    font-size: 30px;
    background-color: #fff;
    padding: 0 36px;
    margin: 20px 0;
    .m-radio{
      display: block;
      width: 50px;
      height: 50px;
      background: url("/static/images/icon-radio.png") no-repeat;
      background-size: 100%;
      margin: 30px;
      &.active{
        background: url("/static/images/icon-radio-active.png") no-repeat;
        background-size: 100%;
      }
    }
  }
  .m-address-btn{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    height: 100px;
    line-height: 100px;
    background-color: @mainColor;
    color: #fff;
    font-size: 34px;
  }
  .m-picker-box{
    position: fixed;
    bottom: 0;
    left: 0;
    height: 450px;
    width: 100%;
    background-color: #fff;
    text-align: right;
    .m-picker-btn{
      display: inline-block;
      padding: 10px 20px;
    }
  }
}
</style>
