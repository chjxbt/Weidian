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
          <p class="m-ft-30">{{item.actext}}</p>
          <img :src="item.media[0].amimage" class="m-img-l">
          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>{{item.acbrowsenum}}</span>
                <span class="m-smile-icon" :class="item.alreadylike?'active':''" @click="likeThis(item, index)"></span>
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
              <p><span class="m-comment-name">A玲珑服饰有限责任公司</span> : 感谢平台31个省市去均有店铺的
                库存</p>
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
        show_modal: false,
        activity_list: [
          {
            "acbrowsenum": 0,
            "accreatetime": "20180829142337",
            "acendtime": "20180905142337",
            "acid": "1095e152-ab54-11e8-8746-0cd292f93404",
            "acisended": false,
            "acistop": false,
            "acstarttime": "20180829142337",
            "actext": "速度来抢呀, 哈哈呀",
            "actype": "满赠",
            "alreadylike": false,
            "foward": 0,
            "likenum": 1,
            "media": [
              {
                "amid": "1095e153-ab54-11e8-8746-0cd292f93404",
                "amimage": "http://i1.ygimg.cn/pics/annzo/2010/99962601/99962601_03_b.jpg?94"
              }
            ],
            "prid": "343ff445-c02d-4065-8f01-58608171aadc",
            "product": {
              "prchannelid": null,
              "prchannelname": null,
              "prid": "343ff445-c02d-4065-8f01-58608171aadc",
              "primporturl": "http://primporturl.com",
              "prishot": false,
              "prkeeperprice": "181.98",
              "prmainpic": "http://mainpi2.com",
              "prname": "这是商品名字2",
              "proldprice": 499,
              "prprice": "202.20",
              "prsavemonty": "20.22",
              "prstock": 321321,
              "prtitle": "这是商品的标题2",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559"
            },
            "remaintime": [
              5,
              22,
              0
            ],
            "soldnum": 0,
            "suuser": {
              "suheader": "http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559",
              "suname": "这是用户名称"
            },
            "tags": [
              {
                "atid": "1095e154-ab54-11e8-8746-0cd292f93404",
                "atname": "爆款"
              }
            ],
            "topnavid": "5ed4e908-a6db-11e8-b2ff-0cd292f93404"
          },
          {
            "acbrowsenum": 0,
            "accreatetime": "20180829142337",
            "acendtime": "20180905142337",
            "acid": "1095e152-ab54-11e8-8746-0cd292f93404",
            "acisended": false,
            "acistop": false,
            "acstarttime": "20180829142337",
            "actext": "速度来抢呀, 哈哈呀",
            "actype": "满赠",
            "alreadylike": false,
            "foward": 0,
            "likenum": 1,
            "media": [
              {
                "amid": "1095e153-ab54-11e8-8746-0cd292f93404",
                "amimage": "http://i1.ygimg.cn/pics/annzo/2010/99962601/99962601_03_b.jpg?94"
              }
            ],
            "prid": "343ff445-c02d-4065-8f01-58608171aadc",
            "product": {
              "prchannelid": null,
              "prchannelname": null,
              "prid": "343ff445-c02d-4065-8f01-58608171aadc",
              "primporturl": "http://primporturl.com",
              "prishot": false,
              "prkeeperprice": "181.98",
              "prmainpic": "http://mainpi2.com",
              "prname": "这是商品名字2",
              "proldprice": 499,
              "prprice": "202.20",
              "prsavemonty": "20.22",
              "prstock": 321321,
              "prtitle": "这是商品的标题2",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559"
            },
            "remaintime": [
              5,
              22,
              0
            ],
            "soldnum": 0,
            "suuser": {
              "suheader": "http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559",
              "suname": "这是用户名称"
            },
            "tags": [
              {
                "atid": "1095e154-ab54-11e8-8746-0cd292f93404",
                "atname": "爆款"
              }
            ],
            "topnavid": "5ed4e908-a6db-11e8-b2ff-0cd292f93404"
          },
          {
            "acbrowsenum": 0,
            "accreatetime": "20180829142337",
            "acendtime": "20180905142337",
            "acid": "1095e152-ab54-11e8-8746-0cd292f93404",
            "acisended": false,
            "acistop": false,
            "acstarttime": "20180829142337",
            "actext": "速度来抢呀, 哈哈呀",
            "actype": "满赠",
            "alreadylike": false,
            "foward": 0,
            "likenum": 1,
            "media": [
              {
                "amid": "1095e153-ab54-11e8-8746-0cd292f93404",
                "amimage": "http://i1.ygimg.cn/pics/annzo/2010/99962601/99962601_03_b.jpg?94"
              }
            ],
            "prid": "343ff445-c02d-4065-8f01-58608171aadc",
            "product": {
              "prchannelid": null,
              "prchannelname": null,
              "prid": "343ff445-c02d-4065-8f01-58608171aadc",
              "primporturl": "http://primporturl.com",
              "prishot": false,
              "prkeeperprice": "181.98",
              "prmainpic": "http://mainpi2.com",
              "prname": "这是商品名字2",
              "proldprice": 499,
              "prprice": "202.20",
              "prsavemonty": "20.22",
              "prstock": 321321,
              "prtitle": "这是商品的标题2",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559"
            },
            "remaintime": [
              5,
              22,
              0
            ],
            "soldnum": 0,
            "suuser": {
              "suheader": "http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559",
              "suname": "这是用户名称"
            },
            "tags": [
              {
                "atid": "1095e154-ab54-11e8-8746-0cd292f93404",
                "atname": "爆款"
              }
            ],
            "topnavid": "5ed4e908-a6db-11e8-b2ff-0cd292f93404"
          },
          {
            "acbrowsenum": 0,
            "accreatetime": "20180829142337",
            "acendtime": "20180905142337",
            "acid": "1095e152-ab54-11e8-8746-0cd292f93404",
            "acisended": false,
            "acistop": false,
            "acstarttime": "20180829142337",
            "actext": "速度来抢呀, 哈哈呀",
            "actype": "满赠",
            "alreadylike": false,
            "foward": 0,
            "likenum": 1,
            "media": [
              {
                "amid": "1095e153-ab54-11e8-8746-0cd292f93404",
                "amimage": "http://i1.ygimg.cn/pics/annzo/2010/99962601/99962601_03_b.jpg?94"
              }
            ],
            "prid": "343ff445-c02d-4065-8f01-58608171aadc",
            "product": {
              "prchannelid": null,
              "prchannelname": null,
              "prid": "343ff445-c02d-4065-8f01-58608171aadc",
              "primporturl": "http://primporturl.com",
              "prishot": false,
              "prkeeperprice": "181.98",
              "prmainpic": "http://mainpi2.com",
              "prname": "这是商品名字2",
              "proldprice": 499,
              "prprice": "202.20",
              "prsavemonty": "20.22",
              "prstock": 321321,
              "prtitle": "这是商品的标题2",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559"
            },
            "remaintime": [
              5,
              22,
              0
            ],
            "soldnum": 0,
            "suuser": {
              "suheader": "http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg",
              "suid": "632303b0-d81c-42bf-a6b9-ca06ee18c559",
              "suname": "这是用户名称"
            },
            "tags": [
              {
                "atid": "1095e154-ab54-11e8-8746-0cd292f93404",
                "atname": "爆款"
              }
            ],
            "topnavid": "5ed4e908-a6db-11e8-b2ff-0cd292f93404"
          }
        ]
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
            // this.activity_list = res.data.data;
            console.log(this.activity_list);

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
              // this.activity_list[i].actext.length > 90 && (this.activity_list[i].show_text = true);
            }
          }else{
            Toast({ message: res.data.message, className: 'm-toast-fail' });
          }
        })
      },
      /*每个活动icon点击*/
      iconClick(v){
        console.log(v)
        switch (v){
          case 0:
            this.show_fixed = true;
            break;
          case 1:
            // this.show_modal = true;
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
              this.activity_list[index].relikenum -= 1;
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
              this.activity_list[index].relikenum += 1;
              this.activity_list[index].alreadylike = true;
              Toast({ message: res.data.message, className: 'm-toast-success' });
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        }
      },
    },
    mounted() {
      this.getActivity();
      // console.log(this.tnid);
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/discover";
</style>
