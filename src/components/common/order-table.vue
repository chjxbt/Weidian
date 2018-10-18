<template>
  <div class="order-table">
    <el-table :data="orderList" style="width: 100%" class="outside-table" :default-expand-all="expandAll" stripe size="mini"
              v-loading="orderLoading" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="30"></el-table-column>
      <el-table-column type="expand" width="30">
        <template slot-scope="scope">
          <el-table class="inside-table" :data="scope.row.productinfo" border style="width: 100%" size="mini">
            <el-table-column align="center" prop="opiproductimages" label="商品图片" width="100">
              <template slot-scope="scope">
                <img :src="scope.row.opiproductimages" class="product-img">
              </template>
            </el-table-column>
            <el-table-column align="center" prop="opiproductname" label="商品名称"></el-table-column>
            <el-table-column align="center" prop="zh_status" label="订单商品状态" width="100"></el-table-column>
            <el-table-column align="center" prop="PBprice" label="单价"></el-table-column>
            <el-table-column align="center" prop="PRnumber" label="数量"></el-table-column>
            <el-table-column align="center" prop="opilogisticssn" label="物流单号"></el-table-column>
            <el-table-column align="center" prop="logistic_company" label="物流公司"></el-table-column>
            <el-table-column align="center" prop="opilogisticstext" label="物流信息"></el-table-column>
            <el-table-column fixed="right" label="管理" width="150">
              <template slot-scope="scope">
                <el-button type="text" size="small" @click="">详情</el-button>
                <el-button type="text" size="small">|</el-button>
                <el-button type="text" size="small" @click="">退款</el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column align="center" label="订单号" prop="oiid" width="260"></el-table-column>
      <el-table-column align="center" label="订单状态" prop="oipaystatusmsg" width="80"></el-table-column>
      <el-table-column align="center" label="总价" prop="oimount" width="80"></el-table-column>
      <el-table-column align="center" label="下单时间" prop="oicreatetime" width="140"></el-table-column>
      <el-table-column align="center" label="收货人" prop="oirecvname" width="140"></el-table-column>
      <el-table-column align="center" label="收货电话" prop="oirecvphone" width="100"></el-table-column>
      <el-table-column align="center" label="留言内容" prop="oileavetext"></el-table-column>
    </el-table>

    <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
  </div>
</template>

<script>
  // 0: "已取消", 7: "未支付", 14: "支付中", 21: "已支付",28: "已发货", 35: "已收货", 42: "已完成", 49: "已评价", 56: "退款中"
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    props: ["order"],
    name: "all-order-table",
    data() {
      return {
        expandAll: false,       // 表格是否默认展开行
        orderList: [],          // 订单list
        orderLoading: false,    // 订单表格加载中
        page_size: 10,          // 每页请求的数量
        page_num: 1,            // 第几页
        total_page: 1,          // 总页数
        statusnum: "",          // 暂存订单状态
        orderOutList: [],       // 要导出的订单list
      }
    },
    components: { Pagination },
    methods: {
      // 依据订单状态获取订单
      getOrder(statusnum) {
        this.statusnum = statusnum;
        this.orderLoading = true;
        this.orderList = [];
        axios.get(api.get_order_list + "?token=" + localStorage.getItem("token") + "&paystatus=" + statusnum + "&page=" + this.page_num + "&count=" + this.page_size).then(res => {
          if(res.data.status == 200) {
            this.orderList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);

            console.log(this.orderList);
            this.orderLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 详情按钮
      detailClick(){
        this.$emit('detailClick')
      },

      // 退款按钮
      returnClick(){
        this.$emit('returnClick')
      },

      // 表格多选事件
      handleSelectionChange(value) {
        this.orderOutList = value;
      },

      // 分页组件的提示
      pageChange(v){
        this.page_num = v;
        this.getOrder(this.statusnum);      // 依据订单状态获取订单
      }
    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  /*@import "../../common/css/_variate.less";*/

  .order-table {
    .outside-table {
      .inside-table {
        .product-img {
          width: 0.4rem;
          height: 0.4rem;
        }
      }
    }
    .page-box {
      text-align: right;
      margin-top: 0.1rem;
    }
  }
</style>
