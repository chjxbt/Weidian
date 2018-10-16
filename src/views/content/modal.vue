<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <w-tab :list="tab_list" @wTabClick="wTabClick"></w-tab>
      <!--首页-->
     <div class="m-index" v-if="page == '首页'">
       <!--<h3 class="m-title">浮窗管理</h3>-->

       <div class="title-img-box">
         <h3 class="m-title">任务等级奖励管理</h3>
         <img v-if="levelTableClose" class="table-close-img" src="../../assets/images/table_close.png" @click="tableOpen">
         <img v-if="!levelTableClose" class="table-close-img" src="../../assets/images/table_open.png" @click="tableOpen">
       </div>

       <div v-if="!levelTableClose" class="content-table" style="margin-bottom: 0.2rem">
         <el-table :data="levelList" border style="width: 100%" v-loading="levelLoading">
           <el-table-column prop="taLevel" label="任务等级" width="120"></el-table-column>
           <!--<el-table-column prop="raward" label="奖励方式" v-if="scope.row.disabled"></el-table-column>-->
           <el-table-column prop="raward" label="奖励方式">
             <template slot-scope="scope">
               <p v-if="scope.row.raward">{{scope.row.raward}}<span class="edit-reward-btn" v-if="!scope.row.disabled" @click="editReward(scope)">编辑</span></p>
               <p v-else>暂无奖励<span class="edit-reward-btn" v-if="!scope.row.disabled" @click="editReward(scope)">编辑</span></p>
             </template>
           </el-table-column>
           <el-table-column prop="tacomplatenotifications" label="完成提示" width="120">
             <template slot-scope="scope">
               <div @click="rowClick(scope.$index, 'img')">
                 <el-upload class="task-done-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                            :on-success="uploadTaskDonePicture" :disabled="scope.row.disabled">
                   <img v-if="scope.row.tacomplatenotifications" :src="scope.row.tacomplatenotifications" class="task-done-icon">
                   <i v-else class="el-icon-plus task-done-icon"></i>
                 </el-upload>
               </div>
             </template>
           </el-table-column>
           <el-table-column prop="tarole" label="规则">
             <template slot-scope="scope">
               <el-input v-model="scope.row.tarole" size="mini" placeholder="请输入任务等级规则" :disabled="scope.row.disabled"></el-input>
             </template>
           </el-table-column>
           <el-table-column fixed="right" label="管理" width="150">
             <template slot-scope="scope">
               <el-button @click="editDone(scope, 'taskLevel')" type="text" size="small" v-if="scope.row.disabled">编辑</el-button>
               <el-button @click="saveTaskLevel(scope, 'cancel')" type="text" size="small" v-if="!scope.row.disabled">取消</el-button>
               <el-button type="text" size="small" readonly>|</el-button>
               <el-button @click="deleteDone(scope, 'level')" type="text" size="small" v-if="scope.row.disabled">删除</el-button>
               <el-button @click="saveTaskLevel(scope, 'save')" type="text" size="small" v-if="!scope.row.disabled">保存</el-button>
             </template>
           </el-table-column>
         </el-table>

         <el-tooltip class="item" effect="light" content="添加任务等级奖励" placement="right">
           <span class="m-item-add" style="left: 3.5rem; margin-top: 0.05rem" v-if="!rewardEdit" @click="addTaskLevel">+</span>
         </el-tooltip>

         <div v-if="rewardEdit">
           <div class="reward-title">请编辑{{rewardTitle}}的奖励方式：</div>
           <div class="level-reward-box" v-for="(item, index) in rewardBoxList">
             <el-input v-model="item.ranumber" placeholder="数量" class="reward-num">
               <template slot="append">张</template>
             </el-input>
             <el-select v-model="item.raid" clearable placeholder="请选择任务等级奖励内容" class="reward-content">
               <el-option v-for="item in rewardList" :key="item.raid" :label="item.rewardstr" :value="item.raid"></el-option>
             </el-select>
             <div class="add-btn" @click="addReward(index)">-</div>
             <div class="add-btn" v-if="index == (rewardBoxList.length - 1)" @click="addReward()">+</div>
           </div>
         </div>
       </div>

       <h3 class="m-title">任务管理</h3>
       <div class="content-table">
         <el-table :data="taskList" border style="width: 100%" v-loading="taskLoading">
           <el-table-column prop="taname" label="任务标题"></el-table-column>
           <el-table-column prop="tatype" label="任务类型"></el-table-column>
           <el-table-column prop="raward" label="任务奖励"></el-table-column>
           <el-table-column fixed="right" label="管理" width="150">
             <template slot-scope="scope">
               <el-button @click="editDone(scope, 'task')" type="text" size="small">编辑</el-button>
               <el-button type="text" size="small" readonly>|</el-button>
               <el-button @click="deleteDone(scope, 'task')" type="text" size="small">删除</el-button>
             </template>
           </el-table-column>
         </el-table>
       </div>

       <el-form :label-position="labelPosition" label-width="100px" :model="formIndex">
         <div class="m-form-item m-item-modal">
           <el-form-item label="任务名称：" class="required">
             <el-input v-model="formIndex.title" class="m-input-m" placeholder="请输入任务名称"></el-input>
           </el-form-item>
           <el-form-item label="任务等级：" class="required">
             <el-select v-model="formIndex.taskLevel" clearable placeholder="请选择任务等级">
               <el-option v-for="item in levelList" :key="item.talevel" :label="item.taLevel" :value="item.talevel"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="任务类型：" class="required">
             <el-select v-model="taskType" clearable placeholder="请选择任务类型" @change="taskTypeChange" @clear="clearType">
               <el-option v-for="item in taskTypeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
             </el-select>
           </el-form-item>
           <el-form-item label="图标：" class="m-s required" style="width: 2rem; min-height: 1rem">
             <el-upload class="avatar-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                        :on-success="uploadTaskPicture">
               <img v-if="taskImg" :src="taskImg" class="avatar">
               <i v-else class="el-icon-plus avatar-uploader-icon"></i>
             </el-upload>
           </el-form-item>
           <el-form-item :label="video_ratio">
             <el-input v-model="formIndex.content" class="m-input-m" placeholder="选填"></el-input>
           </el-form-item>
         </div>
         <el-form-item label="备注：">
           <el-input v-model="formIndex.memo" class="m-input-m" placeholder="选填"></el-input>
         </el-form-item>
         <el-form-item label="活动时间：">
           <el-date-picker v-model="activityTime" type="datetimerange" range-separator="至"
                           value-format="yyyy-MM-dd HH:mm:ss"
                           start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
           </el-date-picker>
         </el-form-item>
         <el-form-item label="持续时间：">
           <el-input v-model="formIndex.duration" class="m-input-m" placeholder="选填">
             <template slot="append">天</template>
           </el-input>
           <!--<span class="m-item-add">+</span>-->
         </el-form-item>
       </el-form>
     </div>
      <!--发现-->
      <div class="m-discovery" v-if="page == '发现'">
        <h3 class="m-title">弹框图片</h3>
        <div class="m-form-item">
          <div class="m-item-content">
            <div class=" m-item-row">
              <div class="upload-box" @click="setWhichImg('owner')">
                <el-upload class="owner-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                  <img v-if="ownerImg" :src="ownerImg" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </div>
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
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('unRevelRule')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="unRevelRuleImg" :src="unRevelRuleImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">等级规则（已开店）</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('revelRule')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="revelRuleImg" :src="revelRuleImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">专属粉丝管理规则</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('fansRule')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="fansRuleImg" :src="fansRuleImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">开店邀请海报规则</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('invitationRule')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="invitationRuleImg" :src="invitationRuleImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">开店邀请函规则</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('storeInvitation')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="storeInvitationImg" :src="storeInvitationImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
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
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('invitationFans')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="invitationFansImg" :src="invitationFansImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">邀请开店海报</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('invitationStore')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="invitationStoreImg" :src="invitationStoreImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">我的导师</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('myTeacher')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="myTeacherImg" :src="myTeacherImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">专属粉丝收益详情</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('incomeDetail')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="incomeDetailImg" :src="incomeDetailImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">提现帮助</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('withdrawalHelp')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="withdrawalHelpImg" :src="withdrawalHelpImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">客服</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('service')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="serviceImg" :src="serviceImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="m-personal-left-right">
          <h3 class="m-title">专属粉丝</h3>
          <div class="m-form-item-box">
            <div class="m-form-img-item">
              <p class="m-form-label">专属粉丝分享海报</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('fansShare')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="fansShareImg_o" :src="fansShareImg_o" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item" v-if="fansNum > 0">
              <p class="m-form-label">专属粉丝分享海报</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('fansShare')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="fansShareImg_tw" :src="fansShareImg_tw" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item" v-if="fansNum > 1">
              <p class="m-form-label">专属粉丝分享海报</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('fansShare')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="fansShareImg_th" :src="fansShareImg_th" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <!--<div class="m-form-img-item" v-if="fansNum > 2">
              <p class="m-form-label">专属粉丝分享海报</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('fansShare')">
                    <el-upload class="rule-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="fansShareImg_f" :src="fansShareImg_f" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>-->
          </div>
        </div>
        <div class="m-personal-left-right">
          <h3 class="m-title">静态广告</h3>
          <div class="m-form-item-box">
            <div class="m-form-img-item" style="margin-right: 0.7rem">
              <p class="m-form-label">小静态广告</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('smallAd')">
                    <el-upload class="small-ad-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="smallAdImg" :src="smallAdImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-form-img-item">
              <p class="m-form-label">大静态广告</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <div class="upload-box" @click="setWhichImg('bigAd')">
                    <el-upload class="big-ad-upload" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false" :on-success="uploadPicture">
                      <img v-if="bigAdImg" :src="bigAdImg" class="avatar">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="m-form-confirm-btn ">
        <!--<span v-if="page == '首页'">暂 停</span>-->
        <span @click="clearInput" v-if="editTask">取 消</span>
        <span @click="submit" v-if="!editTask">保 存</span>
        <span @click="saveTask" v-if="editTask">保 存</span>
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
        levelTableClose: false,      // 任务等级管理隐藏
        levelList: [],              // 任务等级list
        levelIndex: "",             // 正在编辑的任务等级行号
        rewardEdit: false,          // 任务奖励编辑中
        rewardTitle: "",            // 任务奖励编辑时的标题
        rewardNum: "",              // 任务等级奖励的数量
        rewardValue: "",            // 任务等级奖励的选中值
        rewardList: [],             // 任务奖励list
        rewardBoxList: [],          // 任务奖励合集list
        rowNum: "",                 // 确定点击的图片是第几行的
        levelLoading: true,         // 任务表格加载中
        taskList: [],               // 任务表格
        taskLoading: false,         // 任务表格加载中
        editTask: false,            // 是否在编辑任务
        editTaskRow: "",            // 正在编辑的任务行号
        activityTime: [],           // 任务的活动时间
        video_ratio: "视频/完成度：",
        ownerImg: "",               // 发现页 - 弹框图片
        unRevelRuleImg: "",         // 等级规则 - 未开店
        revelRuleImg: "",           // 等级规则 - 已开店
        fansRuleImg: "",            // 等级规则 - 专属粉丝管理规则
        invitationRuleImg: "",      // 等级规则 - 开店邀请海报规则
        invitationFansImg: "",      // 邀请专属粉丝海报
        fansShareImg_o: "",         // 专属粉丝分享海报
        fansShareImg_tw: "",        // 专属粉丝分享海报
        fansShareImg_th: "",        // 专属粉丝分享海报
        // fansShareImg_f: "",         // 专属粉丝分享海报
        invitationStoreImg: "",     // 邀请开店海报
        myTeacherImg: "",           // 我的导师
        withdrawalHelpImg: "",      // 提现帮助
        serviceImg: "",             // 客服
        storeInvitationImg: "",     // 开店邀请函规则
        incomeDetailImg: "",        // 邀请专属粉丝的收益详情
        smallAdImg: "",             // 我的 - 小静态广告
        bigAdImg: "",               // 我的 - 大静态广告
        whichImg: "",               // 用来暂存是哪个img
        fansNum: 0,                 // 用来暂存已经上传多少个专属粉丝分享海报
        taskType: '',               // 任务类型
        taskTypeList: [{ value: "", label: "" }],   // 任务类型list
        taskImg:'',                 // 任务图标
        labelPosition: 'left',      // 表单左对齐
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
              this.levelList[i].taLevel = '等级' + this.levelList[i].talevel;
              this.levelList[i].disabled = true;
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取所有任务
      getAllTask(){
        this.taskLoading = true;
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
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取所有任务奖励
      getAllRaward(){
        this.levelLoading = true;
        axios.get(api.get_all_raward + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.rewardList = res.data.data;
            // console.log(this.rewardList);

            this.levelLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取任务类型
      getAllTaskType() {
        axios.get(api.get_all_task_type).then(res => {
          if(res.data.status == 200){
            for(let i = 0; i < res.data.data.length; i ++) {
              this.taskTypeList[i] = { value: i, label: res.data.data[i] };
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 选择任务类型
      taskTypeChange(v) {
        // 任务类型为观看视频时，视频。否则为完成度
        if(String(v) == "") {
          this.video_ratio = "视频/完成度：";
        }else if(String(v) == "0") {
          this.video_ratio = "视频：";
        }else if(String(v) == "1" || String(v) == "2" || String(v) == "3") {
          this.video_ratio = "完成度：";
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

      // 编辑任务奖励的内容和数量
      editReward(scope) {
        // console.log(scope.row);
        this.rewardTitle = scope.row.taLevel;
        this.getAllRaward();      // 获取所有奖励 - 用于任务等级奖励管理的编辑

        this.rewardEdit = true;
        if(scope.row.rawardparams == undefined) {
          this.addReward();
        }else {
          this.rewardBoxList = scope.row.rawardparams;
        }
        console.log(this.rewardBoxList);
      },

      // 确定暂存是哪个img
      setWhichImg(which) {
        this.whichImg = which;
      },

      // 上传发现页/我的 - 各种图片
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = modal", form).then(res => {
          if(res.data.status == 200){
            // 根据不同img，将结果赋值给不同的img
            if(this.whichImg == "owner") {
              this.ownerImg = res.data.data;            // 发现页 - 弹框图片
            }else if(this.whichImg == "unRevelRule") {
              this.unRevelRuleImg = res.data.data;      // 等级规则 - 未开店
            }else if(this.whichImg == "revelRule") {
              this.revelRuleImg = res.data.data;        // 等级规则 - 已开店
            }else if(this.whichImg == "fansRule") {
              this.fansRuleImg = res.data.data;         // 等级规则 - 专属粉丝管理规则
            }else if(this.whichImg == "invitationRule") {
              this.invitationRuleImg = res.data.data;   // 等级规则 - 开店邀请海报规则
            }else if(this.whichImg == "invitationFans") {
              this.invitationFansImg = res.data.data;   // 邀请专属粉丝海报
            }else if(this.whichImg == "fansShare") {
              if(this.fansNum == 0) {
                this.fansShareImg_o = res.data.data;    // 专属粉丝分享海报
                this.fansNum += 1;
              }else if(this.fansNum == 1) {
                this.fansShareImg_tw = res.data.data;   // 专属粉丝分享海报
                this.fansNum += 1;
              }else if(this.fansNum == 2) {
                this.fansShareImg_th = res.data.data;   // 专属粉丝分享海报
                this.fansNum += 1;
              }/*else if(this.fansNum == 3) {
                this.fansShareImg_f = res.data.data;    // 专属粉丝分享海报
                this.fansNum += 1;
              }*/
            }else if(this.whichImg == "invitationStore") {
              this.invitationStoreImg = res.data.data;  // 邀请开店海报
            }else if(this.whichImg == "myTeacher") {
              this.myTeacherImg = res.data.data;        // 我的导师
            }else if(this.whichImg == "withdrawalHelp") {
              this.withdrawalHelpImg = res.data.data;   // 提现帮助
            }else if(this.whichImg == "service") {
              this.serviceImg = res.data.data;          // 客服
            }else if(this.whichImg == "storeInvitation") {
              this.storeInvitationImg = res.data.data;  // 开店邀请函规则
            }else if(this.whichImg == "incomeDetail") {
              this.incomeDetailImg = res.data.data;     // 邀请专属粉丝的收益详情
            }else if(this.whichImg == "smallAd") {
              this.smallAdImg = res.data.data;          // 我的 - 小静态广告
            }else if(this.whichImg == "bigAd") {
              this.bigAdImg = res.data.data;            // 我的 - 大静态广告
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 上传任务完成的提示图片
      uploadTaskDonePicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = task", form).then(res => {
          if(res.data.status == 200){
            this.levelList[this.rowNum].tacomplatenotifications = res.data.data;
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 上传任务图标图片
      uploadTaskPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = task", form).then(res => {
          if(res.data.status == 200){
            this.taskImg = res.data.data;
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 确定点击的图片是第几行的
      rowClick(index, col) {
        // console.log(col);
        this.rowNum = index;
      },

      // 编辑按钮
      editDone(scope, where) {
        // 任务表格编辑
        if(where == "task") {
          this.editTask = true;
          this.editTaskRow = scope.$index;
          for(let i = 0; i < this.taskTypeList.length; i ++) {
            if(scope.row.tatype = this.taskTypeList[i].label) {
              this.taskType = this.taskTypeList[i].value;
            }
          }
          this.formIndex.title = scope.row.taname;
          this.formIndex.taskLevel = scope.row.tlid;
          this.taskImg = scope.row.tahead;
          this.formIndex.content = scope.row.taurl;
          this.formIndex.memo = scope.row.tamessage;
          this.activityTime = [scope.row.tastarttime, scope.row.taendtime];
          this.formIndex.duration = scope.row.taduration;

        }else if(where == "taskLevel") {    // 任务等级表格编辑
          this.rewardEdit = false;
          this.levelIndex = scope.$index;

          // 可以没有奖励
          if(scope.row.rawardparams == undefined) {
            this.rewardBoxList = [];
          }else {
            this.rewardBoxList = scope.row.rawardparams;
          }

          this.levelList[scope.$index].disabled = false;
          this.levelList = this.levelList.concat();
        }
      },

      // 保存任务等级或取消
      saveTaskLevel(scope, where) {
        if(where == "cancel") {
          this.rewardEdit = false;

          this.levelList[scope.$index].disabled = true;
          this.levelList = this.levelList.concat();
        }else if(where == "save") {
          // console.log(this.levelList[this.levelList.length - 1]);
          let params = {};
          // 新增的任务等级奖励信息
          if(this.levelIndex == "") {
            this.levelIndex = this.levelList.length - 1;
            params = {
              TAlevel: this.levelList[this.levelIndex].talevel,
              TArole: this.levelList[this.levelIndex].tarole,
              TAcomplateNotifications: this.levelList[this.levelIndex].tacomplatenotifications,
              reward: this.rewardBoxList
            };
          }else {     // 编辑任务等级奖励信息
            params = {
              TAlevel: this.levelList[this.levelIndex].talevel,
              TArole: this.levelList[this.levelIndex].tarole,
              TAcomplateNotifications: this.levelList[this.levelIndex].tacomplatenotifications,
              reward: this.rewardBoxList
            };
          }
          this.levelLoading = false;
          axios.post(api.edit_task_level + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success', duration: 1500 });
              this.rewardEdit = false;
              this.getAllTaskLevel();   // 获取所有任务等级奖励内容 - 用于任务等级奖励管理的查看
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }
      },

      // 添加任务等级的+号
      addTaskLevel() {
        // 新加一行任务等级奖励内容
        let index = this.levelList.length;
        this.levelList[index] = {};
        this.levelList[index].disabled = false;
        this.levelList[index].tacomplatenotifications = "";
        this.levelList[index].taLevel = "等级" + (this.levelList[index - 1].talevel + 1);
        this.levelList[index].talevel = this.levelList[index - 1].talevel + 1;
        this.levelList[index].tarole = "";
        this.levelList = this.levelList.concat();
      },

      // 添加任务等级奖励的+号
      addReward(i) {
        // 新加一行任务等级奖励内容
        if(i == undefined) {
          if(this.rewardBoxList == undefined) {
            this.rewardBoxList = [{ ranumber: "", raid: "" }];
          }else {
            let index = this.rewardBoxList.length;
            this.rewardBoxList[index] = {};
            this.rewardBoxList[index].ranumber = "";
            this.rewardBoxList[index].raid = "";
            this.rewardBoxList = this.rewardBoxList.concat();
          }
        }else {
          this.rewardBoxList.splice(i, 1);
        }
      },

      // 删除按钮
      deleteDone(scope, where) {
        this.$confirm('此操作将删除该行, 是否继续?', '提示', {
          confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          if(where == "task") {     // 删除任务
            this.taskLoading = true;
            axios.post(api.del_task + '?token=' + localStorage.getItem('token'),
              { TAid: scope.row.taid }).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.taskList.splice(scope.$index, 1);
                this.taskLoading = false;
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }else if(where == "level") {    // 删除任务等级
            this.levelLoading = true;
            axios.post(api.del_task_level + '?token=' + localStorage.getItem('token'),
              { tlid: scope.row.tlid }).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.levelList.splice(scope.$index, 1);
                this.levelLoading = false;
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }
        }).catch();
      },

      // 弹框管理-首页-提交   添加任务
      submit() {
        if(this.page == "首页") {
          let params = {
            TAname: this.formIndex.title,
            TAtype: this.taskType,
            TAhead: this.taskImg,
            TLid: this.formIndex.taskLevel,
            TAstartTime: this.activityTime[0],
            TAendTime: this.activityTime[1],
            TAduration: this.formIndex.duration,
            TAmessage: this.formIndex.memo,
            TAurl: this.formIndex.content
          };
          if(params.TAname == "" || String(params.TAtype) == "" || params.TAhead == "" || params.TLid == "") {
            this.$message({ type: 'warning', message: '请完整填写', duration: 1500 });
          }else {
            this.taskLoading = true;
            axios.post(api.add_task + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.taskLoading = false;
                this.getAllTask();        // 获取所有任务
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.clearInput();         // 将编辑框置空
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }
        }else if(this.page == "发现" || this.page == "我的") {
          let params = {};
          if(this.page == "发现") {
            params = {
              adimage: [
                { aiimage: this.ownerImg, aitype: "3"}
              ]
            };
          }else if(this.page == "我的") {
            params = {
              adimage: [
                { aiimage: this.unRevelRuleImg, aitype: "4"},
                { aiimage: this.revelRuleImg, aitype: "5"},
                { aiimage: this.fansRuleImg, aitype: "6"},
                { aiimage: this.invitationRuleImg, aitype: "7"},
                { aiimage: this.invitationFansImg, aitype: "9"},
                { aiimage: this.fansShareImg_o, aitype: "10"},
                { aiimage: this.fansShareImg_tw, aitype: "10"},
                { aiimage: this.fansShareImg_th, aitype: "10"},
                // { aiimage: this.fansShareImg_f, aitype: "10"},
                { aiimage: this.invitationStoreImg, aitype: "8"},
                { aiimage: this.myTeacherImg, aitype: "0"},
                { aiimage: this.smallAdImg, aitype: "1"},
                { aiimage: this.bigAdImg, aitype: "2"},
                { aiimage: this.withdrawalHelpImg, aitype: "11"},
                { aiimage: this.serviceImg, aitype: "12"},
                { aiimage: this.storeInvitationImg, aitype: "13"},
                { aiimage: this.incomeDetailImg, aitype: "14"}
              ]
            };
          }
          axios.post(api.add_image + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ type: 'success', message: "保存成功", duration: 1500 });
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }
      },

      // 保存编辑后的任务
      saveTask() {
        let params = {
          TAid: this.taskList[this.editTaskRow].taid,
          TAname: this.formIndex.title,
          TAtype: this.taskType,
          TAhead: this.taskImg,
          TLid: this.formIndex.taskLevel,
          TAstartTime: this.activityTime[0],
          TAendTime: this.activityTime[1],
          TAduration: this.formIndex.duration,
          TAmessage: this.formIndex.memo,
          TAurl: this.formIndex.content
        };
        if(params.TAname == "" || String(params.TAtype) == "" || params.TAhead == "" || params.TLid == "") {
          this.$message({ type: 'warning', message: '请完整填写', duration: 1500 });
        }else {
          this.taskLoading = true;
          axios.post(api.add_task + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success', duration: 1500 });
              // 保存后把新数据回显到表格中
              this.taskList[this.editTaskRow].taname = this.formIndex.title;
              this.taskList[this.editTaskRow].tlid = this.formIndex.taskLevel;
              this.taskList[this.editTaskRow].tahead = this.taskImg;
              this.taskList[this.editTaskRow].taurl = this.formIndex.content;
              this.taskList[this.editTaskRow].tamessage = this.formIndex.memo;
              this.taskList[this.editTaskRow].tastarttime = this.activityTime[0];
              this.taskList[this.editTaskRow].taendtime = this.activityTime[1];
              this.taskList[this.editTaskRow].taduration = this.formIndex.duration;

              this.taskLoading = false;
              this.clearInput();         // 将编辑框置空
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }
      },

      // 将编辑框置空
      clearInput() {
        this.editTask = false;
        this.formIndex.title = "";
        this.formIndex.taskLevel = "";
        this.formIndex.duration = "";
        this.formIndex.memo = "";
        this.formIndex.content = "";
        this.taskType = "";
        this.taskImg = "";
        this.activityTime = [];
      },

      // 顶部首页、发现、我的点击切换
      wTabClick(i){
        this.clearInput();         // 将编辑框置空

        // 获取已有的各种图片
        if(i == 1) {
          axios.get(api.get_img_by_aitype + '?token=' + localStorage.getItem('token') + "&aitype=3").then(res => {
            if(res.data.status == 200) {
              this.ownerImg = res.data.data.aiimage;
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }else if(i == 2) {
          axios.get(api.get_img_by_aitype + '?token=' + localStorage.getItem('token') + "&aitype=[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]").then(res => {
            if(res.data.status == 200) {

              for(let i = 0; i <res.data.data.length; i ++) {
                if(res.data.data[i].aitype == 0) {
                  this.myTeacherImg = res.data.data[i].aiimage;           // 我的导师
                }else if(res.data.data[i].aitype == 1) {
                  this.smallAdImg = res.data.data[i].aiimage;             // 我的 - 小静态广告
                }else if(res.data.data[i].aitype == 2) {
                  this.bigAdImg = res.data.data[i].aiimage;               // 我的 - 大静态广告
                }else if(res.data.data[i].aitype == 4) {
                  this.unRevelRuleImg = res.data.data[i].aiimage;         // 等级规则 - 未开店
                }else if(res.data.data[i].aitype == 5) {
                  this.revelRuleImg = res.data.data[i].aiimage;           // 等级规则 - 已开店
                }else if(res.data.data[i].aitype == 6) {
                  this.fansRuleImg = res.data.data[i].aiimage;            // 等级规则 - 专属粉丝管理规则
                }else if(res.data.data[i].aitype == 7) {
                  this.invitationRuleImg = res.data.data[i].aiimage;      // 等级规则 - 开店邀请海报规则
                }else if(res.data.data[i].aitype == 8) {
                  this.invitationStoreImg = res.data.data[i].aiimage;     // 邀请开店海报
                }else if(res.data.data[i].aitype == 9) {
                  this.invitationFansImg = res.data.data[i].aiimage;      // 邀请专属粉丝海报
                }else if(res.data.data[i].aitype == undefined) {
                  if(res.data.data[i].length == 1) {
                    this.fansNum = 0;
                    this.fansShareImg_o = res.data.data[i][0].aiimage;           // 专属粉丝分享海报
                  }else if(res.data.data[i].length == 2) {
                    this.fansNum = 1;
                    this.fansShareImg_o = res.data.data[i][0].aiimage;           // 专属粉丝分享海报
                    this.fansShareImg_tw = res.data.data[i][1].aiimage;           // 专属粉丝分享海报
                  }else if(res.data.data[i].length == 3) {
                    this.fansNum = 2;
                    this.fansShareImg_o = res.data.data[i][0].aiimage;           // 专属粉丝分享海报
                    this.fansShareImg_tw = res.data.data[i][1].aiimage;           // 专属粉丝分享海报
                    this.fansShareImg_th = res.data.data[i][2].aiimage;           // 专属粉丝分享海报
                  }
                }else if(res.data.data[i].aitype == 11) {
                  this.withdrawalHelpImg = res.data.data[i].aiimage;      // 提现帮助
                }else if(res.data.data[i].aitype == 12) {
                  this.serviceImg = res.data.data[i].aiimage;             // 客服
                }else if(res.data.data[i].aitype == 13) {
                  this.storeInvitationImg = res.data.data[i].aiimage;     // 开店邀请函规则
                }else if(res.data.data[i].aitype == 14) {
                  this.incomeDetailImg = res.data.data[i].aiimage;        // 邀请专属粉丝的收益详情
                }
              }
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }

        let arr = [].concat(this.tab_list);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.page = arr[i].name;
        this.tab_list = [].concat(arr);
      }
    },
    watch:{
      // 判断活动时间是否有问题
      activityTime(newValue, oldValue) {
        if(!this.activityTime) {
          if(newValue[0] == newValue[1]) {
            this.$message({ type: 'error', message: "活动时间不正确，请重新选择", duration: 1500 });
            this.activityTime = "";
          }
        }
      }
    },
    mounted() {
      this.getAllTaskType();    // 获取任务类型 - 用于任务管理
      this.getAllTask();        // 获取所有任务 - 用于任务管理
      this.getAllTaskLevel();   // 获取所有任务等级奖励内容 - 用于任务等级奖励管理的查看
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
  .reward-title {
    font-size: 0.12rem;
    margin-top: 0.1rem;
  }
  .level-reward-box {
    display: flex;
    margin-top: 0.1rem;
    &:last-child {
      margin-bottom: -0.2rem;
    }
    .reward-num {
      width: 1rem;
      margin-right: 0.2rem;
    }
    .reward-content {
      width: 2rem !important;
      margin-left: -2px;
    }
    .add-btn {
      font-size: 0.2rem;
      margin: 0.04rem 0 0 0.2rem;
    }
  }
  .edit-reward-btn {
    margin-left: 0.1rem;
    color: #4169E1;
    border-bottom: 1px solid #4169E1;
  }
</style>
