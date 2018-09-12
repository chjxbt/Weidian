<template>
    <div class="m-collect" @touchmove="touchMove" >
      <template v-for="(item,index) in collect_list">
        <div class="m-collect-one">
          <img :src="item.productinfo.prmainpic" class="m-collect-img" alt="">
          <div class="m-collect-text">
            <div>
              <span class="m-check" :class="item.click?'active':''" @click.stop="checkClick(index)"></span>
              <span class="m-red">{{item.productinfo.prsalestatus}}</span>
            </div>
            <span>已有{{item.forwardnum}}人发圈</span>
          </div>
        </div>
      </template>
      <div class="m-collect-fixed">
        <div class="m-left">
          <span class="m-check" :class="all_check?'active':''" @click="allClick"></span>
          <span>全选</span>
        </div>
        <span class="m-right" @click="deleteClick">删除</span>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../api/api';
  import common from '../../common/js/common';
  import {Toast} from 'mint-ui';
    export default {
        data() {
            return {
                name: '',
              collect_list:[],
              all_check:false,
              page_size:10,
              page_num:1,
              total_count:0,
              isScroll:true
            }
        },
        components: {},
        methods: {
          getCollect(page){
            axios.get(api.get_prlike_productlike,{
              params:{
                token: localStorage.getItem('token'),
                page_num: page || 1,
                page_size:this.page_size || 10
              }
            }).then(res => {
              if(res.data.status == 200){
                for(let i=0;i<res.data.data.length;i++){
                  res.data.data[i].click = false;
                }
                this.total_count = res.data.count;
                if(page){
                  this.collect_list = this.collect_list.concat(res.data.data);
                }else{
                  this.collect_list = [].concat(res.data.data);
                }

              }
            })
          },
          checkClick(i){
            this.collect_list[i].click = ! this.collect_list[i].click;
            this.all_check = this.checkAll();
            console.log(this.all_check)
          },
          checkAll(){
            let all  = true;
            for(let i=0;i<this.collect_list.length;i++){
              if(this.collect_list[i].click == false){
                all = false;
                return all;
              }
            }
            return all;
          },
          allClick(){
            this.all_check = !this.all_check;
            for(let i=0;i<this.collect_list.length;i++){
              this.collect_list[i].click = this.all_check;
            }
          },
          touchMove(){
            let scrollTop = common.getScrollTop();
            let scrollHeight = common.getScrollHeight();
            let ClientHeight = common.getClientHeight()
            if (scrollTop + ClientHeight >= scrollHeight) {
              if(this.isScroll){
                this.isScroll = false;
                this.page_num = this.page_num +1;
                this.getCollect(this.page_num);
              }else  if(this.collect_list.length == this.total_count){
                this.isScroll = false;
                Toast({ message: '数据已加载完', className: 'm-toast-warning' });
              }

            }
          },
          deleteClick(){
            let arr=[];
            for(let i=0;i<this.collect_list.length;i++){
              if(this.collect_list[i].click){
                arr.push(this.collect_list[i].plid);
              }
            }
            axios.post(api.batch_del_productlike+'?token='+localStorage.getItem('token'),{
              plid:arr.join(',')
            }).then(res => {
                if(res.data.status == 200){
                  Toast({ message: res.data.message, className: 'm-toast-success' });
                  this.getCollect();
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-fail' });
                }
            })
          }
        },
        created() {
          this.getCollect();
        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
.m-collect{
  display: flex;
  flex-flow: row;
  align-items: center;
  justify-content: flex-start;
  flex-wrap: wrap;
  padding: 30px 55px;
  .m-collect-one{
    margin-bottom: 20px;
    &:nth-child(odd){
      margin-right: 40px;
    }
    .m-collect-img{
      display: block;
      width: 300px;
      height: 300px;
      box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
      margin-bottom: 20px;
    }
    .m-collect-text{
      font-size: 21px;
      line-height: 28px;
      display: flex;
      flex-flow: row;
      align-items: center;
      justify-content: space-between;
      .m-red{
        color: #f53b52;
      }

    }
  }
  .m-check{
    display: inline-block;
    width: 24px;
    height: 24px;
    vertical-align: text-bottom;
    background: url("/static/images/icon-complain-check.png") no-repeat;
    background-size: 100% 100%;
    &.active{
      background: url("/static/images/icon-complain-check-active.png") no-repeat;
      background-size: 100% 100%;
    }
  }
  .m-collect-fixed{
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 100;
    width: 100%;
    height: 100px;
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 -3px 6px 0 rgba(0, 0, 0, 0.16);
    background-color: #fff;
    .m-check{
      margin: 0 28px 0 55px;
    }
    .m-right{
      margin-right: 55px;
    }
  }
}
</style>
