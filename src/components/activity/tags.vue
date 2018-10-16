<template>
  <div>
    <el-dialog title="活动角标" :visible.sync="badgeDialog" width="4.8rem">
      <div class="dialog-img">
        <div class="img-box" v-for="(item, index) in badgeList">
          <img class="badge-img" :src="item.atname" @click="chooseImg(index)">
          <img class="choose-ok-img" v-if="item.choose" src="../../common/images/tag_ok.png">
          <div class="delete-tags" @click="deleteTag(item, index)">X</div>
        </div>
        <el-upload class="badge-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                   :on-success="uploadBadgeImg">
          <img v-if="activityBadgeTemp" :src="activityBadgeTemp" style="width: 0.5rem; height: 0.5rem;">
          <i v-else class="el-icon-plus badge-icon"></i>
        </el-upload>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button class="at-img-dialog-btn btn-color" type="primary" @click="chooseOK">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    name: "tags",
    data() {
      return {
        activityBadgeTemp: '',      // 推文-活动角标暂存
        badgeDialog: false,         // 推文-活动角标-dialog
        badgeList: [],              // 推文-活动角标list
        badgeIndex: "",             // 推文-活动角标序号暂存
      }
    },
    components: {},
    methods: {
      // 上传活动角标图片
      uploadBadgeImg(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = badge", form).then(res => {
          if(res.data.status == 200){
            let atname = res.data.data;
            // 上传活动角标图片到api
            axios.post(api.upload_tags + '?token=' + localStorage.getItem('token'), { tags: [{ atname: atname }] }).then(res => {
              if(res.data.status == 200){
                this.$message({ type: 'success', message: "上传成功", duration: 1500 });
                this.badgeList.push({ atid: res.data.data.atid_list[0], atname: atname });
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取推文角标
      getTags(activityBadge){
        this.badgeDialog = true;
        axios.get(api.get_all_tags + "?token=" + localStorage.getItem("token")).then(res => {
          if(res.data.status == 200) {
            this.badgeList = res.data.data.tags_list;
            for(let i = 0; i < this.badgeList.length; i ++) {
              this.badgeList[i].choose = false;
              if(this.badgeList[i].atname == activityBadge) {
                this.badgeList[i].choose = true;
              }
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 删除推文角标
      deleteTag(item, index){
        this.$confirm('此操作将删除该专题, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          axios.post(api.del_exist_tags + '?token=' + localStorage.getItem('token'), { atid: item.atid }).then(res => {
            if(res.data.status == 200){
              this.$message({ type: 'success', message: res.data.message, duration: 1500 });
              this.badgeList.splice(index, 1);
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }).catch(() => {  });
      },

      // 选择该推文角标
      chooseImg(index){
        for(let i = 0; i < this.badgeList.length; i ++) {
          this.badgeList[i].choose = false;
        }
        this.badgeList[index].choose = true;
        this.badgeIndex = index;
        this.badgeList = this.badgeList.concat();
      },

      // 确认按钮，传回选中图片
      chooseOK() {
        console.log(this.badgeIndex);
        this.$emit("getData", this.badgeList[this.badgeIndex].atname);
        this.badgeDialog = false;
      }
    },
    mounted() {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .dialog-img {
    width: 4.6rem;
    display: flex;
    flex-wrap: wrap;
    margin-top: -0.2rem;
    .img-box {
      position: relative;
      .badge-img {
        width: 0.5rem;
        height: 0.5rem;
        margin: 0.2rem 0 0 0.2rem;
        border: 1px solid #ababab;
      }
      .choose-ok-img {
        width: 0.182rem;
        height: 0.13333rem;
        position: absolute;
        bottom: 0;
        right: -0.02rem;
      }
      .delete-tags {
        color: #ababab;
        position: absolute;
        top: 0.14rem;
        right: -0.02rem;
      }
    }
  }
  .dialog-footer {
    .at-img-dialog-btn {
      padding: 0.05rem 0.1rem;
      font-size: 14px;
    }
    .btn-color {
      border-color: @btnActiveColor;
      background-color: @btnActiveColor;
    }
  }
</style>
