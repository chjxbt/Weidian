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
          <span class="m-smile-icon" :class="recommend.alreadylike?'active':''" @click="likeThis(recommend)"></span>
          <span>{{recommend.relikenum}}</span>
        </div>
      </div>
      <div class="line"></div>
    </div>

    <mt-loadmore :top-method="loadTop" ref="loadmore">
      <div class="m-index-section">
        <template v-for="(item,index) in activity_list">
          <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
        </template>
      </div>
    </mt-loadmore>

    <share v-if="show_fixed" @fixedClick="fixedClick"></share>
  </div>
</template>

<script type="text/ecmascript-6">
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
  import ctx from '../../index/components/ctx';
  import share from '../../../components/common/share';

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
    components: { ctx, share },
    methods: {
      // 获取每日推荐内容
      getData(){
        let token = localStorage.getItem('token');
        axios.get(api.get_info_recommend + '?token=' + token).then(res => {
          if(res.data.status == 200) {
            this.recommend = res.data.data[0];
            this.suuser = this.recommend.suuser;

            this.recommend.products.push(this.recommend.products[0]);
            this.recommend.products.push(this.recommend.products[0]);
            this.recommend.products.push(this.recommend.products[0]);
            this.recommend.products.push(this.recommend.products[0]);

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
            let oli = document.getElementsByTagName("li");
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
      // 去活动内容页
      toActivity(item) {
        console.log(item);
      },
      // 去产品详情页
      toProduct(i) {
        let product = this.recommend.products[i - 4];
        this.$router.push({path: "/productDetail", query: { product }});
      },
      /*分享按钮点击*/
      fixedClick(){
        this.show_fixed = false;
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          case 1:
            this.show_modal = true;
            break;
          case 2:
            this.show_fixed = true;
            break;
        }
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
      // 展开全文、收齐全文
      showMoreText(bool,v){
        let arr = [].concat(this.activity_list);
        arr[v] = Object.assign({}, arr[v], { show_text: bool });
        this.activity_list = [].concat(arr);
      },
      loadTop() {
        for(let i=0;i<this.nav_list.length;i++){
          if(this.nav_list[i].click){
            this.getActivity(this.nav_list[i].tnid);
          }
        }
        this.$refs.loadmore.onTopLoaded();
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
