<template>
  <div class="order-table">
    <el-table :data="orderList" style="width: 100%" class="outside-table" :default-expand-all="expandAll" stripe size="small" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="30"></el-table-column>
      <el-table-column type="expand" width="30">
        <template slot-scope="scope">
          <el-table class="inside-table" :data="scope.row.productinfo" border style="width: 100%" size="small">
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
      <el-table-column align="center" label="收货电话" prop="oirecvphone" width="110"></el-table-column>
      <el-table-column align="center" label="留言内容" prop="oileavetext"></el-table-column>
    </el-table>

    <div class="bottom-box">
      <div class="export-btn" @click="exportClick">批量导出</div>
      <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
    </div>
  </div>
</template>

<script>
  import Pagination from "../../components/common/page";

  export default {
    name: "all-order-table",
    data() {
      return {
        expandAll: false,       // 表格是否默认展开行
        statusnum: "",          // 暂存订单状态
        orderOutList: [],       // 要导出的订单list
      }
    },
    props:{
      orderList:{ type: Array, default: [] },
      total_page:{ type: Number, default: 1 },
    },
    components: { Pagination },
    methods: {
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

      // 批量导出
      exportClick(){
        console.log(this.orderOutList);
      },

      // 分页组件的提示
      pageChange(v){
        this.$emit('pageChange', v)
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
  }
  .bottom-box {
    display: flex;
    justify-content: space-between;
    margin-top: 0.1rem;
    .page-box {

    }
    .export-btn {
      width: 0.5rem;
      height: 0.2rem;
      line-height: 0.2rem;
      font-size: 0.12rem;
      white-space: nowrap;
      align-items: center;
      text-align: center;
      padding: 0.03rem 0.15rem;
      border-radius: 0.05rem;
      color: #ffffff;
      background-color: #9fd0bf;
    }
  }
</style>
