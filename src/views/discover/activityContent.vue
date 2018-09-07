<template>
  <div>
    <img class="activity-img" :src="rbimage">

    <mt-loadmore :top-method="loadTop" ref="loadmore">
      <div class="m-index-section">
        <template v-for="(item,index) in activity_list">
          <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
        </template>
      </div>
    </mt-loadmore>
    <share v-if="show_fixed" @fixedClick="fixedClick"></share>

    <m-footer></m-footer>
  </div>
</template>

<script>
  import mFooter from '../../components/common/footer';
  import ctx from '../index/components/ctx';
  import share from '../../components/common/share';
  import api from '../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';

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
        show_fixed: false,
        tnid: "5ed4e908-a6db-11e8-b2ff-0cd292f93404"
      }
    },
    components: { mFooter, ctx, share },
    methods: {
      /*获取活动列表*/
      getActivity(start, count, tnid){
        let token = localStorage.getItem('token');
        axios.get(api.get_all_activity + '?token=' + token, {
          params: { start: 0, count: 5, tnid: this.tnid }}).then(res => {
          if(res.data.status == 200){
            this.activity_list = res.data.data;
            // console.log(this.activity_list);

            for(let i = 0; i < this.activity_list.length; i ++){
              this.activity_list[i].icon = this.icon_list;
              this.activity_list[i].icon[0].name = this.activity_list[i].likenum;
              this.activity_list[i].icon[0].alreadylike = this.activity_list[i].alreadylike;
              this.activity_list[i].actext.length > 92 && (this.activity_list[i].show_text = true);

              /*if(this.activity_list[i].alreadylike) {
                this.icon_list[0].src = "icon-like-active";
              }*/
            }
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      // 下拉刷新
      loadTop() {
        for(let i=0;i<this.nav_list.length;i++){
          if(this.nav_list[i].click){
            this.getActivity(this.nav_list[i].tnid);
          }
        }
        this.$refs.loadmore.onTopLoaded();
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          case 1:
            this.copyText(list);
            break;
          case 2:
            this.show_fixed = true;
            break;
        }
      },
      // 活动点赞
      changeLike(index) {
        axios.post(api.ac_like + '?token=' + localStorage.getItem('token'), {
          acid: this.activity_list[index].acid
        }).then(res => {
          if(res.data.status == 200){
            if(this.activity_list[index].alreadylike) {
              this.activity_list[index].likenum -= 1;
              this.activity_list[index].alreadylike = false;
              Toast({ message: res.data.message, className: 'm-toast-warning' });

            }else if(!this.activity_list[index].alreadylike) {
              this.activity_list[index].likenum += 1;
              this.activity_list[index].alreadylike = true;
              Toast({ message: res.data.message, className: 'm-toast-success' });
            }
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
        let link = "https://daaiti.cn/WeiDian/#/productDetail?prid=" + this.activity_list[list].prid;
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
