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
                <el-radio :label="0" disabled>全部</el-radio>
                <el-radio :label="1">专题</el-radio>
                <el-radio :label="2">商品</el-radio>
              </el-radio-group>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <p class="m-form-label" style="margin: 0.1rem 0">微信分享设置</p>
      <div class="m-form-item">
        <p class="m-form-label required" style="width: 0.8rem; font-size: 0.12rem">分享标题</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="shareTitle" placeholder="请输入分享标题" maxlength="25" class="hot-message-input"></el-input>
          </div>
        </div>
      </div>
      <div class="m-form-item">
        <p class="m-form-label required" style="width: 0.8rem; font-size: 0.12rem">分享内容</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 2 }" placeholder="请输入分享内容" v-model="shareText" style="width: 4rem"></el-input>
          </div>
          <!--<p class="m-item-alert" style="margin-top: 0.05rem; font-size: 0.12rem"><span style="color: red">* </span>字数控制在25字以内</p>-->
        </div>
      </div>
      <div class="m-form-item">
        <p class="m-form-label required" style="width: 0.8rem; font-size: 0.12rem">分享图片</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <div class="upload-box">
              <el-upload class="share-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                <img v-if="shareImg" :src="shareImg" class="share-img">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
          </div>
        </div>
      </div>
      <div class="m-form-confirm-btn">
        <span @click="saveShare">保 存</span>
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
          { name: "我的", content: "VIP数据统计", show: false },
          { name: "我的", content: "我的订单-待评价板块", show: false }
        ],
        jumpLoading: false,
        jumpList: [{ name: "首页", to: "" }],
        jumpTo: 0,
        status: "",       // 暂存隐藏状态
        shareTitle: "",   // 微信分享标题
        shareText: "",    // 微信分享内容
        shareImg: "",     // 微信分享图片
      }
    },
    components: { pageTitle },
    methods: {
      // 隐藏控制的变化钩子，保存点击的状态
      hiddenRow(v) {
        if(v) {
          this.status = 1;
        }else if(!v) {
          this.status = 0;
        }
      },
      // 获取点击的行数，发送请求
      rowClick(row) {
        let params = {};
        this.hiddenLoading = true;
        if(row == 0) {
          params = { material: this.status };
        }else if(row == 1) {
          params = { vip_match: this.status };
        }else if(row == 2) {
          params = { wait_apply: this.status };
        }
        axios.post(api.set_schedual + '?token=' + localStorage.getItem('token'), params).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
            this.hiddenLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 隐藏控制
      /*hiddenControl() {

      },*/
      // 获取隐藏控制的值
      getHidden() {
        this.hiddenLoading = true;
        axios.get(api.get_schedual).then(res => {
          if(res.data.status == 200) {
            // 从接口中拿到显示的状态，并转换
            if(res.data.data.material == "0") {     // 素材圈
              this.hiddenList[0].show = false;
            }else if(res.data.data.material == "1") {
              this.hiddenList[0].show = true;
            }
            if(res.data.data.vip_match == "0") {    // vip
              this.hiddenList[1].show = false;
            }else if(res.data.data.vip_match == "1") {
              this.hiddenList[1].show = true;
            }
            if(res.data.data.wait_apply == "0") {   // 待评价
              this.hiddenList[2].show = false;
            }else if(res.data.data.wait_apply == "1") {
              this.hiddenList[2].show = true;
            }
            this.hiddenLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 获取跳转控制的值
      getJumpto() {
        this.jumpLoading = true;
        axios.get(api.get_show_type + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.jumpTo = Number(res.data.data.skiptype);
            this.jumpLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
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
      },
      // 上传分享图片
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = banner", form).then(res => {
          if(res.data.status == 200){
            this.shareImg = res.data.data;
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 获取微信分享参数
      getShare() {
        axios.get(api.get_share_params + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.shareTitle = res.data.data.title;
            this.shareText = res.data.data.content;
            this.shareImg = res.data.data.img;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 保存微信分享参数
      saveShare() {
        let params = {
          title: this.shareTitle,
          content: this.shareText,
          img: this.shareImg,
        };
        axios.post(api.set_share_params + '?token=' + localStorage.getItem('token'), params).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      }
    },
    mounted() {
      this.getHidden();     // 获取隐藏控制的值
      this.getJumpto();     // 获取跳转控制的值
      this.getShare();      // 获取微信分享参数
    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

</style>
