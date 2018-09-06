<template>
  <div>
    <mt-swipe :auto="2000">
      <mt-swipe-item v-for="item in bannerList" :key="item.id">
        <img :src="item.src" @click="toVideo(item)">
      </mt-swipe-item>
    </mt-swipe>
    <navbar :list="nav_list" @navClick="navClick"></navbar>
    <div class="class-box" v-for="item in classList">
      <div class="box-left">
        <div class="box-left-top">
          <span class="m-mark m-ft-20" v-if="item.top">置顶</span>
          <span class="m-text m-ft-26 tl">{{item.title}}</span>
        </div>
        <div class="box-left-bottom">
          <img class="teacher-img" :src="item.src">
          <span class="teacher-text m-grey-color tl">{{item.name}}</span>
          <span class="teacher-text m-grey tr">{{item.num}}人已学</span>
        </div>
      </div>
      <div class="box-right">
        <img class="box-right-img" :src="item.video">
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  export default {
    name: "advancedClass",
    data(){
      return{
        bannerList: [
          { src: "http://img57.ddimg.cn/118320000279366.jpg" },
          { src: "http://img57.ddimg.cn/118320000279366.jpg" },
          { src: "http://img57.ddimg.cn/118320000279366.jpg" },
          { src: "http://img57.ddimg.cn/118320000279366.jpg" },
          { src: "http://img57.ddimg.cn/118320000279366.jpg" }
        ],
        nav_list: [
          { click: true, tnname: "中级进阶" },
          { click: false, tnname: "高级提升" },
          { click: false, tnname: "店主故事" }
        ],
        classList: [
          { top: true, title: "视频标题巴拉巴拉巴拉吧视频标题巴拉巴拉巴拉吧", src: "/static/images/product1.png", name: "导师名字", num: "150", video: "http://img1.imgtn.bdimg.com/it/u=466950367,3866012290&fm=26&gp=0.jpg" },
          { top: true, title: "视频标题巴拉巴拉巴拉吧视频标题巴拉巴拉巴拉吧", src: "/static/images/product1.png", name: "导师名字", num: "150", video: "http://img1.imgtn.bdimg.com/it/u=466950367,3866012290&fm=26&gp=0.jpg" },
          { top: true, title: "视频标题巴拉巴拉巴拉吧视频标题巴拉巴拉巴拉吧", src: "/static/images/product1.png", name: "导师名字", num: "150", video: "http://img1.imgtn.bdimg.com/it/u=466950367,3866012290&fm=26&gp=0.jpg" },
          { top: false, title: "视频标题巴拉巴拉巴拉吧视频标题巴拉巴拉巴拉吧", src: "/static/images/product1.png", name: "导师名字", num: "150", video: "http://img1.imgtn.bdimg.com/it/u=466950367,3866012290&fm=26&gp=0.jpg" },
          { top: false, title: "视频标题巴拉巴拉巴拉吧视频标题巴拉巴拉巴拉吧", src: "/static/images/product1.png", name: "导师名字", num: "150", video: "http://img1.imgtn.bdimg.com/it/u=466950367,3866012290&fm=26&gp=0.jpg" },
        ]
      }
    },
    components: { navbar },
    methods: {
      // 去视频播放页
      toVideo(item) {

      },
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .class-box {
    width: 100%;
    display: flex;
    border-bottom: 2px #E5E5E5 solid;
    .box-left {
      flex: 1;
      margin: 54px 0 54px 40px;
      .box-left-top {
        width: 100%;
        display: flex;
        .m-mark{
          width: 60px;
          height: 35px;
          display: inline-block;
          padding: 3px 10px;
          margin-right: 20px;
          text-align: center;
          background-color: @mainColor;
          color: #fff;
          border-radius: 10px;
          font-size: 20px;
        }
        .m-text {
          width: 80%;
          margin-bottom: 30px;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          overflow: hidden;
        }
      }
      .box-left-bottom {
        width: 100%;
        display: flex;
        .teacher-img {
          width: 34px;
          height: 34px;
          margin-right: 15px;
          border-radius: 50%;
        }
        .teacher-text {
          flex: 1;
          font-size: 22px;
        }
      }
    }
    .box-right {
      margin: 54px 21px;
      .box-right-img {
        width: 239px;
        height: 136px;
      }
    }
  }
</style>
