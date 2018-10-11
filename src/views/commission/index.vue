<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <el-form :inline="true" :model="form" class="demo-form-inline">
        <div class="m-select-box">
          <el-form-item label="店主ID">
            <el-input v-model="form.name" class="m-input-s m-green-b" placeholder=""></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
          </el-form-item>
        </div>
      </el-form>
      <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
        <el-table :data="user" stripe style="width: 100%">
          <el-table-column align="center" prop="userName" label="店主ID"></el-table-column>
          <el-table-column align="center" prop="userId" label="店主等级" ></el-table-column>
          <el-table-column align="center" prop="userName" label="联系方式"></el-table-column>
          <el-table-column align="center" prop="group" label="获得总佣金" ></el-table-column>
          <el-table-column align="center" prop="group" label="销售金额佣金" ></el-table-column>
          <el-table-column align="center" prop="group" label="邀请开店佣金" ></el-table-column>
          <el-table-column align="center" prop="userName" label="专粉支出佣金"></el-table-column>
          <el-table-column align="center" prop="userId" label="团队佣金" ></el-table-column>
          <el-table-column align="center" prop="userName" label="奖励佣金"></el-table-column>
          <el-table-column align="center" prop="group" label="账户余额" ></el-table-column>
          <el-table-column align="center" prop="group" label="待到账金额" ></el-table-column>
          <el-table-column align="center" prop="group" label="正提现金额" ></el-table-column>
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
        name:'佣金管理',
        form:{
          name:''
        },
        page_data:{
          total_page:1,
          current_page:1,
          total_num:0,
          page_size:10
        },
        user:[
          {
            group:'',
            userName:'',
            userId:'',

          }
        ]
      }
    },
    components:{
      pageTitle,
      Pagination
    },
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
