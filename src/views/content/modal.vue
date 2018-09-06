<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <ul class="m-weidian-tabbox m-no-margin">
        <li>
          <span class="m-tab-name active">首页</span>
          <span class="m-tab-line">/</span>
        </li>
        <li>
          <span class="m-tab-name ">发现</span>
          <span class="m-tab-line">/</span>
        </li>
        <li>
          <span class="m-tab-name ">我的</span>
        </li>
      </ul>
      <!--首页-->
     <div class="m-index">
       <el-form :label-position="labelPosition" label-width="100px" :model="formIndex">
         <div class="m-form-item m-item-modal">
           <span class="m-item-add">+</span>
           <p class="m-form-label">浮窗管理</p>
           <el-form-item label="任务标题">
             <el-input v-model="formIndex.value" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="副标题">
             <el-input v-model="formIndex.value" class="m-input-m"></el-input>
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
             <el-input v-model="formIndex.value" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="完成度">
             <el-input v-model="formIndex.value" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="备注">
             <el-input v-model="formIndex.value" class="m-input-m"></el-input>
           </el-form-item>
           <el-form-item label="图片" class="m-f">
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
         <el-form-item label="备注">
           <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
         </el-form-item>
       </el-form>

     </div>
      <!--发现-->
      <div class="m-discovery">


      </div>
      <!--我的-->
      <div class="m-personal">


      </div>
      <div class="m-form-confirm-btn ">
        <span>暂停</span>
        <span>发布</span>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  export default {
    data(){
      return{
        name:'首页管理',
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
        imageUrl:'',
        labelPosition:'left',
        formIndex:{
          value:''
        }
      }
    },
    components:{
      pageTitle
    },
    methods:{
      handleAvatarSuccess(){

      },
      beforeAvatarUpload(){

      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";
</style>
