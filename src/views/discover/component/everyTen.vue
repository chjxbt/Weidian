<template>
  <div class="m-discover-every">
    <div class="m-swipe-box">
      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in items" :key="item.id">
          <a :href="item.href" rel="external nofollow" >
            <img :src="item.url" class="img"/>
            <span class="desc"></span>
          </a>
        </mt-swipe-item>
      </mt-swipe>
      <div class="m-scroll">
        <ul class="m-img-list">
          <li>
            <img src="http://images.51bi.com/opt/siteimg/pb/20140307/c29ad52051879f0d13f1da57472abe88.jpeg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥169</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img.eelly.com/G01/M00/00/89/small_oYYBAFWOxpSIBiLzAAMKSN5SRlQAAA1rgDeJeEAAwpg61.jpeg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img.eelly.com/G02/M00/00/7F/small_pIYBAFVfLxCIItqyAATKYNG5CMEAAAxsQHbafcABMp4028.jpg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img5.imgtn.bdimg.com/it/u=2506569644,813669471&fm=26&gp=0.jpg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
        </ul>
      </div>

      <div class="m-title">
        <div>
          <img src="" class="m-item-title-img" alt="">
          <span>拉夏贝尔La Chapelle</span>
        </div>
        <div class="m-lookinfo-box">
          <span class="m-look-icon"></span>
          <span>1231</span>
          <span class="m-smile-icon"></span>
          <span>21231</span>
        </div>
      </div>
    </div>
    <div class="m-swipe-box">
      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in items" :key="item.id">
          <a :href="item.href" rel="external nofollow" >
            <img :src="item.url" class="img"/>
            <span class="desc"></span>
          </a>
        </mt-swipe-item>
      </mt-swipe>
      <div class="m-scroll">
        <ul class="m-img-list">
          <li>
            <img src="http://images.51bi.com/opt/siteimg/pb/20140307/c29ad52051879f0d13f1da57472abe88.jpeg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥169</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img.eelly.com/G01/M00/00/89/small_oYYBAFWOxpSIBiLzAAMKSN5SRlQAAA1rgDeJeEAAwpg61.jpeg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img.eelly.com/G02/M00/00/7F/small_pIYBAFVfLxCIItqyAATKYNG5CMEAAAxsQHbafcABMp4028.jpg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
          <li>
            <img src="http://img5.imgtn.bdimg.com/it/u=2506569644,813669471&fm=26&gp=0.jpg" class="m-img-list-img" alt="">
            <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
          </li>
        </ul>
      </div>

      <div class="m-title">
        <div>
          <img src="" class="m-item-title-img" alt="">
          <span>拉夏贝尔La Chapelle</span>
        </div>
        <div class="m-lookinfo-box">
          <span class="m-look-icon"></span>
          <span>1231</span>
          <span class="m-smile-icon"></span>
          <span>21231</span>
        </div>
      </div>
    </div>
    <!--<div class="m-item-one">
      <ul class="m-item-img-list">
        <li>
          <img src="" class="m-item-img m-item-img-l" alt="">
        </li>
        <li>
          <img src="" class="m-item-img" alt="">
        </li>
        <li>
          <img src="" class="m-item-img" alt="">
        </li>
        <li>
          <img src="" class="m-item-img" alt="">
        </li>
      </ul>
      <div class="m-title">
        <div>
          <img src="" class="m-item-title-img" alt="">
          <span>拉夏贝尔La Chapelle</span>
        </div>
        <div class="m-lookinfo-box">
          <span class="m-look-icon"></span>
          <span>1231</span>
          <span class="m-smile-icon"></span>
          <span>21231</span>
        </div>
      </div>
    </div>-->
  </div>

</template>

<script type="text/ecmascript-6">
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
    export default {
      data() {
        return {
          items: [{
            title: '你的名字',
            href: 'http://google.com', url: 'http://img.zcool.cn/community/013a6159532b74a8012193a314e51c.png'
          }, {
            title: '我的名字',
            href: 'http://baidu.com', url: 'http://img.zcool.cn/community/015b8556fca6f16ac7257948ffdc3d.jpg'
          }]
        }
      },
      components: {},
      methods: {
        // 获取每日推荐内容
        getData(){
          let token = localStorage.getItem('token');
          axios.get(api.get_info_recommend + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              console.log(res.data.data[0]);
            }else{
              Toast(res.data.message);
            }
          },error => {
            Toast(error.data.message);
          })
        },
        // 获取banner
        getBanner() {
          let token = localStorage.getItem('token');
          axios.get(api.get_all_recommendbanner + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              console.log(res.data.data[0]);
              Toast(res.data.message);
            }else{
              Toast(res.data.message);
            }
          },error => {
            Toast(error.data.message);
          })
        }
      },
      created() {
        this.getData();
        this.getBanner();
      }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/discover";
  .img {

    border-radius: 20px;
  }
</style>
