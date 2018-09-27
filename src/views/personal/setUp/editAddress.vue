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
               <input type="number" v-model="form.UAphone" class="m-editAddress-input" placeholder="输入收货人联系方式">
             </div>
          </div>
        </div>
        <div class="m-editAddress-row">
          <span class="m-editAddress-row-name">收货地址</span>
          <div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="address.province" @click="pickerSave(true,'','province')" class="m-editAddress-input m-s" placeholder="选择省" readonly>
              <span>-</span>
              <input type="text" v-model="address.city" @click="pickerSave(true,'','city')" class="m-editAddress-input m-s" placeholder="选择市" readonly>
              <span>-</span>
              <input type="text" v-model="address.area" @click="pickerSave(true,'','area')" class="m-editAddress-input m-s" placeholder="选择区(县)" readonly>
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
      <picker :slots="slots" :params="params" :show_picker="show_picker" @pickerSave="pickerSave"></picker>

    </div>

</template>

<script type="text/ecmascript-6">
  import { Picker } from 'mint-ui';
  import Vue from 'vue';
  import axios from 'axios';
  import api from '../../../api/api';
  import {Toast,MessageBox} from 'mint-ui';
  import picker from '../../../components/common/picker';
  import common from '../../../common/js/common';
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
          address_id:{
            provinceid:'',
            cityid:'',
            areaid:''
          },
          address:{
            province:'',
            city:'',
            area:''
          },
          address_list:{
              province:[],
            city:[],
            area:[]
          },
          slots: [
            {
              flex: 1,
              values: ['浙江', '上海', '重庆', '四川', '安徽'],
              className: 'slot1',
              textAlign: 'center'
            }
          ],
          params:'province'
        }
      },
      components: {
        picker
      },
      methods: {
        getSlot(id){
          switch (id){
            case 'province':
              // console.log("province", id);
              axios.get(api.get_province).then(res => {
                if(res.data.status == 200){
                  this.address_list[id] = res.data.data;
                  this.slots[0].values = this.dealArr(res.data.data);
                }
              });
              break;
            case 'city':
              // console.log("city", id);
              axios.get(api.get_city,{
                params:{
                  provinceid:this.address_id.provinceid
                }
              }).then(res => {
                if(res.data.status == 200){
                  this.address_list[id] = res.data.data;
                  this.slots[0].values = this.dealArr(res.data.data);
                }
              });
              break;
            case 'area':
              // console.log("area", id);
              axios.get(api.get_area,{
                params:{
                  cityid:this.address_id.cityid
                }
              }).then(res => {
                if(res.data.status == 200){
                  this.address_list[id] = res.data.data;
                  this.slots[0].values = this.dealArr(res.data.data);
                }
              });
              break;
          }

        },
        radioChange(){
          this.form.UAdefault = !this.form.UAdefault;
        },
        pickerSave(v,target,id){

          // 取消按钮
          if(!v) {
            this.show_picker = v;
          }

          if(id == 'province') {
            this.show_picker = v;
          }else if(id == 'city') {
            if(this.address_id.provinceid) {
              this.show_picker = v;
            }else {
              Toast('请依次选择省-市-区/县');
            }
          }else if(id == 'area') {
            if(this.address_id.provinceid  && this.address_id.cityid) {
              this.show_picker = v;
            }else {
              Toast('请依次选择省-市-区/县');
            }
          }

          if(target){
            this.address[id] = target;
            for(let i = 0;i<this.address_list[id].length;i++){
              if(this.address_list[id][i].name == target){
                this.address_id[id + 'id'] = this.address_list[id][i][id +'id'];
              }
            }
          }else if(target == '' && id && this.show_picker){
            this.params = id;
            this.getSlot(id);
          }

        },
        saveClick(){
          this.form.UAdefault = Boolean(this.form.UAdefault);
          this.form.areaid = this.address_id.areaid;

          if(this.form.UAname && this.form.UAphone != '' && this.form.UAtext && this.form.areaid) {
            if(this.form.UAid){
              axios.post(api.update_address +'?token='+localStorage.getItem('token') + '&uaid=' + this.form.UAid,this.form).then(res => {
                if(res.data.status == 200 ){
                  Toast({ message: '修改成功', className: 'm-toast-success' });
                  this.$router.push('/receiverAddress');
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-warning' });
                }
              })
            }else{
              axios.post(api.add_address +'?token='+localStorage.getItem('token'),this.form).then(res => {
                if(res.data.status == 200 ){
                  Toast({ message: '添加成功', className: 'm-toast-success' });
                  this.$router.push('/receiverAddress');
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-warning' });
                }
              })
            }
          }else {
            Toast('请完整填写收货地址');
            console.log(this.form.UAdefault, this.form.UAname, this.form.UAphone != '', this.form.UAtext, this.form.areaid)
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

        },
        dealArr(list){
          let arr = [];
          for(let i=0;i<list.length;i++){
            arr.push(list[i].name);
          }
          return arr;
        }
      },
      mounted(){
          if(this.$route.query){
            this.form.UAdefault = this.$route.query.UAdefault;
            this.form.UAname = this.$route.query.UAname;
            this.form.UAphone = this.$route.query.UAphone;
            this.form.UAtext = this.$route.query.UAtext;
            this.form.UAid = this.$route.query.UAid;
            this.address.province = this.$route.query.province;
            this.address.city = this.$route.query.city;
            this.address.area = this.$route.query.area;
            this.address_id.provinceid = this.$route.query.provinceid;
            this.address_id.cityid = this.$route.query.cityid;
            this.address_id.areaid = this.$route.query.areaid;
          }
          // this.getSlot('province');
        common.changeTitle('编辑地址');
      },
      created() {

      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
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
          font-size: 28px;
          &.m-s{
            width: 28%;
            &::-webkit-input-placeholder {
              /*text-align: center;*/
            }
          }
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

}
</style>
