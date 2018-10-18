<template>
  <div class="m-weidians">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-contents">

      <div class="content-table">
        <div class="search-box">
          <div class="search-title">店主ID：</div>
          <el-input class="search-input" v-model="userID" size="mini" clearable></el-input>
          <div class="search-btn">查 询</div>
        </div>
        <el-table :data="commissionList" border style="width: 100%" v-loading="commissionLoading">
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
    data(){
      return{
        name:'佣金管理',
        userID: "",                     // 查询的店主ID
        commissionList: [],             // 佣金管理的list
        commissionLoading: false,       // 佣金管理表格加载中
        page_size: 10,                  // 每页请求的数量
        total_page: 1,                  // 总页数
      }
    },
    components:{ pageTitle, Pagination },
    methods:{

      // 分页点击方法
      pageChange(v) {
        if(!this.searching) {
          this.getActivity(this.page_size * (v - 1), this.page_size);
        }else {
          this.searchActivity(this.page_size * (v - 1), this.page_size);
        }
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .m-weidians {
    background-color: #fff;
    .m-weidian-contents {
      padding: 0.25rem 0.45rem 0.25rem;
      .content-table {
        .search-box {
          display: flex;
          font-size: 0.12rem;
          .search-title {
            line-height: 0.2rem;
          }
          .search-input {
            width: 1.5rem;
          }
          .search-btn {
            width: 0.28rem;
            white-space: nowrap;
            align-items: center;
            padding: 0.03rem 0.15rem;
            margin: 0 0 0.1rem 0.3rem;
            border-radius: 0.05rem;
            color: #ffffff;
            background-color: #9fd0bf;
          }
        }
        .page-box {
          text-align: right;
          margin-top: 0.1rem;
        }
      }
    }
  }
</style>
