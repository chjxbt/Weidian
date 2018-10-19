<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <div class="m-middle" style="width: 100%">
        <el-table :data="userList" style="width: 100%" border v-loading="userLoading">
          <el-table-column align="center" prop="usname" label="用户名"></el-table-column>
          <el-table-column align="center" prop="userId" label="会员等级" ></el-table-column>
          <el-table-column align="center" prop="buyordercount" label="下单量"></el-table-column>
          <el-table-column align="center" prop="sellordercount" label="销售量" ></el-table-column>
          <el-table-column align="center" prop="upperd" label="上级" ></el-table-column>
          <el-table-column align="center" prop="group" label="下级" >
            <template slot-scope="scope">
              <span class="blue-btn" @click="lowerBox(scope)">查看</span>
            </template>
          </el-table-column>
          <el-table-column align="center" label="管理" width="160">
            <template slot-scope="scope">
              <span>管理</span>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>

      <!--下级会员-->
      <el-dialog title="下级会员" :visible.sync="lowerDialog" width="6.5rem">
        <div class="send-box">
          <div class="user-box">
            <div class="user-name" v-for="item in lowerList" :title="item.usname">{{item.usname}}</div>
          </div>
          <Pagination class="page-box" :total="total_page_lower" @pageChange="pageChangeLower"></Pagination>
        </div>
      </el-dialog>
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
        page_num: 1,              // 页码
        total_page: 1,            // 总页数
        page_size_lower: 10,      // 每页请求的数量
        page_num_lower: 1,        // 页码
        total_page_lower: 1,      // 总页数
        lowerList: [],            // 下级会员list
        lowerDialog: false,       // 下级会员的展示dialog
      }
    },
    components:{ pageTitle, Pagination },
    methods:{
      // 分页组件的提示
      pageChange(v){
        this.page_num = v;
        this.getUserList();       // 获取用户list
      },
      // dialog分页组件的提示
      pageChangeLower(v){
        this.page_num_lower = v;
        this.lowerBox();       // 打开展示下级用户的dialog
      },
      // 获取用户list
      getUserList() {
        this.userLoading = true;
        axios.get(api.get_all_user + "?token=" + localStorage.getItem('token') + "&page_size=" + this.page_size + "&page_num=" + this.page_num).then(res => {
          if(res.data.status == 200) {
            this.userList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);
            this.userLoading = false;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 打开展示下级用户的dialog
      lowerBox(scope) {
        this.lowerDialog = true;

        axios.get(api.get_user_sub + "?token=" + localStorage.getItem('token') + "&page_size=" + this.page_size_lower + "&page_num=" + this.page_num + "&usid=" + scope.row.usid).then(res => {
          if(res.data.status == 200) {
            this.lowerList = res.data.data;
            this.total_page_lower = Math.ceil(res.data.count / this.page_size_lower);
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      }
    },
    mounted() {
      this.getUserList();       // 获取用户list
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .page-box {
    text-align: right;
    margin-top: 0.2rem;
  }
  .send-box {
    margin: -0.1rem 0.2rem 0 0.4rem;
    .user-box {
      display: flex;
      flex-wrap: wrap;
      .user-name {
        width: 0.85rem;
        border: 1px #707070 solid;
        margin: 0 0 -1px -1px;
        text-align: center;
        padding: 0.08rem 0.1rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
  }
</style>
