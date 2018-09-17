<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <w-tab :list="tab_list" @wTabClick="wTabClick"></w-tab>
      <!--首页-->
     <div class="m-index" v-if="page == '首页'">

       <div class="content-table">
         <el-table :data="tableData" border style="width: 100%">
           <el-table-column prop="title" label="任务标题" width="280"></el-table-column>
           <el-table-column prop="content" label="内容"></el-table-column>
           <el-table-column prop="reward" label="奖励方式"></el-table-column>
           <el-table-column fixed="right" label="操作" width="280">
             <template slot-scope="scope">
               <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
               <el-button type="text" size="small">|</el-button>
               <el-button type="text" size="small">编辑</el-button>
             </template>
           </el-table-column>
         </el-table>
       </div>

       <h3 class="m-title">浮窗管理</h3>
       <el-form :label-position="labelPosition" label-width="100px" :model="formIndex">
         <div class="m-form-item m-item-modal">
           <span class="m-item-add">+</span>
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

         <el-form-item label="奖励方式">
           <el-select v-model="value" placeholder="请选择">
             <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
           </el-select>
         </el-form-item>


         <el-form-item label="规则">
           <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
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
        <h3 class="m-title">弹框图片</h3>
        <div class="m-form-item">
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
        <div class="m-form-item">
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
        <h3 class="m-title">规则弹框</h3>
        <el-form :label-position="labelPosition" label-width="180px" :model="formIndex">
          <el-form-item label="等级规则（未开店）">
            <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
          </el-form-item>
          <el-form-item label="等级规则（已开店）">
            <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
          </el-form-item>
          <el-form-item label="专属粉丝管理规则">
            <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
          </el-form-item>
          <el-form-item label="开店邀请海报规则">
            <textarea v-model="formIndex.value" class="m-textarea" placeholder="请输入内容"></textarea>
          </el-form-item>
        </el-form>
      </div>
      <div class="m-form-confirm-btn ">
        <span v-if="page == '首页'">暂停</span>
        <span>发布</span>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';
  export default {
    data(){
      return{
        page:'首页',
        name:'弹框管理',
        tab_list:[
          {
            name:'首页',
            url:'',
            active:true
          },
          {
            name:'发现',
            url:'',
            active:false
          },
          {
            name:'我的',
            url:'',
            active:false
          }
        ],
        tableData: [
          { title: '任务1', content: '任务1的内容', reward: '两张99-10新衣币' },
          { title: '任务2', content: '任务2的内容', reward: '佣金上涨30%' },
          { title: '任务3', content: '任务3的内容', reward: '两张99-10新衣币' },
          { title: '任务4', content: '任务4的内容', reward: '佣金上涨30%' },
        ],
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
      pageTitle,
      wTab
    },
    methods:{
      // 任务列表的操作方法
      handleClick(row) {
        console.log(row);
      },
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
