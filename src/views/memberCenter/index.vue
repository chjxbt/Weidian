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
  export default {
    name: "index",
    data(){
      return{
        show_modal: false
      }
    },
    methods: {
      // 从会员页跳转至支页面
      toPage(page) {
        this.$router.push(page);
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

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
