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

      <div>
        <div class="content-row">
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">收藏转化率</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">收藏点击转化率</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">下单转化率</div>
            <div class="box-row-b hex-text row-2-2">80</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">总支付转化率</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">领了未用转化率</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
        </div>
      </div>

      <div>
        <div class="content-row">
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">领了且用转化率</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">无优惠券转化率</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">下单转化率</div>
            <div class="box-row-b hex-text row-2-2">80</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">彻底完成转化率</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">复购率</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
        </div>
      </div>

      <div>
        <div class="content-row">
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">从收藏夹进入并支付的UV/藏夹整体UV</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">商品被加入收藏夹次数/PV</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">订单数/PV</div>
            <div class="box-row-b hex-text row-2-2">80</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">支付订单数/PV</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">领取优惠券未使用/PV</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
        </div>
      </div>

      <div>
        <div class="content-row">
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">领取优惠券并使用订单数/PV</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">没有优惠券的有效订单数/PV</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-20">
            <div class="box-row-a title-text row-2-1">收货且没有退货换的订单数/当日支付成功订单数</div>
            <div class="box-row-b hex-text row-2-2">80</div>
          </div>
        </div>
      </div>

      <w-tab :list="tab_list"  @wTabClick="wTabClick"></w-tab>

      <div v-if="page == '店主数据' || page == '非店主数据'">
        <div>
          <div class="time-outside" style="margin-top: 0.2rem">
            <div class="time-text">时间段：</div>
            <div class="time-box">
              <el-date-picker v-model="time_table_buy" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
            </div>
            <div class="outside-btn">下载报表</div>
          </div>

          <div class="black-title">复购率报表</div>
          <div class="table-box">
            <el-table :data="buyAgainList" border style="width: 100%" v-loading="buyAgainLoading">
              <el-table-column prop="cotype" label="购买1次用户占比"></el-table-column>
              <el-table-column prop="cotype" label="购买2次用户占比"></el-table-column>
              <el-table-column prop="cotype" label="购买3次用户占比"></el-table-column>
              <el-table-column prop="cotype" label="购买4次以上用户占比"></el-table-column>
              <el-table-column prop="cotype" label="购买1次用户销售额占比"></el-table-column>
              <el-table-column prop="cotype" label="购买2次用户销售额占比"></el-table-column>
              <el-table-column prop="cotype" label="购买3次用户销售额占比"></el-table-column>
              <el-table-column prop="cotype" label="购买3次以上用户销售额占比"></el-table-column>
            </el-table>
          </div>
        </div>

        <div>
          <div class="time-outside" style="margin-top: 0.2rem">
            <div class="time-text">时间段：</div>
            <div class="time-box">
              <el-date-picker v-model="time_table_retention" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
            </div>
            <div class="outside-btn">下载报表</div>
          </div>

          <div class="black-title">留存率报表</div>
          <div class="table-box">
            <el-table :data="retentionList" border style="width: 100%" v-loading="retentionLoading">
              <el-table-column prop="cotype" label="次日"></el-table-column>
              <el-table-column prop="cotype" label="7日"></el-table-column>
              <el-table-column prop="cotype" label="15日"></el-table-column>
              <el-table-column prop="cotype" label="30日"></el-table-column>
              <el-table-column prop="cotype" label="60日"></el-table-column>
              <el-table-column prop="cotype" label="90日"></el-table-column>
            </el-table>
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
        name: '转化概况',
        list: [                       // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: true },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        tab_list: [                   // 顶部导航的list
          { id: "", name: "店主数据", active: true },
          { id: "", name: "非店主数据", active: false }
        ],
        time: "",                     // 时间段
        time_table_buy: "",           // 时间段
        time_table_retention: "",     // 时间段
        page: "店主数据",              // 默认页面
        buyAgainList: [],             // 复购率报表list
        buyAgainLoading: false,       // 复购率报表加载中
        retentionList: [],            // 留存率报表list
        retentionLoading: false,      // 留存率报表加载中
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
        this.page = arr[i].name;
        this.tab_list = [].concat(arr);
      },
    },
    mounted() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/data.less";

</style>
