<template>
  <div>
    <navbar :list="nav_list" @navClick="navClick"></navbar>

    <div class="detail-table" v-if="nav_select == 0 || nav_select == 1">
      <different-days></different-days>
      <div class="detail-table-header">
        <div class="detail-th detail-th-text">微信名</div>
        <div class="detail-th">
          <span class="detail-th-text">销售额</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
          <span class="detail-th-num">3%</span>
        </div>
      </div>
      <div class="detail-table-row" v-for="(item, index) in trList">
        <img class="tr-img" :src="item.src">
        <div class="tr-name" :class="index == 0 || index == 1?'active':''">{{item.name}}</div>
        <div class="detail-tr">
          <span class="detail-tr-num" :class="index == 0 || index == 1?'active':''">9000</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
        </div>
      </div>
    </div>

    <div class="since-selling" v-if="nav_select == 2">
      <div class="since-selling-top">
        <div class="since-selling-bac"></div>
        <div class="top-left">
          <div class="m-ft-30 m-grey-color">预估到账金额</div>
          <div class="m-ft-40 m-red m-ft-b m_t_5">230.00</div>
        </div>
        <div class="top-right">
          <div class="m-ft-30 m-grey-color">已到账金额</div>
          <div class="m-ft-40 m-red m-ft-b m_t_5">230.00</div>
        </div>
        <div class="member-info-bottoms">
          <div class="member-detail">
            <ul class="m-part-list">
              <li>
                <span>今日销售额</span>
                <span class="m-red m-num">1250</span>
              </li>
              <div class="line"></div>
              <li>
                <span>今日赚</span>
                <span class="m-red m-num">900</span>
              </li>
              <div class="line"></div>
              <li>
                <span>额外赚</span>
                <span class="m-red m-num">500</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  import differentDays from "../memberCenter/components/differentDays";

  export default {
    name: "resultSituation",
    data(){
      return{
        nav_list: [
          { click: false, tnname: "店主销售额" },
          { click: false, tnname: "合伙人销售额" },
          { click: true, tnname: "自卖销售额" }
        ],
        trList: [
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } },
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } },
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } }
        ],
        nav_select: 2
      }
    },
    components: { navbar, differentDays },
    methods: {
      // 点击导航栏
      navClick(v){
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
        this.nav_select = v;
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .detail-table {
    .growth-reduce-img {
      width: 17px;
      height: 22px;
    }
    .detail-table-header {
      width: 100%;
      display: flex;
      padding: 30px 0;
      border-bottom: 2px #E5E5E5 solid;
      .detail-th-text {
        font-size: 28px;
        font-weight: 500;
        color: @greyColor;
      }
      .detail-th-num {
        font-size: 18px;
        color: @mainColor;
        margin-top: 6px;
      }
      .detail-th {
        width: 50%;
        text-align: center;
        white-space: nowrap;
      }
    }
    .detail-table-row {
      width: 100%;
      display: flex;
      padding: 16px 0;
      line-height: 70px;
      border-bottom: 2px #F1F1F1 solid;
      .tr-img {
        width: 70px;
        height: 70px;
        margin-left: 110px;
        border-radius: 50%;
      }
      .tr-name {
        width: 26%;
        margin: 0 20px;
        font-size: 28px;
        text-align: left;
        &.active{
          color: @mainColor;
        }
      }
      .detail-tr {
        width: 50%;
        text-align: center;
        white-space: nowrap;
        .detail-tr-num {
          font-size: 28px;
          &.active{
            color: @mainColor;
          }
        }
      }
    }
  }
  .since-selling {
    .since-selling-top {
      .since-selling-bac {
        width: 750px;
        height: 366px;
        background-image: linear-gradient(to right, #F8629A, #F37965);
      }
      .top-left {
        position: fixed;
        top: 100px;
        left: 60px;
        width: 200px;
        padding: 30px 40px;
        border-radius: 20px;
        background-color: @bgMainColor;
      }
      .top-right {
        position: fixed;
        top: 100px;
        right: 60px;
        width: 200px;
        padding: 30px 40px;
        border-radius: 20px;
        background-color: @bgMainColor;
      }
      .member-info-bottoms {
        position: fixed;
        top: 330px;
        .member-detail {
          width: 690px;
          margin: 0 30px 30px 30px;
          border-radius: 20px;
          background-color: @bgMainColor;
          box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.15);
          .m-part-list{
            .flex-row(space-around);
            padding: 40px 0 35px 0;
            li{
              .flex-col(center);
              .m-num{
                font-size: 36px;
                margin-top: 30px;
                font-weight: bold;
              }
            }
            .line {
              width: 2px;
              height: 80px;
              opacity: 0.15;
              background-color: @grey;
              margin: 0 -100px;
            }
          }
        }
      }
    }
  }
</style>
