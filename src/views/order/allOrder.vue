<template>
  <div class="m-weidians">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-contents">
      <div class="search-box">
        <div class="search-group">
          <div class="group-title">订单编号：</div>
          <el-input class="group-content search-input" v-model="orderNo" size="mini" clearable></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">物流单号：</div>
          <el-input class="group-content search-input" v-model="logisticsNo" size="mini" clearable></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">下单时间：</div>
          <el-date-picker v-model="orderTime" type="daterange" start-placeholder="开始日期" range-separator="至"
                          end-placeholder="结束日期" style="width: 2.5rem;" size="mini">
          </el-date-picker>
        </div>
        <div class="search-group">
          <div class="group-title">收货电话：</div>
          <el-input class="group-content search-input" v-model="buyerTel" size="mini" clearable></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">退回单号：</div>
          <el-input class="group-content search-input" v-model="returnNo" size="mini" clearable></el-input>
        </div>
        <div class="search-btn color-btn">搜 索</div>
      </div>

      <div class="out-btn color-btn">批量导出</div>
      <div class="tab-list">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <div v-for="item in tabList">
            <el-tab-pane :label="item.status" :key="item.status.slice(0, 3)" :name="item.statusnum" :lazy="lazyStatus">
              <order-table ref="orderTable"></order-table>
            </el-tab-pane>
          </div>
        </el-tabs>
      </div>

    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import orderTable from '../../components/common/order-table';
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    data() {
        return {
          name: '所有订单',
          orderNo: "",                  // 订单编号
          orderTime: [],                // 下单时间
          returnNo: "",                 // 退回单号
          logisticsNo: "",              // 物流单号
          buyerTel: "",                 // 收货人电话
          activeName: "0",              // tabs标签默认选中的项
          tabList: [                    // tabs标签的list
            { statusnum: "0", status: "全 部" }, { statusnum: "1", status: "待付款" }, { statusnum: "5", status: "待收货" },
            { statusnum: "6", status: "已完成" }, { statusnum: "11", status: "退换货" }
          ],
          lazyStatus: false,            // 标签是否延迟渲染
        }
    },
    components: { pageTitle, orderTable },
    methods: {
      // 获取获取订单各种状态的预览数
      getOrderCount() {
        axios.get(api.get_order_count + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            // 拼接标签页显示的标题
            for(let i = 0; i < res.data.data.length; i ++) {
              for(let j = 0; j < this.tabList.length; j ++) {
                if(this.tabList[j].statusnum == res.data.data[i].statusnum) {
                  this.tabList[j].status = this.tabList[j].status + "(" + res.data.data[i].count + ")";
                }
              }
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // tab标签页被选中时触发
      handleClick(tab, event) {
        this.$refs.orderTable[tab.index].getOrder(tab.name);
      },

      // 详情按钮
      detailClick(){

      },

      // 退款按钮
      returnClick(){

      },
    },
    mounted() {
      this.getOrderCount();         // 获取获取订单各种状态的预览数
      this.$refs.orderTable[0].getOrder(0);
    }
  }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/weidian";

  .m-weidians {
    background-color: #fff;
    .m-weidian-contents {
      padding: 0.25rem 0.3rem;
      .search-box {
        display: flex;
        flex-wrap: wrap;
        margin-top: -0.1rem;
        background-color: #f7f7f7;
        padding: 0.1rem 0.2rem;
        border-radius: 0.1rem;
        .search-group {
          display: flex;
          margin: 0.1rem 0.5rem 0 0;
          .group-title {
            font-size: 0.12rem;
            line-height: 0.2rem;
          }
          .group-content {

          }
          .search-input {
            width: 2rem;
          }
        }
        .search-btn {
          width: 0.33rem;
          height: 0.18rem;
          line-height: 0.18rem;
        }
      }
    }
  }
  .out-btn {
    width: 0.5rem;
    height: 0.2rem;
    line-height: 0.2rem;
    position: absolute;
    top: 2.25rem;
    right: 1rem;
  }
  .color-btn {
    font-size: 0.12rem;
    white-space: nowrap;
    align-items: center;
    text-align: center;
    padding: 0.03rem 0.15rem;
    border-radius: 0.1rem;
    margin: 0.15rem 0 0 2.4rem;
    color: #ffffff;
    background-color: #9fd0bf;
  }
  .tab-list {
    margin-top: 0.2rem;
  }
</style>
