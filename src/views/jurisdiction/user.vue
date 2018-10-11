<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <el-form :inline="true" :model="form" class="demo-form-inline">
        <div class="m-select-box">
          <el-form-item label="用户名">
            <el-input v-model="form.name" class="m-input-s m-green-b" placeholder=""></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
          </el-form-item>
        </div>
      </el-form>
      <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
        <el-table :data="user" stripe style="width: 100%">
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
      <div class="m-page-box">
        <Pagination :total="page_data.total_page" @pageChange="pageChange"></Pagination>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  export default {
    data(){
      return{
        name:'会员管理',
        form:{ name:'' },
        page_data:{
          total_page:1,
          current_page:1,
          total_num:0,
          page_size:10
        },
        user:[
          { group:'', userName:'', userId:'' }
        ]
      }
    },
    components:{ pageTitle, Pagination },
    methods:{
      /*分页点击*/
      pageChange(v){
        // if(v == this.current_page){
        //   this.$message({ message: '这已经是第' + v + '页数据了', type: 'warning', duration: 1500 });
        //   return false;
        // }
        // this.current_page = v;

      },
      storeSubmit(){

      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";
</style>
