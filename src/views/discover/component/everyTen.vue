<template>
  <div class="m-discover-every">
    <div class="m-swipe-box">
      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
            <img :src="item.rbimage" class="img" @click="toProduct(item)">
            <!--<span class="desc"></span>-->
        </mt-swipe-item>
      </mt-swipe>
      <div class="m-scroll">
        <ul class="m-img-list" id="m-img-list">
          <!--<li>
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
          </li>-->
        </ul>
        <!--<ul class="m-img-list" v-for="item in list">
          <li>
            <img :src="item.prmainpic" class="m-img-list-img" alt="">
            <p><span class="m-price">￥{{item.prprice}}</span><span class="m-red">赚{{(item.prprice-item.proldprice).toFixed(2)}}</span></p>
          </li>
        </ul>-->
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
      <div class="line"></div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import api from '../../../api/api';
  import axios from 'axios';
  import { Toast } from 'mint-ui';
    export default {
      data() {
        return {
          bannerList: [],
          recommend: {},
          list: []
        }
      },
      components: {},
      methods: {
        // 获取每日推荐内容
        getData(){
          let token = localStorage.getItem('token');
          axios.get(api.get_info_recommend + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              // console.log(res.data.data);
              this.recommend = res.data.data;
              console.log(this.recommend);
              for(let i=0;i<5;i++) {
                this.list.push(this.recommend[0].products[0]);
              }
              console.log(this.list);

              for(let i=0;i<this.list.length;i++) {
                var elem_li = document.createElement('li'); // 生成一个 li元素
                elem_li.innerHTML = "<img src=\"http://img.eelly.com/G02/M00/00/7F/small_pIYBAFVfLxCIItqyAATKYNG5CMEAAAxsQHbafcABMp4028.jpg\" class=\"m-img-list-img\" alt=\"\"><p><span class=\"m-price\">￥69</span><span class=\"m-red\">赚12</span></p>"; // 设置元素的内容

                document.getElementById('m-img-list').appendChild(elem_li);
              }
              console.log(document.getElementById('m-img-list'));

            }else{
              Toast({ message: '操作失败', className: 'm-toast-fail' });
            }
          },error => {
            Toast({ message: '操作失败', className: 'm-toast-fail' });
          })
        },
        // 获取banner
        getBanner() {
          let token = localStorage.getItem('token');
          axios.get(api.get_all_recommendbanner + '?token=' + token).then(res => {
            if(res.data.status == 200) {
              this.bannerList = res.data.data;
              // console.log(res.data.data);
              // Toast({ message: '操作成功', className: 'm-toast-success' });
            }else{
              Toast({ message: '操作失败', className: 'm-toast-fail' });
            }
          },error => {
            Toast({ message: '操作失败', className: 'm-toast-fail' });
          })
        },
        toProduct(item) {
          console.log(item);
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
  /*滚动条样式*/
  ::-webkit-scrollbar {
    height: 0;
  }
</style>
