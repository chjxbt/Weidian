<template>
  <div @touchmove="touchMove">
    <div v-if="!show_big_img">
      <img class="activity-img" :src="banner">

      <mt-loadmore :top-method="loadTop" ref="loadmore">
        <div class="m-index-section">
          <template v-for="(item,index) in activity_list">
            <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
          </template>
        </div>
      </mt-loadmore>

      <!--<share v-if="show_fixed" @fixedClick="fixedClick"></share>-->
      <attention v-if="show_fixed" @closeModal="closeModal('show_fixed')"></attention>
      <div class="bottom-prompt" v-if="bottom_show">
        <div class="bottom-line"></div>
        <div class="m-grey-color">我是有底线的</div>
        <div class="bottom-line"></div>
      </div>
    </div>
    <div class="m-big-img" v-else>
      <img class="activity-img " :src="bigImg">
    </div>
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
        baid: "",
        banner:'',
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
        count: 5,
        bottom_show:false,
        code_src:'',
        components_src:'',
        shareParams: {
          media:[],
          product:{}
        },
        bigImg:'',
        show_big_img:false
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
        let ClientHeight = common.getClientHeight();
        if (scrollTop + ClientHeight  >= scrollHeight -10) {
          if(this.isScroll){
            this.isScroll = false;
            if(this.activity_list.length == this.total_count){
              this.bottom_show = true;
            }else{
              this.loadBottom();
            }
          }

        }
      },
      /*获取活动列表*/
      getActivity(start, count){
        axios.get(api.get_bigactivity + '?token=' + localStorage.getItem('token'), {
          params: { page_num: start || 1, page_size: count || this.count, baid: this.baid }}).then(res => {
          if(res.data.status == 200){
            this.isScroll = true;
            this.total_count = res.data.data.total_count;
            this.banner = res.data.data.banner;
            if(res.data.data.batype ==1 ){
              if(start){
                this.activity_list = this.activity_list.concat(res.data.data.activity);
                if(this.activity_list.length == this.total_count){
                  this.isScroll = false;
                }
              }else{
                this.activity_list = res.data.data.activity;
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
              this.show_big_img = false;
            }else{
              this.show_big_img = true;
              this.bigImg = res.data.data.banner;
            }
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
        // this.$refs.loadmore.onBottomLoaded();
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          case 1:
            // this.show_fixed = true;
            this.shareDone(list);
            break;
        }
      },
      // 处理合成图片要的参数
      shareDone(list) {
        this.getEr(this.activity_list[list].acskiptype,list);
      },
      changeRoute(type,list,name){
        let _url = '';let params = '';
        if(name){
          switch (type){
            case 0:
              return false;
              break;
            case 1:
              // _url = this.title +'activityContent?openid=' + localStorage.getItem('openid') + '&baid=' + (name?this.activity_list[list].aclinkvalue : list);
              params = this.title +'activityContent&openid=' + localStorage.getItem('openid') + '&baid=' + (name?this.activity_list[list].aclinkvalue : list);
              _url = this.title + 'index/index?linkUrl="' + params+'"';
              break;
            case 2:
              // _url = this.title + 'productDetail?openid=' + localStorage.getItem('openid')+ '&prid=' + (name?this.activity_list[list].product.prid : list);
              params =  'productDetail&openid=' + localStorage.getItem('openid')+ '&prid=' + (name?this.activity_list[list].product.prid : list);
              _url = this.title + 'index/index?linkUrl='+params;
              break;
            case 3:
              _url = this.title + 'index/index?linkUrl=discover/index&openid=' + localStorage.getItem('openid') + '&acid=' + (name?this.activity_list[list].acid : list)+'&name=赚钱学院';
              break;
            case 4:
              _url = this.title + 'index/index?linkUrl=discover/index&openid=' + localStorage.getItem('openid')+ '&acid=' + (name?this.activity_list[list].acid : list) +'&name=公告';
              break;
          }
          return _url;
        }else{
          switch (type){
            case 0:
              return false;
              break;
            case 1:
              this.$router.push({path: '/activityContent', query: { openid :localStorage.getItem('openid'), baid: list}});
              break;
            case 2:
              this.$router.push({path: '/productDetail', query: { openid :localStorage.getItem('openid'), prid: list}});
              break;
            case 3:
              this.$router.push({path: '/discover', query: { openid :localStorage.getItem('openid'), acid: list,name: '赚钱学院'}});
              break;
            case 4:
              this.$router.push({path: '/discover', query: { openid :localStorage.getItem('openid'), acid: list,name: '公告'}});
              break;
          }
        }


      },
      /*获取分享的二维码**/
      getEr(id,list){
        let _url = '';
        _url = this.changeRoute(id,list,'活动');
        axios.post(api.share_qrcode +'?token=' + localStorage.getItem('token'),{
          dataurl:_url
        }).then(res => {
          if(res.data.status == 200){
            this.code_src = res.data.qrcodeurl;
            this.components_src = res.data.components;
            this.shareParams.product = this.activity_list[list].product;
            this.shareParams.media = this.activity_list[list].media;
            this.show_fixed = true;
          }
        })
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
      // /*分享按钮点击*/
      // fixedClick(){
      //   this.show_fixed = false;
      // },
      // 展开全文、收齐全文
      showMoreText(bool,v){
        let arr = [].concat(this.activity_list);
        arr[v] = Object.assign({}, arr[v], { show_text: bool });
        this.activity_list = [].concat(arr);
      },
    },
    mounted() {

      // if(this.$route.query.baimage){
      //   this.show_big_img= true;
      //   this.bigImg = this.$route.query.baimage;
      // }
      this.baid = this.$route.query.baid;
      this.getActivity();


    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .activity-img {
    width: 750px;
    height: 280px;
    margin-bottom: 40px;
  }
  .m-big-img{
    width: 100%;
    img{
      display: block;
      width: 100%;
      height: auto;
    }
  }
</style>
