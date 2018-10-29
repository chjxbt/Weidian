<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <div>
        <div class="time-outside" style="margin-top: 0.2rem">
          <div class="time-text">时间段：</div>
          <div class="time-box">
            <el-date-picker v-model="time" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
          </div>
          <div class="outside-btn">下载报表</div>
        </div>

        <div class="black-title">首页上半部分</div>
        <div class="table-box">
          <el-table :data="userList" border style="width: 100%" v-loading="userLoading">
            <el-table-column prop="cotype" label="平台商品佣金支出"></el-table-column>
            <el-table-column prop="cotype" label="邀请开店支出"></el-table-column>
            <el-table-column prop="cotype" label="周周奖"></el-table-column>
            <el-table-column prop="cotype" label="周周奖"></el-table-column>
            <el-table-column prop="cotype" label="额外奖励"></el-table-column>
            <el-table-column prop="cotype" label="专粉佣金支出"></el-table-column>
            <el-table-column prop="cotype" label="新店主任务佣金支出"></el-table-column>
          </el-table>
        </div>
      </div>

      <div>
        <div class="time-outside" style="margin-top: 0.2rem">
          <div class="time-text">时间段：</div>
          <div class="time-box">
            <el-date-picker v-model="time_input" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
          </div>
          <div class="search-input">
            <el-input v-model="userName" placeholder="用户名" style="width: 2rem"></el-input>
          </div>
          <div class="search-input">
            <el-input v-model="userTel" placeholder="用户手机号" style="width: 2rem"></el-input>
          </div>
          <div class="outside-btn">下载报表</div>
        </div>

        <div class="black-title">店主数据展示</div>
        <div class="table-box">
          <el-table :data="userList" border style="width: 100%" v-loading="userLoading">
            <el-table-column prop="cotype" label="用户名"></el-table-column>
            <el-table-column prop="cotype" label="手机号"></el-table-column>
            <el-table-column prop="cotype" label="专粉佣金"></el-table-column>
            <el-table-column prop="cotype" label="开店佣金"></el-table-column>
            <el-table-column prop="cotype" label="新店主任务奖励佣金"></el-table-column>
            <el-table-column prop="cotype" label="商品销售佣金"></el-table-column>
          </el-table>
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
        name: '佣金概况',
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: true },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        time: "",                // 时间段
        time_input: "",          // 时间段
        userName: "",            // 用户名
        userTel: "",             // 用户手机号
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
