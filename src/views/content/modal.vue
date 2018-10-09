<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <w-tab :list="tab_list" @wTabClick="wTabClick"></w-tab>
      <!--首页-->
     <div class="m-index" v-if="page == '首页'">
       <h3 class="m-title">浮窗管理</h3>

       <div class="title-img-box">
         <h3 class="m-title">任务等级管理</h3>
         <img v-if="levelTableClose" class="table-close-img" src="../../assets/images/table_close.png" @click="tableOpen">
         <img v-if="!levelTableClose" class="table-close-img" src="../../assets/images/table_open.png" @click="tableOpen">
       </div>

       <div v-if="!levelTableClose" class="content-table">
         <el-table :data="levelList" border style="width: 100%" v-loading="levelLoading">
           <el-table-column prop="talevel" label="任务等级" width="120"></el-table-column>
           <el-table-column prop="reward" label="奖励方式"></el-table-column>
           <el-table-column prop="doneTip" label="完成提示" width="120"></el-table-column>
           <el-table-column prop="tarole" label="规则"></el-table-column>
           <el-table-column fixed="right" label="管理" width="150">
             <template slot-scope="scope">
               <el-button @click="editDone(scope.row)" type="text" size="small">编辑</el-button>
               <el-button type="text" size="small" readonly>|</el-button>
               <el-button @click="deleteDone" type="text" size="small">删除</el-button>
             </template>
           </el-table-column>
         </el-table>
       </div>

       <h3 class="m-title">任务管理</h3>
       <div class="content-table">
         <el-table :data="taskList" border style="width: 100%" v-loading="taskLoading">
           <el-table-column prop="taname" label="任务标题"></el-table-column>
           <el-table-column prop="tatype" label="任务类型"></el-table-column>
           <el-table-column fixed="right" label="管理" width="260">
             <template slot-scope="scope">
               <el-button @click="editDone(scope.row)" type="text" size="small">编辑</el-button>
               <el-button type="text" size="small" readonly>|</el-button>
               <el-button @click="deleteDone" type="text" size="small">删除</el-button>
             </template>
           </el-table-column>
         </el-table>
       </div>

       <el-form :label-position="labelPosition" label-width="100px" :model="formIndex">
         <div class="m-form-item m-item-modal">
           <el-form-item label="任务等级" class="required">
             <el-select v-model="formIndex.taskLevel" clearable placeholder="请选择">
               <el-option v-for="item in taskLevelList" :key="item.value" :label="item.label" :value="item.value"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="任务标题" class="required">
             <el-input v-model="formIndex.title" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="任务类型" class="required">
             <el-select v-model="taskType" clearable placeholder="请选择" @change="taskTypeChange" @clear="clearType">
               <el-option v-for="item in taskTypeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="图标" class="m-s required" style="width: 2rem;">
             <el-upload class="avatar-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                        :on-success="uploadPicture">
               <img v-if="imageUrl" :src="imageUrl" class="avatar">
               <i v-else class="el-icon-plus avatar-uploader-icon"></i>
             </el-upload>
           </el-form-item>
           <el-form-item :label="video_ratio" class="required">
             <el-input v-model="formIndex.content" class="m-input-m"></el-input>
           </el-form-item>
         </div>
         <el-form-item label="备注">
           <el-input v-model="formIndex.memo" class="m-input-m"></el-input>
         </el-form-item>
         <el-form-item label="活动时间">
           <el-date-picker v-model="activityTime" type="datetimerange" range-separator="至"
                           value-format="yyyy-MM-dd HH:mm:ss"
                           start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
           </el-date-picker>
         </el-form-item>
         <el-form-item label="持续时间">
           <el-input v-model="formIndex.duration" class="m-input-m">
             <template slot="append">天</template>
           </el-input>
           <span class="m-item-add">+</span>
         </el-form-item>
       </el-form>
     </div>
      <!--发现-->
      <div class="m-discovery" v-if="page == '发现'">
        <h3 class="m-title">弹框图片</h3>
        <div class="m-form-item">
          <div class="m-item-content">
            <div class=" m-item-row m-f">
              <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
          </div>
        </div>
      </div>
      <!--我的-->
      <div class="m-personal" v-if="page == '我的'">
        <div class="m-personal-left-right">
          <h3 class="m-title">规则弹框</h3>
          <div class="m-form-item-box">
            <div class="m-form-img-item">
              <p class="m-form-label">等级规则（未开店）</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">等级规则（已开店）</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">专属粉丝管理规则</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">开店邀请海报规则</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="m-personal-left-right">
          <h3 class="m-title">弹框图片</h3>
          <div class="m-form-item-box">
            <div class="m-form-img-item">
              <p class="m-form-label">邀请专属粉丝海报</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label"></p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">邀请开店海报</p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label"></p>
              <div class="m-item-content">
                <div class=" m-item-row m-f">
                  <el-upload
                    class="avatar-uploader"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="m-form-item-box" v-if="page == '我的'">
        <div class="m-form-img-item">
          <p class="m-form-label">我的导师</p>
          <div class="m-item-content">
            <div class=" m-item-row m-f">
              <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
          </div>
        </div>
      </div>

      <div class="m-form-confirm-btn ">
        <span v-if="page == '首页'">暂停</span>
        <span @click="submit">发布</span>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    data(){
      return{
        page:'首页',
        name:'弹框管理',
        tab_list:[
          { name:'首页', url:'', active:true },
          { name:'发现', url:'', active:false },
          { name:'我的', url:'', active:false }
        ],
        levelTableClose: true,
        levelList: [],
        levelLoading: true,
        taskList: [],
        taskLoading: true,
        activityTime: [],
        video_ratio: "视频/完成度",

        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value: '',
        taskLevelList: [
          { value: "1", label: "等级 1" }, { value: "2", label: "等级 2" }, { value: "3", label: "等级 3" }, { value: "4", label: "等级 4" }
        ],
        taskType: '',
        taskTypeList: [{ value: "", label: "" }],
        imageUrl:'',
        labelPosition:'left',
        formIndex:{ value:'', title: '', content: '', ratio: '', memo: '', rule: '', duration: '', taskLevel: '' },
      }
    },
    components:{ pageTitle, wTab },
    methods:{
      // 获取所有任务等级
      getAllTaskLevel() {
        axios.get(api.get_all_task_level + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.levelList = res.data.data;
            this.levelLoading = false;
            for(let i = 0; i < this.levelList.length; i ++) {
              this.levelList[i].talevel = '等级' + this.levelList[i].talevel;
              this.levelList[i].doneTip = "【图片】";

              // 显示奖励
              let raward = this.levelList[i].raward;
              this.levelList[i].reward = "";
              for(let j = 0; j < raward.length; j ++) {
                if(raward[j].ratype == 0) {
                  // 如果是多个奖励，则在每两个奖励之间加上 + 号
                  if(this.levelList[i].reward) {
                    this.levelList[i].reward = this.levelList[i].reward + " + ";
                  }
                  this.levelList[i].reward = this.levelList[i].reward + raward[j].ranumber + "张满" + raward[j].rafilter + "-" + raward[j].raamount + "新衣币";
                }else if(raward[j].ratype == 1) {
                  if(this.levelList[i].reward) {
                    this.levelList[i].reward = this.levelList[i].reward + " + ";
                  }
                  if(raward[j].ranumber == 1) {
                    this.levelList[i].reward = this.levelList[i].reward + "售出首单佣金上涨" + raward[j].raratio + "%";
                  }else if(raward[j].ranumber > 1) {
                    this.levelList[i].reward = this.levelList[i].reward + "佣金上涨" + raward[j].raratio + "%";
                  }
                }else if(raward[j].ratype == 2) {
                  if(this.levelList[i].reward) {
                    this.levelList[i].reward = this.levelList[i].reward + " + ";
                  }
                  this.levelList[i].reward = this.levelList[i].reward + raward[j].ranumber + "张" + raward[j].raamount + "元无门槛新衣币";
                }
              }
            }
            // console.log(this.levelList);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 获取所有任务
      getAllTask(){
        axios.get(api.get_all_task + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.taskList = res.data.data;
            // console.log(this.taskList);

            for(let i = 0; i < this.taskList.length; i ++) {

              // 判断任务类型   0: "满减", 1: "佣金加成", 2: "无门槛"
              switch (this.taskList[i].tatype){
                case 0:
                  this.taskList[i].tatype = this.taskTypeList[0].label;
                  break;
                case 1:
                  this.taskList[i].tatype = this.taskTypeList[1].label;
                  break;
                case 2:
                  this.taskList[i].tatype = this.taskTypeList[2].label;
                  break;
                case 3:
                  this.taskList[i].tatype = this.taskTypeList[3].label;
                  break;
              }
            }
            this.taskLoading = false;
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 获取任务类型
      getAllTaskType() {
        axios.get(api.get_all_task_type).then(res => {
          if(res.data.status == 200){
            for(let i = 0; i < res.data.data.length; i ++) {
              this.taskTypeList[i] = { value: i, label: res.data.data[i] };
            }
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 选择任务类型
      taskTypeChange(v) {
        console.log(v)
        // 任务类型为观看视频时，视频。否则为完成度
        if(String(v) == "") {
          this.video_ratio = "视频/完成度";
        }
        if(String(v) == "0") {
          this.video_ratio = "视频";
        }
        if(String(v) == "1" || String(v) == "2" || String(v) == "3") {
          this.video_ratio = "完成度";
        }
      },
      // 清空任务类型选择时
      clearType(v) {
        // console.log(v);
      },
      // 打开/关闭任务表格
      tableOpen() {
        if(this.levelTableClose) {
          this.levelTableClose = false;
          // this.getAllTaskLevel();   // 获取所有任务等级
        }else if(!this.levelTableClose) {
          this.levelTableClose = true;
        }
      },

      // 上传任务图标图片
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = task", form).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }
          // console.log(res.data);
          this.imageUrl = res.data.data;
        });
      },
      // 编辑按钮
      editDone(row) {
        console.log(row);
      },
      // 删除按钮
      deleteDone() {
        this.$confirm('此操作将删除该任务, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({ type: 'success', message: '删除成功!' });
        }).catch(() => {
          this.$message({ type: 'info', message: '已取消删除' });
        });
      },
      // 弹框管理-首页-提交   添加任务
      submit() {
        let params = {
          TAname: this.formIndex.title,
          TAtype: this.taskType,
          TAhead: this.imageUrl,
          TLid: this.formIndex.taskLevel,
          TAstartTime: this.activityTime[0],
          TAendTime: this.activityTime[1],
          TAduration: this.formIndex.duration,
          TAmessage: this.formIndex.memo,
          TAurl: this.formIndex.content
        };
        if(params.TAname == "" || String(params.TAtype) == "" || params.TAhead == "" || params.TLid == "" || params.TAurl == "") {
          this.$message({ type: 'warning', message: '请填写全部必填项' });
          console.log(params.TAname == "", String(params.TAtype) == "", params.TAhead == "", params.TLid == "", params.TAurl == "")
        }else {
          axios.post(api.add_task + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success' });
              this.getAllTask();        // 获取所有任务

              this.formIndex.title = "";
              this.formIndex.taskLevel = "";
              this.formIndex.duration = "";
              this.formIndex.memo = "";
              this.formIndex.content = "";
              this.taskType = "";
              this.imageUrl = "";
              this.activityTime = [];

            }else{
              this.$message.error(res.data.message);
            }
          }, res=>{
            this.$message.error(res.data.message);
          });
        }
      },
      // 顶部首页、发现、我的点击切换
      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.page = arr[i].name
        this.tab_list = [].concat(arr);
      },
    },
    watch:{
      // 判断活动时间是否有问题
      activityTime(newValue, oldValue) {
        if(!this.activityTime) {
          if(newValue[0] == newValue[1]) {
            this.$message.error("活动时间不正确，请重新选择");
            this.activityTime = "";
          }
        }
      }
    },
    mounted() {
      this.getAllTaskLevel();   // 获取所有任务等级
      this.getAllTaskType();    // 获取任务类型
      this.getAllTask();        // 获取所有任务
    }
  }
</script>

<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/weidian";
  .m-title{
    font-size: 18px;
    margin-bottom: 0.1rem;
  }
  .title-img-box {
    display: flex;
    justify-content: flex-start;
  }
  .table-close-img {
    width: 0.18rem;
    height: 0.12rem;
    padding: 0.02rem 0 0 0.2rem;
  }
  .avatar {
    width: 0.85rem;
    height: 0.85rem;
  }

/*  !* 设置滚动条的样式 *!
  ::-webkit-scrollbar {
    width: 10px;
  }
  !* 滚动槽 *!
  ::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    border-radius: 10px;
  }
  !* 滚动条滑块 *!
  ::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: #bbb;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
  }
  ::-webkit-scrollbar-thumb:window-inactive {
    background: #bbb;
  }*/
</style>
