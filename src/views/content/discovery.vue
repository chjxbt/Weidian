<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">

      <p class="m-form-label" style="margin-bottom: 0.2rem">轮播图管理</p>
      <div class="content-table">
        <el-table :data="bannerList" border style="width: 100%">
          <el-table-column prop="batext" label="专题名称" width="200"></el-table-column>
          <el-table-column prop="baimage" label="内容">
            <template slot-scope="scope">
              <div>
                <el-upload class="avatar-uploader" action="https://weidian.daaiti.cn/task/upload_task_img" :show-file-list="false"
                           :on-success="uploadPicture" :before-upload="beforeAvatarUploads">
                  <img v-if="scope.row.baimage" :src="scope.row.baimage" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="title" label="时间">
            <template slot-scope="scope">
              <div>
                {{scope.row.bastarttime}} 至 {{scope.row.baendtime}}
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="product" label="展示">
            <template slot-scope="scope">
              <el-switch v-model="scope.row.baisdisplay" active-text="展示" inactive-text="关闭">
              </el-switch>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="180">
            <template slot-scope="scope">
              <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <div style="display: flex; margin-top: 0.1rem">
          <div class="add-box" style="flex: 1;">
            <span class="m-item-add" style="left: 3.5rem">+</span>
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
          { value: '2', label: '专题' },
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
        activityTime: [],
        hotmessages: [
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
          { num: "18/09/13 18:30 ", content: "推文内容" },
        ],
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


      // 获取banner滚动图
      getBanner() {
        /*axios.get(api.get_home_banner + '?lasting=true&token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200) {
            this.bannerList = res.data.data;
            // console.log(res.data.data);
          }else{
            this.$message.error(res.data.message);
          }
        })*/
      },
      // 上传标题图片
      uploadPicture(res, file) {
        console.log(res, file)
        let form = new FormData();
        form.append("file", file.raw);
        form.append("FileType", 'NewsPic');
        form.append("index", 1);
        axios.post(api.upload_task_img + '?token=' + localStorage.getItem('token'), form).then(res => {
          if(res.data.status == 200){
            // this.$message({ type: 'success', message: res.data.message });
          }else{
            this.$message({ type: 'error', message: res.data.message });
          }
          // console.log(res.data);
          this.imageUrl = res.data.data;
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
          this.$message.error('上传图片大小不能超过 2MB!');
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
