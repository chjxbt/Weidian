<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <div class="time-outside">
        <div class="time-text">时间段：</div>
        <div class="time-box">
          <el-date-picker v-model="time" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
        </div>
        <div class="outside-btn">下载报表</div>
      </div>

      <div class="content-row">
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">平台销售总GMV</div>
          <div class="box-row-b hex-text">29</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">526.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">除优惠券平台销售总GMV</div>
          <div class="box-row-b hex-text">12</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">邀请开店GMV</div>
          <div class="box-row-b hex-text">80</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">商品销售GMV</div>
          <div class="box-row-b hex-text">20</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">专粉GMV</div>
          <div class="box-row-b hex-text">50</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
      </div>

      <div class="content-row">
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">总订单数（笔）</div>
          <div class="box-row-b hex-text">29</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">526.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">支付订单数（笔）</div>
          <div class="box-row-b hex-text">12</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">支付件数（件）</div>
          <div class="box-row-b hex-text">80</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">支付子订单数（笔）</div>
          <div class="box-row-b hex-text">20</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">投诉订单数（笔）</div>
          <div class="box-row-b hex-text">50</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
      </div>

      <div class="content-row">
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">退货订单数（笔）</div>
          <div class="box-row-b hex-text">29</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">526.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">快速投诉通道订单数（笔）</div>
          <div class="box-row-b hex-text">12</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">客单价（用券前）</div>
          <div class="box-row-b hex-text">80</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">客单价（用券后）</div>
          <div class="box-row-b hex-text">20</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">-5.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
        </div>
      </div>

      <div class="content-row">
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">支付UV</div>
          <div class="box-row-b hex-text">29</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">1.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">526.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
        </div>
        <div class="content-box width-20 row-4">
          <div class="box-row-a title-text">支付老客UV</div>
          <div class="box-row-b hex-text">12</div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较前一日</div>
            <div class="cow-b">-1.00%</div>
            <img class="cow-c" :src="img(-5.00)">
          </div>
          <div class="box-row-c grey-text">
            <div class="cow-a">较上周同期</div>
            <div class="cow-b">5.00%</div>
            <img class="cow-c" :src="img(5.00)">
          </div>
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
        name: '交易概况',
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: true },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        time: "",                 // 时间段
      }
    },
    components:{ pageTitle },
    methods: {
      // 判断数据增减图标
      img(num) {
        if(num < 0){
          return "/static/icon_down.png";
        }else if(num == 0){
          return "/static/icon_zero.png";
        }else if(num > 0){
          return "/static/icon_up.png";
        }
      }
    },
    mounted() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/data.less";

</style>
