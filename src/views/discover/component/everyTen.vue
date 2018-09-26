<template>
  <div class="m-discover-every" @touchmove="touchMove">
    <div class="m-swipe-box">
      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
          <img :src="item.rbimage" class="img" @click="toActivity(item)">
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
          <span class="m-smile-icon" :class="recommend.alreadylike?'active':''" @click="likeThis(recommend)"></span>
          <span>{{recommend.relikenum}}</span>
        </div>
      </div>
      <div class="line"></div>
    </div>

    <div class="m-index-section">
      <template v-for="(item,index) in activity_list">
        <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
      </template>
    </div>

    <div class="bottom-prompt" v-if="bottom_show">
      <div class="bottom-line"></div>
      <div class="m-grey-color">我是有底线的</div>
      <div class="bottom-line"></div>
    </div>

    <!--<share v-if="show_fixed" @fixedClick="fixedClick"></share>-->
    <attention v-if="show_fixed" @closeModal="closeModal('show_fixed')" :show_fixed="show_fixed" :shareParams="shareParams"></attention>
  </div>
</template>

<script type="text/ecmascript-6">
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
  import ctx from '../../index/components/ctx';
  import share from '../../../components/common/share';
  import common from '../../../common/js/common';
  import attention from '../../../components/common/attention';

  export default {
    data() {
      return {
        bannerList: [],
        recommend: { suuser: {} },
        activity_list:[],
        icon_list:[
          {
            src:'icon-like',
            name:'收藏',
            url:'icon-like'
          },
          /*{
            src:'icon-lian',
            name:'复制链接',
            url:'icon-lian'
          },*/
          {
            src:'icon-share',
            name:'转发',
            url:'icon-share'
          }
        ],
        show_task: false,
        show_fixed: false,
        isScroll: true,
        total_count: 0,
        count: 5,
        bottom_show: false,
        shareParams: {}
      }
    },
    props:{
      tnid:{ type: String, default: null }
    },
    components: { ctx, share, attention },
    methods: {
      touchMove(){
        let scrollTop = common.getScrollTop();
        let scrollHeight = common.getScrollHeight();
        let ClientHeight = common.getClientHeight();
        if (scrollTop + ClientHeight >= scrollHeight -10) {
          if(this.isScroll){
            this.isScroll = false;
            // console.log(this.activity_list.length, this.total_count);
            if(this.activity_list.length == this.total_count || this.activity_list.length > this.total_count){
              this.bottom_show = true;
              // Toast({ message: '数据已加载完', className: 'm-toast-warning' });
            }else{
              this.loadBottom();
            }
          }
        }
      },
      // 获取banner滚动图
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
      // 获取每日推荐内容
      getData(){
        let token = localStorage.getItem('token');
        axios.get(api.get_info_recommend + '?token=' + token).then(res => {
          if(res.data.status == 200) {
            this.recommend = res.data.data[0];
            this.suuser = this.recommend.suuser;
            // this.recommend.products.push(this.recommend.products[0]);

            // 往ul中添加li
            for(let i = 0; i < this.recommend.products.length; i ++) {
              var elem_li = document.createElement('li'); // 生成一个 li元素
              // 设置元素的内容
              elem_li.innerHTML = "<img src=" + this.recommend.products[i].prmainpic + " class='m-img-list-img'><p><span class='m-price'>￥" + this.recommend.products[i].prprice +
                "</span><span class='m-red'>赚" + this.recommend.products[i].prsavemonty + "</span></p>";
              document.getElementById('m-img-list').appendChild(elem_li);
            }
            // 给每个li添加点击事件
            let that = this;
            // let oli = document.getElementsByTagName("li");
            let oli = document.getElementsByClassName("m-img-list-img");
            for(let i = 0; i < oli.length; i ++){
              (function(j){
                oli[j].onclick = function () {
                  that.toProduct(j);
                };
              })(i)
            }
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      /*获取活动列表*/
      getActivity(start, count){
        axios.get(api.get_all_activity + '?token=' + localStorage.getItem('token'), {
          params: { lasting: true, start: start || 0, count: count || this.count, tnid: this.tnid }}).then(res => {
          if(res.data.status == 200){
            this.isScroll = true;
            this.total_count = res.data.count;

            if(start){
              this.activity_list = this.activity_list.concat(res.data.data);
            }else{
              this.activity_list = res.data.data;
            }

            let arr = [].concat(this.activity_list);
            for(let i=0;i<arr.length;i++) {
              let _arr = [
                {
                  src: 'icon-like',
                  name: '123123',
                  url: 'icon-like'
                },
                /*{
                  src: 'icon-lian',
                  name: '复制链接',
                  url: 'icon-lian'
                },*/
                {
                  src: 'icon-share',
                  name: '转发',
                  url: 'icon-share'
                }
              ];
              _arr[0].name = arr[i].likenum;
              _arr[0].alreadylike = arr[i].alreadylike;
              arr[i].actext.length > 92 && (arr[i].show_text = true);
              arr[i].icon = [].concat(_arr);
            }
            this.activity_list = [].concat(arr);
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      // 去活动内容页
      toActivity(activity) {
        let rbimage = activity.rbimage;
        this.$router.push({path: "/activityContent", query: { rbimage }});
      },
      // 去产品详情页
      toProduct(i) {
        let prid = this.recommend.products[i].prid;
        this.$router.push({path: "/productDetail", query: { prid }});
      },
      /*分享按钮点击*/
      fixedClick(){
        this.show_fixed = false;
      },
      /*关闭分享的模态框*/
      closeModal(v){
        // console.log(v);
        this[v]  = false;
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          case 1:
            // this.copyText(list);
            this.shareDone(list);
            break;
          case 2:
            // this.show_fixed = true;
            break;
        }
      },
      // 处理合成图片要的参数
      shareDone(list) {
        this.shareParams.product = this.activity_list[list].product;
        this.shareParams.media = this.activity_list[list].media;

        // console.log(this.shareParams);
        this.show_fixed = true;
      },
      // 每日推荐的点赞
      likeThis(recommend) {
        if(recommend.alreadylike) {
          axios.post(api.re_like + '?token=' +  localStorage.getItem('token'), {
            reid: recommend.reid
          }).then(res => {
            if(res.data.status == 200){
              this.recommend.relikenum -= 1;
              this.recommend.alreadylike = false;
              Toast({ message: res.data.message, className: 'm-toast-warning' });
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        }else if(!recommend.alreadylike) {
          axios.post(api.re_like + '?token=' +  localStorage.getItem('token'), {
            reid: recommend.reid
          }).then(res => {
            if(res.data.status == 200){
              this.recommend.relikenum += 1;
              this.recommend.alreadylike = true;
              Toast({ message: res.data.message, className: 'm-toast-success' });
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        }
      },
      // 活动点赞
      changeLike(index) {
        let arr = this.activity_list[index].icon[0];
        // console.log(arr);
        axios.post(api.ac_like + '?token=' + localStorage.getItem('token'), {
          acid: this.activity_list[index].acid
        }).then(res => {
          if(res.data.status == 200){
            if(arr.alreadylike) {
              arr.name -= 1;
              arr.alreadylike = false;
              Toast({ message: res.data.message, className: 'm-toast-warning' });
            }else if(!arr.alreadylike) {
              arr.name = Number(arr.name) + 1;
              arr.alreadylike = true;
              Toast({ message: res.data.message, className: 'm-toast-success' });
            }
            // console.log(arr);
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        });
      },
      // 展开全文、收齐全文
      showMoreText(bool,v){
        let arr = [].concat(this.activity_list);
        arr[v] = Object.assign({}, arr[v], { show_text: bool });
        this.activity_list = [].concat(arr);
      },
      // 复制链接
      copyText(list) {
        let link = window.location.href + this.activity_list[list].prid;
        this.$copyText(link).then(function (e) {
          // console.log(link);
          Toast({ message: "复制成功", className: 'm-toast-success' });
        })
      },
      // 下拉刷新
      loadTop() {
        this.getActivity();
      },
      // 上拉加载更多
      loadBottom() {
        this.getActivity(this.activity_list.length, this.count);
      },
    },
    mounted() {
      this.getData();
      this.getBanner();
      this.getActivity();
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/discover";
  /*@import "../../../common/css/modal";*/
  .img {
    border-radius: 20px;
  }
  /*滚动条样式*/
  ::-webkit-scrollbar {
    /*margin-right: -40px;*/
    width: 0;
    height: 0;
  }
</style>
