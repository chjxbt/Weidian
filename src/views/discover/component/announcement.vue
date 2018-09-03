<template>
  <div class="m-discover-announcement">
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
          <p><span class="m-mark">置顶</span>{{item.actype}}</p>

          <p class="textP m-ft-30" :class="!item.show_text ? 'active':''">{{item.actext}}</p>
          <span class="m-section-more" v-if="item.show_text" @click="showMore(false, index)">展开全文</span>
          <span class="m-section-more" v-if="item.actext.length > 86 && !item.show_text" @click="showMore(true, index)">收起全文</span>

          <div class="m-img-list">
            <img class="m-section-text-img" :src="item.media[0].amimage">
          </div>
          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>{{item.acbrowsenum}}</span>
                <span class="m-good-icon" :class="item.alreadylike?'active':''" @click="likeThis(item, index)"></span>
                <span>{{item.likenum}}</span>
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
                <span class="m-comment-name">{{comment.actext}}</span>: {{comment.actext}}
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
    <share v-if="show_fixed" :num="2" @fixedClick="fixedClick"></share>
  </div>
</template>

<script type="text/ecmascript-6">
  import iconList from'../../../components/common/iconList';
  import share from '../../../components/common/share';
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';

  export default {
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
      }
    },
    props:{
      tnid: { type: String, default: null }
    },
    components: { iconList, share },
    methods: {
      /*获取活动列表*/
      getActivity(start, count, tnid){
        axios.get(api.get_all_activity, {
          params: { start: 0, count: 15, tnid: this.tnid }}).then(res => {
          if(res.data.status == 200){
            this.activity_list = res.data.data;
            // console.log(this.activity_list);

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

              // 展开全文、显示全文
              this.activity_list[i].actext.length > 90 && (this.activity_list[i].show_text = true);

              console.log(this.activity_list[i].comment);
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
      // 点赞
      likeThis(item, index) {
        if(item.alreadylike) {
          axios.post(api.ac_like + '?token=' +  localStorage.getItem('token'), {
            acid: item.acid
          }).then(res => {
            if(res.data.status == 200){
              this.activity_list[index].likenum -= 1;
              this.activity_list[index].alreadylike = false;
              Toast({ message: res.data.message, className: 'm-toast-warning' });
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        }else if(!item.alreadylike) {
          axios.post(api.ac_like + '?token=' +  localStorage.getItem('token'), {
            acid: item.acid
          }).then(res => {
            if(res.data.status == 200){
              this.activity_list[index].likenum += 1;
              this.activity_list[index].alreadylike = true;
              Toast({ message: res.data.message, className: 'm-toast-success' });
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        }
      },
      // 添加评论
      commentDone(item, index) {
        axios.post(api.add_comment + '?token=' +  localStorage.getItem('token'), {
          acid: item.acid, ACtext: this.comment
        }).then(res => {
          if(res.data.status == 200){
            this.show_input = false;
            this.activity_list[index].comment.splice(0, 0, {usname: "我", actext: this.comment});
            Toast({ message: "评论成功", className: 'm-toast-success' });
          }else{
            Toast({ message: "评论失败", className: 'm-toast-fail' });
          }
        })
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
