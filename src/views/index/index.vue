<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <w-tab :list="tab_list"  @wTabClick="wTabClick"></w-tab>

      <div class="time-outside">
        <div class="time-text">时间段：</div>
        <div class="time-box">
          <el-date-picker v-model="time" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
        </div>
        <div class="outside-btn">下载报表</div>
      </div>

      <div>
        <div class="content-row">
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">全部订单（笔）</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">支付订单数（笔）</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">支付转化率（%）</div>
            <div class="box-row-b hex-text row-2-2">80%</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">客单价（用券后）（元）</div>
            <div class="box-row-b hex-text row-2-2">￥12.00元</div>
          </div>
        </div>

        <div class="content-row">
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">平台总UV</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">平台总支付UV</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">平台总新增一级店主（人）</div>
            <div class="box-row-b hex-text row-2-2">56</div>
          </div>
        </div>

        <div class="content-row">
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">平台支出总额（元）</div>
            <div class="box-row-b hex-text row-2-2">2956</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">活动奖励支出总额（元）</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    data() {
      return {
        name: '首页',
        list: [                   // 标题list
          { name: "首页", url: "index", active: true },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        tab_list: [               // 顶部导航的list
          { id: "", name: "平台总GMV", active: true },
          { id: "", name: "24h数据", active: false }
        ],
        time: "",                 // 时间段
      }
    },
    components:{ pageTitle, wTab },
    methods: {
      // 顶部导航的点击事件
      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a = 0; a < arr.length; a ++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list = [].concat(arr);
      },
    },
    mounted() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/data.less";
  @import "../../common/css/weidian.less";

</style>
