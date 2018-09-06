<template>
  <div>
    <div class="member-info">
      <div class="member-rule m-ft-30 tr">规 则</div>
      <div class="member-info-bottom">
        <div class="member-info-left">
          <img class="member-info-img" src="/static/images/product1.png">
          <div class="member-info-name m-ft-38 m-bg-main-color">微信名</div>
        </div>
        <div class="member-info-right">
          <p class="member-info-text m-ft-30 tl">已超过 58% 的合伙人</p>
          <p class="member-info-text m-ft-26 tl">还差￥3650元获得额外奖励</p>
        </div>
        <div class="member-info-question m-ft-24 m-bg-main-color" @click="show_modal = true">？</div>
      </div>
    </div>

    <div class="m-modal" v-if="show_modal">
      <div class="m-modal-state">
        <div class="modal-close m-ft-30 m-grey tr" @click="closeModal">X</div>
        <div class="m-modal-head">
          <navbar :list="nav_list" @navClick="navClick"></navbar>
        </div>
        <div class="m-modal-content" v-for="item in weekList">
          <div class="list-row-one m-ft-20 m-grey-color tl">{{item.time}}</div>
          <div class="list-row-two">
            <span class="list-row-text m-ft-26 m-red">￥{{item.money}}</span>
            <span class="list-row-text m-ft-22 m-red">返佣{{item.percentage}}%</span>
            <span class="list-row-text m-ft-22 m-red">{{item.date}}</span>
          </div>
          <div class="list-row-three">
            <span class="list-row-text m-ft-20 m-grey-color">销售额</span>
            <span class="list-row-text m-ft-20 m-grey-color">销售额达到2千</span>
            <span class="list-row-text m-ft-20 m-grey-color">发奖日期</span>
          </div>
        </div>
        <div class="modal-foot">
          <div class="foot-text m-ft-24 m-black tl">奖励规则</div>
          <div class="m-ft-22 m-grey-color">本活动最终所有权贵本平台所有。</div>
        </div>
      </div>
    </div>

    <div class="member-info-bottoms">
      <div class="member-detail">
        <div class="member-detail-top" @click="toPage('memberDetail')">
          <img class="member-detail-img" src="/static/images/product1.png">
          <div class="member-detail-title m-ft-30 m-black m-ft-b tl">会员详情</div>
          <div class="member-detail-to m-ft-22 m-grey">查看明细</div>
          <img class="member-detail-img-to" src="/static/images/icon-list-right.png">
        </div>
        <div class="member-detail-bottom">
          <ul class="m-part-list">
            <li>
              <span>会员总人数</span>
              <span class="m-red m-num">20</span>
            </li>
            <div class="line"></div>
            <li>
              <span>昨日增加</span>
              <span class="m-red m-num">2</span>
            </li>
            <div class="line"></div>
            <li>
              <span>会员成单率</span>
              <span class="m-red m-num">30%</span>
            </li>
            <img class="growth-reduce" src="/static/images/num-up.png">
          </ul>
        </div>
      </div>

      <div class="member-detail">
        <div class="member-detail-top" @click="toPage('resultSituation')">
          <img class="member-detail-img" src="/static/images/product1.png">
          <div class="member-detail-title m-ft-30 m-black m-ft-b tl">业绩概况</div>
          <div class="member-detail-to m-ft-22 m-grey">查看明细</div>
          <img class="member-detail-img-to" src="/static/images/icon-list-right.png">
        </div>
        <div class="member-detail-bottom">
          <ul class="m-part-list">
            <li>
              <span>今日赚</span>
              <span class="m-red m-num">2000</span>
            </li>
            <div class="line"></div>
            <li>
              <span>会员销售额</span>
              <span class="m-red m-num">6000.50</span>
            </li>
            <div class="line"></div>
            <li>
              <span>自卖销售额</span>
              <span class="m-red m-num">3000.00</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="member-detail">
        <div class="member-detail-top" @click="toPage('upToSpeed')">
          <img class="member-detail-img" src="/static/images/product1.png">
          <div class="member-detail-title m-ft-30 m-black m-ft-b tl">成长速度</div>
          <div class="member-detail-to m-ft-22 m-grey">查看明细</div>
          <img class="member-detail-img-to" src="/static/images/icon-list-right.png">
        </div>
      </div>

      <div class="member-detail">
        <div class="member-detail-top" @click="toPage('advancedClass')">
          <img class="member-detail-img" src="/static/images/product1.png">
          <div class="member-detail-title m-ft-30 m-black m-ft-b tl">进阶课堂</div>
          <div class="member-detail-to m-ft-22 m-grey">查看明细</div>
          <img class="member-detail-img-to" src="/static/images/icon-list-right.png">
        </div>
      </div>

      <div class="member-detail">
        <div class="member-detail-top" @click="toPage('helpCenter')">
          <img class="member-detail-img" src="/static/images/product1.png">
          <div class="member-detail-title m-ft-30 m-black m-ft-b tl">帮助中心</div>
          <div class="member-detail-to m-ft-22 m-grey">查看明细</div>
          <img class="member-detail-img-to" src="/static/images/icon-list-right.png">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  export default {
    name: "index",
    data(){
      return{
        show_modal: true,
        nav_list: [
          { click: true, tnname: "周周奖" },
          { click: false, tnname: "本月奖励" }
        ],
        weekList: [
          { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
          { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
          { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
          { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" }
        ]
      }
    },
    components: { navbar },
    methods: {
      // 从会员页跳转至支页面
      toPage(page) {
        this.$router.push(page);
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
        // 本月奖励
        if(v == 0) {
          this.weekList = [
            { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
            { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
            { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" },
            { time: "8月01号-8月07号（第1周）", money: "50.00", percentage: "20", date: "8月14日" }
          ];
        }else if(v == 1) {
          this.weekList = [{ time: "", money: "50.00", percentage: "20", date: "8月14日" }];
        }
      },
      // 关闭modal
      closeModal() {
        this.show_modal = false;
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
  @import "../../common/css/modal";

  .m-modal{
    .m-modal-state{
      height: 980px;
      .modal-close {
        margin: 20px;
      }
      .m-modal-head{
        width: 100%;
        display: block;
        margin: -80px 0 0 -20px;
      }
      .m-modal-content{
        padding: 20px 30px;
        border-bottom: 2px #E5E5E5 solid;
        .list-row-one {

        }
        .list-row-two {
          width: 100%;
          display: flex;
          margin: 30px 0 10px 0;
        }
        .list-row-three {
          width: 100%;
          display: flex;
        }
        .list-row-text {
          width: 33%;
        }
      }
      .modal-foot{
        .foot-text {
          margin: 40px 0 20px 30px;
        }
      }
    }
  }
  .member-info {
    width: 750px;
    height: 413px;
    background-image: linear-gradient(to right, #F3629A, #F37865);
    .member-rule {
      color: #fefefe;
      padding: 25px 34px 10px 0;
    }
    .member-info-bottom {
      display: flex;
      margin-left: 80px;
      .member-info-left {
        .member-info-img {
          width: 138px;
          height: 138px;
          border-radius: 50%;
        }
        .member-info-name {
          margin-top: 26px;
          letter-spacing: 3.8px;
        }
      }
      .member-info-right {
        .member-info-text {
          color: #f1f1f1;
          margin: 92px 0 -60px 57px;
          letter-spacing: 3px;
        }
      }
      .member-info-question {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        margin: 165px 0 0 20px;
        background-color: @blue;
      }
    }
  }
  .member-info-bottoms {
    position: absolute;
    top: 320px;
    .member-detail {
      width: 690px;
      margin: 0 30px 30px 30px;
      border-radius: 20px;
      background-color: @bgMainColor;
      box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.15);
      .member-detail-top {
        display: flex;
        .member-detail-img {
          width: 60px;
          height: 60px;
          margin: 24px 30px;
        }
        .member-detail-title {
          flex: 1;
          margin-top: 30px;
        }
        .member-detail-to {
          margin-top: 33px;
        }
        .member-detail-img-to {
          width: 30px;
          height: 30px;
          margin: 35px 20px 0 10px;
        }
      }
      .member-detail-bottom {
        .m-part-list{
          .flex-row(space-around);
          padding: 20px 0 35px 0;
          li{
            .flex-col(center);
            letter-spacing: 2.2px;
            .m-num{
              font-size: 36px;
              margin-top: 30px;
              font-weight: bold;
              letter-spacing: 3.2px;
            }
          }
          .line {
            width: 2px;
            height: 80px;
            opacity: 0.15;
            background-color: @grey;
            margin: 0 -120px;
          }
          .growth-reduce {
            width: 20px;
            height: 30px;
            margin: -70px 0 0 -150px;
          }
        }
      }
    }
  }
</style>
