<template>
  <div class="m-discover-every">
    <div class="m-swipe-box">
      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
            <img :src="item.rbimage" class="img" @click="toProduct(item)">
            <!--<span class="desc"></span>-->
        </mt-swipe-item>
      </mt-swipe>
      <div class="m-scroll">
        <ul class="m-img-list" id="m-img-list">
        </ul>
      </div>
      <div class="m-title">
        <div>
          <img :src="recommend.suuser.suheader" class="m-item-title-img">
          <span>{{recommend.suuser.suname}}</span>
        </div>
        <div class="m-lookinfo-box">
          <span class="m-look-icon"></span>
          <span>{{recommend.reviewnum}}</span>
          <span class="m-smile-icon"></span>
          <span>{{recommend.relikenum}}</span>
        </div>
      </div>
      <div class="line"></div>
    </div>

    <div class="m-index-section">
      <template v-for="item in activity_list">
        <ctx :icon="icon_list" :list="item" @iconClick="iconClick"></ctx>
      </template>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
  import ctx from '../../index/components/ctx';

    export default {
      data() {
        return {
          bannerList: [],
          recommend: { suuser: {} },
          activity_list:[],
          icon_list:[
            {
              src:'icon-like',
              name:'123123',
              url:'icon-like'
            },
            {
              src:'icon-lian',
              name:'复制链接',
              url:'icon-lian'
            },
            {
              src:'icon-share',
              name:'转发',
              url:'icon-share'
            }
          ],
          show_task: false,
          show_fixed: false
        }
      },
      props:{
        tnid:{ type: String, default: null }
      },
      components: { ctx },
      methods: {
        // 获取每日推荐内容
        getData(){
          let token = localStorage.getItem('token');
          axios.get(api.get_info_recommend + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              this.recommend = res.data.data[0];
              this.suuser = this.recommend.suuser;
              // console.log(this.recommend);

              // 往ul中添加li
              for(let i = 0; i < this.recommend.products.length;i++) {
                var elem_li = document.createElement('li'); // 生成一个 li元素
                // 设置元素的内容
                elem_li.innerHTML = "<img src=" + this.recommend.products[i].prmainpic + " class='m-img-list-img'><p><span class='m-price'>￥" + this.recommend.products[i].prprice +
                  "</span><span class='m-red'>赚" + (this.recommend.products[i].prprice - this.recommend.products[i].proldprice).toFixed(2) + "</span></p>";
                document.getElementById('m-img-list').appendChild(elem_li);
              }

            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 获取banner
        getBanner() {
          let token = localStorage.getItem('token');
          axios.get(api.get_all_recommendbanner + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              this.bannerList = res.data.data;
              // console.log(res.data.data);
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        /*获取活动列表*/
        getActivity(start, count, tnid){
          axios.get(api.get_all_activity, {
            params: { start: 0, count: 15, tnid: '5ed4e908-a6db-11e8-b2ff-0cd292f93404' }}).then(res => {
            if(res.data.status == 200){
              this.activity_list = res.data.data;
              console.log(this.activity_list);

              for(let i = 0; i < this.activity_list.length; i ++){
                this.activity_list[i].icon = this.icon_list;
                this.activity_list[i].icon[0].name = this.activity_list[i].likenum;
              }
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 去产品详情页
        toProduct(item) {
          console.log(item);
        },
        /*每个活动icon点击*/
        iconClick(v, list){
          switch (v){
            case 0:
              break;
            case 1:
              this.show_modal = true;
              break;
            case 2:
              this.show_fixed = true;
              break;
          }
        }
      },
      mounted() {
        this.getData();
        this.getBanner();
        this.getActivity();
      }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/discover";
  .img {
    border-radius: 20px;
  }
  /*滚动条样式*/
  ::-webkit-scrollbar {
    height: 0;
  }
</style>
