<template>
    <div class="m-index" @touchmove="touchMove" @touchend="touchEnd" @touchstart="touchStart">
      <div class="m-suspend-btn " id="m-suspend-btn" :class="show_task_btn ? '':'active'" @click.stop="showModal('show_task')" >
        <span>开始转发</span>
      </div>
      <mt-loadmore :top-method="loadTop"   :bottom-all-loaded="!isScroll" ref="loadmore">
          <div class="m-top">
            <search :search="search" @searchClick="searchClick" @inputClick="inputClick"></search>
            <navbar :list="nav_list" @navClick="navClick"></navbar>
          </div>

          <mt-swipe :auto="2000">
            <mt-swipe-item v-for="item in swipe_items" :key="item.baid" >
              <a :href="item.href" rel="external nofollow" >
                <img :src="item.baimage" class="img"/>
                <span class="desc"></span>
              </a>
            </mt-swipe-item>
          </mt-swipe>
          <div class="m-recommend">
            <template v-for="(item,index) in hot_list" ><!---->
              <div class="m-recommend-one" :class="index == hot_index?'active':''" :keys="item.hmid">
                <span class="m-recommend-span">
                  <span class="m-recommend-label">热文</span>
                  <span>{{item.hmtext}}</span>
                </span>
              </div>
            </template>

          </div>

          <div class="m-index-section">
            <template v-for="(item,index) in activity_list">
              <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
            </template>
          </div>
      </mt-loadmore>
      <div class="m-modal m-copy-text" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal('show_modal')"> x </span>
          </div>
          <div class="m-modal-content">
            <h3>链接已经复制成功</h3>
            <p>您可以去分享给好友啦！
            </p>
          </div>
          <!--<div class="m-modal-foot">-->
            <!--<span class="m-modal-foot-btn">复制文案</span>-->
          <!--</div>-->
        </div>
      </div>
      <div class="m-modal" v-if="show_task">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal('show_task')"> x </span>
          </div>
          <div class="m-modal-content">
            <h3 class="m-modal-award-title">
              <span>奖励任务</span>
              <span class="m-modal-award-info">15元新衣币*2张</span>
            </h3>
            <div class="m-scroll">
              <ul class="m-modal-award-ul">
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn active">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span><span class="m-red">首单佣金翻倍</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
              </ul>
            </div>
            <div class="m-modal-award-rule">
              <h3>规则</h3>
              <p class="m-modal-award-rule-info">
                完成任务领取奖励balbalalabanal
                bababa
              </p>
            </div>
          </div>

        </div>
      </div>
      <share v-if="show_fixed"  @fixedClick="fixedClick" @share="share"></share>
      <img :src="'/static/images/course/course-'+ course + '.png'" v-if="show_course" class="m-course-img" alt="" @click.stop="courseClick">
      <img src="/static/images/fen.png" v-if="show_fen" class="m-course-img" alt="" @click.stop="fenClick">
    </div>

</template>

<script type="text/ecmascript-6">
  import navbar from '../../components/common/navbar';
  import search from '../../components/common/search';
  import ctx from './components/ctx';
  import share from '../../components/common/share';
  import api from '../../api/api';
  import axios from 'axios';
  import {Toast} from 'mint-ui';
  import wxapi from '../../common/js/mixins';
  import common from '../../common/js/common';
  import wx from 'weixin-js-sdk';
    export default {
      mixins: [wxapi],
        data() {
            return {
              course:1,
              count:2,
              total_count:0,
              search:true,
              show_course: false,
              show_modal: false,
              show_task:false,
              show_fixed:false,
              show_task_btn:true,
              show_fen:false,
              _fixed:null,
              swipe_items: [{
                title: '你的名字',
                href: 'http://google.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }, {
                title: '我的名字',
                href: 'http://baidu.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }],
              hot_list:[

              ],
              hot_index:0,
              interval:null,
              activity_list:[],
              nav_list:[
                {
                  sub: [],
                  tnid: "c3281b16-ab6b-11e8-97e2-00163e0cc024",
                  tnname: "特卖",
                  tntype: 1,
                  tsort: 57
                }
              ],
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
              isScroll: true
            }
        },
        components: {
          navbar,
          search,
          ctx,
          share
        },
      mounted(){
          this.getSwipe();
          this.getHot();
        this.getTopnav();
          let that =this;
        this.interval = window.setInterval(that.animation,3000);

        // this.$nextTick(function () {
          wxapi.wxRegister(this.wxRegCallback)
        // })


      },
        methods: {
          /*手指滑动显示隐藏*/
          touchStart(){
            // this.show_task_btn = false;
            // this.search = true;
          },
          touchMove(){
            this.show_task_btn = false;
            this.search = true;
            this.show_fixed = false;
            let scrollTop = common.getScrollTop();
            let scrollHeight = common.getScrollHeight();
            let ClientHeight = common.getClientHeight()
            if (scrollTop + ClientHeight >= scrollHeight) {
              if(this.isScroll){
                this.isScroll = false;
                this.loadBottom();
              }else  if(this.activity_list.length == this.total_count){
                this.isScroll = false
                Toast({ message: '数据已加载完', className: 'm-toast-warning' });
              }

            }
          },
          touchEnd(){
            this.show_task_btn = true;
          },
          touchStartBtn(ev){
            console.log(ev)
            ev = ev || event;
            ev.preventDefault();
            if(ev.changedTouches.length == 1) {    //tounches类数组，等于1时表示此时有只有一只手指在触摸屏幕
              // this.endX = ev.changedTouches[0].clientX; // 记录开始位置
              let ele = document.getElementById('m-suspend-btn');
              ele.style.top = ev.changedTouches[0].clientY;
            }
          },
          touchEndBtn(ev){
            ev = ev || event;
            ev.preventDefault();
            if(ev.changedTouches.length == 1) {    //tounches类数组，等于1时表示此时有只有一只手指在触摸屏幕
              // this.endX = ev.changedTouches[0].clientX; // 记录开始位置
              let ele = document.getElementById('m-suspend-btn');
              ele.style.top = ev.changedTouches[0].clientY;
            }
          },
        /*分享*/
          wxRegCallback () {
            this.wxShare()
          },
          wxShare (v,item) {
            const url = window.location.href;
            let opstion = {
              title: '微点'+item.acid, // 分享标题
              link: url,      // 分享链接
              // imgUrl: 'http://www.jzdlink.com/wordpress/wp-content/themes/wordpress_thems/images/lib/logo.png',// 分享图标
              success: function () {
                alert('分享成功')
              },
              error: function () {
                alert('分享失败')
              }
            }
            // 将配置注入通用方法
            switch (v){
              case 'appmessage':
                wxapi.ShareTimeline(opstion);
                this.show_fen = true
                break;
              case 'line':
                wxapi.ShareAppMessage(opstion);
                this.show_fen = true;
            }
          },
          share(v){
            this.wxShare(v,this._fixed);
          },
          fenClick(){
            this.show_fen = false
          },
          /*获取导航*/
          getTopnav(){
            axios.get(api.get_home_topnav).then(res => {
              if(res.data.status == 200){
                this.nav_list = [].concat(res.data.data);
                for(let i=0;i<this.nav_list.length;i++){
                  this.nav_list[i].click =false;
                }
                this.nav_list[0].click =true;
                this.getActivity(this.nav_list[0].tnid);
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            })
          },
          /*获取滚动轮播图*/
          getSwipe(){
            axios.get(api.get_all_banner,{params:{
                lasting:true
              }}).then(res => {
               if(res.data.status == 200){
                 this.swipe_items = res.data.data;
               }else{
                 Toast({ message: res.data.message, className: 'm-toast-fail' });
               }
            })
          },
          /*获取热文*/
          getHot(){
            axios.get(api.get_all_hotmessage,{params:{
                lasting:true
              }}).then(res => {
              if(res.data.status == 200){
                this.hot_list = res.data.data;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            })
          },
          /*获取活动列表*/
          getActivity(tnid,start,count){
            axios.get(api.get_all_activity +'?token=' +  localStorage.getItem('token'),{params:{
                lasting:true,
                start:start || 0,
                count:count || this.count,
                tnid:'shangxin'
              }}).then(res => {
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
                for(let i=0;i<arr.length;i++){
                  let _arr = [
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
                  ];
                  _arr[0].name = arr[i].likenum;
                  _arr[0].alreadylike = arr[i].alreadylike;
                  arr[i].actext.length >92 && (arr[i].show_text = true) ;
                  arr[i].icon = [].concat(_arr);
                  console.log(_arr[0].name,arr[i].likenum)
                }
                this.activity_list = [].concat(arr)
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            })
          },
          /*热文轮播*/
          animation(v){
            v = v || 1;
            if(this.hot_index == this.hot_list.length -1){
              this.hot_index = 0;
            }else{
              this.hot_index = this.hot_index + v;
            }
          },
          /*点赞*/
          changeLike(id,index){
            let arr = this.activity_list[index].icon[0];
              axios.post(api.ac_like+'?token=' +  localStorage.getItem('token'),{
                  acid:id
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
                    console.log(arr)
                  }else{
                    Toast({ message: res.data.message, className: 'm-toast-fail' });
                  }
              })
          },
          /*搜索*/
          inputClick(){
            this.search = false;
          },
          searchClick(v){
            console.log(v)
            axios.get(api.get_search,{params:{
                token:localStorage.getItem('token'),
                PRname:v,
                page:1,
                start:0,
                count:this.count
              }}).then(res => {
                if(res.data.status == 200){
                  if(res.data.data.length < 1 ){
                    Toast({ message: '无匹配内容', className: 'm-toast-warning' });
                  }
                  this.activity_list = res.data.data;
                  for(let i=0;i<this.activity_list.length;i++){
                    this.activity_list[i].icon = this.icon_list;
                    this.activity_list[i].icon[0].name = this.activity_list[i].likenum;
                    this.activity_list[i].icon[0].alreadylike = this.activity_list[i].alreadylike;
                    this.activity_list[i].actext.length >92 && (this.activity_list[i].show_text = true) ;
                  }
                }else{
                  Toast({ message: res.data.message, className: 'm-toast-fail' });
                }
            })
          },
          /*关闭模态框*/
          closeModal(v){
            this[v]  = false;
          },
          /*开启模态框*/
          showModal(v){
            this[v] = true;
          },
          /*分享按钮点击*/
          fixedClick(){
            this.show_fixed = false;

          },
          /*导航点击*/
          navClick(v){
            let arr = this.nav_list;
            for(let i=0;i<arr.length;i++){
              arr[i].click = false;
            }
            arr[v].click = true;
            this.nav_list = [].concat(arr);
            this.getActivity(this.nav_list[v].tnid);
          },
          /*每个活动icon点击*/
          iconClick(v,list){
            switch (v){
              case 0:
                this.changeLike(this.activity_list[list].acid,list);
                break;
              case 1:
                this.download('121312312')
                break;
              case 2:
                this.show_fixed = true;
                this._fixed = this.activity_list[list];
                break;
            }
          },
          /*复制链接*/
          download(url){
            let that =this;
            this.$copyText(window.location.href).then(function (e) {
              that.show_modal = true;
            }, function (e) {

            })
            // alert(url)
            // wx.chooseImage({
            //   // count: 1, // 默认9
            //   sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
            //   sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
            //   success: function (res) {
            //     var localIds = res.localIds[0]; // 返回选定照片的本地ID列表，localId可以作为img标签的src属性显示图片
            //     wx.uploadImage({
            //       localId: localIds, // 需要上传的图片的本地ID，由chooseImage接口获得
            //       isShowProgressTips: 1, // 默认为1，显示进度提示
            //       success: function (res) {
            //         localStorage.setItem('id',res.serverId)  ; // 返回图片的服务器端ID
            //       }
            //     });
            //   }
            // });
            // wx.downloadImage({
            //   serverId: localStorage.getItem('id'), // 需要下载的图片的服务器端ID，由uploadImage接口获得
            //   isShowProgressTips: 1, // 默认为1，显示进度提示
            //   success: function (res) {
            //     var localId = res.localId; // 返回图片下载后的本地ID
            //     alert(localId)
            //   }
            // });
          },
          /*展开全文*/
          showMoreText(bool,v){
            let arr = [].concat(this.activity_list);
            arr[v] = Object.assign({}, arr[v], { show_text: bool });
            this.activity_list = [].concat(arr);
          },
          /*下拉刷新*/
          loadTop() {
            for(let i=0;i<this.nav_list.length;i++){
              if(this.nav_list[i].click){
                this.getActivity(this.nav_list[i].tnid);
              }
            }
            this.$refs.loadmore.onTopLoaded();
          },
          /*上拉加载更多**/
          loadBottom() {
            for(let i=0;i<this.nav_list.length;i++){
              if(this.nav_list[i].click){
                this.getActivity(this.nav_list[i].tnid,this.activity_list.length);
              }
            }
            // this.allLoaded = true;// 若数据已全部获取完毕
            // this.$refs.loadmore.onBottomLoaded();
          },
          courseClick(){
            if(this.course <6){
              this.course += 1;
            }else{
              this.show_course = false;
            }
          }
        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
  @import "../../common/css/modal";
.m-top{
  margin-top: 10px;
}
  .m-course-img{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10000;
  }
  .m-recommend{
    width: 100%;
    background-color: #F9F9F9;
    height: 44px;
    line-height: 44px;
    font-size: 20px;
    overflow: hidden;
    position: relative;
    .m-recommend-one{
      position: absolute;
      bottom:-44px;
      text-align: center;
      width: 100%;
      z-index: -1;
      &.active{
        bottom:0;
        z-index: 1;
      }
     .m-recommend-span{
       display: inline-block;
       .m-recommend-label{
         display: inline-block;
         padding: 0 10px;
         height: 27px;
         line-height: 27px;
         font-size: 20px;
         color: @mainColor;
         border: 1px solid @mainColor;
         border-radius: 4px;
         margin-right: 12px;
       }
     }

    }

  }
  .m-index-section{

  }
.m-suspend-btn{
  position: fixed;
  top:50%;
  right: 5px;
  transform: translateY(-56.5px);
  width: 113px;
  height: 113px;
  box-shadow: 0 7px 13px rgba(245, 78, 100, 0.83) ;
  background-color: rgba(245, 78, 100, 0.83);
  color: rgba(248, 248, 249, 0.8);
  border-radius: 50%;
  z-index: 1001;
  vertical-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  transition: right 0.5s;
  &.active{
    right: -113px;
  }
}
.m-index{
  .m-modal{
    &.m-copy-text{
      .m-modal-state{
        /*height: auto;*/
        width: 620px;
        height: 300px;
        .m-modal-head{
          margin-bottom: 40px;
        }
      }
    }
    .m-modal-state{
      /*height: auto;*/
      width: 620px;
      height: 1000px;
      .m-modal-head{
        padding: 0 20px;
      }
      .m-modal-content{
        padding: 0;
        .m-modal-award-title{
          .flex-row(space-between);
          color: #333;
          padding: 10px 33px 30px;
          font-size: 30px;
          font-weight: normal;
          border-bottom: 1px solid @borderColor;
          margin-bottom: 20px;
          .m-modal-award-info{
            color: @grey;
            font-size: 24px;
          }
        }
        .m-scroll{
          height: 620px;
          overflow-y: auto;
          .m-modal-award-ul{
            li{
              .flex-row(space-between);
              margin: 0 25px;
              border-bottom: 1px solid @borderColor;
              padding: 30px 0;
              .m-modal-award-img-box{
                .flex-row(flex-start);
                text-align: left;
                .m-modal-award-img{
                  display: block;
                  width: 77px;
                  height: 77px;
                  background-color: #a3a3a3;
                  border-radius: 50%;
                  margin-right: 30px;
                }
                h3{
                  font-size: 26px;
                  line-height: 30px;
                }
                .m-modal-award-complete{
                  font-size: 22px;
                  .m-red{
                    margin-left: 20px;
                  }
                }
              }
              .m-modal-award-btn{
                display: block;
                width: 137px;
                height: 46px;
                line-height: 46px;
                text-align: center;
                border-radius: 23px;
                background:  linear-gradient(to right, #ff3146, #ff7044);
                -webkit-background-clip: text;
                color: transparent;
                border: 2px solid #ff3146;
                &.active{
                  color: #fff;
                  border: solid 2px transparent;
                  background-image: linear-gradient(to right, #ff3146, #ff7044), linear-gradient(to right, #ff3146, #ff7044);
                  background-origin: border-box;
                  background-clip: content-box, border-box;
                }
              }
            }
          }
        }
        .m-modal-award-rule{
          text-align: left;
          h3{
            margin: 0 33px 20px;
            font-size: 30px;
          }
          .m-modal-award-rule-info{
            padding: 10px 80px;
            font-size: 20px;
            line-height: 24px;
          }
        }
      }
    }

  }
}

</style>
