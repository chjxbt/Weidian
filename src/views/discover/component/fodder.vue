<template>
  <div class="m-discover-fodder">
    <span class="m-filtrate-box" v-for="(item, index) in filtrateList">
      <span class="m-filtrate" :class="index == filtrateActivity?'active':''" @click="changefiltrateActivity(item, index)">{{item.tnname}}</span>
    </span>
    <div class="m-discover-fodder-content">
      <div class="m-section-one" v-for="item in activity_list">
        <img :src="item.suuser.suheader" class="m-section-img"/>
        <div class="m-section-content">
          <div class="m-section-title">
            <span class="m-title">{{item.suuser.suname}}</span>
          </div>
          <p class="m-fodder-time">{{item.accreatetime}} 发布</p>
          <div class="m-section-text">
            <p>7月9日上午9:00开播99款，本次活动2天。</p>
            <ul class="m-img-list">
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
            </ul>
            <div class="m-section-bottom">
              <div>
                <div>805人已发圈</div>
              </div>
              <div>
                <icon-list :list="icon_list" @iconClick="iconClick"></icon-list>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <share v-if="show_fixed"  @fixedClick="fixedClick"></share>
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
          filtrateList: [],
          activity_list:[]
        }
      },
      props:{
        tnid: { type: String, default: null }
      },
      components: { 'icon-list':iconList, share },
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
          axios.get(api.get_all_activity, {
            params: { lasting: false, start: start, count: count, tnid: tnid }}).then(res => {
            if(res.data.status == 200){
              this.activity_list = res.data.data;

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

                if(time1 != createTime1) {
                  let createTime3 = createTime.slice(0, 4) + "-" + createTime.slice(4, 6) + "-" + createTime.slice(6, 8) + " "
                    + createTime.slice(8, 10) + ":" + createTime.slice(10, 12) + ":" + createTime.slice(12, 14);
                  this.activity_list[i].accreatetime = createTime3;
                }else if(time1 == createTime1) {

                }

              }

              // console.log(this.activity_list[0]);
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 获取上部导航
        getTopnav() {
          axios.get(api.get_dp_topnav).then(res => {
            if(res.data.status == 200) {
              this.filtrateList = res.data.data[1].sub;
              // console.log(this.filtrateList);
              this.getActivity(0, 15, this.filtrateList[0].tnid);
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          });

        },
        // 改变第二行导航
        changefiltrateActivity(item, index) {
          this.filtrateActivity = index;
          this.getActivity(0, 15, item.tnid);
        }
      },
      mounted() {
        this.getTopnav();
      }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/discover";

</style>
