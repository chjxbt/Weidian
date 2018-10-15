<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">


      <p class="m-form-label" style="margin-bottom: 0.2rem">专题管理</p>
      <div class="content-table">
        <el-table :data="bannerList" border style="width: 100%" v-loading="bannerLoading">
          <!--<el-table-column prop="baid" label="Id" width="300"></el-table-column>-->
          <el-table-column prop="batext" label="专题名称" width="150">
            <template slot-scope="scope">
              <el-input v-model="scope.row.batext" placeholder="请输入专题名称" :disabled="scope.row.disabled"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="baimage" label="内容" width="220">
            <template slot-scope="scope">
              <div @click="rowClick(scope.$index, 'img')">
                <el-upload class="avatar-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                           :on-success="uploadPicture" :disabled="scope.row.disabled">
                  <img v-if="scope.row.baimage" :src="scope.row.baimage" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="title" label="时间" width="480">
            <template slot-scope="scope">
              <el-date-picker v-model="scope.row.activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 3.5rem;" :disabled="scope.row.disabled" @blur="timeClick(scope)">
              </el-date-picker>
            </template>
          </el-table-column>
          <el-table-column prop="title" label="跳转" width="150">
            <template slot-scope="scope">
              <el-select v-model="scope.row.bannerToValue" class="m-input-l" placeholder="请选择" :disabled="scope.row.disabled"
                         style="width: 0.8rem" @change="bannerToValueChange">
                <el-option v-for="item in bannerToList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column prop="product" label="图片" width="220">
            <template slot-scope="scope">
              <div @click="rowClick(scope.$index, 'img')" v-if="scope.row.showPicture">
                <el-upload class="jump-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                           :on-success="uploadLongPicture" :disabled="scope.row.disabled">
                  <img v-if="scope.row.balongimg" :src="scope.row.balongimg" class="jump-img">
                  <i v-else class="el-icon-plus jump-img"></i>
                </el-upload>
              </div>
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
              <el-button type="text" size="small" @click="upBanner(scope)" v-if="scope.row.addSaveEdit != '1'" :disabled="scope.$index == '0'">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="display: flex; margin-top: 0.1rem">
          <div class="add-box" style="flex: 1;">
            <el-tooltip class="item" effect="light" content="添加专题" placement="right">
              <span class="m-item-add" @click="addBanner" v-if="addBannerBtn">+</span>
            </el-tooltip>
          </div>
          <p class="m-item-alert tr"><span style="color: red">* </span>轮播图尺寸大小750*280</p>
        </div>
      </div>


      <p class="m-form-label" style="margin-bottom: 0.2rem">热文管理</p>
      <div class="content-table">
        <el-table :data="hotMessageList" border style="width: 100%" v-loading="hotLoading">
          <!--<el-table-column prop="hmsort" label="热文顺序" width="100"></el-table-column>-->
          <el-table-column prop="hmtext" label="热文内容">
            <template slot-scope="scope">
              <el-input v-model="scope.row.hmtext" size="mini" placeholder="请输入热文内容" :disabled="scope.row.disabled"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="hmskiptype" label="跳转类型" width="130">
            <!--<template slot-scope="scope">
              <el-select v-model="scope.row.hmskiptype" class="m-input-l" placeholder="请选择" :disabled="scope.row.disabled"
                         style="width: 0.8rem" @change="bannerToValueChange">
                <el-option v-for="item in hotJumpList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </template>-->
          </el-table-column>
          <el-table-column prop="hmdisplaytype" label="热文读者" width="130"></el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'hot')" type="text" size="small" v-if="scope.row.editSave == '1'">编辑</el-button>
              <el-button @click="saveClick(scope, 'hot')" type="text" size="small" v-if="scope.row.editSave == '2'">保存</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteHotMessage(scope)">删除</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="upHotMessage(scope)" :disabled="scope.$index == '0' || scope.$index == hmdisplaytype">上移</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div style="display: flex">
        <div style="flex: 1">
          <el-tooltip effect="light" content="添加热文" placement="right">
            <span class="m-item-add" v-if="!show_div" @click="showDiv" style="margin-top: -0.1rem">+</span>
          </el-tooltip>
          <span class="m-item-add" v-if="show_div" @click="showDiv" style="margin-top: -0.1rem;">-</span>
        </div>
      </div>

      <div class="m-form-item" v-if="show_div" style="margin: 0.2rem 0 0.3rem 0">
        <p class="m-form-label">热文内容</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="hotValue" placeholder="请输入热文内容" maxlength="25" class="hot-message-input"></el-input>
          </div>
          <p class="m-item-alert" style="margin-top: 0.05rem; font-size: 0.12rem"><span style="color: red">* </span>字数控制在25字以内</p>
        </div>
        <p class="m-form-label">热文分类</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="hotJumpValue" class="m-input-l" placeholder="商品/专题/教程/公告">
              <el-option v-for="item in hotJump" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-if="hotJumpValue != ''" v-model="jumpToValue" filterable placeholder="请选择" style="width: 4rem; margin-left: 0.5rem">
              <el-option v-for="item in jumpToList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <p class="m-form-label">活动时间</p>
        <div class="m-item-content">
          <el-date-picker v-model="hotTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                          start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
          </el-date-picker>
        </div>
        <p class="m-form-label">热文读者</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="hotReader" class="m-input-l" placeholder="请选择可看到该热文的对象">
              <el-option v-for="item in hotReaderList" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
        <div class="save-btn" @click="addHotMessage">保 存</div>
      </div>


      <w-tab :list="tab_list"  @wTabClick="wTabClick" style="margin-top: 0.3rem"></w-tab>

      <div class="m-form-label choose-banner">
        <div class="title">推文管理</div>
        <div class="choose-box tr" style="margin-bottom: 0.1rem">
          <el-input v-model="activitySearch" placeholder="请输入推文内容搜索" style="width: 3rem; margin-right: 0.4rem"></el-input>
        </div>
        <div class="banner-btn" style="margin-right: 0.1rem" @click="searchActivity">搜 索</div>
      </div>
      <div class="content-table">
        <el-table :data="activityList" border style="width: 100%" v-loading="activityLoading" @selection-change="selectionChange">
          <el-table-column fixed="left" type="selection" width="55" v-if="activityToBanner"></el-table-column>
          <el-table-column prop="time" label="推文时间" width="320">
            <!--<template slot-scope="scope">
              <el-date-picker v-model="scope.row.activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 3.5rem;" @blur="activityTimeClick(scope)" :disabled="scope.row.disabled">
              </el-date-picker>
            </template>-->
          </el-table-column>
          <el-table-column prop="actext" label="推文内容">
            <template slot-scope="scope">
              <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 3 }" placeholder="请输入推文内容" v-model="scope.row.actext" :disabled="scope.row.disabled"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="acSkiptype" label="跳转类型" width="100"></el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'activity')" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteActivityClick(scope)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-form-label choose-banner" style="margin: -0.1rem 0 0.2rem 0; border-bottom: 1px solid #707070">
        <!--<div class="title">推文管理</div>-->
        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>

        <div class="choose-box tr" style="margin-bottom: 0.1rem">
          <el-select v-model="toBanner" class="m-input-l" placeholder="请选择专题内容页所对应的专题" style="width: 3rem; margin-right: 0.3rem">
            <el-option v-for="item in toBannerList" :key="item.value" :label="item.value" :value="item.id"></el-option>
          </el-select>
        </div>
        <el-tooltip class="item" effect="light" content="筛选出能跳转到专题内容页的推文" placement="bottom" v-if="!activityToBanner">
          <div class="banner-btn" @click="toBannerClick('1')">筛选推文</div>
        </el-tooltip>
        <div class="banner-btn" @click="toBannerClick('2')" v-if="activityToBanner" :disabled="true">绑定专题</div>
      </div>


      <div>
        <div class="m-form-item">
          <p class="m-form-label required" style="width: 0.8rem;">推文内容</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" placeholder="请输入推文内容" v-model="activityACtext" style="width: 4rem" ref="actext"></el-input>
            </div>
          </div>
        </div>
        <div class="m-form-item" style="min-height: 1.6rem; max-height: 1.8rem">
          <p class="m-form-label required" style="width: 0.8rem;">推文图片</p>
          <div class="m-item-content" style="width: 6rem;" :class="activityMediaSort > 4 ? 'five':''" id="abcd">
            <div class=" m-item-row">
              <el-upload action="string" :http-request="uploadActivityPicture" list-type="picture-card" :file-list="activityPictureList"
                         :on-preview="handlePictureCardPreview" :limit="9" :on-remove="pictureRemove" id="activityPicture" :on-exceed="onExceed">
                <i class="el-icon-plus"></i>
              </el-upload>
              <el-dialog :visible.sync="dialogVisible">
                <img :src="dialogImageUrl" alt="">
              </el-dialog>
            </div>
          </div>
        </div>
        <p class="m-form-label required" style="width: 0.8rem;">跳转类型</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="activityJumpValue" class="m-input-l" placeholder="请选择" :disabled="editActivity" style="width: 1.75rem">
              <el-option v-for="item in activityJumpList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <el-select v-if="activityJumpValue == '1' || activityJumpValue == '专题'" v-model="activityJumpToValue" @focus="focusselect('banner')" class="m-input-l" :placeholder="activityJumpToValue" style="width: 4rem; margin-left: 0.5rem">
              <el-option v-for="item in activityJumpToList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <el-select v-if="activityJumpValue == '2' || activityJumpValue == '商品'" v-model="activityJumpToValue" @focus="focusselect('product')" filterable :placeholder="activityJumpToValue" style="width: 4rem; margin-left: 0.5rem">
              <el-option v-for="item in activityJumpToList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <div v-if="activityJumpValue == '2' || activityJumpValue == '商品'" style="margin-left: 0.5rem">
              <span>虚拟销量：</span>
              <el-input v-model="activityProductSales" style="width: 1rem; text-align: center"></el-input>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label required" style="width: 0.8rem;">活动类型</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="activityType" class="m-input-l" placeholder="请选择">
                <el-option v-for="item in activityTypeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </div>
          </div>
        </div>
        <p class="m-form-label required" style="width: 0.8rem;">活动时间</p>
        <div class="m-item-content">
          <el-date-picker v-model="activityActivityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                          start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
          </el-date-picker>
        </div>
        <div class="num-list">
          <div class="num-box">
            <p class="m-form-label required" style="width: 0.9rem;">虚拟点赞数</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="likeNum" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box">
            <p class="m-form-label required" style="width: 0.8rem;">活动角标</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="activityBadge" class="m-input-s" placeholder="限两个字" maxlength="2"></el-input>
              </div>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label" style="width: 0.65rem; margin-top: 0.1rem">发布者</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="author" class="m-input-l" placeholder="请选择发布者" @focus="focusselect('author')">
                <!--<el-option v-for="item in authorList" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
                <el-option v-for="item in authorList" :key="item.value" :label="item.label" :value="item.value">
                  <div style="float: left; width: 3.4rem">{{ item.label }}</div>
                  <img style="float: left; width: 0.25rem; height: 0.25rem; border-radius: 50%" :src="item.suheader">
                </el-option>
              </el-select>
            </div>
          </div>
        </div>
        <div class="m-form-confirm-btn">
          <span @click="addActivity" v-if="!editActivity">保 存</span>
          <span @click="cancelActivity" v-if="editActivity">取 消</span>
          <span @click="saveClick('', 'activity')" v-if="editActivity">保 存</span>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import wTab from '../../components/common/wTab';
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    data(){
      return{
        name:'首页管理',
        hotJump: [          // 添加热文时的热文分类
          { value: '1', label: '商品' },
          { value: '2', label: '专题' },
          { value: '3', label: '教程' },
          { value: '4', label: '公告' }
        ],
        rowNum: "",         // 定位专题编辑-点击图片时是哪一行
        hotValue: '',       // 填写的热文内容
        hotJumpValue: '',   // 热文分类选择的值
        jumpToValue: '',    // 热文分类选择-后面选择器的值
        jumpToList: [],     //  热文分类选择-后面选择器的选择项
        hotTime: [],        // 热文分类的活动时间
        bannerList: [],       // 专题/banner的list
        bannerLoading: true,  // 专题表格加载中
        selectionList: [],    // 筛选推文时盛放acid的list
        toBanner: "",         // 筛选推文时专题的选择值
        toBannerList: [],     // 筛选推文时专题的可选择项
        activityToBanner: false,  // 依此判断筛选专题和绑定专题（前部勾选框）的显示情况
        hotLoading: true,         // 热文表格加载中
        hotMessageList: [],       // 热文集合
        hmdisplaytype: 0,         // 热文中普通用户可查看的热文数量
        hotJumpList: [            // 热文 - 跳转类型
          { value: "0", label: "无跳转" },
          { value: "1", label: "专题" },
          { value: "2", label: "商品" },
          { value: "3", label: "公告" },
          { value: "4", label: "教程" }
        ],
        hotReader: "",              // 热文 - 读者
        hotReaderList: [            // 热文 - 读者list
          { value: "0", label: "普通用户" },
          { value: "1", label: "合伙人" }
        ],
        activityLoading: true,    // 推文/活动表格加载中
        addBannerBtn: true,       // 依此判断添加banner按钮的显示情况
        // activityTime: [],
        activityMedia: [],        // 添加推文时盛放图片的list
        activityMediaSort: 0,     // 添加推文时图片的顺序编号
        activityPictureList: [],  // 推文上传/编辑时的图片墙list
        activitySearch: "",       // 搜索推文时输入的内容
        dialogImageUrl: '',       // 推文上传图片后预览的url
        dialogVisible: false,     // 推文上传图片后预览的允许与否
        editActivity: false,      // 是否在编辑activity
        activityList: [],         // 推文 - 活动list
        activityTypeList: [       // 添加推文/活动时的活动类型选择项
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
        likeNum: '',                // 推文-虚拟点赞数
        author: "",                 // 推文-发布者
        authorList: [],             // 推文-发布者list
        activityType: '',           // 添加推文/活动时的活动类型选择的值
        activityBadge: '',          // 推文-活动角标
        activityACtext: '',         // 推文-活动内容
        activityEditScope: '',      // 确定编辑的推文行数据，便于后续存回该行
        activityJumpValue: '',      // 推文-跳转类型选择的值
        activityJumpList: [         // 推文-跳转类型可选择的跳转项
          { value: '1', label: '专题' },
          { value: '2', label: '商品' }
        ],
        activityJumpToValue: '',    // 推文-跳转类型选择后具体的跳转id
        activityJumpToList: [],     // 推文-跳转类型选择后可选择的跳转项
        activityActivityTime: [],   // 推文-活动时间
        acidTemp: "",             // 用来暂存acid
        bannerToList: [           // 专题跳转去向的可选择项
          { value: '0', label: '长图' },
          { value: '1', label: '专题页' }
        ],
        activityProductSales: '', // 虚拟销量
        show_div: false,  // 显示添加热文的div
        tab_list: [],     // 顶部导航的list
        page_size: 5,     // 推文每页请求的数量
        total_page: 1,    // 推文 - 总页数
        tnid: "",         // 暂存导航栏的tnid
      }
    },
    components:{ pageTitle, Pagination, wTab },
    methods:{

      // 上传推文图片
      uploadActivityPicture(item) {
        let media = {};
        this.activityMediaSort = this.activityMediaSort + 1;
        let form = new FormData();
        form.append("file", item.file);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = activity", form).then(res => {
          if(res.data.status == 200){
            media = { amimage: res.data.data, amsort: this.activityMediaSort };
            this.activityMedia.push(media);
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 点击推文图片时执行的方法 - 预览
      handlePictureCardPreview(file, fileList) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },

      // 移除推文图片时执行的方法
      pictureRemove(file, fileList) {
        // console.log(file, fileList);
        this.activityMediaSort = this.activityMediaSort - 1;
        // this.activityMedia = [];
      },

      // 超过文件数量限制时执行的方法
      onExceed(file, fileList) {
        this.$message({ type: 'warning', message: "最多上传9张图片", duration: 1500 });
      },

      // select选择器获得焦点时执行
      focusselect(where) {
        // console.log(where)
        // 获取发布者/管理员list
        if(where == "author") {
          this.getAdmin();      // 获取管理员
        }
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

      // 当选择项发生变化时会触发该事件
      selectionChange(selection) {
        this.selectionList = [];
        // 将所选中推文的acid push到list中
        for(let i = 0; i < selection.length; i ++) {
          this.selectionList.push(selection[i].acid);
        }
      },

      // 点击编辑后-点击时间选择器时清空时间
      activityTimeClick(scope) {
        this.activityList = this.activityList.concat();
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
        this.bannerList[index].showPicture = true;
        this.bannerList[index].disabled = false;
        // this.bannerList[index].upDisabled = false;
        this.bannerList[index].addSaveEdit = "1";
        this.bannerList = this.bannerList.concat();
      },

      // 显示添加热文的div
      showDiv() {
        // 防止未添加的专题影响
        if(this.bannerList[this.bannerList.length - 1].baid == undefined) {
          this.addBannerBtn = true;
          this.bannerList.splice(this.bannerList.length - 1, 1);    // 刷新视图
        }
        // 显示添加热文的div
        if(this.show_div) {
          this.show_div = false;
        }else if(!this.show_div) {
          this.show_div = true;
        }
      },

      // 列表的编辑方法
      editClick(scope, where) {
        if(where == "banner") {
          this.bannerList[scope.$index].disabled = false;
          this.bannerList[scope.$index].addSaveEdit = "2";
          this.bannerList = this.bannerList.concat();
        }else if(where == "hot") {
          this.hotMessageList[scope.$index].disabled = false;
          this.hotMessageList[scope.$index].editSave = "2";
        }else if(where == "activity") {
          console.log(scope.row);
          // console.log(this.activityMedia);
          this.activityMedia = scope.row.media;     // 把已有图片赋给activityMedia
          this.editActivity = true;
          this.activityEditScope = scope.$index;
          this.acidTemp = this.activityList[scope.$index].acid;   // 暂存acid
          this.$refs.actext.focus();    // 推文内容输入框获得焦点
          this.activityPictureList = [];  // 图片list置为[]

          // 把点击的那一行数据赋给activity
          let activity = this.activityList[scope.$index];
          this.activityACtext = activity.actext;
          // console.log(activity);

          // 商品
          if(activity.acskiptype == "2") {
            this.activityJumpValue = "商品";
            this.activityJumpToValue = activity.product.prname;
            this.activityProductSales = activity.soldnum;
          }else if(activity.acskiptype == "1") {
            // 专题
            this.activityJumpValue = "专题";
            this.activityJumpToValue = activity.bigactivity.baid;
          }else if(activity.acskiptype == "0") {
            this.activityJumpValue = "0";
            // this.activityJumpToValue = activity.bigactivity.baid;
          }
          // console.log(this.activityJumpToValue);

          // 把activity的图片赋值给图片集合，同时把图片序号同步成图片数量
          for(let i = 0; i < activity.media.length; i ++) {
            this.activityPictureList.push({ url: activity.media[i].amimage });
          }
          this.activityMediaSort = activity.media.length;

          this.activityType = activity.actype;
          this.activityActivityTime = [activity.acstarttime, activity.acendtime];
          this.likeNum = activity.likenum;
          this.activityBadge = activity.tags[0].atname;
          this.author = activity.suuser.suname;
        }
      },

      // 保存编辑后的banner、热文、推文
      saveClick(scope, where) {
        // console.log(scope, where);
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
              this.$message({ message: "保存成功", type: 'success', duration: 1500 });

              this.bannerList[scope.$index].disabled = true;
              this.bannerList[scope.$index].addSaveEdit = "3";
              this.bannerList = this.bannerList.concat();
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }else if(where == "hot") {
          let hotMessage = this.hotMessageList[scope.$index];
          let params = {
            hmid: hotMessage.hmid,
            hmtext: hotMessage.hmtext
          };
          axios.post(api.update_one_hot_message + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success', duration: 1500 });

              this.hotMessageList[scope.$index].disabled = true;
              this.hotMessageList[scope.$index].editSave = "1";
              this.hotMessageList = this.hotMessageList.concat();
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }else if(where == "activity") {
          if(this.activityMediaSort != 4 && this.activityMediaSort != 6 && this.activityMediaSort != 9) {
            this.$message({ message: "上传推文图片时，数量需为4张、6张或9张", type: 'warning', duration: 1500 });
          }else {
            if(this.activityACtext == "" || this.activityJumpValue == "" || this.activityType == "" || this.activityBadge == "" || this.likeNum == ""
            // if(this.activityACtext == "" || this.activityJumpValue == "" || this.activityJumpToValue == "" || this.activityType == "" || this.activityBadge == "" || this.likeNum == ""
              || this.activityActivityTime.length != 2) {
              this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
              if(this.tnid == "") {
                this.$message({ message: "请刷新页面后重试", type: 'warning', duration: 1500 });
              }
            }else {
              let actype = "";
              for(let i = 0; i < this.activityTypeList.length; i ++) {
                if(this.activityTypeList[i].label == this.activityType) {
                  actype = this.activityTypeList[i].value;
                }
              }

              // 编辑推文后post的参数
              let params = {
                actype: actype,
                topnavid: this.tnid,
                actext: this.activityACtext,
                media: this.activityMedia,
                tags: [{ atname: this.activityBadge }],
                aclikeFakeNum: this.likeNum,
                acstarttime: this.activityActivityTime[0],
                acendtime: this.activityActivityTime[1],
                suid: this.author
              };

              if(this.activityProductSales != "") {
                params.acproductssoldfakenum = this.activityProductSales;   // 虚拟销量
              }
              console.log(params);
              axios.post(api.update_act + '?token=' + localStorage.getItem('token') + "&acid=" + this.acidTemp, params).then(res=>{
                if(res.data.status == 200){
                  this.$message({ message: res.data.message, type: 'success', duration: 1500 });

                  // 保存后把新数据回显到表格中
                  this.activityList[this.activityEditScope].actext = this.activityACtext;
                  this.activityList[this.activityEditScope].activityTime = this.activityActivityTime;
                  this.activityList = this.activityList.concat();

                  // 清空推文的编辑框
                  this.activityACtext = "";
                  this.activityJumpValue = "";
                  this.activityJumpToValue = "";
                  this.activityType = "";
                  this.activityActivityTime = "";
                  this.likeNum = "";
                  this.activityBadge = "";
                  this.author = "";
                  this.activityPictureList = [];  // 图片list置为[]
                  this.activityMediaSort = 0;   // 上传成功后图片数量置为0
                }else{
                  this.$message({ type: 'error', message: res.data.message, duration: 1500 });
                }
              });
            }
          }
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

          this.bannerLoading = true;
          axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + '&baid=' + this.bannerList[scope.$index].baid,
            { baisdelete: true }).then(res=>{
            if(res.data.status == 200){
              this.bannerLoading = false;
              this.$message({ message: "专题删除成功", type: 'success', duration: 1500 });
              this.bannerList.splice(scope.$index, 1);    // 刷新视图
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }).catch(() => {  });
      },

      // 删除热文
      deleteHotMessage(scope) {
        this.$confirm('此操作将删除该热文, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          axios.post(api.update_one_hot_message + '?token=' + localStorage.getItem('token'), { hmid: this.hotMessageList[scope.$index].hmid, HMisdelete: true }).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "热文删除成功", type: 'success', duration: 1500 });
              this.hotMessageList.splice(scope.$index, 1);    // 刷新视图
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }).catch(() => {  });
      },

      // 编辑/删除活动/推文
      deleteActivityClick(scope) {
        this.$confirm('此操作将删除该推文, 是否继续?', '提示',
        {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          this.activityLoading = true;
          axios.post(api.update_act + '?token=' + localStorage.getItem('token') + "&acid=" + this.activityList[scope.$index].acid, { acisdelete: true }).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "推文删除成功", type: 'success', duration: 1500 });
              this.activityList.splice(scope.$index, 1);    // 刷新视图
              this.activityLoading = false;
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }).catch(() => {  });
      },

      // 搜索推文
      searchActivity() {

      },

      // 编辑推文 - 取消
      cancelActivity() {
        // 点击取消按钮清空编辑框
        this.activityMediaSort = 0;
        this.activityACtext = "";
        this.activityJumpValue = "";
        this.activityJumpToValue = "";
        this.activityType = "";
        this.activityActivityTime = "";
        this.likeNum = "";
        this.activityBadge = "";
        this.author = "";
        this.activityPictureList = [];  // 图片list置为[]

        this.editActivity = false;      // 隐藏取消按钮
      },

      // 上移banner/专题
      upBanner(scope) {
        this.bannerLoading = true;
        axios.post(api.update_bact + '?token=' + localStorage.getItem('token') + "&baid=" + this.bannerList[scope.$index].baid,
          { basort: this.bannerList[scope.$index - 1].basort }).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: "专题上移成功", type: 'success', duration: 1500 });
            this.bannerList = [];
            this.getBanner();     // 获取专题
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 上移热文
      upHotMessage(scope) {
        this.hotLoading = true;
        axios.post(api.update_one_hot_message + '?token=' + localStorage.getItem('token'),
          { hmid: this.hotMessageList[scope.$index].hmid, hmsort: this.hotMessageList[scope.$index - 1].hmsort }).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: "热文上移成功", type: 'success', duration: 1500 });
            this.hotMessageList = [];
            this.hmdisplaytype = 0;
            this.getHotMessage();     // 获取热文
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取banner滚动图
      getBanner() {
        axios.get(api.get_bigactivitys + '?lasting=false&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.bannerLoading = false;

            this.bannerList = [];
            for(let i = 0; i < res.data.data.length; i++) {
              if(res.data.data[i].baposition == "0") {
                this.bannerList.push(res.data.data[i]);
              }
            }
            for(let i = 0; i < this.bannerList.length; i ++) {
              this.bannerList[i].activityTime = [this.bannerList[i].bastarttime, this.bannerList[i].baendtime];
              this.bannerList[i].disabled = true;
              this.bannerList[i].addSaveEdit = "3";

              if(this.bannerList[i].batype == "0") {
                this.bannerList[i].bannerToValue = "长图";
                this.bannerList[i].showPicture = true;     // 是否显示长图
              }else if(this.bannerList[i].batype == "1") {
                this.bannerList[i].bannerToValue = "专题页";
                this.bannerList[i].showPicture = false;     // 是否显示长图
              }
            }

            // 将专题内容页对应的专题筛选出来
            let toBanner = {};
            for(let i = 0; i < this.bannerList.length; i ++) {
              if(this.bannerList[i].batype == "1") {
                toBanner = { value: this.bannerList[i].batext, id: this.bannerList[i].baid };
                this.toBannerList.push(toBanner);
              }
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // 获取热文
      getHotMessage() {
        axios.get(api.get_all_hot_message + '?lasting=false&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.hotLoading = false;

            this.hotMessageList = res.data.data;
            for(let i = 0; i < this.hotMessageList.length; i ++) {
              // 转换热文读者
              if(this.hotMessageList[i].hmdisplaytype == "0") {
                this.hotMessageList[i].hmdisplaytype = "普通用户";
                this.hmdisplaytype += 1;
              }else if(this.hotMessageList[i].hmdisplaytype == "1") {
                this.hotMessageList[i].hmdisplaytype = "合伙人";
              }
              // 转换热文跳转类型
              if(this.hotMessageList[i].hmskiptype == "0") {
                this.hotMessageList[i].hmskiptype = "无跳转";
              }else if(this.hotMessageList[i].hmskiptype == "1") {
                this.hotMessageList[i].hmskiptype = "专题";
              }else if(this.hotMessageList[i].hmskiptype == "2") {
                this.hotMessageList[i].hmskiptype = "商品";
              }else if(this.hotMessageList[i].hmskiptype == "3") {
                this.hotMessageList[i].hmskiptype = "教程";
              }else if(this.hotMessageList[i].hmskiptype == "4") {
                this.hotMessageList[i].hmskiptype = "公告";
              }
              this.hotMessageList[i].disabled = true;
              this.hotMessageList[i].editSave = "1";
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // 模糊搜索-获取所有可选项
      getJumpTo(to, where) {
        // 搜索商品
        if(to == 'product') {
          axios.get(api.get_product + '?kw=').then(res => {
            if(res.data.status == 200) {
              let product = {};
              for(let i = 0; i < res.data.data.length; i ++) {
                product = { label: res.data.data[i].prname, value: res.data.data[i].prid };
                if(where == "activity") {
                  this.activityJumpToList.push(product);
                }else if(where == "hot") {
                  this.jumpToList.push(product);
                }
              }
              // console.log(this.jumpToList);
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          })
          // 搜索专题
        }else if(to == 'banner') {
          let banner = {};
          for(let i = 0; i < this.bannerList.length; i ++) {
            banner = { label: this.bannerList[i].batext, value: this.bannerList[i].baid };
            if(where == "activity") {
              // 防止未添加的专题影响
              if(this.bannerList[this.bannerList.length - 1].baid == undefined) {
                this.addBannerBtn = true;
                this.bannerList.splice(this.bannerList.length - 1, 1);    // 刷新视图
              }
              this.activityJumpToList.push(banner);
            }else if(where == "hot") {
              this.jumpToList.push(banner);
            }
          }
          // 搜索公告、教程
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
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          })
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
          BAtype: banner.bannerToValue,
          BAlongimg: banner.balongimg,
        };
        if(this.bannerList.length == 1) {
          params.BAsort = 0;
        }else {
          params.BAsort = this.bannerList[this.bannerList.length - 2].basort + 1      // -2为包含新添加的
        }
        // console.log(params);
        if(params.BAimage == undefined || params.BAtext == "" || params.BAstarttime == undefined || params.BAendtime == undefined || params.BAtype == undefined) {
          this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
        }else {
          if(params.BAtype == "0" && params.BAlongimg == undefined) {
            this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
          }else {
            axios.post(api.create_hbact + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: "保存成功", type: 'success', duration: 1500 });
                this.getBanner();       // 获取专题
                this.addBannerBtn = true;
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }
        }
      },

      // 添加热文
      addHotMessage () {
        if(this.hotValue == "" || this.hotTime.length != 2 || this.hotJumpValue == "" || this.jumpToValue == "" || this.hotReader == "") {
          this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
        }else {
          let params = {
            HMtext: this.hotValue,
            HMstarttime: this.hotTime[0],
            HMendtime: this.hotTime[1],
            HMSkipType: this.hotJumpValue,
            HMcontent: this.jumpToValue,
            HMdisplaytype: this.hotReader
          };
          // 添加热文时热文的HMsort
          if(this.hotMessageList.length == 0) {
            params.HMsort = 1;
          }else if(this.hotMessageList.length == 1) {
            params.HMsort = this.hotMessageList[0].hmsort + 1;
          }else if(this.hotMessageList.length > 1) {
            for(let i = 0; i < (this.hotMessageList.length - 1); i ++) {
              if(this.hotMessageList[i].hmsort > this.hotMessageList[i + 1].hmsort) {
                params.HMsort = this.hotMessageList[i].hmsort + 1;
              }else {
                params.HMsort = this.hotMessageList[i + 1].hmsort + 1;
              }
            }
          }
          axios.post(api.add_one_hot_message + '?token=' + localStorage.getItem('token'), params).then(res => {
            if(res.data.status == 200){
              this.$message({ type: 'success', message: res.data.message, duration: 1500 });
              this.getHotMessage();     // 获取热文

              this.hotValue = "";
              this.hotJumpValue = "";
              this.jumpToValue = "";
              this.hotReader = "";
              this.hotTime = [];
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }
      },

      // 添加推文/活动
      addActivity () {
        // 推文图片的数量需为0、4、6、9
        if(this.activityMediaSort != 4 && this.activityMediaSort != 6 && this.activityMediaSort != 9) {
          this.$message({ message: "上传推文图片时，数量需为4张、6张或9张", type: 'warning', duration: 1500 });
        }else {
          if(this.activityACtext == "" || this.activityJumpValue == "" || this.activityJumpToValue == "" || this.activityType == "" || this.activityBadge == "" || this.likeNum == ""
            || this.activityActivityTime.length != 2) {
            this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
            if(this.tnid == "") {
              this.$message({ message: "请刷新页面后重试", type: 'warning', duration: 1500 });
            }
          }else {
            let params = {
              ACSkipType: this.activityJumpValue,
              AClinkvalue: this.activityJumpToValue,
              ACtype: this.activityType,
              TopnavId: this.tnid,
              ACtext: this.activityACtext,
              media: this.activityMedia,
              tags: [{ ATname: this.activityBadge }],
              AClikeFakeNum: this.likeNum,
              ACstarttime: this.activityActivityTime[0],
              ACendtime: this.activityActivityTime[1]
            };
            if(this.activityProductSales != "") { // 虚拟销量不为空时
              params.ACProductsSoldFakeNum = this.activityProductSales;
            }
            if(this.author != "") { // 发布者不为空时
              params.SUid = this.author;
            }
            this.activityLoading = true;
            console.log(params);
            axios.post(api.add_one_activity + '?token=' + localStorage.getItem('token'), params).then(res => {
              if(res.data.status == 200){
                this.$message({ type: 'success', message: res.data.message, duration: 1500 });
                this.getActivity(0, this.page_size);     // 获取推文/内容

                // 保存成功后将input等置空
                this.activityACtext = "";
                this.activityJumpValue = "";
                this.activityJumpToValue = "";
                this.activityProductSales = "";
                this.activityType = "";
                this.activityActivityTime = "";
                this.likeNum = "";
                this.activityBadge = "";
                this.activityMedia = [];
                this.activityPictureList = [];   // 上传成功后图片list置为[]
                this.activityMediaSort = 0;   // 上传成功后图片数量置为0
                this.author = "";
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }
        }
      },

      // 获取首页顶部导航nav
      getTopNav() {
        axios.get(api.get_home).then(res => {
          if(res.data.status == 200) {
            for(let i = 0; i < res.data.data.length; i++) {
              let nav = { name: res.data.data[i].tnname, url: "", active: false, tnid: res.data.data[i].tnid };
              this.tab_list.push(nav);

              this.tab_list[0].active = true;
              this.tnid = this.tab_list[0].tnid;
            }
            this.getActivity(0, this.page_size);   // 获取首页活动/推文内容列表
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // 获取首页活动/推文内容列表
      getActivity(start, page_size, skiptype) {
        this.activityLoading = true;
        axios.get(api.get_all_activity + '?lasting=false&token=' + localStorage.getItem('token'),
          { params: { lasting: false, start: start || 0, count: page_size || this.page_size, tnid: this.tnid, skiptype: skiptype || "all" }}).then(res => {
          if(res.data.status == 200) {
            this.activityLoading = false;
            this.activityList = res.data.data;
            this.total_page = Math.ceil(res.data.count/this.page_size);

            for(let i = 0; i < this.activityList.length; i ++) {
              // 推文的跳转类型
              if(this.activityList[i].acskiptype == "0") {
                this.activityList[i].acSkiptype = "全部";
              }else if(this.activityList[i].acskiptype == "1") {
                this.activityList[i].acSkiptype = "专题页";
              }else if(this.activityList[i].acskiptype == "2") {
                this.activityList[i].acSkiptype = "商品";
              }
              // this.activityList[i].activityTime = [this.activityList[i].acstarttime, this.activityList[i].acendtime];
              this.activityList[i].time = this.activityList[i].acstarttime + " 至 " + this.activityList[i].acendtime;
              this.activityList[i].disabled = true;
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // 绑定专题并筛选推文
      toBannerClick(v) {
        if(v == "1") {
          // 只获取能跳转商品的推文，即acskiptype=2
          this.getActivity(0, this.page_size, "2");

          this.activityToBanner = true;
        }else if(v == "2") {
          if(this.selectionList.length == 0 || this.toBanner == "") {
            if(this.selectionList.length == 0) {
              this.$message({ type: 'warning', message: "请勾选推文", duration: 1500 });
            }
            if(this.toBanner == "") {
              this.$message({ type: 'warning', message: "请选择专题", duration: 1500 });
            }
            if(this.selectionList.length == 0 && this.toBanner == "") {
              this.$message({ type: 'warning', message: "请选择专题和推文", duration: 1500 });
            }
          }
          else {
            let params = {
              ACid_list: this.selectionList,
              BAid: this.toBanner,
            };
            axios.post(api.add_to_bigact + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.activityToBanner = false;
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }
        }
      },

      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list = [].concat(arr);

        this.tnid = this.tab_list[i].tnid;
        this.getActivity(0, this.page_size);   // 获取首页活动/推文内容列表
      },

      bannerToValueChange(v) {
        // console.log(v);
      },

      // 上传banner长图
      uploadLongPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = bannerLong", form).then(res => {
          if(res.data.status == 200){
            // console.log(res, file);
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }

          this.bannerList[this.rowNum].balongimg = res.data.data;
          this.bannerList = this.bannerList.concat();
          // this.imageUrl = res.data.data;
        });
      },

      // 上传banner图片
      uploadPicture(res, file) {
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = banner", form).then(res => {
          if(res.data.status == 200){
            // console.log(res, file);
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }

          this.bannerList[this.rowNum].baimage = res.data.data;
          this.bannerList = this.bannerList.concat();
          // this.imageUrl = res.data.data;
        });
      },

      // 上传图片前的限制方法
      /*beforeAvatarUpload(file) {
        this.$message({ type: 'warning', message: "上传中，请等待" });
        const isJPG = file.type === 'image/jpeg' || 'image/png';
        const isLt2M = file.size / 1024 / 1024 < 20;

        if (!isJPG) {
          this.$message({ type: 'error', message: "上传图片只能是 JPG 或 PNG 格式", duration: 1500 });
        }
        if (!isLt2M) {
          this.$message({ type: 'error', message: "上传图片大小不能超过 20MB", duration: 1500 });
        }
        return isJPG && isLt2M;
      },*/

      // 获取管理员
      getAdmin(){
        this.authorList = [];
        axios.get(api.get_all_suser + "?sutype=all&token=" + localStorage.getItem("token")).then(res => {
          if(res.data.status == 200) {
            for(let i = 0; i < res.data.data.length; i ++) {
              let author = { value: res.data.data[i].suid, label: res.data.data[i].suname, suheader: res.data.data[i].suheader };
              this.authorList.push(author);
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 分页点击方法
      pageChange(v) {
        console.log(v);
        this.getActivity(this.page_size * (v - 1), this.page_size);
      }
    },
    watch: {
      // 热文跳转类型的值发生变化
      hotJumpValue(newValue, oldValue) {
        // console.log(newValue);
        this.jumpToList = [];
        this.jumpToValue = "";
        if(newValue == "1") {
          this.getJumpTo("product", "hot");     // 获取所有商品
        }else if(newValue == "2") {
          this.getJumpTo("banner", "hot");     // 获取所有专题
        }else if(newValue == "3") {
          this.getJumpTo("3", "hot");     // 获取所有教程
        }else if(newValue == "4") {
          this.getJumpTo("4", "hot");     // 获取所有公告
        }
      },

      // 推文/活动跳转类型的值发生变化
      activityJumpValue(newValue, oldValue) {
        this.activityJumpToList = [];
        this.activityJumpToValue = "";
        if(newValue == "2") {
          // this.activityJumpToValue = "请输入关键词搜索商品";
          this.getJumpTo("product", "activity");     // 获取所有商品
        }else if(newValue == "1") {
          // this.activityJumpToValue = "请选择专题";
          this.getJumpTo("banner", "activity");     // 获取所有专题
        }else if(newValue == "") {

        }
      }
    },
    mounted() {
      this.getBanner();                 // 获取首页专题
      this.getHotMessage();             // 获取热文
      this.getTopNav();                 // 获取首页顶部导航nav
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
  .num-list {
    display: flex;
    .num-box {
      margin-right: 0.5rem;
    }
  }
  .choose-banner {
    display: flex;
    justify-content: space-between;
    .title {
      white-space: nowrap;
    }
    .choose-box {
      flex: 1;
    }
    .banner-btn {
      color: #ffffff;
      height: 0.2rem;
      line-height: 0.22rem;
      white-space: nowrap;
      font-size: 0.12rem;
      border-radius: 0.1rem;
      padding: 0.05rem 0.2rem;
      background-color: @mainColor;
    }
    .page-box {
      // margin: 0.1rem 0 0 -1.8rem;
    }
  }
</style>
