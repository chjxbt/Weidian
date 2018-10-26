<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <div class="content-table">
        <el-table :data="productList" border style="width: 100%" v-loading="productLoading">
          <el-table-column prop="product" label="店主ID"></el-table-column>
          <el-table-column prop="product" label="店主等级"></el-table-column>
          <el-table-column prop="product" label="联系方式"></el-table-column>
          <el-table-column prop="product" label="获得总佣金"></el-table-column>
          <el-table-column prop="product" label="销售商品佣金"></el-table-column>
          <el-table-column prop="product" label="邀请开店佣金"></el-table-column>
          <el-table-column prop="product" label="专粉支出佣金"></el-table-column>
          <el-table-column prop="product" label="团队佣金"></el-table-column>
          <el-table-column prop="product" label="奖励佣金"></el-table-column>
          <el-table-column prop="product" label="账户余额"></el-table-column>
          <el-table-column prop="product" label="待到账金额"></el-table-column>
          <el-table-column prop="product" label="正提现金额"></el-table-column>
          <el-table-column fixed="right" label="管理">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">编辑</el-button>
            </template>
          </el-table-column>
        </el-table>

        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    name: "product",
    data() {
      return {
        name:'商品管理',
        productList: [],              // 商品管理的list
        productLoading: false,        // 商品管理表格加载中
        page_size: 10,                // 每页请求的数量
        total_page: 1,                // 总页数
      }
    },
    components:{ pageTitle, Pagination },
    methods: {
      // 分页点击方法
      pageChange(v) {

      }
    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .content-table {
    padding-bottom: 0 !important;
    .page-box {
      text-align: right;
      padding-top: 0.1rem;
    }
  }
</style>
