<template>
  <div>
    <navbar :list="nav_list" @navClick="navClick"></navbar>
    <different-days></different-days>

    <div class="detail-table">
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
          { click: true, tnname: "店主销售额" },
          { click: false, tnname: "合伙人销售额" },
          { click: false, tnname: "自卖销售额" }
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
</style>
