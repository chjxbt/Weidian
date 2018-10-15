<template>
    <div class="m-index"  @touchmove.stop="touchMove" @touchend.stop="touchEnd" @touchstart.stop="touchStart">
      <div class="m-suspend-btn " v-if="is_vip" id="m-suspend-btn" :class="show_task_btn ? '':'active'" @click.stop="showModal('show_task')" >
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
                <img :src="item.baimage" class="img" @click="toActivity(item)"/>
                <span class="desc"></span>
              </a>
            </mt-swipe-item>
          </mt-swipe>
          <div class="m-recommend">
            <template v-for="(item,index) in hot_list" ><!---->
              <div class="m-recommend-one" :class="index == hot_index?'active':''" :keys="item.hmid" @click="hotClick(item)">
                <span class="m-recommend-span">
                  <span class="m-recommend-label">热文</span>
                  <span>{{item.hmtext}}</span>
                </span>
              </div>
            </template>

          </div>

          <div class="m-index-section">
            <template v-for="(item,index) in activity_list">
              <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText" ></ctx>
            </template>
          </div>
      </mt-loadmore>
      <!--<div class="m-modal m-copy-text" v-if="show_modal">-->
        <!--<div class="m-modal-state">-->
          <!--<div class="m-modal-head">-->
            <!--<span class="m-close" @click="closeModal('show_modal')"> x </span>-->
          <!--</div>-->
          <!--<div class="m-modal-content">-->
            <!--<h3>链接已经复制成功</h3>-->
            <!--<p>您可以去分享给好友啦！-->
            <!--</p>-->
          <!--</div>-->
          <!--&lt;!&ndash;<div class="m-modal-foot">&ndash;&gt;-->
            <!--&lt;!&ndash;<span class="m-modal-foot-btn">复制文案</span>&ndash;&gt;-->
          <!--&lt;!&ndash;</div>&ndash;&gt;-->
        <!--</div>-->
      <!--</div>-->
      <div class="m-modal" v-if="show_task" @click.stop="closeModal('show_task')" >
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click.stop="closeModal('show_task')"> x </span>
          </div>
          <div class="m-modal-content">
            <h3 class="m-modal-award-title">
              <span>奖励任务</span>
              <span class="m-modal-award-info" v-if="task_reward">{{task_reward.raward}}</span>
              <!--<span class="m-modal-award-info" v-if="task_reward && task_reward.ratype == 0">满{{task_reward.rafilter}}减{{task_reward.raamount}}</span>-->
              <!--<span class="m-modal-award-info" v-if="task_reward && task_reward.ratype == 1">佣金上浮{{task_reward.raratio}}</span>-->
              <!--<span class="m-modal-award-info" v-if="task_reward">{{task_reward.raamount}}元新衣币<span v-if="task_reward.ranumber">*{{task_reward.ranumber}}张</span></span>-->
            </h3>
            <div class="m-scroll">
              <ul class="m-modal-award-ul">
                <template v-for="(item,index) in task_list">
                  <li>
                    <div class="m-modal-award-img-box">
                      <img :src="item.tahead" class="m-modal-award-img" alt="">
                      <div>
                        <h3>{{item.taname}}</h3>
                        <p class="m-modal-award-complete" >
                          <span v-if="item.tatype == 0">完成 {{item.tunumber}}/1</span>
                          <span v-else>完成{{item.tunumber}}/{{item.taurl}}</span>
                          <span class="m-red" v-if="item.tamessage">{{item.tamessage}}</span></p>
                      </div>
                    </div>
                    <span class="m-modal-award-btn" :class="item.tustatus >0 ?'active':''" v-if="item.tustatus == 1" >完 成</span>
                    <span class="m-modal-award-btn" v-else-if="item.talevel == 99">额外奖励</span>
                    <span class="m-modal-award-btn"  v-else @click.stop="makeTask(index)">做任务</span>
                  </li>
                </template>
              </ul>
            </div>
            <div class="m-modal-award-rule">
              <h3>规则</h3>
              <p class="m-modal-award-rule-info">
               {{TArole}}
              </p>
            </div>
          </div>
        </div>
      </div>
      <attention v-if="show_fixed" :src="code_src" :components_src="components_src" :shareParams="shareParams" @closeModal="closeModal('show_fixed')"></attention>
      <img :src="'/static/images/course/course-'+ course + '.png'" v-if="show_course" class="m-course-img" alt="" @click.stop="courseClick">
      <!--<img src="/static/images/fen.png" v-if="show_fen" class="m-course-img" alt="" @click.stop="fenClick">-->
      <m-video v-if="show_video" :src="video_src" @videoClose="videoClose"></m-video>
      <img-modal v-if="show_img" :src="img_src" @closeModal="closeModal"></img-modal>
      <div class="bottom-prompt" v-if="bottom_show">
        <div class="bottom-line"></div>
        <div class="m-grey-color">我是有底线的</div>
        <div class="bottom-line"></div>
      </div>
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
  import attention from '../../components/common/attention';
  import mVideo from '../../components/common/video';
  import imgModal from '../../components/common/imgModal';
  import wx from 'weixin-js-sdk';
  var scroll = (function (className) {
    var scrollTop;
    return {
      afterOpen: function () {
        scrollTop = document.scrollingElement.scrollTop || document.body.scrollTop;
        document.body.classList.add(className);
        document.body.style.top = -scrollTop + 'px';
      },
      beforeClose: function () {
        document.body.classList.remove(className);
        document.scrollingElement.scrollTop = scrollTop;
        document.body.scrollTop = scrollTop;
      }
    };
  })('scroll');
    export default {
      mixins: [wxapi],
        data() {
            return {
              title: 'https://weidianweb.daaiti.cn/#/',
              // title:'http://www.daaiti.cn:8080/#/',
              course:1,
              count:5,
              total_count:0,
              search:true,
              show_course: false,
              show_modal: false,
              show_task:false,
              show_fixed:false,
              show_task_btn:true,
              show_fen:false,
              show_video:false,
              show_img:false,
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
                // {
                //   src:'icon-lian',
                //   name:'复制链接',
                //   url:'icon-lian'
                // },
                {
                  src:'icon-share',
                  name:'转发',
                  url:'icon-share'
                }
              ],
              isScroll: true,
              shareParams: {
                media:[],
                product:{}
              },
              bottom_show:false,
              task_list:[],
              video_src:'',
              img_src:'',
              TArole:'',
              code_src:'',
              components_src:'',
              task_reward:null,
              is_vip:true
            }
        },
        components: {
          navbar,
          search,
          ctx,
          share,
          attention,
          mVideo,
          imgModal
        },
      mounted(options){
        //判断是否登录
        if(!localStorage.getItem('token') &&!common.GetQueryString('code')){
          this.login();
        }
        if(this.isWeiXin()){    //是来自微信内置浏览器
          // 获取微信信息，如果之前没有使用微信登陆过，将进行授权登录
          if(common.GetQueryString('code')){
            // alert(common.GetQueryString('code'))
            window.localStorage.setItem("code",common.GetQueryString('code'));
            axios.get(api.get_accesstoken,{
              params:{
                code: common.GetQueryString('code'),
                UPPerd:localStorage.getItem('UPPerd') || ''
              }
            }).then(res => {
              if(res.data.status == 200){
                window.localStorage.setItem("access_token",res.data.data.access_token);
                window.localStorage.setItem("token",res.data.data.token);
                window.localStorage.setItem("openid",res.data.data.openid);
                window.localStorage.setItem("is_first",String(res.data.data.is_first));
                window.localStorage.setItem("wximg",res.data.data.wximg);
                window.localStorage.setItem("subscribe",res.data.data.subscribe);
                window.localStorage.setItem("is_today_first",res.data.data.is_today_first);
                window.localStorage.setItem("user_level",res.data.data.user_level);
                this.$store.state.tabbar = res.data.data.icon;
                this.$store.state.tabbar_select = res.data.data.icon[0].name;
                this.init();
                // this.$router.push('/index/index');
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            });
          }
        }

        if(localStorage.getItem('token')){
          this.init();
        }

        // })
      },
      watch:{
        show_task:function (val,oldVal) {
          if(val){
            scroll.afterOpen();
          }else{
            scroll.beforeClose();
          }
        }
      },
        methods: {
        init(){
          if(this.$route.query.linkUrl && localStorage.getItem('is_click') != '1'){
            switch (this.$route.query.linkUrl){
              case 'activityContent':
                this.$router.push({path:'/'+this.$route.query.linkUrl,query:{
                    baid:this.$route.query.baid,
                  }});
                localStorage.setItem('is_click','1')
                break;
              case 'productDetail':
                this.$router.push({path:'/'+this.$route.query.linkUrl,query:{
                    prid:this.$route.query.prid,
                  }})
                localStorage.setItem('is_click','1')
                break;
              case 'discover/index':
                this.$router.push({path:'/'+this.$route.query.linkUrl,query:{
                    acid:this.$route.query.acid,
                    name:this.$route.query.name
                  }});
                localStorage.setItem('is_click','1')
                break;

            }
            return false;
          }
          common.changeTitle('首页');
          if(common.GetQueryString('UPPerd')){
            localStorage.setItem('UPPerd',common.GetQueryString('UPPerd'));
            alert(common.GetQueryString('UPPerd'))
            if(localStorage.getItem('token')){
              this.$router.push('/login');
            }
          }
          this.getSwipe();
          this.getHot();
          this.getTopnav();
          if(localStorage.getItem('level') == 'partner'){
            this.is_vip = true;
            this.getTask();
          }else{
            this.is_vip = false;
          }

          if(localStorage.getItem('is_first')  == 'true' || localStorage.getItem('is_first')  == '1'){
            this.show_course = true;
            localStorage.setItem("is_first", "0");
          }
          let that =this;
          this.interval = window.setInterval(that.animation,3000);

          // this.$nextTick(function () {
          wxapi.wxRegister(this.wxRegCallback)
        },
          login(){
            axios.get(api.get_config,{
              params:{
                url: window.location.href
              }
            } ).then((res) => {
              if(res.data.status == 200){
                const id = res.data.data.appId;
                const url = window.location.href;
                // const  url = 'https://daaiti.cn/WeiDian/#/login';
                window.location.href = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='
                  +  id + '&redirect_uri='+ encodeURIComponent(url) + '&response_type=code&scope=snsapi_userinfo&state=1#wechat_redirect'
              }

            }).catch((error) => {
              console.log(error ,'1111')
            })
          },
          isWeiXin() {
            let ua = window.navigator.userAgent.toLowerCase();
            console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
            if (ua.match(/MicroMessenger/i) == 'micromessenger') {
              return true;
            } else {
              return false;
            }

          },
          /*手指滑动显示隐藏*/
          touchStart(e){

            // this.show_task_btn = false;
            // this.search = true;
          },
          touchMove(e){
            this.show_task_btn = false;
            this.search = true;
            this.show_fixed = false;
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
          touchEnd(){
            this.show_task_btn = true;
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
          hotClick(item){
            // this.changeRoute(item.hmskiptype,item.hmcontent)
           this.changeRoute(item.hmskiptype,item.hmcontent);
          },
          changeRoute(type,list,name){
            let _url = '';let params ='';
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
          /*获取任务*/
          getTask(v){
            axios.get(api.get_user_task,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
               this.task_list = res.data.data;
               this.TArole = res.data.TArole;
               this.task_reward = res.data.RAward;
                if(localStorage.getItem('is_today_first') == 1){
                  this.show_task = true;
                  window.localStorage.setItem("is_today_first",0);
                }
               if(res.data.is_complate){
                  // if(v)
                  //   return false;
                 this.img_src = res.data.TAcomplateNotifications;
                 this.show_img = true;
               }
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            })
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
            /*axios.get(api.get_all_banner,{params:{
                lasting:true
              }}).then(res => {
              if(res.data.status == 200){
                this.swipe_items = res.data.data;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            })*/

            // 获取轮播图的新接口
            axios.get(api.get_home_banner + '?lasting=true&token=' + localStorage.getItem('token')).then(res => {
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
                lasting:true,
                token:localStorage.getItem('token')
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
                tnid:tnid,
                // skiptype: 'all'
              }}).then(res => {
              if(res.data.status == 200){
                this.isScroll = true;
                this.total_count = res.data.count;
                if(start){
                  this.activity_list = this.activity_list.concat(res.data.data);
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
                      src:'icon-share',
                      name:'转发',
                      url:'icon-share'
                    }
                  ];
                  _arr[0].name = arr[i].likenum;
                  _arr[0].alreadylike = arr[i].alreadylike;
                  arr[i].actext.length >92 && (arr[i].show_text = true) ;
                  arr[i].icon = [].concat(_arr);
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
                      Toast({ message: res.data.message,duration: 800, className: 'm-toast-warning' });
                    }else if(!arr.alreadylike) {
                      arr.name = Number(arr.name) + 1;
                      arr.alreadylike = true;
                      Toast({ message: res.data.message, duration: 800, className: 'm-toast-success' });
                    }
                    // this.activity_list[index].icon[0] = arr;
                    // this.$set(this.activity_list[index].icon[0],'name',arr.name);
                    // this.$set(this.activity_list[index].icon[0],'alreadylike',arr.alreadylike);

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
          /*关闭视频*/
          videoClose(){
            this.show_video = false;
          },
          /*开启模态框*/
          showModal(v){
            this[v] = true;
            if(v == 'show_task'){
              this.getTask('two');
            }
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
            this.activity_list = [];
            this.getActivity(this.nav_list[v].tnid);
          },
          /*每个活动icon点击*/
          iconClick(v,list){
            switch (v){
              case 0:
                this.changeLike(this.activity_list[list].acid,list);
                break;
              case 1:
                // this.show_fixed = true;
                // this._fixed = this.activity_list[list];
                this.shareDone(list);
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
            if(this.course <3){
              this.course += 1;
            }else{
              this.show_course = false;
            }
          },
          // 处理合成图片要的参数
          shareDone(list) {
            this.getEr(this.activity_list[list].acskiptype,list);
          },
          /*做任务*/
          makeTask(i){
            if(this.task_list[i].tatype !=0){
              this.show_task = false;
              return false;
            }else{
              this.video_src = this.task_list[i].taurl;
              this.show_video = true;
            }
            axios.post(api.do_task + '?token='+localStorage.getItem('token'),{
              TUid:this.task_list[i].tuid
            }).then(res => {
                if(res.data.status == 200){
                  this.getTask();
                }
            })
          },
          // 去活动内容页
          toActivity(activity) {
            let rbimage = activity.baimage;
            this.$router.push({path: "/activityContent", query: { rbimage:rbimage,baid:activity.baid }});
          },
        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
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
    &.m-share{
      .m-modal-state{
        height: 560px;
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
          overflow-x: hidden;
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
