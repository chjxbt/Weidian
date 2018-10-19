<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <w-tab :list="tab_list"  @wTabClick="wTabClick"></w-tab>
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
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: false },
          { name: "转化概况", url: "conversion", active: true },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        tab_list: [               // 顶部导航的list
          { id: "", name: "店主数据", active: true },
          { id: "", name: "非店主数据", active: false }
        ],
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

</style>
