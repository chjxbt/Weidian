<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">

      <w-tab :list="tab_list1"  @wTabClick="wTabClick1"></w-tab>

      <div v-if="page == '每日10荐'">
        <p class="m-form-label">轮播图管理</p>
        <div class="content-table">
          <el-table :data="bannerList" border style="width: 100%" v-loading="bannerLoading">
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
            <el-table-column prop="product" label="长图" width="120">
              <template slot-scope="scope">
                <div @click="rowClick(scope.$index, 'img')" v-if="scope.row.showPicture">
                  <el-upload class="avatar-uploader-long" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                             :on-success="uploadLongPicture" :disabled="scope.row.disabled">
                    <img v-if="scope.row.balongimg" :src="scope.row.balongimg" class="long-picture">
                    <i v-else class="long-picture"></i>
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
            <el-table-column fixed="right" label="管理" width="220">
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
                <span class="m-item-add" style="left: 3.5rem" @click="addBanner" v-if="addBannerBtn">+</span>
              </el-tooltip>
            </div>
            <p class="m-item-alert tr">轮播图尺寸大小750*280</p>
          </div>
        </div>


        <div v-if="page == '每日10荐'" style="border-bottom: 1px #707070 solid; padding-bottom: 0.2rem; margin-bottom: 0.5rem">
          <p class="m-form-label" style="margin-bottom: 0.1rem">商品推荐管理</p>
          <div class="num-list" style="font-size: 16px; margin-bottom: -0.1rem">
            <div class="num-box">
              <p class="m-form-label">虚拟查看数</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <el-input v-model="productViewNum" class="m-input-s" placeholder="请输入查看数" :disabled="productDisabled"></el-input>
                </div>
              </div>
            </div>
            <div class="num-box">
              <p class="m-form-label">虚拟喜欢数</p>
              <div class="m-item-content">
                <div class=" m-item-row">
                  <el-input v-model="productLikeNum" class="m-input-s" placeholder="请输入喜欢数" :disabled="productDisabled"></el-input>
                </div>
              </div>
            </div>
            <div class="product-btn" @click="editClick('product', 'product')" v-if="!productEdit">编 辑</div>
            <div class="product-btn" @click="saveClick('product', 'product')" v-if="productEdit">保 存</div>
            <div class="product-btn" @click="cancelProduct" v-if="productEdit">取 消</div>
          </div>
          <div class="content-table">
            <el-table :data="productList" border v-loading="productLoading" style="width: 100%">
              <el-table-column prop="num" label="商品图片" width="200">
                <template slot-scope="scope">
                  <img class="product-img" :src="scope.row.prmainpic" style="width: 0.5rem; height: 0.5rem">
                </template>
              </el-table-column>
              <el-table-column prop="prname" label="商品名称">
                <template slot-scope="scope">
                  <el-select v-model="scope.row.prname" @focus="focusselect(scope.$index, 'product')" filterable placeholder="请输入关键词搜索商品" :disabled="productDisabled" @change="productChange">
                    <el-option v-for="item in activityJumpToList" :key="item.id" :label="item.label" :value="item.value" :disabled="item.disabled"></el-option>
                  </el-select>
                </template>
              </el-table-column>
              <el-table-column fixed="right" label="管理" width="300">
                <template slot-scope="scope">
                  <el-button type="text" size="small" @click="upProduct(scope)" :disabled="scope.$index == '0'">上移</el-button>
                  <el-button type="text" size="small">|</el-button>
                  <el-button type="text" size="small" @click="deleteProduct(scope)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
            <el-tooltip class="item" effect="light" content="添加推荐商品" placement="right">
              <span class="m-item-add" style="left: 3.5rem; margin-top: 0.1rem" @click="addProduct">+</span>
            </el-tooltip>
          </div>
        </div>
      </div>


      <w-tab :list="tab_list2" v-if="page == '素材圈'" class="m-ft-12"  @wTabClick="wTabClick2"></w-tab>

      <div class="m-form-label choose-banner">
        <div class="title">推文管理</div>
        <div class="choose-box tr">
          <el-input v-model="activitySearch" placeholder="请输入推文内容搜索" style="width: 3rem; margin-right: 0.2rem"></el-input>
        </div>
        <div class="banner-btn" @click="searchActivity(0, 5)" v-if="!searching">搜 索</div>
        <div class="banner-btn" @click="searchActivity(0, 5)" v-if="searching">搜 索</div>
        <div class="banner-btn" @click="cancelSearch" v-if="searching">取 消</div>
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
          <el-table-column prop="actitle" label="推文标题" width="150" v-if="page == '公告' || page == '教程'"></el-table-column>
          <el-table-column prop="actext" label="推文内容">
            <!--<template slot-scope="scope">
              <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 3 }" placeholder="请输入推文内容" v-model="scope.row.actext" :disabled="scope.row.disabled"></el-input>
            </template>-->
          </el-table-column>
          <el-table-column prop="acSkiptype" label="跳转类型" width="100"></el-table-column>
          <el-table-column prop="product" label="评论管理" width="100" v-if="page == '公告' || page == '教程'">
            <template slot-scope="scope">
              <div class="comments-text" @click="commentsDialog(scope)">查看</div>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="editClick(scope, 'activity')" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteActivityClick(scope)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
        <comments ref="comments"></comments>
      </div>


      <div>
        <div class="m-form-item" v-if="page == '公告' || page == '教程'">
          <p class="m-form-label required" style="width: 0.9rem;">推文标题：</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input v-model="activityTitle" placeholder="请输入内容" style="width: 4rem"></el-input>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label required" style="width: 0.9rem;">推文内容：</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" placeholder="请输入推文内容" v-model="activityACtext" style="width: 4rem" ref="actext"></el-input>
            </div>
          </div>
        </div>

        <div style="margin: 0.05rem 0 0.2rem 0" v-if="page == '教程'">
          <el-switch v-model="imgVideo" active-text="长图" inactive-text="视频" active-color="#91aeb5" inactive-color="#719aab"></el-switch>
        </div>

        <div class="m-form-item" style="min-height: 1.6rem; max-height: 1.8rem" v-if="page != '教程'">
          <p class="m-form-label required" style="width: 0.9rem;">推文图片：</p>
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

        <div class="m-form-item" v-if="page == '教程' && imgVideo">
          <p class="m-form-label required" style="width: 0.9rem;">推文图片：</p>
          <div class="m-item-content" style="width: 6rem;">
            <div class=" m-item-row">
              <el-upload class="long-upload" action="string" :http-request="uploadActivityLong" :show-file-list="false">
                <img v-if="longImg" class="long-img" :src="longImg">
                <i v-else class="el-icon-plus avatar-uploader-icon" style="line-height: 1.815rem"></i>
              </el-upload>
            </div>
          </div>
        </div>
        <div class="m-form-item" v-if="page == '教程' && !imgVideo">
          <p class="m-form-label required" style="width: 0.9rem;">教程视频：</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-upload class="video-upload" action="string" :http-request="uploadActivityVideo" :show-file-list="false">
                <img v-if="videoImgUrl" class="video-img" src="../../common/images/video-demo.jpg">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
          </div>
        </div>
        <div class="m-form-item" v-if="page == '每日10荐'">
          <p class="m-form-label required" style="width: 0.9rem;">跳转类型：</p>
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
        </div>
        <div class="m-form-item" v-if="page == '每日10荐'">
          <p class="m-form-label required" style="width: 0.9rem;">活动类型：</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="activityType" class="m-input-l" placeholder="请选择">
                <el-option v-for="item in activityTypeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </div>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label required" style="width: 0.9rem;" v-if="page == '每日10荐'">活动时间：</p>
          <p class="m-form-label" style="width: 0.9rem;" v-else>活动时间：</p>
          <div class="m-item-content">
            <el-date-picker v-model="activityActivityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                            start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
            </el-date-picker>
          </div>
        </div>
        <div class="num-list">
          <div class="num-box" v-if="page == '公告' || page == '教程'">
            <p class="m-form-label">虚拟浏览量：</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="viewsNum" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box" v-if="page == '素材圈'">
            <p class="m-form-label">虚拟发圈数：</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="hairLapsNum" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box" v-if="page != '素材圈'">
            <p class="m-form-label">虚拟点赞数：</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="likeNum" class="m-input-s" placeholder="请输入"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box box-display" v-if="page == '每日10荐'">
            <div class="m-form-label" style="margin-top: 0.28rem">活动角标：</div>
            <div class="m-item-content">
              <div class=" m-item-row">
                <div style="position: relative">
                  <img class="at-img" v-if="activityBadge" :src="activityBadge" @click="tagsDialog">
                  <div class="delete-tags" v-if="activityBadge" @click="activityBadge = ''">x</div>
                  <div class="at-text" v-if="!activityBadge" @click="tagsDialog">请点此选择</div>
                </div>
              </div>
            </div>
            <tags ref="tags" @getData="getData"></tags>
          </div>
        </div>
        <div class="m-form-item">
          <p class="m-form-label" style="width: 0.65rem;">发布者：</p>
          <div class="m-item-content">
            <div class=" m-item-row">
              <el-select v-model="author.name" class="m-input-l" placeholder="请选择发布者" @focus="focusselect('', 'author')">
                <!--<el-option v-for="item in authorList" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
                <el-option v-for="item in authorList" :key="item.value" :label="item.label" :value="item.value">
                  <div style="float: left; width: 3.4rem">{{ item.label }}</div>
                  <img style="float: left; width: 0.25rem; height: 0.25rem; border-radius: 50%" :src="item.suheader">
                </el-option>
              </el-select>
            </div>
          </div>
        </div>
        <div class="num-list" v-for="(item, index) in commentsList" v-if="page == '公告' || page == '教程'">
          <div class="num-box">
            <p class="m-form-label" style="width: 0.9rem;">评论人：</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="item.acorobot" style="width: 1.2rem"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box">
            <p class="m-form-label" style="width: 0.8rem;">评论内容：</p>
            <div class="m-item-content">
              <div class=" m-item-row">
                <el-input v-model="item.acotext" style="width: 2.3rem"></el-input>
              </div>
            </div>
          </div>
          <div class="num-box add-btn" v-if="index == (commentsList.length - 1)" @click="addComments()">+</div>
          <div class="num-box add-btn" v-else @click="addComments(index)">-</div>
        </div>
        <div class="m-form-item" v-if="page == '公告' || page == '教程'">
          <p class="m-form-label">推文置顶：</p>
          <el-switch style="margin: 0.1rem 0 0.2rem 0" v-model="placedTop" active-color="#91aeb5" inactive-color="#DCDCDC">
          </el-switch>
        </div>
        <div class="m-form-confirm-btn">
          <span @click="addActivity" v-if="!editActivity">保 存</span>
          <span @click="cancelActivity" v-if="editActivity">取 消</span>
          <span @click="saveClick('', 'activity')" v-if="editActivity">保 存</span>
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
                <el-button @click="handleClick(scope.row)" type="text" size="small">回复</el-button>
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
  import Pagination from "../../components/common/page";
  import wTab from '../../components/common/wTab';
  import tags from '../../components/activity/tags';
  import comments from '../../components/activity/comments';
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
        longImg: "",              // 长图url
        imgVideo: true,           // 选择视频或长图
        videoUrl:'',              // 教程页的视频链接
        videoImgUrl:'',           // 教程页的视频缩略图
        bannerList: [],           // 专题/banner的list
        bannerLoading: true,      // 专题表格加载中
        bannerToList: [           // 专题跳转去向的可选择项
          { value: '0', label: '长图' },
          { value: '1', label: '专题页' }
        ],
        author: { id: "", name: "" },               // 推文-发布者
        authorList: [],           // 推文-发布者list
        selectionList: [],        // 筛选推文时盛放acid的list
        toBanner: "",             // 筛选推文时专题的选择值
        toBannerList: [],         // 筛选推文时专题的可选择项
        addBannerBtn: true,
        activitySearch: "",       // 搜索推文时输入的内容
        searching: false,         // 是否正在搜索推文
        activityLoading: true,    // 推文/活动表格加载中
        activityTitle: '',        // 推文标题
        activityList: [],         // 推文/活动list
        activityToBanner: false,  // 依此判断筛选专题和绑定专题（前部勾选框）的显示情况
        hairLapsNum: '',          // 推文-虚拟发圈数
        viewsNum: '',             // 推文-虚拟浏览数
        likeNum: '',              // 推文-虚拟点赞数
        activityType: '',         // 添加推文/活动时的活动类型选择的值
        activityBadge: '',        // 推文-活动角标
        placedTop: false,         // 推文置顶
        activityACtext: '',       // 推文-活动内容
        dialogImageUrl: '',       // 推文上传图片后预览的url
        dialogVisible: false,     // 推文上传图片后预览的允许与否
        editActivity: false,      // 是否在编辑activity
        activityJumpValue: '',    // 推文-跳转类型选择的值
        activityJumpList: [       // 推文-跳转类型可选择的跳转项
          { value: '1', label: '专题' },
          { value: '2', label: '商品' }
        ],
        activityJumpToValue: '',  // 推文-跳转类型选择后具体的跳转id
        activityJumpToList: [],   // 推文-跳转类型选择后可选择的跳转项
        activityMedia: [],        // 添加推文时盛放图片的list
        activityMediaSort: 0,     // 添加推文时图片的顺序编号
        activityPictureList: [],  // 推文上传/编辑时的图片墙list
        activityProductSales: '', // 虚拟销量
        productList: [],          // 推荐商品的list
        productReid: [],          // 暂存推荐商品的reid
        productLoading: false,    // 推荐商品表格加载中
        productEdit: false,       // 是否在编辑推荐商品
        productDisabled: true,    // 推荐商品disabled
        productChoose: "",        // 编辑推荐商品-切换商品后选择的值
        productViewNum: "",       // 虚拟查看数
        productLikeNum: "",       // 虚拟喜欢数
        activityActivityTime: [], // 推文-活动时间
        commentsList: [             // 自行添加评论
          { acorobot: "", acotext: "" }
        ],
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
        page: "公告",  // 默认显示的页面
        tab_list1:[],     // 导航栏
        tab_list2:[],     // 素材圈的导航栏
        tableData: [
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' },
          { object: '新鲜出炉的周周奖现已发放，还不快去查收！', who: '张三', time: '2018-09-15 18:56:21', content: '评论测试评论测试评论测试评论测试评论测试评论测试评论测试' }
        ],
        page_size: 5,     // 推文每页请求的数量
        total_page: 1,    // 推文 - 总页数
        tnid: "",         // 暂存导航栏的tnid
      }
    },
    components:{ pageTitle, Pagination, wTab, tags, comments },
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

      // 上传教程长图
      uploadActivityLong(item) {
        let media = {};
        // this.activityMediaSort = this.activityMediaSort + 1;
        let form = new FormData();
        form.append("file", item.file);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = course", form).then(res => {
          if(res.data.status == 200){
            this.longImg = res.data.data;

            media = { amimage: res.data.data, amsort: 1 };
            this.activityMedia = [];
            this.activityMedia.push(media);
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 上传教程视频
      uploadActivityVideo(item) {
        let media = {};
        // this.activityMediaSort = this.activityMediaSort + 1;
        let form = new FormData();
        form.append("file", item.file);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token') + "&filetype = video", form).then(res => {
          if(res.data.status == 200){
            this.videoImgUrl = "../../common/images/video-demo.jpg";

            media = { amvideo: res.data.data };
            this.activityMedia = [];
            this.activityMedia.push(media);
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
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
      },

      // 超过文件数量限制时执行的方法
      onExceed(file, fileList) {
        this.$message({ type: 'warning', message: "最多上传9张图片", duration: 1500 });
      },

      handleRemove(file, fileList) {
        console.log(file, fileList);
      },

      // 轮播图管理-确定点击的是第几行
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
        if(where == "banner") {
          this.bannerList[scope.$index].disabled = false;
          this.bannerList[scope.$index].addSaveEdit = "2";
          this.bannerList = this.bannerList.concat();
        }else if(where == "product") {
          // this.productList[scope.$index].disabled = false;
          // this.productList[scope.$index].editSave = "2";
          this.productDisabled = false;
          this.productEdit = true;
        }else if(where == "activity") {
          this.editActivity = true;
          this.activityEditScope = scope.$index;
          this.acidTemp = this.activityList[scope.$index].acid;   // 暂存acid
          this.$refs.actext.focus();    // 推文内容输入框获得焦点
          this.activityPictureList = [];  // 图片list置为[]

          // 把点击的那一行数据赋给activity
          let activity = this.activityList[scope.$index];
          this.activityACtext = activity.actext;
          // console.log(activity);

          // 把activity的图片赋值给图片集合，同时把图片序号同步成图片数量
          for(let i = 0; i < activity.media.length; i ++) {
            this.activityPictureList.push({ url: activity.media[i].amimage });
          }
          this.activityMediaSort = activity.media.length;
          this.activityActivityTime = [activity.acstarttime, activity.acendtime];
          this.author.name = activity.suuser.suname;
          this.author.id = activity.suuser.suid;

          if(this.page == "每日10荐") {
            // 商品
            if(activity.acskiptype == "2") {
              this.activityJumpValue = "商品";
              // this.activityJumpToValue = activity.product.prname;
              // this.activityProductSales = activity.soldnum;
            }else if(activity.acskiptype == "1") {
              // 专题
              this.activityJumpValue = "专题";
              // this.activityJumpToValue = activity.bigactivity.baid;
            }else if(activity.acskiptype == "0") {
              this.activityJumpValue = "0";
              // this.activityJumpToValue = activity.bigactivity.baid;
            }
            // console.log(this.activityJumpToValue);

            this.activityType = activity.actype;
            this.activityMedia = activity.media;
            this.likeNum = activity.likenum;
            this.activityBadge = activity.tags[0].atname;
          }else if(this.page == "素材圈") {
            this.hairLapsNum = activity.foward;
            this.activityMedia = activity.media;
          }else if(this.page == "公告" || this.page == "教程") {
            this.activityTitle = activity.actitle;
            this.activityMedia = activity.media;
            this.likeNum = activity.likenum;
            this.viewsNum = activity.acbrowsenum;
            this.commentsList = [];
            for(let i = 0; i < activity.comment.length; i ++) {
              this.commentsList.push({ acorobot: activity.comment[i].user.usname, acotext: activity.comment[i].actext });
            }
            this.placedTop = activity.acistop;
            if(this.page == "教程" && this.imgVideo) {
              this.longImg = activity.media[0].amimage;
            }else if(this.page == "教程" && !this.imgVideo) {
              // this.videoImgUrl = activity.media[0].amvideo;
            }
          }
        }
      },

      // 编辑推文 - 取消
      cancelActivity() {
        // 点击取消按钮清空编辑框
        this.activityMediaSort = 0;
        this.activityTitle = "";
        this.activityACtext = "";
        this.activityJumpValue = "";
        this.activityJumpToValue = "";
        this.activityType = "";
        this.activityActivityTime = "";
        this.likeNum = "";
        this.viewsNum = "";
        this.hairLapsNum = "";
        this.activityBadge = "";
        this.longImg = "";
        this.videoImgUrl = "";
        this.placedTop = false;
        this.author = {};
        this.commentsList = [{ acorobot: "", acotext: "" }];
        this.activityPictureList = [];  // 图片list置为[]

        this.editActivity = false;      // 隐藏取消按钮
      },

      // select选择器获得焦点时执行
      focusselect(index, where) {
        if(where == "product") {
          this.rowNum = index;      // 确定点击的是第几行

          // console.log(this.productList);
          this.getJumpTo("product", "product");
        } else if(where == "author") {    // 获取发布者/管理员list
          this.getAdmin();
        }
      },

      // select选择器获得焦点时执行
      productChange(value) {
        this.productChoose = value;

        // 更新选中商品的行数据
        for(let i = 0; i < this.activityJumpToList.length; i ++) {
          if(value == this.activityJumpToList[i].value) {
            this.productList[this.rowNum].prid = this.activityJumpToList[i].id;
            this.productList[this.rowNum].prmainpic = this.activityJumpToList[i].prmainpic;
          }
        }
        this.productList = this.productList.concat();
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
        }else if(where == "product") {
          let PRid_list = [];
          for(let i = 0; i < this.productList.length; i ++) {
            // 保存时去除空商品
            if(this.productList[i].prid == undefined) {
              this.productList.splice(i, 1);
            }else if(this.productList[i].prid != "") {
              PRid_list.push({ prid: this.productList[i].prid, prsort: i });
            }
          }
          let params = {
            reviewnum: this.productViewNum,
            relikenum: this.productLikeNum,
            prid_list: PRid_list
          };
          this.productLoading = true;
          axios.post(api.update + '?token=' + localStorage.getItem('token') + "&reid=" + this.productReid, params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "保存成功", type: 'success', duration: 1500 });

              this.productLoading = false;
              this.productDisabled = true;
              this.productEdit = false;
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }else if(where == "activity") {
          // if(this.activityMediaSort != 4 && this.activityMediaSort != 6 && this.activityMediaSort != 9) {
          //   this.$message({ message: "上传推文图片时，数量需为4张、6张或9张", type: 'warning', duration: 1500 });
          // }else {
            if(this.activityACtext == ""
            // if(this.activityACtext == "" || this.activityJumpValue == "" || this.activityJumpToValue == "" || this.activityType == "" || this.activityActivityTime.length != 2
            ) {
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
                accomments: this.commentsList,
                tags: [{ atname: this.activityBadge }],
                aclikeFakeNum: this.likeNum,
                acbrowsenum: this.viewsNum,
                acforwardFakenum: this.hairLapsNum,
                acstarttime: this.activityActivityTime[0],
                acendtime: this.activityActivityTime[1],
                suid: this.author.id,
                acistop: this.placedTop
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
                  this.activityTitle = "";
                  this.activityACtext = "";
                  this.activityJumpValue = "";
                  this.activityJumpToValue = "";
                  this.activityType = "";
                  this.activityActivityTime = "";
                  this.likeNum = "";
                  this.viewsNum = "";
                  this.hairLapsNum = "";
                  this.activityBadge = "";
                  this.longImg = "";
                  this.placedTop = false;
                  this.activityTitle = "";
                  this.author = {};
                  this.commentsList = [{ acorobot: "", acotext: "" }];  // 自行添加评论
                  this.activityPictureList = [];  // 图片list置为[]
                  this.activityMediaSort = 0;   // 上传成功后图片数量置为0
                }else{
                  this.$message({ type: 'error', message: res.data.message, duration: 1500 });
                }
              });
            }
          // }
        }
      },

      // 清空from的编辑框
      clearFrom() {
        // 清空推文的编辑框
        this.activityTitle = "";
        this.activityACtext = "";
        this.activityJumpValue = "";
        this.activityJumpToValue = "";
        this.activityType = "";
        this.activityActivityTime = "";
        this.likeNum = "";
        this.viewsNum = "";
        this.hairLapsNum = "";
        this.activityBadge = "";
        this.placedTop = false;
        this.activityTitle = "";
        this.author = {};
        this.activityPictureList = [];  // 图片list置为[]
        this.activityMediaSort = 0;   // 上传成功后图片数量置为0
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
            axios.post(api.create_dbact + '?token=' + localStorage.getItem('token'), params).then(res=>{
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

      // 取消添加banner
      cancelAdd(scope) {
        this.addBannerBtn = true;
        this.bannerList.splice(scope.$index, 1);    // 刷新视图
      },

      // 取消添加Product
      cancelProduct() {
        this.productEdit = false;
        this.productDisabled = true;

        // console.log()
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

      // 推荐商品 - 添加商品
      addProduct() {
        this.productEdit = true;
        this.productDisabled = false;
        let index = this.productList.length;
        this.productList[index] = {};
        this.productList[index].prmainpic = "";
        this.productList[index].prname = "";
        this.productList = this.productList.concat();
      },

      // 添加推文/活动 - 判空
      addActivity () {
        if(this.tnid == "") {
          this.$message({ message: "请刷新页面后重试", type: 'warning', duration: 1500 });
        }else {
          if(this.activityACtext == "") {
            this.$message({ message: "请填写推文内容", type: 'warning', duration: 1500 });
          }else {
            // 素材圈、公告、教程页面的活动时间非必填
            if(this.activityActivityTime.length != 2 && this.page == "每日10荐") {
              this.$message({ message: "请填写推文时间", type: 'warning', duration: 1500 });
            }
            else {
              if(this.page == "每日10荐" || this.page == "素材圈" || this.page == "公告") {
                // 除教程外的其他页面，推文图片的数量需为0、4、6、9
                if(this.activityMediaSort != 4 && this.activityMediaSort != 6 && this.activityMediaSort != 9) {
                  this.$message({ message: "上传推文图片时，数量需为4张、6张或9张", type: 'warning', duration: 1500 });
                }else {
                  // 每日十荐需要选择跳转
                  if(this.page == "每日10荐") {
                    if(this.activityJumpValue == "" || this.activityJumpToValue == "" || this.activityType == "") {
                      this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
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
                      this.activityParams(params);
                    }
                  }else if(this.page == "素材圈") {
                    let params = {
                      TopnavId: this.tnid,
                      ACtext: this.activityACtext,
                      media: this.activityMedia,
                      ACforwardFakenum: this.hairLapsNum,
                      ACstarttime: this.activityActivityTime[0],
                      ACendtime: this.activityActivityTime[1]
                    };
                    // console.log(params);
                    this.activityParams(params);
                  }else if(this.page == "公告") {
                    if(this.activityTitle == "") {
                      this.$message({ message: "请填写推文标题", type: 'warning', duration: 1500 });
                    }else {
                      let params = {
                        TopnavId: this.tnid,
                        ACtitle: this.activityTitle,
                        ACtext: this.activityACtext,
                        media: this.activityMedia,
                        accomments: this.commentsList,
                        AClikeFakeNum: this.likeNum,
                        ACbrowsenum: this.viewsNum,
                        ACstarttime: this.activityActivityTime[0],
                        ACendtime: this.activityActivityTime[1],
                        ACistop: this.placedTop
                      };
                      // console.log(params);
                      this.activityParams(params);
                    }
                  }
                }
              }else {
                let params = {
                  TopnavId: this.tnid,
                  ACtitle: this.activityTitle,
                  ACtext: this.activityACtext,
                  media: this.activityMedia,
                  accomments: this.commentsList,
                  AClikeFakeNum: this.likeNum,
                  ACbrowsenum: this.viewsNum,
                  ACstarttime: this.activityActivityTime[0],
                  ACendtime: this.activityActivityTime[1],
                  ACistop: this.placedTop
                };
                // console.log(params);
                if(this.author.id != "") { // 发布者不为空时
                  params.SUid = this.author.id;
                }
                this.activityParams(params);
              }
            }
          }
        }
      },

      // 拼装activity参数
      activityParams(params) {
        if(this.activityProductSales != "") {
          params.ACProductsSoldFakeNum = this.activityProductSales;
        }
        this.activityLoading = true;
        console.log(params);
        axios.post(api.add_one_activity + '?token=' + localStorage.getItem('token'), params).then(res => {
          if(res.data.status == 200){
            this.$message({ type: 'success', message: res.data.message, duration: 1500 });
            this.getActivity(0, this.page_size);     // 获取推文/内容

            // 保存成功后将input等置空
            this.activityTitle = "";
            this.activityACtext = "";
            this.activityJumpValue = "";
            this.activityJumpToValue = "";
            this.activityProductSales = "";
            this.activityType = "";
            this.activityActivityTime = "";
            this.likeNum = "";
            this.viewsNum = "";
            this.hairLapsNum = "";
            this.activityBadge = "";
            this.longImg = "";
            this.videoImgUrl = "";
            this.placedTop = false;
            this.activityMedia = [];
            this.commentsList = [{ acorobot: "", acotext: "" }];  // 自行添加评论
            this.activityPictureList = [];   // 上传成功后图片list置为[]
            this.activityMediaSort = 0;   // 上传成功后图片数量置为0
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
              if(res.data.data[i].baposition == "1") {
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
              // this.tnid = this.tab_list2[0].tnid;
            }

            this.getActivity(0, this.page_size);      // 获取首页活动/推文内容列表
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 获取首页活动/推文内容列表
      getActivity(start, page_size, skiptype) {
        this.activityLoading = true;
        axios.get(api.get_all_activity + '?token=' + localStorage.getItem('token'),
          { params: { lasting: false, start: start || 0, count: page_size || this.page_size, tnid: this.tnid, skiptype: skiptype || "all" }}).then(res => {
          if(res.data.status == 200) {
            this.activityLoading = false;
            this.activityList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);

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
        });
      },

      // 上传banner图
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
        });
      },

      // 模糊搜索-获取所有可选项
      getJumpTo(to, where) {
        this.activityJumpToList = [];     // 先将可选择项置为空
        if(to == 'product') {
          axios.get(api.get_product + '?kw=').then(res => {
            if(res.data.status == 200) {
              let product = {};
              for(let i = 0; i < res.data.data.length; i ++) {
                product = { value: res.data.data[i].prname, id: res.data.data[i].prid, prmainpic: res.data.data[i].prmainpic };
                if(where == "activity") {
                  this.activityJumpToList.push(product);
                }else if(where == "product") {
                  this.activityJumpToList.push(product);

                  // 双重循环将已选择的商品disabled
                  for(let i = 0; i < this.activityJumpToList.length; i ++) {
                    if(this.productList[this.productList.length - 1].prname == "") {
                      for(let j = 0 ; j < (this.productList.length - 1); j ++) {
                        if(this.productList[j].prid == this.activityJumpToList[i].id) {
                          this.activityJumpToList[i].disabled = true;
                        }
                      }
                    }else {
                      for(let j = 0 ; j < this.productList.length; j ++) {
                        if(this.productList[j].prid == this.activityJumpToList[i].id) {
                          this.activityJumpToList[i].disabled = true;
                        }
                      }
                    }
                  }
                }
              }
              // console.log(this.jumpToList);
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
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

      // 搜索推文
      searchActivity(start, page_size) {
        if(this.activitySearch) {
          // if(!this.searching) {
          this.searching = true;

          this.activityLoading = true;
          axios.get(api.get_search + '?token=' + localStorage.getItem('token'),
            { params: { PRname: this.activitySearch, start: start || 0, count: page_size || this.page_size, serachact: true, tnid: this.tnid } }).then(res => {
            if(res.data.status == 200) {
              this.activityLoading = false;
              this.activityList = res.data.data;
              this.total_page = Math.ceil(res.data.count / this.page_size);

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
          });
          // }
        }else if(this.activitySearch == "") {
          this.getActivity(0, this.page_size);
        }
      },

      // 取消搜索
      cancelSearch() {
        this.searching = false;
        this.activitySearch = "";
        this.getActivity(0, this.page_size);
      },

      // 当选择项发生变化时会触发该事件
      selectionChange(selection) {
        this.selectionList = [];
        // 将所选中推文的acid push到list中
        for(let i = 0; i < selection.length; i ++) {
          this.selectionList.push(selection[i].acid);
        }
      },

      // 评论列表的操作方法
      handleClick(row) {
        console.log(row);
      },

      // 导航栏
      wTabClick1(i){
        let arr = [].concat(this.tab_list1);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.page = arr[i].name;
        this.tab_list1 = [].concat(arr);

        this.tnid = this.tab_list1[i].tnid;
        this.clearFrom();         // 清空输入框
        this.getActivity(0, this.page_size);   // 获取首页活动/推文内容列表
        if(this.page == "每日10荐") {
          this.getProduct();  // 获取推荐商品
        }else if(this.page == "素材圈") {
          this.tnid = this.tab_list2[0].tnid;
        }
      },

      // 素材圈的导航栏
      wTabClick2(i){
        let arr = [].concat(this.tab_list2);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list2 = [].concat(arr);

        this.tnid = this.tab_list2[i].tnid;
        this.clearFrom();         // 清空输入框
        this.getActivity(0, this.page_size);   // 获取首页活动/推文内容列表
      },

      // 获取推荐商品
      getProduct() {
        this.productList = [];
        this.productLoading = true;
        axios.get(api.get_info + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.productViewNum = res.data.data[0].reviewnum;     // 虚拟查看数
            this.productLikeNum = res.data.data[0].relikenum;     // 虚拟喜欢数

            for(let i = 0; i < res.data.data[0].products.length; i ++) {
              let product = res.data.data[0].products[i];
              // product.disabled = true;
              // product.editSave = "1";
              this.productList.push(product);
            }
            this.productReid = res.data.data[0].reid;
            this.productLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        })
      },

      // 上移推荐商品
      upProduct(scope) {
        let params = {
          prid_list: [
            { prid: this.productList[scope.$index].prid, rpsort: this.productList[scope.$index - 1].rpsort }
          ]
        };
        this.productLoading = true;
        axios.post(api.update + '?token=' + localStorage.getItem('token') + "&reid=" + this.productReid, params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: "上移成功", type: 'success', duration: 1500 });
            this.getProduct();    // 获取推荐商品
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 删除推荐商品
      deleteProduct(scope) {
        this.$confirm('此操作将删除该推荐, 是否继续?', '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          let params = {
            prid_list: [
              { prid: this.productList[scope.$index].prid, prisdelete: true }
            ]
          };
          this.productLoading = true;
          axios.post(api.update + '?token=' + localStorage.getItem('token') + "&reid=" + this.productReid, params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "删除成功", type: 'success', duration: 1500 });
              this.productList.splice(scope.$index, 1);
              this.productLoading = false;
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }).catch(() => {  });
      },

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

      // 打开tags子组件的dialog
      tagsDialog() {
        this.$refs.tags.getTags(this.activityBadge);
      },

      // 打开comments子组件的dialog
      commentsDialog(scope) {
        this.$refs.comments.getComments(scope.row);
      },

      // 接收子组件传过来的勾选角标
      getData(atname) {
        this.activityBadge = atname;
      },

      // 添加一行评论
      addComments(i) {
        if(i == undefined) {
          let index = this.commentsList.length;
          this.commentsList[index] = {};
          this.commentsList[index].acorobot = "";
          this.commentsList[index].acotext = "";
          this.commentsList = this.commentsList.concat();
        }else {
          this.commentsList.splice(i, 1);
        }
      },

      // 分页点击方法
      pageChange(v) {
        if(!this.searching) {
          this.getActivity(this.page_size * (v - 1), this.page_size);
        }else {
          this.searchActivity(this.page_size * (v - 1), this.page_size);
        }
      }
    },
    watch: {
      // 推文/活动跳转类型的值发生变化
      activityJumpValue(newValue, oldValue) {
        this.activityJumpToList = [];
        // this.activityJumpToValue = "";
        if(newValue == "2") {
          // this.activityJumpToValue = "请输入关键词搜索商品";
          this.getJumpTo("product", "activity");     // 获取所有商品
        }else if(newValue == "1") {
          // this.activityJumpToValue = "请选择专题";
          this.getJumpTo("banner", "activity");     // 获取所有专题
        }else if(newValue == "") {

        }
      },

      // productList的值发生变化
      productList(newValue, oldValue) {
        // console.log(newValue, oldValue);
      }
    },
    mounted() {
      this.getBanner();     // 获取首页专题
      this.getTopNav();     // 获取首页顶部导航nav
      if(this.page == "每日10荐") {
        this.getProduct();  // 获取推荐商品
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .long-picture {
    width: 0.3rem;
    height: 0.5rem;
  }
  .content-table {
    padding-top: 0.1rem;
    .page-box {
      margin-top: 0.1rem;
    }
    .comments-text {
      color: #4169E1;
      font-size: 0.11rem;
    }
  }
  .el-table .cell {
    text-align: left;
  }
  .product-img {

  }
  .num-list {
    display: flex;
    justify-content: flex-start;
    .num-box {
      margin-right: 0.5rem;
    }
    .box-display {
      display: flex;
    }
    .add-btn {
      font-size: 0.2rem;
      margin: 0.3rem 0 0 -0.3rem;
    }
    .product-btn {
      height: 0.2rem;
      line-height: 0.21rem;
      white-space: nowrap;
      color: #ffffff;
      background-color: @mainColor;
      border-radius: 0.1rem;
      padding: 0.02rem 0.15rem;
      margin: 0.26rem 0 0 0.3rem;
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
      margin-left: 0.1rem;
      background-color: @mainColor;
    }
  }
  .at-img {
    width: 0.35rem;
    height: 0.35rem;
    margin: 0.13rem 0 0 0.2rem;
    border: 1px solid #ababab;
  }
  .delete-tags {
    color: #ababab;
    position: absolute;
    top: 0.05rem;
    right: -0.03rem;
  }
  .at-text {
    color: #4169E1;
    font-size: 0.12rem;
    margin: 0.22rem 0 0 0.1rem;
    border-bottom: 1px solid #4169E1;
  }
</style>
