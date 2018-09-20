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
      <div class="m-form-item  m-item-m">
        <span class="m-item-add">+</span>
        <p class="m-form-label">商品轮播图管理</p>
        <div class="m-item-content">
          <div class=" m-item-row m-s">
            <el-upload
              class="avatar-uploader"
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
        </div>
      </div>
      <w-tab :list="tab_list1"  @wTabClick="wTabClick1"></w-tab>
      <w-tab :list="tab_list2" v-if="page == '素材圈'" class="m-ft-12"  @wTabClick="wTabClick2"></w-tab>
      <!--<div class="m-form-item">
        <p class="m-form-label">商品名称</p>
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
      </div>-->
      <div class="m-form-item">
        <p class="m-form-label">商品描述</p>
        <div class="m-item-content">
          <div class=" m-item-row">
            <textarea v-model="value" class="m-textarea" placeholder="请输入内容"></textarea>
          </div>
        </div>
      </div>
      <div class="m-form-item  m-item-m">
        <span class="m-item-add">+</span>
        <p class="m-form-label">商家图片</p>
        <div class="m-item-content">
          <div class=" m-item-row m-s">
            <el-upload
              class="avatar-uploader"
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
      <!--<div class="m-form-confirm-btn">
        <span>确定</span>
      </div>-->
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';
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
        page:'每日10荐',
        tab_list1:[
          {
            name:'每日10荐',
            url:'',
            active:true
          },
          {
            name:'素材圈',
            url:'',
            active:false
          },
          {
            name:'公告',
            url:'',
            active:false
          },
          {
            name:'教程',
            url:'',
            active:false
          }
        ],
        tab_list2:[
          {
            name:'精选',
            url:'',
            active:true
          },
          {
            name:'心灵鸡汤',
            url:'',
            active:false
          },
          {
            name:'店主招募',
            url:'',
            active:false
          },
          {
            name:'新手必发',
            url:'',
            active:false
          }
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
