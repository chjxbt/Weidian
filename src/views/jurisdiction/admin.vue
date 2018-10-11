<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <el-button class="m-top-button-button top-btn" size="mini" @click="addAdminVisible=true" style="margin-bottom: 0.1rem">添加管理员</el-button>
      </div>
      <div class="m-middle">
        <el-table :data="adminList" stripe border style="width: 100%" v-loading="adminLoading">
          <el-table-column align="center" prop="suheader" label="用户头像">
            <template slot-scope="scope">
              <img class="user-img" :src="scope.row.suheader">
            </template>
          </el-table-column>
          <el-table-column align="center" prop="suname" label="用户名称"></el-table-column>
          <el-table-column align="center" prop="suLevel" label="用户级别"></el-table-column>
          <el-table-column align="center" prop="suStatus" label="用户状态"></el-table-column>
          <el-table-column align="center" label="管理" fixed="right" width="220">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="editAdmin(scope)" :disabled="scope.row.suLevel == '超级管理员'">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="editAdminStatus(scope, 'lock')" v-if="scope.row.suStatus == '正常'" :disabled="scope.row.suLevel == '超级管理员'">封禁</el-button>
              <el-button type="text" size="small" @click="editAdminStatus(scope, 'unlock')" v-if="scope.row.suStatus == '封禁中'" :disabled="scope.row.suLevel == '超级管理员'">解封</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="editAdminStatus(scope, 'delete')" :disabled="scope.row.suLevel == '超级管理员'">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <!--编辑管理员弹出框-->
        <el-dialog :title="editAdminTitle" :visible.sync="editAdminVisible" width="40%" show-close center>
          <div v-if="dialog=='index'">
            <div class="edit-dialog" style="margin-top: 0.25rem">
              <div class="change" @click="dialog='changePicture'">
                <img class="change-pictures" src="../../assets/images/changePicture.png"/>
                <div>修改管理员头像</div>
              </div>
              <div class="change" @click="dialog='changePw'">
                <img class="change-pictures" src="../../assets/images/changePw.png"/>
                <div>修改管理员密码</div>
              </div>
              <div v-if="row.MAstatus == '可用'">
                <div class="change" @click="lockAdmin('封禁')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>封禁管理员</div>
                </div>
              </div>
              <div v-if="row.MAstatus == '禁用'">
                <div class="change" @click="lockAdmin('解封')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>解封管理员</div>
                </div>
              </div>
              <div v-if="row.MAstatus == '未激活'">
                <div class="change" @click="lockAdmin('激活')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>激活管理员</div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePicture'">
            <div class="edit-dialog" style="margin-top: 0.15rem">
              <el-upload class="avatar-uploader" action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.2rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button class="m-top-button-button" @click="dialog='index'">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePw'">
            <div class="edit-dialog">
              <el-form :model="form" style="margin-right: 0.4rem">
                <el-form-item label="请输入旧密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.oldPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
                <el-form-item label="请输入新密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.newPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
                <el-form-item label="请确认新密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.againNewPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.1rem">
                <el-button @click="dialog='index'" size="mini">取 消</el-button>
                <el-button class="m-top-button-button" @click="changePwDone" size="mini">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changeMAstatus'">
            <div class="edit-dialog" style="margin-top: 0.25rem;height: 1.2rem">
              <div style="text-align: center;font-size: 18px">确认{{operation}}该管理员吗？</div>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.4rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button class="m-top-button-button" @click="changeMAstatus">确 定</el-button>
              </div>
            </div>
          </div>
        </el-dialog>
        <!--添加/编辑管理员弹出框-->
        <el-dialog :title="editAdminText" :visible.sync="addAdminVisible" width="30%" center>
          <div class="add-dialog">
            <el-form :model="addForm">
              <el-form-item label="用户名称：" :label-width="addFormWidth">
                <el-input v-model="addForm.userName" size="mini" style="width: 80%"></el-input>
              </el-form-item>
              <el-form-item label="用户头像：" :label-width="addFormWidth">
                <el-upload class="user-img-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                           :on-success="uploadPicture">
                  <img v-if="addForm.userImg" :src="addForm.userImg" class="user-img-picture">
                  <i v-else class="el-icon-plus user-img-picture"></i>
                </el-upload>
              </el-form-item>
              <div v-if="editAdminPw">
                <el-form-item label="输入密码：" :label-width="addFormWidth">
                  <el-input type="password" v-model="addForm.password" size="mini" style="width: 80%"></el-input>
                </el-form-item>
                <el-form-item label="确认密码：" :label-width="addFormWidth">
                  <el-input type="password" v-model="addForm.againPassword" size="mini" style="width: 80%"></el-input>
                </el-form-item>
              </div>
              <el-form-item label="用户级别：" :label-width="addFormWidth"><el-radio-group v-model="addForm.level">
                <el-radio :label="0">客服</el-radio>
                <el-radio :label="1">普通管理员</el-radio>
                <el-radio :label="2" disabled>超级管理员</el-radio>
              </el-radio-group>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.2rem" v-if="!editAdminPw">
              <el-button class="top-btn btn-width" size="mini" @click="editAdminPw = true">修改密码</el-button>
            </div>
            <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.15rem">
              <el-button class="top-btn btn-width" size="mini" @click="cancelAddAdmin">取 消</el-button>
              <el-button class="m-top-button-button top-btn btn-width" size="mini" v-if="editAdminText == '添加管理员'" @click="addAdmin">保 存</el-button>
              <el-button class="m-top-button-button top-btn btn-width" size="mini" v-if="editAdminText == '编辑管理员'" @click="saveEditAdmin">保 存</el-button>
            </div>
          </div>
        </el-dialog>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import api from '../../api/api';
  import axios from 'axios';
  export default {
    data() {
      return {
        name: '管理员管理',
        inputID: '',
        inputName: '',
        adminList: [],              // 管理员list
        adminLoading: false,        // 管理员表格加载中
        editAdminVisible: false,
        addAdminVisible: false,
        editAdminText: "添加管理员", // 编辑管理员的dialog标题
        editAdminPw: true,          // 编辑管理员的密码
        editAdminTitle: '',
        dialog: '',
        imageUrl: '',
        form: {
          oldPw: '',
          newPw: '',
          againNewPw: '',
        },
        addForm: {
          userName: "",
          password: "",
          againPassword: "",
          userImg: "",
          level: 1
        },
        formLabelWidth: '1rem',
        addFormWidth: '1rem',
        total_page: 0,
        current_page: 0,
        total_num: 0,
        page_size: 10,
        searchText: '',
        row: [],
        operation: '',
        MAid: ''
      }
    },
    components:{ pageTitle },
    methods: {
      // 获取管理员
      getAdmin(){
        this.adminLoading = true;
        axios.get(api.get_all_suser + "?sutype=all&token=" + localStorage.getItem("token")).then(res => {
          if(res.data.status == 200) {
            this.adminLoading = false;
            this.adminList = res.data.data;
            for(let i = 0; i < this.adminList.length; i ++) {
              // 用户等级
              if(this.adminList[i].sulevel == "0") {
                this.adminList[i].suLevel = "客服";
              }else if(this.adminList[i].sulevel == "1") {
                this.adminList[i].suLevel = "普通管理员";
              }else if(this.adminList[i].sulevel == "2") {
                this.adminList[i].suLevel = "超级管理员";
              }
              // 用户状态
              if(this.adminList[i].sustatus == "normal") {
                this.adminList[i].suStatus = "正常";
              }else if(this.adminList[i].sustatus == "freeze") {
                this.adminList[i].suStatus = "封禁中";
              }
            }
          }else{
            this.$message.error(res.data.message);
          }
        });
      },
      // 添加管理员时的头像
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = userImg", form).then(res => {
          if(res.data.status == 200){
            this.addForm.userImg = res.data.data;
            // this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }
        });
      },
      // 取消添加管理员
      cancelAddAdmin() {
        this.addAdminVisible = false;
        // 清空addFrom，初始化dialog
        this.addForm = { userName: "", password: "", againPassword: "", userImg: "", level: 1 };
        this.editAdminText = "添加管理员";
        this.editAdminPw = true;
      },
      // 添加管理员
      addAdmin() {
        if(this.addForm.userName == "" || this.addForm.userImg == "" || this.addForm.password == "" || this.addForm.againPassword == "") {
          this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
        }else {
          let reg = new RegExp("[\\u4E00-\\u9FFF]+","g");     // 密码为汉字的正则校验
          if(this.addForm.password.length < 4 || this.addForm.againPassword.length < 4) {
            this.$message({ message: "密码不可短于四位", type: 'warning', duration: 1500 });
          }else if(reg.test(this.addForm.password) || reg.test(this.addForm.againPassword)) {
            this.$message({ message: "密码不可为汉字", type: 'warning', duration: 1500 });
          }else if(this.addForm.password != this.addForm.againPassword) {
            this.$message({ message: "两次输入的密码不一致", type: 'warning', duration: 1500 });
            // 清除已输入的密码
            this.addForm.password = "";
            this.addForm.againPassword = "";
          }else if(this.addForm.password == this.addForm.againPassword) {
            // 添加管理员
            let params = {
              suname: this.addForm.userName,
              password: this.addForm.password,
              suheader: this.addForm.userImg,
            };
            // 用户等级传string，只有0需要处理
            if(this.addForm.level == 0) {
              params.sulevel = "0";
            }
            axios.post(api.add_admin + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: "保存成功", type: 'success', duration: 1500 });

                // 关闭dialog，清空addFrom
                this.addAdminVisible = false;
                this.addForm = { userName: "", password: "", againPassword: "", userImg: "", level: 1 };
              }else{
                this.$message.error(res.data.message);
              }
            });
          }
        }
      },
      // 保存编辑的管理员
      saveEditAdmin() {
        let params = {
          suid: this.adminList[this.row].suid,
          suname: this.addForm.userName,
          suheader: this.addForm.userImg
        };
        // 用户等级传string，只有0需要处理
        if(this.addForm.level == 0) {
          params.sulevel = "0";
        }else if(this.addForm.level != 0) {
          params.sulevel = this.addForm.level;
        }
        // 如果编辑了管理员的密码则把密码加入params
        if(this.editAdminPw) {
          let reg = new RegExp("[\\u4E00-\\u9FFF]+","g");     // 密码为汉字的正则校验
          if(this.addForm.password == undefined || this.addForm.againPassword == undefined) {
            this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
          }else {
            if(this.addForm.password.length < 4 || this.addForm.againPassword.length < 4) {
              this.$message({ message: "密码不可短于四位", type: 'warning', duration: 1500 });
            }else if(reg.test(this.addForm.password) || reg.test(this.addForm.againPassword)) {
              this.$message({ message: "密码不可为汉字", type: 'warning', duration: 1500 });
            }else if(this.addForm.password != this.addForm.againPassword) {
              this.$message({ message: "两次输入的密码不一致", type: 'warning', duration: 1500 });
              // 清除已输入的密码
              this.addForm.password = "";
              this.addForm.againPassword = "";
            }else if(this.addForm.password == this.addForm.againPassword) {
              params.password = this.addForm.password;
              this.saveAdmin(params);   // 保存新编辑的管理员
            }
          }
        }else {
          this.saveAdmin(params);   // 保存新编辑的管理员
        }
      },
      // 保存新编辑的管理员
      saveAdmin(params) {
        this.adminLoading = true;
        axios.post(api.update_admin + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: "保存成功", type: 'success', duration: 1500 });
            this.adminLoading = false;

            // 关闭dialog，清空addFrom，dialog初始化
            this.addAdminVisible = false;
            this.editAdminText = "添加管理员";
            this.editAdminPw = true;
            this.addForm = { userName: "", password: "", againPassword: "", userImg: "", level: 1 };
          }else{
            this.$message.error(res.data.message);
          }
        });
      },
      // 点击编辑管理员数据按钮所对应的方法
      editAdmin(scope) {
        this.row = scope.$index;
        this.editAdminText = "编辑管理员";
        this.editAdminPw = false;
        this.addAdminVisible = true;
        this.addForm = { userName: scope.row.suname, userImg: scope.row.suheader, level: scope.row.sulevel };
      },
      // 编辑管理员状态
      editAdminStatus(scope, where) {
        this.adminLoading = true;
        let params = {};
        if(where == "lock") {             // 封禁管理员
          params = { suid: scope.row.suid, suisfreeze: true };
          axios.post(api.update_admin + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "封禁成功", type: 'success', duration: 1500 });
              this.adminList[scope.$index].suStatus = "封禁中";
              this.adminList = this.adminList.concat();
              this.adminLoading = false;
            }else{
              this.$message.error(res.data.message);
            }
          });
        }else if(where == "unlock") {     // 解封管理员
          params = { suid: scope.row.suid, suisfreeze: false };
          axios.post(api.update_admin + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "解封成功", type: 'success', duration: 1500 });
              this.adminList[scope.$index].suStatus = "正常";
              this.adminList = this.adminList.concat();
              this.adminLoading = false;
            }else{
              this.$message.error(res.data.message);
            }
          });
        }else if(where == "delete") {     // 删除管理员
          params = { suid: scope.row.suid, suisdelete: true };
          axios.post(api.update_admin + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "删除成功", type: 'success', duration: 1500 });
              this.adminList.splice(scope.$index, 1);
              this.adminLoading = false;
            }else{
              this.$message.error(res.data.message);
            }
          });
        }
      },
      // 点击封禁、解封、激活管理员产生的Dialog变化
      lockAdmin(title) {
        this.operation = title;
        this.dialog = 'changeMAstatus'
      },
      // 封禁、解封、激活管理员的方法
      changeMAstatus() {
        let that = this
        let MAstatus = ''
        if(this.row.MAstatus == '未激活' || this.row.MAstatus == '禁用') {
          MAstatus = '可用'
        }else if(this.row.MAstatus == '可用') {
          MAstatus = '禁用'
        }
        let params = {
          MAtelphone: this.row.MAtelphone,
          MAstatus: MAstatus
        }
        axios.post(api.update_manager_by_matel+'?token='+localStorage.getItem('token'), params).then(res => {
          console.log(res)
          if(res.data.status == 200){
            this.editAdminVisible = false
            this.$message({ message:res.data.message, type:'success' });
            that.getData();
          }
        })
      },
      // 更改用户头像
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      },
      // 更改密码
      changePwDone() {
        if(this.form.againNewPw != this.form.newPw) {
          this.$message.error('两次密码输入不一致');
        }else {
          this.$message({ type: 'success', message: '操作成功!' });
          this.dialog = 'index';
        }
      },
      // 页面刷新的方法
      freshClick(){
        console.log('fresh');
      }
    },
    mounted() {
      this.getAdmin();      // 获取管理员
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  @import "../../common/css/weidian.less";
  .m-content {
    padding: 0.2rem;
    background-color: @bgMainColor;
    .m-top {
      display: flex;
      justify-content: flex-end;
    }
    .m-top-button-button {
      background-color: @btnActiveColor;
      border-color: @btnActiveColor;
      color: @bgMainColor;
      float: right;
      font-size: 14px;
    }
    .m-middle {
      .user-img {
        width: 0.3rem;
        height: 0.3rem;
      }
      .edit-admin-button {
        color: @sidebarChildColor;
      }
      /*.el-crud {
        font-size: 14px;
        color: #000000;
      }*/
      .edit-dialog {
        .el-form-item {
          margin-bottom: 0;
        }
        // 更改用户头像
        .avatar-uploader {
          text-align: center;
        }
        .avatar-uploader .el-upload {
          border-radius: 6px;
          cursor: pointer;
          position: relative;
          overflow: hidden;
        }
        .avatar-uploader .el-upload:hover {
          border-color: #409EFF;
        }
        .avatar-uploader-icon {
          font-size: 18px;
          color: #8c939d;
          width: 0.85rem;
          height: 0.85rem;
          line-height: 0.85rem;
          text-align: center;
        }
        .avatar {
          width: 0.85rem;
          height: 0.85rem;
          display: block;
        }
        height: 1.6rem;
        .change {
          float: left;
          width: 28%;
          margin-left: 0.2rem;
          text-align: center;
          .change-pictures {
            width: 0.85rem;
            height: 0.85rem;
          }
        }
      }
      .add-dialog {
        .el-form-item {
          margin-bottom: 0.1rem;
        }
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0 0;
    }
  }
  .m-top-button-button {
    background-color: @btnActiveColor;
    border-color: @btnActiveColor;
    color: @bgMainColor;
    float: right;
    font-size: 14px;
  }
  .top-btn {
    padding: 0.04rem 0.1rem;
  }
  .btn-width {
    width: 0.65rem;
  }
</style>
