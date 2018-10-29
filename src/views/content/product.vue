<template>
  <div class="m-weidians">
    <page-title :title="name"></page-title>
    <div class="m-weidian-contents">
      <div class="search-box">
        <div class="search-group">
          <div class="group-title">单品名称：</div>
          <el-input class="search-input" v-model="productName" size="mini" clearable></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">创建时间：</div>
          <el-date-picker v-model="createTime" type="daterange" start-placeholder="开始日期" range-separator="至"
                          end-placeholder="结束日期" style="width: 2.5rem;" size="mini">
          </el-date-picker>
        </div>
        <div class="search-group">
          <div class="group-title">商家编码：</div>
          <el-input class="search-input" v-model="storeNO" size="mini" clearable></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">价格区间：</div>
          <el-input class="price-input" v-model="leftPrice" placeholder="最低价" size="mini" clearable></el-input>
          <div class="group-title middle-symbol">~</div>
          <el-input class="price-input" v-model="rightPrice" placeholder="最高价" size="mini" clearable></el-input>
        </div>
        <div class="search-btn" @click="">搜 索</div>
      </div>

      <div class="content-table">
        <el-table :data="productList" border style="width: 100%" v-loading="productLoading">
          <el-table-column prop="product" label="运营ID"></el-table-column>
          <el-table-column prop="product" label="单品名称"></el-table-column>
          <el-table-column prop="product" label="单品缩略图"></el-table-column>
          <el-table-column prop="product" label="所在模块"></el-table-column>
          <el-table-column prop="product" label="所在专题"></el-table-column>
          <el-table-column prop="product" label="单品推文内容状态"></el-table-column>
          <el-table-column prop="product" label="商家编码"></el-table-column>
          <el-table-column prop="product" label="进货价"></el-table-column>
          <el-table-column prop="product" label="售价"></el-table-column>
          <el-table-column prop="product" label="支出佣金"></el-table-column>
          <el-table-column prop="product" label="pv"></el-table-column>
          <el-table-column prop="product" label="转化"></el-table-column>
          <el-table-column prop="product" label="单品状态"></el-table-column>
          <el-table-column prop="product" label="认领推文"></el-table-column>
          <el-table-column prop="product" label="大礼包"></el-table-column>
          <el-table-column prop="product" label="创建日期"></el-table-column>
          <el-table-column prop="product" label="操作记录"></el-table-column>
          <el-table-column fixed="right" label="管理">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">编辑</el-button>
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
        name: '商品管理',
        productName: '',              // 单品名称
        storeNO: '',                  // 商家编码
        createTime: [],               // 创建时间
        leftPrice: "",                // 价格区间 - 低价
        rightPrice: "",               // 价格区间 - 高价
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
  /*@import "../../common/css/weidian";*/

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
          margin: 0.1rem 0.6rem 0 0;
          .group-title {
            font-size: 0.12rem;
            line-height: 0.2rem;
            margin-right: 0.1rem;
          }
          .search-input {
            width: 2rem;
          }
          .price-input {
            width: 1.115rem;
          }
          .middle-symbol {
            margin: 0 0.1rem;
          }
        }
        .search-btn {
          width: 0.33rem;
          height: 0.18rem;
          line-height: 0.18rem;
          font-size: 0.12rem;
          white-space: nowrap;
          align-items: center;
          text-align: center;
          padding: 0.03rem 0.15rem;
          border-radius: 0.1rem;
          margin: 0.09rem 0 0 1rem;
          color: #ffffff;
          background-color: #9fd0bf;
        }
      }

      .content-table {
        padding: 0.2rem 0 0 0;
        /*padding-bottom: 0 !important;*/
        .page-box {
          text-align: right;
          padding-top: 0.1rem;
        }
      }
    }
  }
</style>
