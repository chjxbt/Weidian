<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <w-tab :list="tab_list" @wTabClick="wTabClick"></w-tab>
      <!--首页-->
     <div class="m-index" v-if="page == '首页'">

       <div class="content-table">
         <el-table :data="tableData" border style="width: 100%">
           <el-table-column prop="taname" label="任务标题" width="240"></el-table-column>
           <el-table-column prop="tatype" label="任务类型" width="240"></el-table-column>
           <el-table-column prop="reward" label="奖励方式"></el-table-column>
           <el-table-column fixed="right" label="管理" width="240">
             <template slot-scope="scope">
               <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
               <el-button type="text" size="small">|</el-button>
               <el-button type="text" size="small">删除</el-button>
             </template>
           </el-table-column>
         </el-table>
       </div>

       <h3 class="m-title">浮窗管理</h3>
       <el-form :label-position="labelPosition" label-width="100px" :model="formIndex">
         <div class="m-form-item m-item-modal">
           <el-form-item label="任务等级">
             <el-select v-model="taskLevel" placeholder="请选择">
               <el-option v-for="item in taskLevelList" :key="item" :label="item" :value="item"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="任务标题">
             <el-input v-model="formIndex.title" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="任务类型">
             <el-select v-model="taskType" placeholder="请选择" @change="taskTypeChange">
               <el-option v-for="item in taskTypeList" :key="item" :label="item" :value="item"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="图标" class="m-s">
             <el-upload
               class="avatar-uploader"
               action="https://jsonplaceholder.typicode.com/posts/"
               :show-file-list="false"
               :on-success="handleAvatarSuccess"
               :before-upload="beforeAvatarUpload">
               <img v-if="imageUrl" :src="imageUrl" class="avatar">
               <i v-else class="el-icon-plus avatar-uploader-icon"></i>
             </el-upload>
           </el-form-item>
           <el-form-item label="内容">
             <el-input v-model="formIndex.content" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="完成度">
             <el-input v-model="formIndex.ratio" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="完成提示" class="m-f">
             <el-upload
               class="avatar-uploader"
               action="https://jsonplaceholder.typicode.com/posts/"
               :show-file-list="false"
               :on-success="handleAvatarSuccess"
               :before-upload="beforeAvatarUpload">
               <img v-if="imageUrl" :src="imageUrl" class="avatar">
               <i v-else class="el-icon-plus avatar-uploader-icon"></i>
             </el-upload>
           </el-form-item>
         </div>
         <el-form-item label="奖励方式">
           <el-select v-model="value" placeholder="请选择">
             <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
           </el-select>
         </el-form-item>
         <el-form-item label="备注">
           <el-input v-model="formIndex.memo" class="m-input-m"></el-input>
         </el-form-item>
         <el-form-item label="活动时间">
           <el-date-picker v-model="value7" type="daterange" align="right" unlink-panels
                           range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"
                           :picker-options="pickerOptions2">
           </el-date-picker>
           <span class="m-item-add">+</span>
         </el-form-item>
         <el-form-item label="规则">
           <textarea v-model="formIndex.rule" class="m-textarea" placeholder="请输入内容"></textarea>
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
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
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
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </div>
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
        tableData: [],
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
        taskLevel: '',
        taskLevelList: [1, 2, 3, 4],
        taskType: '',
        taskTypeList: [],
        imageUrl:'',
        labelPosition:'left',
        formIndex:{ value:'', title: '', content: '', ratio: '', memo: '', rule: '' },
        pickerOptions2: {
          shortcuts: [{
            text: '最近七天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三十天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近九十天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value7: ''
      }
    },
    components:{ pageTitle, wTab },
    methods:{
      // 任务列表的操作栏方法
      handleClick(row) {
        console.log(row);
      },
      // 获取所有任务
      getAllTask(){
        axios.get(api.get_all_task + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.tableData = res.data.data;

            // 显示奖励内容   0: "满减", 1: "佣金加成", 2: "无门槛"
            for(let i = 0; i < this.tableData.length; i ++) {

              // 判断任务类型   0: "满减", 1: "佣金加成", 2: "无门槛"
              /*if(this.tableData[i].tatype == 0) {
                this.tableData[i].tatype = "满减";
              }else if(this.tableData[i].tatype == 1) {
                this.tableData[i].tatype = "佣金加成";
              }else if(this.tableData[i].tatype == 2) {
                this.tableData[i].tatype = "无门槛";
              }*/

              let raward = res.data.data[i].raward;
              this.tableData[i].reward = "";
              for(let j = 0; j < raward.length; j ++) {
                if(raward[j].ratype == 0) {
                  this.tableData[i].reward = this.tableData[i].reward + raward[j].ranumber + "张满" + raward[j].rafilter + "-" + raward[j].raamount + "新衣币";
                }else if(raward[j].ratype == 1) {
                  if(raward[j].ranumber == 1) {
                    this.tableData[i].reward = this.tableData[i].reward + " + 售出首单佣金上涨" + raward[j].raratio + "%";
                  }else if(raward[j].ranumber > 1) {
                    this.tableData[i].reward = this.tableData[i].reward + " + 佣金上涨" + raward[j].raratio + "%";
                  }
                }else if(raward[j].ratype == 2) {

                }
              }
              // console.log(this.tableData[i]);
            }

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
            this.taskTypeList = res.data.data;
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 选择任务类型
      taskTypeChange(v) {
        console.log(v);
      },
      // 首页提交
      submit() {
        console.log(this.formIndex);
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
      handleAvatarSuccess(){

      },
      beforeAvatarUpload(){

      }
    },
    mounted() {
      this.getAllTask();
      this.getAllTaskType();
    }
  }
</script>

<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/weidian";
  .m-title{
    font-size: 18px;
    margin-bottom: 0.1rem;
  }
</style>
