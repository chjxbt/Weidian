<template>
  <div class="m-weidians">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-contents">

      <div class="content-table">
        <!--<div class="search-box">
          <div class="search-btn" @click="">下载报表</div>
        </div>-->
        <el-table :data="outList" border style="width: 100%" v-loading="outLoading">
          <el-table-column prop="levelname" label=""></el-table-column>
          <el-table-column prop="sold_income" label="平台商品佣金支出"></el-table-column>
          <el-table-column prop="invite_open" label="邀请开店支出"></el-table-column>
          <el-table-column prop="week_reward" label="周周奖"></el-table-column>
          <el-table-column prop="reward_income" label="额外奖励"></el-table-column>
          <el-table-column prop="fans_outincome" label="专粉佣金支出"></el-table-column>
          <el-table-column prop="novice_reward" label="新店主任务佣金支出"></el-table-column>
        </el-table>
      </div>


      <div class="content-table">
        <div class="search-box">
          <div class="search-group">
            <div class="group-title">关键词：</div>
            <el-input class="search-input" v-model="keywords" placeholder="请输入用户名或手机号搜索" size="mini"></el-input>
          </div>
          <div class="search-group">
            <div class="group-title">时间段：</div>
            <el-date-picker v-model="createTime" type="datetimerange" start-placeholder="开始日期" range-separator="至"
                            end-placeholder="结束日期" value-format="yyyy-MM-dd HH:mm:ss" style="width: 3.2rem;" size="mini">
            </el-date-picker>
          </div>
          <div class="search-btn cancel-btn" @click="cancelSearch">取 消</div>
          <div class="search-btn" @click="searchProduct">搜 索</div>
        </div>
        <el-table :data="ownerList" border stripe style="width: 100%" v-loading="ownerLoading">
          <el-table-column prop="usname" label="用户名"></el-table-column>
          <el-table-column prop="usphone" label="手机号"></el-table-column>
          <el-table-column prop="fans_outincome" label="专粉佣金"></el-table-column>
          <el-table-column prop="invite_open" label="开店佣金"></el-table-column>
          <el-table-column prop="novice_reward" label="新店主任务奖励佣金"></el-table-column>
          <el-table-column prop="sold_income" label="商品销售佣金"></el-table-column>
        </el-table>

        <Pagination class="page-box" :total="owner_total_page" @pageChange="ownerChange"></Pagination>
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
        name:'佣金概况',
        userID: "",                     // 查询的店主ID
        outList: [],             // 佣金概况的list
        outLoading: false,       // 佣金概况表格加载中
        page_size: 10,                  // 每页请求的数量
        keywords: "",                   // 关键词 - 店主数据表
        createTime: [],                 // 时间段 - 店主数据表
        ownerList: [],                  // 店主数据lsit - 店主数据表
        ownerLoading: false,            // 店主数据表加载中 - 店主数据表
        owner_total_page: 1,            // 总页数 - 店主数据表
        owner_page_num: 1,              // 第几页 - 店主数据表
        isSearch: false,                // 是否正在搜索 - 店主数据表
      }
    },
    components:{ pageTitle, Pagination },
    methods:{
      // 分页点击方法 - 店主数据表
      ownerChange(v) {
        this.owner_page_num = v;
        if(this.isSearch) {
          this.getOwner(this.owner_page_num, 'search');      // 获取店主佣金数据
        }else {
          this.getOwner();            // 获取店主佣金数据
        }
      },
      // 搜索按钮 - 店主数据表
      searchProduct() {
        console.log(this.keywords != "", this.createTime.length != 0);
        if(this.keywords != "" || this.createTime.length != 0) {
          this.isSearch = true;
          this.getOwner(1, 'search'); // 获取店主佣金数据
        }else {
          this.getOwner();            // 获取店主佣金数据
        }
      },
      // 取消按钮 - 店主数据表
      cancelSearch() {
        if(this.isSearch) {
          this.isSearch = false;
          this.keywords = "";
          this.createTime = [];
          this.getOwner(1, 'search'); // 获取店主佣金数据
        }
      },
      // 获取支出数据
      getOut() {
        this.outLoading = true;
        axios.get(api.get_comm_overview + "?token=" + localStorage.getItem("token")).then(res => {
          if(res.data.status == 200) {
            this.outList = res.data.data;
            this.outLoading = false;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 获取店主佣金数据
      getOwner(page_num, operate) {
        this.ownerLoading = true;
        let params = {
          token: localStorage.getItem("token"),
          page_num: page_num || this.owner_page_num,
          page_size: this.page_size
        };
        // 搜索的拼接
        if(operate) {
          if(this.keywords != "") {
            params.kw = this.keywords;
          }
          if(this.createTime.length != 0) {
            params.time_start = this.createTime[0];
            params.time_end = this.createTime[1];
          }
        }
        console.log(params);
        axios.get(api.get_comm_list, { params: params }).then(res => {
          if(res.data.status == 200) {
            this.owner_total_page = Math.ceil(res.data.count / this.page_size);
            this.ownerList = res.data.data;
            this.ownerLoading = false;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      }
    },
    mounted() {
      this.getOut();            // 获取支出数据
      this.getOwner();          // 获取店主佣金数据
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  /*@import "../../common/css/weidian";*/

  .m-weidians {
    background-color: #fff;
    .m-weidian-contents {
      padding: 0.25rem 0.45rem 0.25rem;
      .content-table {
        .search-box {
          display: flex;
          flex-wrap: wrap;
          justify-content: flex-end;
          margin: 0.3rem 0 0.1rem 0;
          background-color: #f7f7f7;
          padding: 0.1rem 0.2rem;
          border-radius: 0.1rem;
          .search-group {
            display: flex;
            margin: 0.1rem 0.3rem 0 0;
            .group-title {
              width: 0.5rem;
              font-size: 0.12rem;
              line-height: 0.2rem;
            }
            .search-input {
              width: 2.3rem;
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
            margin: 0.09rem 0 0 0.2rem;
            color: #ffffff;
            background-color: #9fd0bf;
          }
          .cancel-btn {
            color: #000000;
            background-color: #DBDCDC;
            margin-left: 0.5rem;
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
