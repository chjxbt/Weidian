<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">


      <p class="m-form-label" style="margin-bottom: 0.2rem">轮播图管理</p>
      <div class="content-table">
        <el-table :data="bannerList" border style="width: 100%" v-loading="bannerLoading">
          <el-table-column prop="batext" label="专题名称" width="200">
            <template slot-scope="scope">
              <el-input v-model="scope.row.batext" placeholder="请输入专题名称" :disabled="scope.row.disabled"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="baimage" label="内容">
            <template slot-scope="scope">
              <div @click="rowClick(scope.$index, 'img')">
                <el-upload class="avatar-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                           :on-success="uploadPicture" :before-upload="beforeAvatarUploads" :disabled="scope.row.disabled">
                  <img v-if="scope.row.baimage" :src="scope.row.baimage" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="title" label="时间" width="490">
            <template slot-scope="scope">
              <el-date-picker v-model="scope.row.activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 3.5rem;" :disabled="scope.row.disabled" @blur="timeClick(scope)">
              </el-date-picker>
            </template>
          </el-table-column>
          <el-table-column prop="product" label="展示" width="150">
            <template slot-scope="scope">
              <el-switch v-model="scope.row.baisdisplay" active-text="展示" inactive-text="关闭" @click="rowClick(scope.$index, 'show')" :disabled="scope.row.disabled">
              </el-switch>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'banner')" type="text" size="small" v-if="scope.row.addSaveEdit== '3'">编辑</el-button>
              <el-button @click="saveClick(scope, 'banner')" type="text" size="small" v-if="scope.row.addSaveEdit == '2'">保存</el-button>
              <el-button @click="addBannerClick(scope)" type="text" size="small" v-if="scope.row.addSaveEdit == '1'">上传</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteBanner(scope)" v-if="scope.row.addSaveEdit != '1'">删除</el-button>
              <el-button type="text" size="small" @click="cancelAdd(scope)" v-if="scope.row.addSaveEdit == '1'">取消</el-button>
              <el-button type="text" size="small" v-if="scope.row.addSaveEdit != '1'">|</el-button>
              <el-button type="text" size="small" @click="upBanner(scope)" v-if="scope.row.addSaveEdit != '1'" :disabled="scope.row.upDisabled">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="display: flex; margin-top: 0.1rem">
          <div class="add-box" style="flex: 1;">
            <el-tooltip class="item" effect="light" content="添加专题" placement="right">
              <span class="m-item-add" style="left: 3.5rem" @click="addBanner" v-if="addBannerBtn">+</span>
            </el-tooltip>
          </div>
          <p class="m-item-alert tr">轮播图尺寸大小750*280</p>
        </div>
      </div>

      <p class="m-form-label">商品选择</p>
      <div class="m-item-content">
        <div class=" m-item-row">
          <el-input v-model="value" placeholder="请输入内容" style="width: 4rem;margin-bottom: 0.1rem"></el-input>
        </div>
      </div>


      <w-tab :list="tab_list1"  @wTabClick="wTabClick1"></w-tab>
      <w-tab :list="tab_list2" v-if="page == '素材圈'" class="m-ft-12"  @wTabClick="wTabClick2"></w-tab>


      <p class="m-form-label" style="margin-bottom: 0.2rem">推文管理</p>
      <div class="content-table">
        <el-table :data="hotmessages" border style="width: 100%">
          <el-table-column prop="num" label="推文时间" width="200"></el-table-column>
          <el-table-column prop="content" label="推文内容"></el-table-column>
          <el-table-column fixed="right" label="管理" width="300">
            <template slot-scope="scope">
              <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>


      <div v-if="page == '每日10荐'">
        <div class="m-form-item">
          <p class="m-form-label">推文描述</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <textarea v-model="value11" class="m-textarea" placeholder="请输入内容"></textarea>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label">推文图片</p>
          <div class="m-item-content">
            <div class=" m-item-row">
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
        <p class="m-form-label">跳转类型</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="value22" class="m-input-l" placeholder="请选择">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-input v-model="value12" placeholder="请输入内容" style="width: 4rem; margin-left: 0.5rem"></el-input>
          </div>
        </div>

        <div class="m-form-item">
          <p class="m-form-label">活动选择</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="value13" class="m-input-l" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </div>
        </div>

        <div class="m-form-item">
          <p class="m-form-label">活动角标</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="value14" class="m-input-l" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </div>
        </div>

        <div class="m-form-item">
          <p class="m-form-label">虚拟点赞数</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value15" class="m-input-s" placeholder="请输入内容"></el-input>
            </div>
          </div>
        </div>

        <div class="m-form-item">
          <p class="m-form-label">虚拟转发数</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value21" class="m-input-s" placeholder="请输入内容"></el-input>
            </div>
          </div>
        </div>

        <p class="m-form-label">活动时间</p>
        <div class="m-item-content">
          <el-date-picker v-model="activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                          start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
          </el-date-picker>
        </div>
      </div>


      <div class="m-form-item" v-if="page == '素材圈' || page == '公告' || page == '教程'">
        <p class="m-form-label" style="font-size: 0.12rem;margin-bottom: 0.2rem">推文信息</p>

        <p class="m-form-label">推文标题</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value16" placeholder="请输入内容" style="width: 4rem"></el-input>
          </div>
        </div>

        <p class="m-form-label">推文内容</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <textarea v-model="value17" class="m-textarea" placeholder="请输入内容"></textarea>
          </div>
        </div>

        <div class="m-form-item">
          <p class="m-form-label">推文图片</p>
          <div class="m-item-content">
            <div class=" m-item-row">
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
        <div class="m-form-item" v-if="page == '素材圈'">
          <p class="m-form-label">虚拟发圈数</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value18" class="m-input-s" placeholder="请输入内容"></el-input>
            </div>
          </div>
        </div>

        <div class="m-form-item" v-if="page == '教程'">
          <p class="m-form-label">教程视频</p>
          <div class="m-item-content">
            <div class=" m-item-row">
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

        <div class="m-form-item" v-if="page == '公告' || page == '教程'">
          <p class="m-form-label">虚拟点击数</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value19" class="m-input-s" placeholder="请输入内容"></el-input>
            </div>
          </div>
          <p class="m-form-label">虚拟浏览数</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value20" class="m-input-s" placeholder="请输入内容"></el-input>
            </div>
          </div>
        </div>
      </div>

      <div class="m-form-item" v-if="page == '公告' || page == '教程'">
        <p class="m-form-label">推文置顶</p>
        <el-switch style="margin: 0.1rem 0 0.2rem 0"
          v-model="value2"
          active-color="#13ce66"
          inactive-color="#ff4949">
        </el-switch>
      </div>

      <div v-if="page == '每日10荐'">
        <div class="m-form-confirm-btn">
          <span>暂 停</span>
          <span>删 除</span>
          <span>新 建</span>
        </div>
      </div>
      <div v-if="page == '素材圈' || page == '公告' || page == '教程'">
        <div class="m-form-confirm-btn">
          <span>新 建</span>
        </div>
      </div>



      <div class="m-form-item" v-if="page == '公告' || page == '教程'">
        <p class="m-form-label">评论管理</p>
        <div class="content-table">
          <el-table :data="tableData" border style="width: 100%">
            <el-table-column prop="object" label="评论对象"></el-table-column>
            <el-table-column prop="who" label="评论人"></el-table-column>
            <el-table-column prop="time" label="评论时间"></el-table-column>
            <el-table-column prop="content" label="评论内容"></el-table-column>
            <el-table-column fixed="right" label="管理">
              <template slot-scope="scope">
                <el-button @click="handleClick(scope.row)" type="text" size="small">置顶</el-button>
                <el-button type="text" size="small">|</el-button>
                <el-button type="text" size="small">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <!--<div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value" placeholder="请输入内容"></el-input>
          </div>
        </div>-->
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
        name:'发现页管理',
        options: [
          { value: '1', label: '商品' },
          { value: '2', label: '专题' }
        ],
        value: '',
        value2: '',
        value11: '',
        value12: '',
        value13: '',
        value14: '',
        value15: '',
        value16: '',
        value17: '',
        value18: '',
        value19: '',
        value20: '',
        value21: '',
        value22: '',
        imageUrl:'',
        bannerList: [],
        bannerLoading: true,
        addBannerBtn: true,
        activityTime: [],
        hotmessages: [
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
        ],
        page:'每日10荐',
        tab_list1:[
          { name:'每日10荐', url:'', active:true },
          { name:'素材圈', url:'', active:false },
          { name:'公告', url:'', active:false },
          { name:'教程', url:'', active:false }
        ],
        tab_list2:[
          { name:'精选', url:'', active:true },
          { name:'心灵鸡汤', url:'', active:false },
          { name:'店主招募', url:'', active:false },
          { name:'新手必发', url:'', active:false }
        ],
        tableData: [
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' }
        ],
      }
    },
    components:{
      pageTitle,
      wTab
    },
    methods:{
      // 轮播图管理-确定点击的图片是第几行
      rowClick(index, col) {
        // console.log(col);
        this.rowNum = index;
      },
      // 点击编辑后-点击时间选择器时清空时间
      timeClick(scope) {
        this.bannerList = this.bannerList.concat();
      },
      // 列表的编辑方法
      editClick(scope, where) {
        console.log("edit", where);
        if(where == "banner") {
          this.bannerList[scope.$index].disabled = false;
          this.bannerList[scope.$index].addSaveEdit = "2";
          this.bannerList = this.bannerList.concat();
        }else if(where == "hot") {
          this.hotMessageList[scope.$index].disabled = false;
          this.hotMessageList[scope.$index].editSave = "2";
        }else if(where == "activity") {
          this.activityList[scope.$index].disabled = false;
          this.activityList[scope.$index].editSave = "2";
          this.activityList = this.activityList.concat();
        }
      },
      // 保存编辑后的banner
      saveClick(scope, where) {
        console.log(scope, where);
        if(where == "banner") {
          let banner = this.bannerList[scope.$index];
          let params = {
            baimage: banner.baimage,
            batext: banner.batext,
            bastarttime: banner.activityTime[0],
            baendtime: banner.activityTime[1],
            baisdisplay: banner.baisdisplay
          };
          axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + "&baid=" + banner.baid, params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success' });

              this.bannerList[scope.$index].disabled = true;
              this.bannerList[scope.$index].addSaveEdit = "3";
              this.bannerList = this.bannerList.concat();
            }else{
              this.$message.error(res.data.message);
            }
          });
        }else if(where == "activity") {
          console.log("activity-save");
          this.activityList[scope.$index].disabled = true;
          this.activityList[scope.$index].editSave = "1";
          this.activityList = this.activityList.concat();
        }
      },
      // 添加banner
      addBannerClick(scope) {
        let banner = this.bannerList[scope.$index];
        let params = {
          BAimage: banner.baimage,
          BAtext: banner.batext,
          BAstarttime: banner.activityTime[0],
          BAendtime: banner.activityTime[1],
          BAisdisplay: banner.baisdisplay,
          BAsort: this.bannerList[this.bannerList.length - 2].basort + 1
        };
        if(params.BAimage == undefined || params.BAtext == "" || params.BAstarttime == undefined || params.BAendtime == undefined) {
          this.$message({ message: "请完整填写", type: 'warning' });
        }else {
          axios.post(api.create_hbact + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success' });
              this.getBanner();       // 获取专题
              this.addBannerBtn = true;
            }else{
              this.$message.error(res.data.message);
            }
          });
        }
      },
      // 删除轮播图/专题
      deleteBanner(scope) {
        this.$confirm('此操作将删除该专题, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + '&baid=' + this.bannerList[scope.$index].baid,
            { baisdelete: true }).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "专题删除成功", type: 'success' });
              this.bannerList.splice(scope.$index, 1);    // 刷新视图
            }else{
              this.$message.error(res.data.message);
            }
          });
        }).catch(() => {  });
      },
      // 取消添加banner
      cancelAdd(scope) {
        this.addBannerBtn = true;
        this.bannerList.splice(scope.$index, 1);    // 刷新视图
      },
      // 上移banner/专题
      upBanner(scope) {
        axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + "&baid=" + this.bannerList[scope.$index].baid,
          { basort: this.bannerList[scope.$index - 1].basort }).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: "专题上移成功", type: 'success' });
            this.bannerList = [];
            this.getBanner();     // 获取专题
          }else{
            this.$message.error(res.data.message);
          }
        });
      },
      // 添加banner的 + 号按钮
      addBanner() {
        this.addBannerBtn = false;
        let index = this.bannerList.length;
        this.bannerList[index] = {};
        this.bannerList[index].batext = "";
        this.bannerList[index].BAimage = "";
        this.bannerList[index].BAstarttime = "";
        this.bannerList[index].BAendtime = "";
        this.bannerList[index].activityTime = "";
        this.bannerList[index].baisdisplay = true;
        this.bannerList[index].disabled = false;
        this.bannerList[index].upDisabled = false;
        this.bannerList[index].addSaveEdit = "1";
        this.bannerList = this.bannerList.concat();
      },
      // 获取banner滚动图
      getBanner() {
        axios.get(api.get_bigactivitys + '?lasting=true&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.bannerLoading = false;

            this.bannerList = [];
            for(let i = 0; i < res.data.data.length; i++) {
              if(res.data.data[i].baposition == "1") {
                this.bannerList.push(res.data.data[i]);
              }
            }
            for(let i = 0; i < this.bannerList.length; i ++) {
              this.bannerList[i].activityTime = [this.bannerList[i].bastarttime, this.bannerList[i].baendtime];
              this.bannerList[i].disabled = true;
              this.bannerList[i].upDisabled = false;
              this.bannerList[i].addSaveEdit = "3";
            }
          }else{
            this.$message.error(res.data.message);
          }
        })
      },



















      // 上传标题图片
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token'), form).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }

          this.bannerList[this.rowNum].baimage = res.data.data;
          this.bannerList = this.bannerList.concat();
          // this.imageUrl = res.data.data;
        });
      },
      // 上传图片前的限制方法
      beforeAvatarUploads(file) {
        this.$message({ type: 'warning', message: "上传中，请等待" });
        const isJPG = file.type === 'image/jpeg' || 'image/png';
        const isLt2M = file.size / 1024 / 1024 < 20;

        if (!isJPG) {
          this.$message.error('上传图片只能是 JPG 或 PNG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传图片大小不能超过 20MB!');
        }
        return isJPG && isLt2M;
      },


      // 评论列表的操作方法
      handleClick(row) {
        console.log(row);
      },
      wTabClick1(i){
        let arr = [].concat(this.tab_list1);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.page = arr[i].name;
        this.tab_list1 = [].concat(arr);
      },
      wTabClick2(i){
        let arr = [].concat(this.tab_list2);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list2 = [].concat(arr);
      },
      handleAvatarSuccess(){

      },
      beforeAvatarUpload(){

      }
    },
    mounted() {
      this.getBanner();
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .content-table {
    padding-top: 0.1rem;
  }
  .el-table .cell {
    text-align: left;
  }
</style>
