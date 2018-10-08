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
              <el-switch v-model="scope.row.show" active-text="展示" inactive-text="隐藏"></el-switch>
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
              <el-radio-group v-model="jumpTo">
                <el-radio :label="3">全部</el-radio>
                <el-radio :label="6">专题</el-radio>
                <el-radio :label="9">商品</el-radio>
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
        jumpList: [{ name: "首页/发现页", to: "" }],
        jumpTo: 3
      }
    },
    components: { pageTitle },
    methods: {
      // 隐藏控制
      hiddenControl() {
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token'), form).then(res => {
          if(res.data.status == 200){
            // console.log(res, file);
            this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }

          this.bannerList[this.rowNum].baimage = res.data.data;
          this.bannerList = this.bannerList.concat();
          // this.imageUrl = res.data.data;
        });
      },
      // 跳转控制
      jumpToWhere() {
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token'), form).then(res => {
          if(res.data.status == 200){
            // console.log(res, file);
            this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }

          this.bannerList[this.rowNum].baimage = res.data.data;
          this.bannerList = this.bannerList.concat();
          // this.imageUrl = res.data.data;
        });
      }
    },
    watch: {
      // 跳转模块的值发生变化
      jumpTo(newValue, oldValue) {
        console.log(newValue)
      }
    },
    mounted() {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

</style>
