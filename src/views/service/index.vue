<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <p class="m-form-label" style="margin-bottom: 0.2rem">投诉管理</p>

      <div class="content-table">
        <el-table :data="complainList" border style="width: 100%" v-loading="complainLoading">
          <el-table-column prop="time" label="推文时间" width="320">
          </el-table-column>
          <el-table-column prop="actitle" label="推文标题" width="150"></el-table-column>
          <el-table-column prop="actext" label="推文内容">
          </el-table-column>
          <el-table-column prop="acSkiptype" label="跳转类型" width="100"></el-table-column>
          <el-table-column prop="product" label="评论管理" width="100">
            <template slot-scope="scope">
              <div class="comments-text" @click="">查看</div>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="">删除</el-button>
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
            console.log(res.data.data);
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
  @import "../../common/css/index";

  .content-table {
    .page-box {

    }
  }
</style>
