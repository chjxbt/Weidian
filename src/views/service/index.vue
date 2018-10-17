<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <p class="m-form-label" style="margin-bottom: 0.2rem">投诉管理</p>

      <div class="content-table">
        <el-table :data="complainList" border style="width: 100%" v-loading="complainLoading">
          <el-table-column prop="oiid" label="订单编号" width="290"></el-table-column>
          <el-table-column prop="cotype" label="投诉类型" width="230"></el-table-column>
          <el-table-column prop="usname" label="投诉人" width="120"></el-table-column>
          <el-table-column prop="cocontent" label="描述内容"></el-table-column>
          <el-table-column prop="cocreatetime" label="投诉时间" width="155"></el-table-column>
          <el-table-column prop="status" label="投诉状态" width="100"></el-table-column>
          <el-table-column fixed="right" label="管理" width="120">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="changeStatus(scope, 'ing')" :disabled="scope.row.cotreatstatus == 2">处理</el-button>
              <!--<el-button type="text" size="small" @click="changeStatus(scope, 'ing')" v-if="scope.row.cotreatstatus == 1">处理</el-button>-->
              <!--<el-button type="text" size="small" @click="changeStatus(scope, 'done')" v-if="scope.row.cotreatstatus == 2">再次处理</el-button>-->
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
        page_size: 10,                // 每页显示的数量
        total_page: 1,                // 总页数
        page_num: 1                   // 第几页
      }
    },
    components: { pageTitle, Pagination },
    methods: {
      // 获取投诉记录
      getComplain() {
        this.complainLoading = true;
        axios.get(api.get_all_complain + '?token=' + localStorage.getItem('token') + "&page_size=" + this.page_size + "&page_num=" + this.page_num).then(res => {
          if(res.data.status == 200) {
            this.complainList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);
            for(let i = 0; i < this.complainList.length; i ++) {
              if(this.complainList[i].cotreatstatus == 0) {
                this.complainList[i].status = "未被投诉";
              }else if(this.complainList[i].cotreatstatus == 1) {
                this.complainList[i].status = "处理中";
              }else if(this.complainList[i].cotreatstatus == 2) {
                this.complainList[i].status = "已处理";
              }
            }
            this.complainLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 改变投诉的处理状态
      changeStatus(scope, status) {
        let params = { coid: scope.row.coid };
        if(status == "ing") {
          params.cotreatstatus = 2;
          this.$confirm("请确认该投诉已处理，是否继续？", "提示",
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            this.complainLoading = true;
            axios.post(api.update_status + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.complainLoading = false;
                this.$message({ message: "处理成功", type: 'success', duration: 1500 });

                // 刷新视图
                this.complainList[scope.$index].cotreatstatus = 2;
                this.complainList[scope.$index].status = "已处理";
                this.complainList = this.complainList.concat();
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }).catch(() => {  });
        }else if(status == "done") {
          params.cotreatstatus = 1;
          this.$confirm("此操作会将该投诉改变为处理中的状态，是否继续？", "提示",
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            this.complainLoading = true;
            axios.post(api.update_status + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.complainLoading = false;
                this.$message({ message: "改变成功", type: 'success', duration: 1500 });

                // 刷新视图
                this.complainList[scope.$index].cotreatstatus = 1;
                this.complainList[scope.$index].status = "处理中";
                this.complainList = this.complainList.concat();
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }).catch(() => {  });
        }
      },

      // 分页点击方法
      pageChange(v) {
        this.page_num = v;
        this.getComplain();     // 获取投诉记录
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
