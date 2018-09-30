<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">

      <w-tab :list="tab_list1"  @wTabClick="wTabClick1"></w-tab>

      <div v-if="page == '每日10荐'">
        <p class="m-form-label">轮播图管理</p>
        <div class="content-table">
          <el-table :data="bannerList" border style="width: 100%" v-loading="bannerLoading">
            <el-table-column prop="batext" label="专题名称">
              <template slot-scope="scope">
                <el-input v-model="scope.row.batext" placeholder="请输入专题名称" :disabled="scope.row.disabled"></el-input>
              </template>
            </el-table-column>
            <el-table-column prop="baimage" label="内容" width="240">
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


        <div style="border-bottom: 1px #707070 solid; padding-bottom: 0.2rem; margin-bottom: 0.5rem">
          <p class="m-form-label">商品推荐管理</p>
          <div class="content-table">
            <el-table :data="productList" border style="width: 100%">
              <el-table-column prop="num" label="商品图片" width="200">
                <template slot-scope="scope">
                  <img class="product-img" src="" alt="">
                </template>
              </el-table-column>
              <el-table-column prop="content" label="商品名称"></el-table-column>
              <el-table-column prop="content" label="商品价格"></el-table-column>
              <el-table-column fixed="right" label="管理" width="300">
                <template slot-scope="scope">
                  <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
                  <el-button type="text" size="small">|</el-button>
                  <el-button type="text" size="small">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>
      </div>


      <w-tab :list="tab_list2" v-if="page == '素材圈'" class="m-ft-12"  @wTabClick="wTabClick2"></w-tab>

      <p class="m-form-label" style="margin-bottom: 0.2rem">推文管理</p>
      <div class="content-table">
        <el-table :data="activityList" border style="width: 100%" v-loading="activityLoading">
          <el-table-column prop="num" label="推文时间" width="490">
            <template slot-scope="scope">
              <el-date-picker v-model="scope.row.activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 3.5rem;" @blur="activityTimeClick(scope)" :disabled="scope.row.disabled">
              </el-date-picker>
            </template>
          </el-table-column>
          <el-table-column prop="actext" label="推文内容">
            <template slot-scope="scope">
              <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 3 }" placeholder="请输入推文内容" v-model="scope.row.actext" :disabled="scope.row.disabled"></el-input>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'activity')" type="text" size="small" v-if="scope.row.editSave == '1'">编辑</el-button>
              <el-button @click="saveClick(scope, 'activity')" type="text" size="small" v-if="scope.row.editSave == '2'">保存</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteActivity(scope)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>


      <div>
        <div class="m-form-item" v-if="page == '公告' || page == '教程'">
          <p class="m-form-label">推文标题</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="value16" placeholder="请输入内容" style="width: 4rem"></el-input>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label">推文内容</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" placeholder="请输入推文内容" v-model="activityACtext" style="width: 4rem"></el-input>
            </div>
          </div>
        </div>
        <div class="m-form-item" style="min-height: 1.8rem; max-height: 1.8rem">
          <p class="m-form-label">推文图片</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-upload action="https://weidian.daaiti.cn/task/upload_task_img" list-type="picture-card" :on-preview="handlePictureCardPreview" :on-remove="handleRemove">
                <i class="el-icon-plus"></i>
              </el-upload>
              <el-dialog :visible.sync="dialogVisible">
                <img :src="dialogImageUrl" alt="">
              </el-dialog>
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
        <div class="m-form-item" v-if="page != '素材圈'">
          <p class="m-form-label">跳转类型</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="activityJumpValue" class="m-input-l" placeholder="请选择" style="width: 1.75rem">
                <el-option v-for="item in activityJumpList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
              <el-select v-if="activityJumpValue == '1'" v-model="activityJumpToValue" filterable placeholder="请输入关键词搜索商品" style="width: 4rem; margin-left: 0.5rem">
                <el-option v-for="item in activityJumpToList" :key="item.value" :label="item.value" :value="item.id"></el-option>
              </el-select>
              <div v-if="activityJumpValue == '1'" style="margin-left: 0.5rem">
                <span>虚拟销量：</span>
                <el-input v-model="activityProductSales" style="width: 1rem; text-align: center"></el-input>
              </div>
              <el-select v-if="activityJumpValue == '2'" v-model="activityJumpToValue" class="m-input-l" placeholder="请选择专题" style="width: 4rem; margin-left: 0.5rem">
                <el-option v-for="item in activityJumpToList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </div>
          </div>
        </div>
        <div class="m-form-item" v-if="page != '素材圈'">
          <p class="m-form-label">活动类型</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="activityType" class="m-input-l" placeholder="请选择">
                <el-option v-for="item in activityTypeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </div>
          </div>
        </div>
        <div class="m-form-item" v-if="page != '素材圈'">
          <p class="m-form-label">活动时间</p>
          <div class="m-item-content">
            <el-date-picker v-model="activityActivityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                            start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
            </el-date-picker>
          </div>
        </div>
        <div class="num-list">
          <div class="num-box" v-if="page == '公告'">
            <p class="m-form-label">虚拟浏览量</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="views" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box" v-if="page == '素材圈'">
            <p class="m-form-label">虚拟发圈数</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="views" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box" v-if="page != '素材圈'">
            <p class="m-form-label">虚拟点赞数</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="likeNum" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box" v-if="page != '素材圈'">
            <p class="m-form-label">活动角标</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="activityBadge" class="m-input-s" placeholder="限两个字" maxlength="2"></el-input>
              </div>
            </div>
          </div>
        </div>
        <div class="m-form-item" v-if="page == '公告' || page == '教程'">
          <p class="m-form-label">推文置顶</p>
          <el-switch style="margin: 0.1rem 0 0.2rem 0"
                     v-model="value2"
                     active-color="#91aeb5"
                     inactive-color="#DCDCDC">
          </el-switch>
        </div>
        <div class="m-form-confirm-btn">
          <span @click="addActivity">保 存</span>
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
        activityLoading: true,
        activityList: [],
        activityACtext: "",
        dialogImageUrl: '',
        dialogVisible: false,
        activityJumpValue: "",
        activityJumpToValue: "",
        activityProductSales: "",
        activityJumpToList: [],
        activityActivityTime: [],
        activityJumpList: [
          { value: '1', label: '商品' },
          { value: '2', label: '专题' }
        ],
        activityTypeList: [
          { value: "0", label: "普通动态" },
          { value: "1", label: "满减" },
          { value: "2", label: "满赠" },
          { value: "3", label: "优惠券" },
          { value: "4", label: "砍价" },
          { value: "5", label: "拼团" },
          { value: "6", label: "单品优惠券" },
          { value: "7", label: "一元秒杀" },
          { value: "8", label: "前 30 分钟半价" },
          { value: "9", label: "限时抢" },
          { value: "10", label: "5 元 10 件" }
        ],
        views: '',
        likeNum: '',
        activityType: '',
        activityBadge: '',


        activityTime: [],
        productList: [
          { num: "18/09/13 18:30 ", content: "商品内容" },
          { num: "18/09/13 18:30 ", content: "商品内容" },
          { num: "18/09/13 18:30 ", content: "商品内容" },
        ],
        hotmessages: [
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
        ],
        page:'每日10荐',
        tab_list1:[],
        tab_list2:[],
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
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      // 轮播图管理-确定点击的图片是第几行
      rowClick(index, col) {
        // console.log(col);
        this.rowNum = index;
      },
      // 点击编辑后-点击时间选择器时清空时间
      timeClick(scope) {
        this.bannerList = this.bannerList.concat();
      },
      // 点击编辑后-点击时间选择器时清空时间
      activityTimeClick(scope) {
        this.activityList = this.activityList.concat();
      },
      // 列表的编辑方法
      editClick(scope, where) {
        console.log("edit", where);
        if(where == "banner") {
          this.bannerList[scope.$index].disabled = false;
          this.bannerList[scope.$index].addSaveEdit = "2";
          this.bannerList = this.bannerList.concat();
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
      // 取消添加banner
      cancelAdd(scope) {
        this.addBannerBtn = true;
        this.bannerList.splice(scope.$index, 1);    // 刷新视图
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
      // 删除活动/推文
      deleteActivity(scope) {
        this.$confirm('此操作将删除该推文, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          /*axios.post(api.del_one + '?token=' + localStorage.getItem('token'), { acid: this.activityList[scope.$index].acid }).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "热文删除成功", type: 'success' });
              this.activityList.splice(scope.$index, 1);    // 刷新视图
            }else{
              this.$message.error(res.data.message);
            }
          });*/
        }).catch(() => {  });
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
      // 添加推文/活动
      addActivity () {
        console.log("activityJumpValue:", this.activityJumpValue);
        console.log("activityJumpToValue:", this.activityJumpToValue);
        console.log("activityType:", this.activityType);
        console.log("tnid:", this.tnid);
        console.log("activityBadge:", this.activityBadge);
        console.log("likeNum:", this.likeNum);
        console.log("activityProductSales:", this.activityProductSales);
        console.log("activityActivityTime:", this.activityActivityTime);

        if(this.activityACtext == "" || this.activityJumpValue == "" || this.activityJumpToValue == "" || this.activityType == "" || this.activityBadge == "" || this.likeNum == ""
          || this.activityActivityTime.length != 2) {
          this.$message({ message: "请完整填写", type: 'warning' });
          if(this.tnid == "") {
            this.$message({ message: "请刷新页面后重试", type: 'warning' });
          }
        }else {
          let params = {
            ACSkipType: this.activityJumpValue,
            AClinkvalue: this.activityJumpToValue,
            ACtype: this.activityType,
            TopnavId: this.tnid,
            ACtext: this.activityACtext,
            // media: [{ AMimage: "", AMsort: "" }],
            tags: [{ ATname: this.activityBadge }],
            AClikeFakeNum: this.likeNum,
            // ACProductsSoldFakeNum: this.activityProductSales,
            ACstarttime: this.activityActivityTime[0],
            ACendtime: this.activityActivityTime[1]
          };
          if(this.activityProductSales != "") {
            params.ACProductsSoldFakeNum = this.activityProductSales;
          }
          console.log(params);
          axios.post(api.add_one_activity + '?token=' + localStorage.getItem('token'), params).then(res => {
            if(res.data.status == 200){
              this.$message({ type: 'success', message: res.data.message });
              this.getActivity();     // 获取推文/内容
            }else{
              this.$message({ type: 'error', message: res.data.message });
            }
          });
        }
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
      // 获取首页顶部导航nav
      getTopNav() {
        axios.get(api.get_dp).then(res => {
          if(res.data.status == 200) {
            for(let i = 0; i < res.data.data.length; i++) {
              let nav = { name: res.data.data[i].tnname, url: "", active: false, tnid: res.data.data[i].tnid };
              this.tab_list1.push(nav);

              this.tab_list1[0].active = true;
              this.tnid = this.tab_list1[0].tnid;
            }
            for(let i = 0; i < res.data.data[1].sub.length; i++) {
              let nav = { name: res.data.data[1].sub[i].tnname, url: "", active: false, tnid: res.data.data[1].sub[i].tnid };
              this.tab_list2.push(nav);

              this.tab_list2[0].active = true;
              this.tnid = this.tab_list2[0].tnid;
            }

            this.getActivity(0, 5);      // 获取首页活动/推文内容列表
          }else{
            this.$message.error(res.data.message);
          }
        })
      },
      // 获取首页活动/推文内容列表
      getActivity(start, count) {
        axios.get(api.get_all_activity + '?token=' + localStorage.getItem('token'),
          { params: { lasting: true, start: start || 0, count: count || this.count, tnid: this.tnid }}).then(res => {
          if(res.data.status == 200) {
            this.activityLoading = false;
            this.activityList = res.data.data;

            for(let i = 0; i < this.activityList.length; i ++) {

              this.activityList[i].activityTime = [this.activityList[i].acstarttime, this.activityList[i].acendtime];
              this.activityList[i].disabled = true;
              this.activityList[i].editSave = "1";
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
      // 模糊搜索-获取所有可选项
      getJumpTo(to, where) {
        if(to == 'product') {
          axios.get(api.get_product + '?kw=').then(res => {
            if(res.data.status == 200) {
              let product = {};
              for(let i = 0; i < res.data.data.length; i ++) {
                product = { value: res.data.data[i].prtitle, id: res.data.data[i].prid };
                if(where == "activity") {
                  this.activityJumpToList.push(product);
                }
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
            if(where == "activity") {
              // 防止未添加的专题影响
              if(this.bannerList[this.bannerList.length - 1].baid == undefined) {
                this.addBannerBtn = true;
                this.bannerList.splice(this.bannerList.length - 1, 1);    // 刷新视图
              }

              this.activityJumpToList.push(banner);
            }
          }
        }
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

        this.activityLoading = true;
        this.tnid = this.tab_list1[i].tnid;
        this.getActivity(0, 5);   // 获取首页活动/推文内容列表
      },
      wTabClick2(i){
        let arr = [].concat(this.tab_list2);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list2 = [].concat(arr);

        this.activityLoading = true;
        this.tnid = this.tab_list2[i].tnid;
        this.getActivity(0, 5);   // 获取首页活动/推文内容列表
      },
      handleAvatarSuccess(){

      },
      beforeAvatarUpload(){

      }
    },
    watch: {
      // 推文/活动跳转类型的值发生变化
      activityJumpValue(newValue, oldValue) {
        this.activityJumpToList = [];
        this.activityJumpToValue = "";
        if(newValue == "1") {
          this.getJumpTo("product", "activity");     // 获取所有商品
        }else if(newValue == "2") {
          this.getJumpTo("banner", "activity");     // 获取所有专题
        }
      },
    },
    mounted() {
      this.getBanner();                 // 获取首页专题
      this.getTopNav();                 // 获取首页顶部导航nav
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
  .product-img {

  }
  .num-list {
    display: flex;
    .num-box {
      margin-right: 0.5rem;
    }
  }
</style>
