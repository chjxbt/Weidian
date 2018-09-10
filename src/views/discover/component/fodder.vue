<template>
  <div class="m-discover-fodder">
    <span class="m-filtrate-box" v-for="(item, index) in sub">
      <span class="m-filtrate" :class="index == filtrateActivity?'active':''" @click="changefiltrateActivity(item, index)">{{item.tnname}}</span>
    </span>
    <div class="m-discover-fodder-content">
      <div class="m-section-one" v-for="(item, index) in activity_list">
        <img :src="item.suuser.suheader" class="m-section-img"/>
        <div class="m-section-content">
          <div class="m-section-title">
            <span class="m-title">{{item.suuser.suname}}</span>
          </div>
          <p class="m-fodder-time">{{item.accreatetime}} 发布</p>
          <div class="m-section-text">
            <p class="textP" :class="!item.show_text ? 'active':''">{{item.actext}}</p>
            <span class="m-section-more" v-if="item.show_text" @click="showMore(false, index)">展开全文</span>
            <span class="m-section-more" v-if="item.actext.length > 86 && !item.show_text" @click="showMore(true, index)">收起全文</span>
            <ul class="m-img-list" id="m-img-list">
              <li>
                <template v-for="img in item.media">
                  <img :src="img.amimage" class="m-section-text-img">
                </template>
              </li>
            </ul>
            <div class="m-section-bottom">
              <div>
                <div>{{item.foward}}</div>
              </div>
              <div>
                <icon-list :list="icon_list" @iconClick="iconClick"></icon-list>
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
  import iconList from '../../../components/common/iconList';
  import share from '../../../components/common/share';
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';

    export default {
      data() {
        return {
          show_fixed:false,
          icon_list:[
            {
              src:'icon-share',
              name:'转发',
              url:'icon-share'
            }
          ],
          filtrateActivity: 0,
          activity_list:[],
          count: 5
        }
      },
      props: {
        tnid: { type: String, default: null },
        sub: { type: Array }
      },
      components: { iconList, share },
      methods: {
        // 转发按钮list
        iconClick(){
            this.show_fixed = true;
        },
        // 分享按钮
        fixedClick(){
          this.show_fixed = false;
        },
        /*获取活动列表*/
        getActivity(start, count, tnid){
          let token = localStorage.getItem('token');
          axios.get(api.get_all_activity + '?token=' + token, {
            params: { lasting: false, start: start || 0, count: count || this.count, tnid: tnid }}).then(res => {
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

                // 展开全文、显示全文
                this.activity_list[i].actext.length > 90 && (this.activity_list[i].show_text = true);

                // 发素材圈的人数，为0时不显示
                if(this.activity_list[i].foward == 0) {
                  this.activity_list[i].foward = "";
                }else {
                  this.activity_list[i].foward = this.activity_list[i].foward + "人已发圈";
                }
              }
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 改变第二行导航
        changefiltrateActivity(item, index) {
          this.filtrateActivity = index;
          this.getActivity(0, this.count, item.tnid);
        },
        // 展开全文、显示全文
        showMore(status, index){
          let arr = [].concat(this.activity_list);
          arr[index] = Object.assign({}, arr[index], { show_text: status });
          this.activity_list = [].concat(arr);
        }
      },
      mounted() {
        this.getActivity(0, this.count, this.sub[0].tnid);
      }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/discover";

</style>
