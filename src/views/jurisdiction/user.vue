<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <div class="m-middle" style="width: 100%">
        <el-table :data="userList" style="width: 100%" border v-loading="userLoading">
          <el-table-column align="center" prop="userName" label="用户名"></el-table-column>
          <el-table-column align="center" prop="userId" label="会员等级" ></el-table-column>
          <el-table-column align="center" prop="userName" label="下单量"></el-table-column>
          <el-table-column align="center" prop="group" label="销售量" ></el-table-column>
          <el-table-column align="center" prop="group" label="上级" ></el-table-column>
          <el-table-column align="center" prop="group" label="下级" ></el-table-column>
          <el-table-column align="center" label="操作" width="160">
            <template slot-scope="scope">
              <span class="m-table-btn">查看</span>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    data(){
      return{
        name:'用户管理',
        userName: "",             // 头部查询的用户名
        userList: [],             // 用户list
        userLoading: false,       // 用户表格加载中
        page_size: 10,            // 每页请求的数量
        total_page: 1,            // 总页数
      }
    },
    components:{ pageTitle, Pagination },
    methods:{
      // 分页组件的提示
      pageChange(v){
        console.log(v)
      },
      // 获取用户list
      getUserList() {
        this.userLoading = true;
        axios.get(api.get_all_user + "?token=" + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.userList = res.data.data;
            this.userLoading = false;
            console.log(this.userList);
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      }
    },
    mounted() {
      // this.getUserList();       // 获取用户list
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";
</style>
