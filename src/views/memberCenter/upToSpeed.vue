<template>
  <div>
    <div class="detail-prompt">
      <p class="detail-prompt-text">7天成长值TOP10榜单：</p>
      <p class="detail-prompt-text"><span class="m-blue">花海、十里桃花、七天七夜... </span>这十位在近一周成长速度</p>
      <p class="detail-prompt-text">最快，快去给予鼓励吧！</p>
    </div>
    <div class="warm-prompt m-ft-20 m-bg-main-color">温馨提示：适当的沟通鼓励帮助会员成长，可获得更多收益贡献哦！</div>
    <different-days></different-days>


    <div class="detail-table">
      <div class="detail-table-header">
        <div class="detail-th-one detail-th-text">微信名</div>
        <div class="detail-th">
          <span class="detail-th-text">销售额</span>
        </div>
        <div class="detail-th">
          <span class="detail-th-text">直收人数</span>
        </div>
        <div class="detail-th">
          <span class="detail-th-text">社群人数</span>
        </div>
        <div class="detail-th">
          <span class="detail-th-text">成长值</span>
        </div>
      </div>
      <div class="detail-table-box">
        <div class="detail-table-row" v-for="(item, index) in trList" :class="index == 0?'active':'' || index == 1?'active1':''  || index == 2?'active2':'' ">
          <img class="tr-img" :src="item.src">
          <div class="tr-name" :class="index == 0 || index == 1 || index == 2?'active':''">{{item.name}}</div>
          <div class="detail-tr">
            <span class="detail-tr-num" :class="index == 0 || index == 1 || index == 2?'active':''">{{item.sales}}</span>
          </div>
          <div class="detail-tr">
            <span class="detail-tr-num" :class="index == 0 || index == 1 || index == 2?'active':''">{{item.one}}</span>
          </div>
          <div class="detail-tr">
            <span class="detail-tr-num" :class="index == 0 || index == 1 || index == 2?'active':''">{{item.two}}</span>
          </div>
          <div class="detail-tr">
            <span class="detail-tr-num" :class="index == 0 || index == 1 || index == 2?'active':''">{{item.three}}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import differentDays from "../memberCenter/components/differentDays";
  export default {
    name: "upToSpeed",
    data(){
      return{
      trList: [
          { src: "/static/images/product1.png", name: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
          { src: "/static/images/product1.png", name: "xxx", sales: "500", one: "600", two: "700", three: "800" },
        ]
      }
    },
    components: { differentDays },
    methods: {

    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .detail-prompt {
    margin: 45px 0 45px 12%;
    .detail-prompt-text {
      font-size: 20px;
      text-align: left;
      color: @mainColor;
    }
  }
  .warm-prompt {
    padding: 16px 0;
    margin-bottom: 20px;
    white-space: nowrap;
    background-color: @mainColor;
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
        font-size: 26px;
        color: @greyColor;
      }
      .detail-th-num {
        font-size: 18px;
        color: @mainColor;
        margin-top: 6px;
      }
      .detail-th-one {
        width: 32%;
        text-align: center;
        white-space: nowrap;
      }
      .detail-th {
        width: 17%;
        text-align: center;
        white-space: nowrap;
      }
    }
    .detail-table-box {
      background-color: #f2f5f7;
      padding-top: 15px;
      .detail-table-row {
        width: 100%;
        display: flex;
        padding: 16px 0;
        line-height: 70px;
        border-bottom: 2px #DBDEDF solid;
        &.active {
          border-radius: 20px;
          background-color: #ffe0e0;
          box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.15);
        }
        &.active1 {
          margin-top: 15px;
          border-radius: 20px;
          background-color: #fff2f2;
          box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.15);
        }
        &.active2 {
          margin-top: 15px;
          border-radius: 20px;
          background-color: @bgMainColor;
          box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.15);
        }
        .tr-img {
          width: 70px;
          height: 70px;
          margin-left: 30px;
          border-radius: 50%;
        }
        .tr-name {
          width: 14%;
          margin: 0 20px;
          font-size: 28px;
          text-align: left;
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
          width: 17%;
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
  }
</style>
