<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <p class="m-form-label" style="margin-bottom: 0.2rem">投诉管理</p>

      <div class="content-table">
        <el-table :data="complainList" border style="width: 100%" v-loading="complainLoading">
          <el-table-column prop="oiid" label="订单编号" width="280"></el-table-column>
          <el-table-column prop="cotype" label="投诉类型" width="130"></el-table-column>
          <el-table-column prop="usname" label="投诉人" width="130"></el-table-column>
          <el-table-column prop="cocontent" label="描述内容"></el-table-column>
          <el-table-column prop="status" label="投诉状态" width="100"></el-table-column>
          <el-table-column fixed="right" label="管理" width="100">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">处理</el-button>
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
    name: "index",
    data() {
      return {
        name: "客服中心",
        complainList: [],             // 投诉list
        complainLoading: false,       // 投诉表格加载中
        page_size: 5,                 // 每页显示的数量
        total_page: 1,                // 总页数
        page_num: 1                   // 第几页
      }
    },
    components: { pageTitle, Pagination },
    methods: {
      // 获取投诉记录
      getComplain() {
        this.complainLoading = true;
        axios.get(api.get_all_complain + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.complainList = res.data.data;
            // this.total_page = Math.ceil(res.data.count / this.page_size);
            for(let i = 0; i < this.complainList.length; i ++) {
              if(this.complainList[i].cotreatstatus == 0) {
                this.complainList[i].status = "未被投诉";
              }else if(this.complainList[i].cotreatstatus == 1) {
                this.complainList[i].status = "处理中";
              }else if(this.complainList[i].cotreatstatus == 2) {
                this.complainList[i].status = "已处理";
              }
              this.complainList[i].usname = "投诉人";
            }
            this.complainLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 分页点击方法
      pageChange(v) {
        console.log(v);
      }
    },
    mounted() {
      this.getComplain();       // 获取投诉记录
    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .content-table {
    .page-box {
      margin-top: 0.2rem;
      text-align: right;
    }
  }
</style>
