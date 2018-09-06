<template>
  <div>
    <!--<div class="m-detail-navs">
      <ul class="m-detail-nav">
        <li>
          全部(158人)
        </li>
        <li>
          已开单(68人)
        </li>
        <li>
          未开单(90人)
        </li>
      </ul>
    </div>-->
    <navbar :list="nav_list" @navClick="navClick"></navbar>
    <div class="detail-prompt">
      <p class="detail-prompt-text">今日提示：</p>
      <p class="detail-prompt-text">你今日需要培训56人，分别是金金、小婷。。。。。</p>
      <p class="detail-prompt-text">等姓名颜色标红者。</p>
      <p class="detail-prompt-text">理由：累计订单超过20笔，持续上升幅度较高。</p>
    </div>
    <different-days></different-days>

    <div class="detail-table">
      <div class="detail-table-header">
        <div class="detail-th detail-th-text">微信名</div>
        <div class="detail-th">
          <span class="detail-th-text">订单量</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
          <span class="detail-th-num">3%</span>
        </div>
        <div class="detail-th">
          <span class="detail-th-text">转发量</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
          <span class="detail-th-num">3%</span>
        </div>
        <div class="detail-th">
          <span class="detail-th-text">直收人数</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
          <span class="detail-th-num">3%</span>
        </div>
      </div>
      <div class="detail-table-row" v-for="(item, index) in trList">
        <img class="tr-img" :src="item.src">
        <div class="tr-name" :class="index == 0?'active':''">{{item.name}}</div>
        <div class="detail-tr">
          <span class="detail-tr-num" :class="index == 0?'active':''">20</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
        </div>
        <div class="detail-tr">
          <span class="detail-tr-num" :class="index == 0?'active':''">500</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
        </div>
        <div class="detail-tr">
          <span class="detail-tr-num" :class="index == 0?'active':''">6</span>
          <img class="growth-reduce-img" src="/static/images/icon-list-right.png"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  import differentDays from "../memberCenter/components/differentDays";

  export default {
    name: "memberDetail",
    data(){
      return{
        nav_list: [
          { click: true, tnname: "全部(158人)" },
          { click: false, tnname: "已开单(68人)" },
          { click: false, tnname: "未开单(90人)" }
        ],
        trList: [
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } },
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } },
          { src: "/static/images/product1.png", name: "xxx", order: { quantity: "200", reduce: true }, forwarding: { quantity: "200", reduce: true }, people: { quantity: "200", reduce: true } }
        ]
      }
    },
    components: { navbar, differentDays },
    methods: {
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .m-detail-navs {
    width: 100%;
    border-bottom:#e3b6c1 2px dashed;
    .m-detail-nav{
      .flex-row(space-around);
      color: #000000;
      font-size: 26px;
      font-weight: 500;
      margin: 35px 40px;
    }
  }
  .detail-prompt {
    margin: 19px 0 40px 15%;
    .detail-prompt-text {
      font-size: 20px;
      text-align: left;
      color: @mainColor;
    }
  }
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
        width: 25%;
        text-align: center;
        white-space: nowrap;
      }
    }
    .detail-table-row {
      width: 100%;
      display: flex;
      line-height: 70px;
      padding: 16px 0;
      border-bottom: 2px #F1F1F1 solid;
      .tr-img {
        width: 70px;
        height: 70px;
        margin-left: 40px;
        border-radius: 50%;
      }
      .tr-name {
        width: 37.5px;
        margin: 0 20px;
        font-size: 28px;
        white-space: nowrap;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 1;
        overflow: hidden;
        &.active{
          color: @mainColor;
        }
      }
      .detail-tr {
        width: 25%;
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
</style>
