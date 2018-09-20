<template>
    <div class="m-receiverAddress">
      <div v-if="address_list.length > 0">
        <template v-for="(item,index) in address_list">
          <div class="m-one-address" >
            <span class="m-check-icon" :class="item.uadefault?'active':''"></span>
            <div class="m-address-info">
              <div class="m-address-row m-address-row1 ">
                <span>{{item.uaname}}</span>
                <span>{{item.uaphone}}</span>
              </div>
              <div class="m-address-row">
                <div class="tl m-address">
                  <span class="m-mo" v-if="item.uadefault">[ 默认地址 ]</span>
                  <span>{{item.area.province}}{{item.area.city}}{{item.area.area}}{{item.uatext}}</span>
                </div>
                <span class="m-edit" @click="addressClick($event,item)">编辑</span>
              </div>
            </div>
          </div>
        </template>
      </div>
      <div class="m-no-address" v-else>
        <img src="/static/images/icon-no-address.png" class="m-no-address-img" alt="">
        <p>您还没有收货地址哦</p>
      </div>

      <div class="m-address-btn" @click="addressClick">添加新地址</div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../../api/api';
  import common from '../../../common/js/common';
    export default {
        data() {
            return {
              have_address:true,
              address_list:[],
              area:{
                province:'',
                city:'',
                area:''
              }
            }
        },
        components: {},
      mounted(){
          this.getInfo();
        common.changeTitle('收货地址');
      },
        methods: {
          addressClick(e,v){
            if(v){
              this.$router.push({
                path:'/editAddress',
                query:{
                  UAdefault: v.uadefault,
                  UAname:v.uaname,
                  UAphone:v.uaphone,
                  UAtext:v.uatext,
                  UAid:v.uaid,
                  province:v.area.province,
                  city:v.area.city,
                  area:v.area.area,
                  provinceid:v.area.provinceid,
                  cityid:v.area.cityid,
                  areaid:v.area.areaid
                }
              })
            }else{
              this.$router.push('/editAddress')
            }

          },
          getInfo(){
            axios.get(api.get_address,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
                if(res.data.status == 200){

                  let arr = [];
                  let _arr =[];
                  for(let i=0;i<res.data.data.length;i++){
                    res.data.data[i].area = {
                      province:'',
                      city:'',
                      area:''
                    };
                    if(res.data.data[i].uadefault){
                      arr.push(res.data.data[i])
                    }else{
                      _arr.push(res.data.data[i])
                    }

                  }
                  arr = arr.concat(_arr);
                  for(let i=0;i<arr.length;i++){
                      arr[i].area.province = arr[i].addressinfo[2].name;
                      arr[i].area.area = arr[i].addressinfo[0].name;
                      arr[i].area.city = arr[i].addressinfo[1].name;
                      arr[i].area.provinceid = arr[i].addressinfo[2].provinceid;
                      arr[i].area.areaid = arr[i].addressinfo[0].areaid;
                      arr[i].area.cityid = arr[i].addressinfo[1].cityid;
                  }
                  this.address_list = [].concat(arr);
                }
            })
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../../common/css/index";
  .m-receiverAddress{
    font-size: 28px;
    margin-bottom: 110px;
    .m-one-address{
      .flex-row(flex-start);
      height: 180px;
      border-bottom: 1px solid @borderColor;
      .m-check-icon{
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
      .m-address-info{
        .m-address-row{
          margin-bottom: 10px;
          .flex-row(flex-start);
          &.m-address-row1{
            .flex-row(space-between);
            padding-right: 120px;
            width: 530px;
            span{
              display: block;
            }
          }
          .m-address{
            width: 530px;
            color: @grey;
            .m-mo{
              color: @mainColor;
            }
          }
          .m-edit{
            display: block;
            padding: 0 15px;
            border-left: 1px solid @borderColor;
            text-align: center;
            color: @grey;
          }
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
    .m-no-address{
      height: 890px;
      background-color: #f1f1f1;
      padding-top: 332px;
      text-align: center;
      font-size: 26px;
      color: @grey;
      .m-no-address-img{
        display: inline-block;
        width: 218px;
        height: 123px;
      }
      p{
        margin-top: 20px;
      }
    }
  }
</style>
