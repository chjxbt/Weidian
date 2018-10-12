<template>
  <div v-if="product_info != null">
    <!--/static/images/icon-more.png-->
    <!--<span class="back-img" @click="backPage"></span>-->
    <!--<img src="http://s9.rr.itc.cn/r/wapChange/20167_8_22/a87n9v8965341955628.jpg" class="product-img">-->
    <img :src="product_info.prmainpic"  class="product-img">
    <div class="product-activity m-ft-26 m-bg-main-color">
      <span class="activity-text-one">限时特卖</span>
      <span class="activity-text-two tr">距离结束仅剩</span>
      <span class="activity-text-three">2天07时11分28秒</span>
    </div>
    <div class="product-prices">
      <span class="new-price m-ft-38 m-black m-ft-b">￥{{product_info.prprice}}</span>
      <span class="old-price m-grey m-ft-28">￥{{product_info.proldprice}}</span>
      <span class="make-money m-ft-38 m-red m-ft-b tl" v-if="is_vip">赚{{product_info.prsavemonty}}</span>
      <span class="make-money m-ft-38 m-red m-ft-b tl" v-else></span>
      <img v-if="collectionVisible" src="/static/images/icon-unlike.png" class="collection-share-img" @click="collection">
      <img v-if="!collectionVisible" src="/static/images/icon-like.png" class="collection-share-img" @click="collection">
      <img src="/static/images/icon-share.png" class="collection-share-img" @click="shareProduct">
    </div>
    <div class="product-name m-ft-32 tl">{{product_info.prtitle}}</div>
    <div class="product-buyer-quantity m-ft-28 m-grey tl">{{product_info.prsoldnum}}人购买</div>
    <div v-if="!is_vip" class="owner-price m-ft-26 m-bg-main-color">
      <img src="/static/images/icon-radio.png" class="owner-price-img">
      <span class="owner-price-one tl">店主价￥{{product_info.prkeeperprice}}</span>
      <span class="owner-price-two tr">成为店主 ></span>
    </div>
    <div class="product-commitment" v-for="item in commitmentList">
      <img src="/static/images/commitment.png" class="commitment-img">
      <div class="commitment-text">{{item}}</div>
    </div>
    <!--<div class="m-commitment">-->
      <!--<img src="" class="m-commitment-img" alt="">-->
    <!--</div>-->
    <!--<div class="product-activity-title">
      <div class="product-activity-name m-ft-26 m-grey">活动1</div>
      <div class="product-activity-content m-ft-28 m-grey-color m-ft-b tl">满89减5;满139减10</div>
      <img src="/static/images/icon-list-right.png" class="to-activity">
    </div>-->
    <product-params :choose="is_choose" :quantity="quantity" :options="params_options" :price="product_info.prprice" :sku="sku" @carChoose="carChoose"  @closeModal="closeModal"></product-params>
    <div class="rectangular"></div>
    <div class="product-evaluation">
      <div class="evaluation-title m-ft-26 m-grey-color b">商品评价（99+）</div>
      <div class="applause-rate m-ft-26 m-grey m-ft-b tr">好评率99.8%</div>
    </div>
    <div class="evaluation-tabs" v-for="item in evaluationTabs">
      <div class="evaluation-tab m-ft-20" @click="getEvaluation">{{item}}</div>
    </div>
    <div class="one-evaluation">
      <div class="evaluator">
        <img src="http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg" class="evaluator-img">
        <div class="evaluator-name m-grey m-ft-20">欣**3</div>
      </div>
      <div class="evaluation-text m-ft-20 m-grey-color">一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺</div>
      <span class="evaluation-pictures" v-for="item in evaluationPictures">
        <img :src="item" class="evaluation-picture">
      </span>
      <div class="more-evaluation m-ft-20 m-grey-color" @click="moreEvaluation">查看更多>></div>
    </div>
    <div class="recommended">
      <div class="recommended-title m-ft-22 m-grey-color">—— 配套推荐 ——</div>
      <div class="recommended-imgs">
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name m-ft-20 m-grey-color">太阳帽女防晒防</p>
          <p class="recommended-price m-ft-22 m-red">￥160</p>
        </div>
      </div>
    </div>
    <div class="product-detail-text m-ft-22 m-grey-color">—— 详情 ——</div>
    <ul style="margin-bottom: 15%">
      <li v-for="brand in product_info.images">
        <img v-lazy="brand.piurl"  class="detail-img">
      </li>
    </ul>
    <div class="to-buy">
      <span class="service-add" @click="toService">
        <img src="/static/images/product_detail_service.png" class="to-buy-icon m-ft-20">
        <p class="to-buy-text m-ft-20">客服</p>
      </span>
      <span class="service-add" @click="toCart">
        <img src="/static/images/produc_detail_shopping_cart.png" class="to-buy-icon m-ft-20">
        <p class="to-buy-text m-ft-20">购物车</p>
      </span>
      <div class="m-vip-btn m-normal m-ft-36 "  v-if="!is_vip" @click="addCart">
        <p>加入购物车</p>
      </div>
      <div class="m-vip-btn m-normal m-ft-36 active" v-if="!is_vip" @click="buyNow">
        <p>立即购买</p>
    </div>
      <div class="m-vip-btn m-ft-36 "  v-if="is_vip" @click="addCart">
        <p>买</p>
        <p class="m-ft-24">省￥6.5</p>
      </div>
      <div class="m-vip-btn m-ft-36 active" v-if="is_vip" @click="buyNow">
        <p>卖</p>
        <p class="m-ft-24">赚￥6.5</p></div>
      </div>
  </div>
</template>

<script>
  import productParams from "../shopping/components/productParams";
  import api from '../../api/api';
  import axios from 'axios';
  import {Toast} from 'mint-ui';
  import common from '../../common/js/common'
  export default {
    data() {
      return {
        name: "productDetail",
        collectionVisible: false,
        ownerVisible: true,
        commitmentList: ["正品保障", "发货&售后", "七天退货", "先行赔付"],
        evaluationTabs: ["衣服不错(50)", "面料好(30)", "穿着舒服(30)"],
        evaluationPictures: ["http://image2.suning.cn/content/catentries/00000000010295/000000000102956200/fullimage/000000000102956200_8f.jpg", "http://image4.suning.cn/content/catentries/00000000010292/000000000102925077/fullimage/000000000102925077_6f.jpg",
                             "http://img0.imgtn.bdimg.com/it/u=12035839,3404122673&fm=26&gp=0.jpg", "http://image3.suning.cn/content/catentries/00000000010295/000000000102955143/fullimage/000000000102955143_2f.jpg"],
        brandList: [],
        product_info:null,
        // brandList: [{img: "http://pic1.win4000.com/wallpaper/8/599d1d60036a2.jpg"}, {img: "http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201804/25/145712qjc3gwcbtvgoct9w.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/57eb314a3c143.jpg"}, {img: "http://pic1.win4000.com/wallpaper/8/57eb322625b50.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc06f60ecf.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc080092c6.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc07478a17.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc08474821.jpg"}]
        params_options:null,
        sku:[],
        is_vip:false,
        choose:null,
        is_choose:false,
        quantity:1,
        click_add:false
      }
    },
    components: { productParams },
    methods: {
      getInfo(){
        axios.get(api.get_one_product,{
          params:{
            prid:this.$route.query.prid,
            token:localStorage.getItem('token')
          }
        }).then(res => {
          if(res.data.status == 200){
            this.product_info =  res.data.data;
            console.log(this.product_info)
            this.params_options = res.data.data.sku_value.psvpropervalue;
            this.sku = res.data.data.sku;
          }
        })
      },
      postCar(){
        axios.post(api.update_shoppingcart + '?token=' + localStorage.getItem('token'),{
          pskid:this.choose[0].pskid,
          changenum:this.quantity
        }).then(res => {
           if(res.data.status == 200){
             this.click_add = false;
             Toast({ message: '已添加到购物车', className: 'm-toast-success' });
           }
        });
      },
      // 返回上一页
      backPage() {
        // if(this.$route.query.last == 'activity' && this.$route.query.baid){
        //   this.$router.push({path:'/activityContent',query:{baid:this.$route.query.baid}});
        // }else{
        //   this.$router.push('/shopping/index');
        // }

      },
      // 收藏
      collection() {
        if(this.collectionVisible) {
          this.collectionVisible = false;
        }else if(!this.collectionVisible) {
          this.collectionVisible = true;
        }
      },
      carChoose(v,num){
        this.choose = v;
        this.quantity = num;
        if(this.click_add){
          this.postCar();
        }
      },
      // 分享商品
      shareProduct() {

      },
      // 获取单个评论
      getEvaluation() {

      },
      // 查看更多评论
      moreEvaluation() {

      },
      // 客服聊天
      toService () {

      },

      // 立即购买
      buyNow() {
        let order = "";
        this.$router.push({path: "/submitOrder", query: { order }});
      },
      // 添加购物车
      addCart(){
        if(!this.choose){
          this.is_choose = true;
          this.click_add = true;
        }else{
          this.postCar();
        }
      },
      closeModal(){
        this.is_choose = false;
      },
      // 引入商品详情图片
      imgsDone() {
        let that = this;
        let imgurl = "https://html.weidiango.com/FpwgKaxAfZdnsiIyDV2ZCbWLNmt8";
        this.$http.get(imgurl).then(function(response){
          // console.log('success', response.data);   // response.data中获取ResponseData实体

          that.brandList = response.data.split("data-src=");
          that.brandList.splice(0, 1);
          for(let i = 0; i < that.brandList.length; i ++) {
            that.brandList[i] = that.brandList[i].match(/"(\S*)" data-ext="jpeg"/)[1];
            that.brandList[i] = "https://img.weidiango.com/" + that.brandList[i];
          }
          console.log(that.brandList)
        },function(response){
          console.log('error', response);   // 发生错误
        });
      },
      // changeNum(num){
      //   this.quantity = num;
      // },
      toCart(){
        this.$router.push('/shopping/index');
      }
    },
    mounted() {
      this.imgsDone();
      this.getInfo();
      common.changeTitle('商品详情');
      if(localStorage.getItem('level') == 'partner'){
        this.is_vip = true;
      }else{
        this.is_vip = false;
      }
    },
    created() {
      let prid = this.$route.query.prid;
      // console.log(prid);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/discover";
  @import "../../common/css/index";
  .back-img {
    float: left;
    width: 24px;
    height: 35px;
    margin: 30px;
    /*transform: rotate(180deg);*/
    background: url("/static/images/icon-list-left.png") no-repeat;
    background-size: 100% 100%;
  }
  .product-img {
    width: 640px;
    height: 640px;
    margin: -20px 54px 40px 54px;
  }
  .product-activity {
    width: 750px;
    height: 59px;
    display: flex;
    line-height: 59px;
    background-image: linear-gradient(to right, #db2295, #c457ac);
    .activity-text-one {
      margin-left: 42px;
    }
    .activity-text-two {
      flex: 1;
      margin-right: 20px;
    }
    .activity-text-three {
      margin-right: 31px;
    }
  }
  .product-prices {
    display: flex;
    .new-price {
      margin: 20px 20px;
    }
    .old-price {
      margin: 30px 0;
      text-decoration:line-through
    }
    .make-money {
      flex: 1;
      margin: 20px 20px;
    }
    .collection-share-img {
      width: 34px;
      height: 30px;
      margin: 30px 30px 0 0;
    }
  }
  .product-name {
    width: 561px;
    margin-left: 25px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
  }
  .product-buyer-quantity {
    margin: 29px 0 23px 22px;
  }
  .owner-price {
    height: 54px;
    display: flex;
    line-height: 54px;
    background-color: #b5c0dc;
    .owner-price-img {
      width: 28px;
      height: 28px;
      margin: 13px 8px 13px 45px;
    }
    .owner-price-one {
      flex: 1;
    }
    .owner-price-two {
      margin-right: 58px;
    }
  }
  .product-commitment {
    width: 21%;
    float: left;
    margin: 25px -2% 15px 5%;
    .commitment-img {
      width: 20px;
      height: 20px;
      float: left;
      margin: 5px 0;
    }
    .commitment-text {
      width: 130px;
      white-space: nowrap;
    }
  }
  .m-commitment{
    .m-commitment-img{
      display: block;
      width: 100%;
      height: 68px;
    }
  }
  .product-activity-title {
    width: 100%;
    display: flex;
    .product-activity-name {
      margin: 25px 25px 10px 25px;
    }
    .product-activity-content {
      flex: 1;
      margin: 25px 0 10px 0;
    }
    .to-activity {
      width: 22px;
      height: 22px;
      margin: 35px 25px 10px 0;
    }
  }
  .rectangular {
    width: 750px;
    height: 19px;
    background-color: #f2f5f7;
  }
  .product-evaluation {
    display: flex;
    .evaluation-title {
      margin: 19px 24px;
    }
    .applause-rate {
      flex: 1;
      margin: 19px 26px;
    }
  }
  .evaluation-tabs {
    width: 100%;
    .evaluation-tab {
      float: left;
      color: #f1f1f1;
      margin: 10px 3%;
      padding: 7px 16px;
      border-radius: 16px;
      background-color: #f27f8d;
    }
  }
  .one-evaluation {
    .evaluator {
      width: 100%;
      display: flex;
      .evaluator-img {
        width: 56px;
        height: 56px;
        margin: 21px 24px;
      }
      .evaluator-name {
        margin-top: 30px;
      }
    }
    .evaluation-text {
      line-height: 35px;
      margin: 10px 23px 20px 23px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
    }
    .evaluation-pictures {
      .evaluation-picture {
        width: 140px;
        height: 140px;
        margin: 12px 45px 0 -25px;
      }
    }
    .more-evaluation {
      width: 708px;
      margin: 32px 0;
      padding: 21px;
      background-color: #f2f5f7;
    }
  }
  .recommended {
    .recommended-title {
      width: 750px;
      margin: 7px 0 53px 0;
    }
    .recommended-imgs {
      overflow-x: auto;
      overflow-y: hidden;
      white-space: nowrap;
      display: -moz-box; /*Firefox*/
      display: -webkit-box; /*Safari,Opera,Chrome*/
      display: flex;
      margin-right: 30px;
      .recommended-box {
        .recommended-img {
          width: 210px;
          height: 210px;
          margin-left: 30px;
        }
        .recommended-name {
          width: 210px;
          margin: 10px 0 10px 30px;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .recommended-price {
          margin-bottom: 43px;
        }
      }
    }
  }
  .product-detail-text {
    padding: 34px 0;
    background-color: #f2f5f7;
  }
  .detail-img {
    width: 750px;
    height: auto;
    margin-bottom: -5px;
  }
  img[lazy=loading] {
    width: 750px;
    height: auto;
    margin: auto;
    background: url("/static/images/loading.gif") no-repeat fixed center;
  }
  .to-buy {
    bottom: 0;
    display: flex;
    position: fixed;
    background-color: @bgMainColor;
    height: 96px;
    color: #666666;
    .service-add {
      flex: 1;
      border-top: 2px solid rgb(231,231,231);
      border-right: 2px solid rgb(231,231,231);
      .to-buy-icon {
        width: 52px;
        height: 45px;
        margin: 14px 44px 0 49px;
      }
      .to-buy-text {
        letter-spacing: 2px;
      }
    }
    .to-buy-btn {
      margin-left: -2px;
      padding: 31px 150px;
      white-space: nowrap;
      letter-spacing: 3.6px;
      background-color: @mainColor;
    }
    .m-vip-btn{
      margin-left: -2px;
      width: 230px;
      height: 96px;
      /*padding: 16px 0;*/
      /*height: 110px;*/
      /*line-height: 110px;*/
      white-space: nowrap;
      display: inline-block;
      letter-spacing: 3.6px;
      background-color: #000;
      color: #fff;
      &.m-normal{
        padding: 0;
        line-height: 96px;
        background-color: #393939;
        p{
          &:first-child{
            margin-top: 0;
          }
        }
      }
      p{
        &:first-child{
          margin-top: 10px;
        }
      }
      &.active{
        background-color: @mainColor;
      }
    }
  }
</style>
