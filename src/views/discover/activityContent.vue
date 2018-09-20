<template>
  <div @touchmove="touchMove">
    <img class="activity-img" :src="rbimage">

    <mt-loadmore :top-method="loadTop" ref="loadmore">
      <div class="m-index-section">
        <template v-for="(item,index) in activity_list">
          <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
        </template>
      </div>
    </mt-loadmore>

    <!--<share v-if="show_fixed" @fixedClick="fixedClick"></share>-->
    <attention v-if="show_fixed" @closeModal="closeModal('show_fixed')"></attention>

    <!--<m-footer></m-footer>-->
  </div>
</template>

<script>
  import mFooter from '../../components/common/footer';
  import ctx from '../index/components/ctx';
  import share from '../../components/common/share';
  import api from '../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
  import common from '../../common/js/common';
  import attention from '../../components/common/attention';

  export default {
    name: "activityContent",
    data() {
      return {
        rbimage: "",
        activity_list: [],
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
        show_fixed: false,
        tnid: "5ed4e908-a6db-11e8-b2ff-0cd292f93404", // ertiao
        isScroll: true,
        total_count: 0,
        count: 5
      }
    },
    components: { mFooter, ctx, share, attention },
    methods: {
      /*关闭分享的模态框*/
      closeModal(v){
        // console.log(v);
        this[v]  = false;
      },
      touchMove(){
        let scrollTop = common.getScrollTop();
        let scrollHeight = common.getScrollHeight();
        let ClientHeight = common.getClientHeight()
        if (scrollTop + ClientHeight >= scrollHeight -10) {
          if(this.isScroll){
            this.isScroll = false;
            this.loadBottom();
          }else  if(this.activity_list.length == this.total_count){
            this.isScroll = false;
            Toast({ message: '数据已加载完', className: 'm-toast-warning' });
          }
        }
      },
      /*获取活动列表*/
      getActivity(start, count){
        axios.get(api.get_all_activity + '?token=' + localStorage.getItem('token'), {
          params: { start: start || 0, count: count || this.count, tnid: this.tnid }}).then(res => {
          if(res.data.status == 200){
            this.isScroll = true;
            this.total_count = res.data.count;

            if(start){
              this.activity_list = this.activity_list.concat(res.data.data);
              if(this.activity_list.length == this.total_count){
                this.isScroll = false;
              }
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
              // console.log(_arr[0].name, arr[i].likenum)
            }
            this.activity_list = [].concat(arr);
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      // 下拉刷新
      loadTop() {
        this.getActivity();
        this.$refs.loadmore.onTopLoaded();
      },
      // 上拉加载更多
      loadBottom() {
        this.getActivity(this.activity_list.length, this.count);
        this.$refs.loadmore.onBottomLoaded();
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          /*case 1:
            this.copyText(list);
            break;*/
          case 1:
            this.show_fixed = true;
            break;
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
      /*分享按钮点击*/
      fixedClick(){
        this.show_fixed = false;
      },
      // 复制链接
      copyText(list) {
        let link = window.location.href + this.activity_list[list].prid;
        this.$copyText(link).then(function (e) {
          Toast({ message: "复制成功", className: 'm-toast-success' });
        })
      },
      // 展开全文、收齐全文
      showMoreText(bool,v){
        let arr = [].concat(this.activity_list);
        arr[v] = Object.assign({}, arr[v], { show_text: bool });
        this.activity_list = [].concat(arr);
      },
    },
    mounted() {
      this.rbimage = this.$route.query.rbimage;

      this.getActivity();
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .activity-img {
    width: 750px;
    height: 280px;
    margin-bottom: 40px;
  }
</style>
