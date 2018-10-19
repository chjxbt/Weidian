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

      <div class="black-title">会员概况表</div>
      <div class="table-box">
        <el-table :data="userList" border style="width: 100%" v-loading="userLoading">
          <el-table-column prop="cotype" label="新增人数"></el-table-column>
          <el-table-column prop="cotype" label="总会员人数"></el-table-column>
          <el-table-column prop="cotype" label="使用率"></el-table-column>
          <el-table-column prop="cotype" label="推广能力值"></el-table-column>
          <el-table-column prop="cotype" label="销售潜力值"></el-table-column>
        </el-table>
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
        name: '会员概况',
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: true },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        time: "",                // 时间段
        userList: [],            // 会员概况表list
        userLoading: false,      // 会员概况表加载中
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
