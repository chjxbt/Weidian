<template>
  <div class="m-discover-announcement" @touchmove="touchMove">
    <div class="m-section-one" v-for="(item, index) in activity_list">
      <div class="m-section-content">
        <div class="m-section-title">
          <img class="m-section-img" :src="item.suuser.suheader"/>
          <div>
            <span class="m-title">{{item.suuser.suname}}</span>
            <p class="m-fodder-time">{{item.accreatetime}} 发布</p>
          </div>
        </div>
        <div class="m-section-text">
          <p class="m-ft-30"><span class="m-mark" v-if="item.acistop">置顶</span>{{item.actitle}}</p>

          <p class="textP m-ft-28" :class="!item.show_text ? 'active':''">{{item.actext}}</p>
          <span class="m-section-more" v-if="item.show_text" @click="showMore(false, index)">展开全文</span>
          <span class="m-section-more" v-if="item.actext.length > 86 && !item.show_text" @click="showMore(true, index)">收起全文</span>

          <div class="m-img-list">
            <img class="m-section-text-img" :src="item.media[0].amimage" @click="test(item.media[0].amimage)">
          </div>
          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>{{item.acbrowsenum}}</span>
                <span class="m-good-icon" :class="item.alreadylike?'active':''" @click="likeThis(item, index)"></span>
                <span>{{item.likenum}}人说好</span>
              </div>
            </div>
            <div>
              <icon-list :list="icon_list" @iconClick="iconClick"></icon-list>
            </div>
          </div>
          <div class="m-comment-box">
            <div class="m-comment-content">
              <span class="m-comment-s"></span>
              <p v-for="comment in item.comment">
                <span class="m-comment-name">{{comment.user.usname}}</span>: {{comment.actext}}
              </p>
              <div v-if="show_input" class="new-comment-box">
                <input type="text" class="new-comment-input" v-model="comment"/>
                <div class="new-comment-done" :class="comment!=''?'active':''" @click="commentDone(item, index)">发送</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bottom-prompt" v-if="bottom_show">
      <div class="bottom-line"></div>
      <div class="m-grey-color">我是有底线的</div>
      <div class="bottom-line"></div>
    </div>

    <!--<share v-if="show_fixed" :num="2" @fixedClick="fixedClick"></share>-->
    <attention v-if="show_fixed" @closeModal="closeModal('show_fixed')"></attention>
  </div>
</template>

<script type="text/ecmascript-6">
  import iconList from'../../../components/common/iconList';
  import share from '../../../components/common/share';
  import attention from '../../../components/common/attention';
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
  import common from '../../../common/js/common';

  import wxapi from '../../../common/js/mixins';
  import wx from 'weixin-js-sdk';
  export default {
    mixins: [wxapi],
    data() {
      return {
        icon_list:[
          {
            src:'icon-share',
            name:'转发',
            url:'icon-share'
          },
          {
            src:'icon-message',
            name:'评论',
            url:'icon-message'
          }
        ],
        show_fixed: false,
        show_input: false,
        activity_list: [],
        comment: "",
        isScroll: true,
        total_count: 0,
        count: 5,
        bottom_show: false
      }
    },
    props:{
      tnid: { type: String, default: null }
    },
    components: { iconList, share, attention },
    methods: {
      test(picture) {

        console.log(picture);

        let options = {
          current: "http://img.zcool.cn/community/019c2958a2b760a801219c77a9d27f.jpg", // 当前显示图片的http链接
          urls: ["http://img.sccnn.com/bimg/338/24556.jpg", "http://pic.58pic.com/58pic/14/62/50/62558PICxm8_1024.jpg", "http://img.zcool.cn/community/01ca8c573c04b832f8757cb97b2444.jpg@1280w_1l_2o_100sh.jpg"],
        };
        // console.log(options);
        // wxapi.previewImage(options);


      },
      touchMove(){
        let scrollTop = common.getScrollTop();
        let scrollHeight = common.getScrollHeight();
        let ClientHeight = common.getClientHeight()
        if (scrollTop + ClientHeight >= scrollHeight) {
          if(this.isScroll){
            this.isScroll = false;
            if(this.activity_list.length == this.total_count){
              this.bottom_show = true;
              // Toast({ message: '数据已加载完', className: 'm-toast-warning' });
            }else{
              this.loadBottom();
            }
          }
        }
      },
      // 下拉刷新
      loadTop() {
        this.getActivity();
      },
      // 上拉加载更多
      loadBottom() {
        this.getActivity(this.activity_list.length, this.count);
      },
      /*获取活动列表*/
      getActivity(start, count){
        axios.get(api.get_all_activity + "?token=" + localStorage.getItem('token'), {
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
            this.activity_list = [].concat(arr);

            // 判断今天、昨天和直接显示日期
            let now = new Date();
            let year = now.getFullYear(); //得到年份
            let month = now.getMonth();//得到月份
            let date = now.getDate();//得到日期
            let hour = now.getHours();//得到小时
            let minu = now.getMinutes();//得到分钟
            let sec = now.getSeconds();//得到秒
            month = month + 1;
            if (month < 10) month = "0" + month;
            if (date < 10) date = "0" + date;
            if (hour < 10) hour = "0" + hour;
            if (minu < 10) minu = "0" + minu;
            if (sec < 10) sec = "0" + sec;
            let time = year + month + date + hour + minu + sec;
            let time1 = time.slice(0,4);// 当前年份
            let time2 = time.slice(4,8);// 当前日期

            for(let i = 0; i < this.activity_list.length; i ++) {
              let createTime = this.activity_list[i].accreatetime;
              if(createTime.indexOf("-") == -1) {
                let createTime1 = createTime.slice(0,4);// 发布年份
                let createTime2 = createTime.slice(4,8);// 发布日期
                // 今年发布的
                if(time1 == createTime1) {
                  // 今年发布且月份相同
                  if(time2.slice(0, 2) == createTime2.slice(0, 2)) {
                    if(Number(time2.slice(2, 4)) == Number(createTime2.slice(2, 4))) {
                      this.activity_list[i].accreatetime = "今天 " + createTime.slice(8, 10) + ":" + createTime.slice(10, 12);
                    }else if(Number(time2.slice(2, 4)) == Number(createTime2.slice(2, 4)) + 1) {
                      this.activity_list[i].accreatetime = "昨天 " + createTime.slice(8, 10) + ":" + createTime.slice(10, 12);
                    }else if(Number(time2.slice(2, 4)) > Number(createTime2.slice(2, 4)) + 1) {
                      // 今年发布的不显示年份
                      let createTime3 = createTime.slice(4, 6) + "-" + createTime.slice(6, 8) + " "
                        + createTime.slice(8, 10) + ":" + createTime.slice(10, 12);
                      this.activity_list[i].accreatetime = createTime3;
                    }
                  }else {
                    // 今年发布的不显示年份
                    let createTime3 = createTime.slice(4, 6) + "-" + createTime.slice(6, 8) + " "
                      + createTime.slice(8, 10) + ":" + createTime.slice(10, 12);
                    this.activity_list[i].accreatetime = createTime3;
                  }
                }else {
                  // 今年以前发布的
                  let createTime3 = createTime.slice(0, 4) + "-" + createTime.slice(4, 6) + "-" + createTime.slice(6, 8) + " "
                    + createTime.slice(8, 10) + ":" + createTime.slice(10, 12);
                  this.activity_list[i].accreatetime = createTime3;
                }
              }
              // 展开全文、显示全文
              this.activity_list[i].actext.length > 90 && (this.activity_list[i].show_text = true);
            }
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      // 展开全文、显示全文
      showMore(status, index){
        let arr = [].concat(this.activity_list);
        arr[index] = Object.assign({}, arr[index], { show_text: status });
        this.activity_list = [].concat(arr);
      },
      // 获取评论
      getCommentList() {
        for(let i = 0; i < this.activity_list.length; i ++) {

        }
        axios.post(api.ac_like, { acid: item.acid }).then(res => {
          if(res.data.status == 200){

            console.log(res.data.data);
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      /*每个活动icon点击*/
      iconClick(v){
        switch (v){
          case 0:
            this.show_fixed = true;
            break;
          case 1:
            if(this.show_input) {
              this.show_input = false;
            }else if(!this.show_input) {
              this.comment = "";
              this.show_input = true;
            }
            break;
        }
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
      // 点赞
      likeThis(item, index) {
        axios.post(api.ac_like + '?token=' + localStorage.getItem('token'), {
          acid: item.acid
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
        })
      },
      // 添加评论
      commentDone(item, index) {
        if(this.comment == "") {
          Toast({ message: "请填写评论内容", className: 'm-toast-warning' });
        }else if(!this.comment == "") {
          axios.post(api.add_comment + '?token=' + localStorage.getItem('token'), {
            acid: item.acid, ACtext: this.comment
          }).then(res => {
            if(res.data.status == 200){
              this.show_input = false;
              this.activity_list[index].comment.splice(0, 0, { user: { usname: "我" }, actext: this.comment });
              Toast({ message: "评论成功", className: 'm-toast-success' });
            }else{
              Toast({ message: "评论失败", className: 'm-toast-fail' });
            }
          })
        }
      }
    },
    mounted() {
      this.getActivity();
      // this.getCommentList();
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/discover";
</style>
