<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <div class="time-outside" style="margin-top: 0.2rem">
        <div class="time-text">时间段：</div>
        <div class="time-box">
          <el-date-picker v-model="time" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
        </div>
        <div class="outside-btn">下载报表</div>
      </div>

      <div class="content-row">
        <div class="content-box width-25">
          <div class="box-row-a title-text row-2-1">优惠券发放数量</div>
          <div class="box-row-b hex-text row-2-2">29</div>
        </div>
        <div class="content-box width-25">
          <div class="box-row-a title-text row-2-1">优惠券领取数量</div>
          <div class="box-row-b hex-text row-2-2">12</div>
        </div>
        <div class="content-box width-25">
          <div class="box-row-a title-text row-2-1">优惠券使用总量</div>
          <div class="box-row-b hex-text row-2-2">80</div>
        </div>
        <div class="content-box width-25">
          <div class="box-row-a title-text row-2-1">优惠券使用总金额</div>
          <div class="box-row-b hex-text row-2-2">80</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    data() {
      return {
        name: '优惠券概况',
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: true }
        ],
        time: "",                // 时间段
      }
    },
    components:{ pageTitle },
    methods: {

    },
    mounted() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/data.less";

</style>
