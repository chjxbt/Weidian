<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <p class="m-form-label" style="margin-bottom: 0.2rem">前台管理</p>

      <p class="m-form-label" style="margin-bottom: 0.1rem">隐藏控制</p>
      <div class="content-table">
        <el-table :data="hiddenList" border style="width: 100%" v-loading="hiddenLoading">
          <el-table-column prop="name" label="板块" width="260"></el-table-column>
          <el-table-column prop="content" label="隐藏内容" width="500"></el-table-column>
          <el-table-column prop="show" label="是否显示" width="300">
            <template slot-scope="scope">
              <div @click="rowClick(scope.$index)">
                <el-switch v-model="scope.row.show" active-text="展示" inactive-text="隐藏" @change="hiddenRow"></el-switch>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <p class="m-form-label" style="margin-bottom: 0.1rem">跳转控制</p>
      <div class="content-table">
        <el-table :data="jumpList" border style="width: 100%" v-loading="jumpLoading">
          <el-table-column prop="name" label="板块" width="260"></el-table-column>
          <el-table-column prop="to" label="跳转模块" width="500">
            <template slot-scope="scope">
              <el-radio-group v-model="jumpTo" @change="jumpToChange">
                <el-radio :label="1">专题</el-radio>
                <el-radio :label="2">商品</el-radio>
              </el-radio-group>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    name: "index",
    data() {
      return {
        name:'控制中心',
        hiddenLoading: false,
        hiddenList: [
          { name: "发现", content: "素材圈", show: false },
          { name: "我的", content: "VIP数据统计", show: true },
          { name: "我的", content: "我的订单-待评价板块", show: true }
        ],
        jumpLoading: false,
        jumpList: [{ name: "首页", to: "" }],
        jumpTo: 0,
        rowNum: ""
      }
    },
    components: { pageTitle },
    methods: {
      // 隐藏控制的变化钩子
      hiddenRow(v) {
        console.log(v);
      },
      // 保存点击的行数
      rowClick(row) {
        this.rowNum = row;
        console.log("row", row);
      },
      // 隐藏控制
      hiddenControl() {

      },
      // 获取跳转控制的值
      getJumpto() {
        this.jumpLoading = true;
        axios.get(api.get_show_type + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.jumpTo = res.data.data.skiptype;
            this.jumpLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },
      // 跳转控制的变化钩子
      jumpToChange(v) {
        this.jumpLoading = true;
        axios.post(api.set_show_type + '?token=' + localStorage.getItem('token'), { skip_type: v }).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
            this.jumpLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      }
    },
    mounted() {
      this.getJumpto();     // 获取跳转控制的值
    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

</style>
