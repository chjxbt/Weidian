<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <div class="m-form-item  m-item-m">
        <span class="m-item-add">+</span>
        <p class="m-form-label">轮播图管理</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-upload
              class="avatar-uploader m-upload"
              action="https://jsonplaceholder.typicode.com/posts/"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload">
              <img v-if="imageUrl" :src="imageUrl" class="avatar">
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
            <el-select v-model="value"  placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <p class="m-item-alert">轮播图尺寸大小750*280</p>
        </div>
      </div>
      <div class="m-form-item m-from-border">
        <span class="m-item-add">+</span>
        <p class="m-form-label">热文编辑</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value" placeholder="请输入内容"></el-input>
          </div>
          <p class="m-item-alert">字数控制在25字以内*280</p>
        </div>
        <p class="m-form-label">商品选择</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="value" class="m-input-l" placeholder="请选择">
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
      <ul class="m-weidian-tabbox">
        <li>
          <span class="m-tab-name active">上新</span>
          <span class="m-tab-line">/</span>
        </li>
        <li>
          <span class="m-tab-name ">特卖</span>
          <span class="m-tab-line">/</span>
        </li>
        <li>
          <span class="m-tab-name ">爆款</span>
          <span class="m-tab-line">/</span>
        </li>
        <li>
          <span class="m-tab-name">预售</span>
        </li>
      </ul>
      <div class="m-form-item">
        <p class="m-form-label">商家名称</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value" placeholder="请输入内容"></el-input>
          </div>
        </div>
      </div>
      <div class="m-form-item">
        <p class="m-form-label">商家头像</p>
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
      <div class="m-form-item">
        <p class="m-form-label">商家描述</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <textarea v-model="value" class="m-textarea" placeholder="请输入内容"></textarea>
          </div>
        </div>
      </div>
      <div class="m-form-item">
        <p class="m-form-label">商家图片</p>
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
      <div class="m-form-item">
        <p class="m-form-label">商家价格</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-input v-model="value" class="m-input-s" placeholder="请输入内容"></el-input>
          </div>
        </div>
      </div>
      <div class="m-form-item">
        <p class="m-form-label">活动选择</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <el-select v-model="value" class="m-input-l" placeholder="请选择">
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
      <div class="m-form-confirm-btn">
        <span>确定</span>
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
        value: ''
      }
    },
    components:{
      pageTitle
    },
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";
</style>
