<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">


      <p class="m-form-label" style="margin-bottom: 0.2rem">专题管理</p>
      <div class="content-table">
        <el-table :data="bannerList" border style="width: 100%">
          <el-table-column prop="batext" label="专题名称" width="200">
            <template slot-scope="scope">
              <div>
                <el-input v-model="scope.row.batext" placeholder="请输入内容" :disabled="scope.row.disabled"></el-input>
              </div>
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
          <el-table-column prop="title" label="时间" width="420">
            <template slot-scope="scope">
              <el-date-picker v-model="scope.row.activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 3rem;" :disabled="scope.row.disabled" @click="clearTime(scope)">
              </el-date-picker>
            </template>
          </el-table-column>
          <el-table-column prop="product" label="展示" width="200">
            <template slot-scope="scope">
              <el-switch v-model="scope.row.baisdisplay" active-text="展示" inactive-text="关闭" @click="rowClick(scope.$index, 'show')" :disabled="scope.row.disabled">
              </el-switch>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="230">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'banner')" type="text" size="small" v-if="scope.row.editSave">编辑</el-button>
              <el-button @click="addBannerClick(scope)" type="text" size="small" v-if="!scope.row.editSave">保存</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteBanner(scope)">删除</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" :disabled="scope.row.upDisabled">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="display: flex; margin-top: 0.1rem">
          <div class="add-box" style="flex: 1;">
            <el-tooltip class="item" effect="light" content="添加专题" placement="right">
              <span class="m-item-add" style="left: 3.5rem" @click="addBanner">+</span>
            </el-tooltip>
          </div>
          <p class="m-item-alert tr">轮播图尺寸大小750*280</p>
        </div>
      </div>


      <p class="m-form-label" style="margin-bottom: 0.2rem">热文管理</p>
      <div class="content-table">
        <el-table :data="hotMessageList" border style="width: 100%">
          <el-table-column prop="hmsort" label="热文顺序" width="200"></el-table-column>
          <el-table-column prop="hmtext" label="热文内容"></el-table-column>
          <el-table-column fixed="right" label="管理" width="300">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'hot')" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">删除</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <el-tooltip class="item" effect="light" content="添加热文" placement="right">
        <span class="m-item-add tc" v-if="!show_div" @click="showDiv" style="margin-top: -0.1rem">+</span>
      </el-tooltip>
      <span class="m-item-add tc" v-if="show_div" @click="showDiv" style="margin-top: -0.1rem;">-</span>
      <div class="m-form-item" v-if="show_div" style="margin-bottom: 0.3rem; margin-top: 0.1rem">
        <p class="m-form-label">热文内容</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="hotValue" placeholder="请输入热文内容" maxlength="25" class="hot-message-input"></el-input>
          </div>
          <p class="m-item-alert" style="margin-top: 0.05rem; font-size: 0.12rem">字数控制在25字以内</p>
        </div>
        <p class="m-form-label">热文分类</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="hotJumpValue" class="m-input-l" placeholder="商品/专题/公告/教程">
              <el-option v-for="item in hotJump" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-if="hotJumpValue != ''" v-model="jumpToValue" filterable placeholder="请选择" style="width: 4rem; margin-left: 0.5rem">
              <el-option v-for="item in jumpToList" :key="item.value" :label="item.value" :value="item.id"></el-option>
            </el-select>
          </div>
        </div>
        <p class="m-form-label">活动时间</p>
        <div class="m-item-content">
          <el-date-picker v-model="hotTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                          start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
          </el-date-picker>
        </div>
        <div class="save-btn" @click="saveHotMessage">保 存</div>
      </div>


      <w-tab :list="tab_list"  @wTabClick="wTabClick" style="margin-top: 0.3rem"></w-tab>

      <p class="m-form-label" style="margin-bottom: 0.2rem">推文管理</p>
      <div class="content-table">
        <el-table :data="hotmessages" border style="width: 100%">
          <el-table-column prop="num" label="推文时间" width="200"></el-table-column>
          <el-table-column prop="content" label="推文内容"></el-table-column>
          <el-table-column fixed="right" label="管理" width="300">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'banner1')" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">删除</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div class="m-form-item">
        <p class="m-form-label">推文描述</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <textarea v-model="value" class="m-textarea" placeholder="请输入内容"></textarea>
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
          <el-select v-model="value4" class="m-input-l" placeholder="请选择">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
          <el-input v-model="value5" placeholder="请输入内容" style="width: 4rem; margin-left: 0.5rem"></el-input>
        </div>
      </div>

      <div class="m-form-item">
        <p class="m-form-label">活动选择</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="value6" class="m-input-l" placeholder="请选择">
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
            <el-select v-model="value8" class="m-input-l" placeholder="请选择">
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
            <el-input v-model="value9" class="m-input-s" placeholder="请输入内容"></el-input>
          </div>
        </div>
      </div>

      <div class="m-form-item">
        <p class="m-form-label">虚拟转发数</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value10" class="m-input-s" placeholder="请输入内容"></el-input>
          </div>
        </div>
      </div>

      <p class="m-form-label">活动时间</p>
      <div class="m-item-content">
        <el-date-picker v-model="activityTime1" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                        start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
        </el-date-picker>
      </div>

      <div class="m-form-confirm-btn">
        <span>确定</span>
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
        name:'首页管理',
        options: [
          { value: '1', label: '商品' },
          { value: '2', label: '专题' },
          { value: '3', label: '公告' },
          { value: '4', label: '教程' }
        ],
        hotJump: [
          { value: '1', label: '商品' },
          { value: '2', label: '专题' },
          { value: '3', label: '教程' },
          { value: '4', label: '公告' }
        ],
        rowNum: "",
        hotValue: '',
        hotJumpValue: '',
        jumpToValue: '',
        jumpToList: [],
        hotTime: [],
        value: '',
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        value9: '',
        value10: '',
        // value3: '',
        bannerList: [],
        // activityTime: ["2000-11-10 10:10:05", "2000-11-11 10:10:05"],
        activityTime: [],
        activityTime1: [],
        hotMessageList: [],
        hotmessages: [
          { time: "18/09/13 18:30 ", content: "推文内容" },
          { time: "18/09/13 18:30 ", content: "推文内容" },
          { time: "18/09/13 18:30 ", content: "推文内容" },
        ],
        imageUrl:'',
        show_div: false,
        tab_list:[
          {
            name:'上新',
            url:'',
            active:true
          },
          {
            name:'特卖',
            url:'',
            active:false
          },
          {
            name:'爆款',
            url:'',
            active:false
          },
          {
            name:'预告',
            url:'',
            active:false
          }
        ],
      }
    },
    components:{
      pageTitle,
      wTab
    },
    methods:{
      // 轮播图管理-确定点击的是第几行
      rowClick(index, col) {
        console.log(col);
        this.rowNum = index;
      },
      // 点击编辑后-点击时间选择器时清空时间
      clearTime(scope) {
        alert("clearTime");
        this.bannerList[scope.$index].activityTime = [];
      },
      // 添加banner的 + 号按钮
      addBanner() {
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
        this.bannerList[index].editSave = false;
        this.bannerList = this.bannerList.concat();
      },
      // 显示添加热文的div
      showDiv() {
        if(this.show_div) {
          this.show_div = false;
        }else if(!this.show_div) {
          this.show_div = true;
        }
      },
      // 获取banner滚动图
      getBanner() {
        axios.get(api.get_bigactivitys + '?lasting=true&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            for(let i = 0; i < res.data.data.length; i++) {
              if(res.data.data[i].baposition == 0) {
                this.bannerList.push(res.data.data[i]);
              }
            }

            for(let i = 0; i < this.bannerList.length; i ++) {
              this.bannerList[i].activityTime = [this.bannerList[i].bastarttime, this.bannerList[i].baendtime];
              this.bannerList[i].disabled = true;
              this.bannerList[i].upDisabled = false;
              this.bannerList[i].editSave = true;
            }
            // console.log(res.data.data);
          }else{
            this.$message.error(res.data.message);
          }
        })
      },
      // 列表的编辑方法
      editClick(scope, where) {
        console.log(scope.$index, where);
        if(where == "banner") {
          this.bannerList[scope.$index].disabled = false;
          this.bannerList[scope.$index].editSave = false;
        }
      },
      // 添加banner
      addBannerClick(scope) {
        // console.log(this.bannerList[scope.$index]);
        let banner = this.bannerList[scope.$index];
        let params = {
          BAimage: banner.baimage,
          BAtext: banner.batext,
          BAstarttime: banner.activityTime[0],
          BAendtime: banner.activityTime[1],
          BAisdisplay: banner.baisdisplay,
          BAsort: scope.$index
        };

        axios.post(api.create_hbact + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: res.data.message, type: 'success' });

            this.bannerList[scope.$index].disabled = true;
            this.bannerList[scope.$index].editSave = true;
          }else{
            this.$message.error(res.data.message);
          }
        });
      },
      // 删除轮播图
      deleteBanner(scope) {

        this.$confirm('此操作将删除该专题, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + '&baid=' + this.bannerList[scope.$index].baid,
            { baisdelete: true }).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "专题删除成功", type: 'success' });
              // 获取首页专题
              // console.log(this.bannerList);
              this.bannerList.splice(scope.$index, 1);
              // this.getBanner();
            }else{
              this.$message.error(res.data.message);
            }
          });

        }).catch(() => {  });
      },

      // 获取热文
      getHotMessage() {
        axios.get(api.get_all_hot_message + '?lasting=true&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.hotMessageList = res.data.data;
            // console.log(this.hotMessageList);
          }else{
            this.$message.error(res.data.message);
          }
        })
      },
      // 模糊搜索-获取所有可选项
      getJumpTo(to) {
        if(to == 'product') {
          axios.get(api.get_product + '?kw=').then(res => {
            if(res.data.status == 200) {
              let product = {};
              for(let i = 0; i < res.data.data.length; i ++) {
                product = { value: res.data.data[i].prtitle, id: res.data.data[i].prid };
                this.jumpToList.push(product);
              }
              // console.log(this.jumpToList);
            }else{
              this.$message.error(res.data.message);
            }
          })
        }else if(to == 'banner') {
          let banner = {};
          for(let i = 0; i < this.bannerList.length; i ++) {
            banner = { value: this.bannerList[i].batext, id: this.bannerList[i].baid };
            this.jumpToList.push(banner);
          }
        }else if(to == '3' || to == '4') {
          axios.get(api.get_activity_list_by_actitle + "?token=" + localStorage.getItem("token") + "&hmtype=" + to + "&actitle=").then(res => {
            if(res.data.status == 200) {
              let activity = {};
              for(let i = 0; i < res.data.data.length; i ++) {
                activity = { value: res.data.data[i].actitle, id: res.data.data[i].acid };
                this.jumpToList.push(activity);
              }
              // console.log(this.jumpToList);
            }else{
              this.$message.error(res.data.message);
            }
          })
        }
      },
      // 添加热文
      saveHotMessage () {
        // console.log(this.hotValue, this.hotJumpValue, this.jumpToValue, this.hotTime[0], this.hotTime[1]);

        let params = {
          HMtext: this.hotValue,
          HMstarttime: this.hotTime[0],
          HMendtime: this.hotTime[1],
          HMsort: this.hotMessageList.length,
          HMSkipType: this.hotJumpValue,
          HMcontent: this.jumpToValue
        };
        axios.post(api.add_one_hot_message + '?token=' + localStorage.getItem('token'), params).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message });
            this.hotValue = "";
            this.hotJumpValue = "";
            this.jumpToValue = "";
            this.hotTime = [];

          }else{
            this.$message({ type: 'error', message: res.data.message });
          }
        });
      },




      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list = [].concat(arr);
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
      handleAvatarSuccess(){

      },
      beforeAvatarUpload(){

      }
    },
    watch: {
      // 热文跳转类型的值发生变化
      hotJumpValue(newValue, oldValue) {
        // console.log(newValue);
        this.jumpToList = [];
        this.jumpToValue = "";
        if(newValue == "1") {
          this.getJumpTo('product');     // 获取所有商品
        }else if(newValue == "2") {
          this.getJumpTo('banner');     // 获取所有专题
        }else if(newValue == "3") {
          this.getJumpTo('3');     // 获取所有教程
        }else if(newValue == "4") {
          this.getJumpTo('4');     // 获取所有公告
        }
      },
    },
    mounted() {
      this.getBanner();       // 获取首页专题
      this.getHotMessage();   // 获取热文
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .save-btn {
    width: 0.5rem;
    text-align: center;
    border-radius: 0.1rem;
    padding: 0.08rem 0.3rem;
    margin: 0.1rem auto 0 auto;
    color: #ffffff;
    background-color: #91aeb5;
  }
</style>
