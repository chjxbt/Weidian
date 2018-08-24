<template>
  <div>
    <img src="/static/images/icon-more.png" class="back-img">
    <img src="http://s9.rr.itc.cn/r/wapChange/20167_8_22/a87n9v8965341955628.jpg" class="product-img">
    <div class="product-activity">
      <span class="activity-text-one">限时特卖</span>
      <span class="activity-text-two">距离结束仅剩</span>
      <span class="activity-text-three">2天07时11分28秒</span>
    </div>
    <div class="product-prices">
      <span class="new-price">￥160</span>
      <span class="old-price">￥299</span>
      <span class="make-money">赚12.5</span>
      <img v-if="collectionVisible" src="/static/images/icon-unlike.png" class="collection-share-img" @click="collection">
      <img v-if="!collectionVisible" src="/static/images/icon-like.png" class="collection-share-img" @click="collection">
      <img src="/static/images/icon-share.png" class="collection-share-img" @click="shareProduct">
    </div>
    <div class="product-name">【眼唇速效 卸妆神器】 Bifesta斌若诗 眼唇卸妆液  145ml 曼巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴</div>
    <div class="product-buyer-quantity">20.5万人购买</div>
    <div v-if="ownerVisible" class="owner-price">
      <img src="/static/images/icon-radio.png" class="owner-price-img">
      <span class="owner-price-one">店主价￥55.00</span>
      <span class="owner-price-two">成为店主 ></span>
    </div>
    <div class="product-commitment" v-for="item in commitmentList">
      <img src="/static/images/commitment.png" class="commitment-img">
      <div class="commitment-text">{{item}}</div>
    </div>
    <!--<div class="product-activity-title">
      <div class="product-activity-name">活动1</div>
      <div class="product-activity-content">满89减5;满139减10</div>
      <img src="/static/images/icon-list-right.png" class="to-activity">
    </div>-->
    <product-params :choose="false"></product-params>
    <div class="rectangular"></div>
    <div class="product"></div>
  </div>
</template>

<script>
  import productParams from "../../components/common/productParams";
  export default {
    data() {
      return {
        name: "productDetail",
        collectionVisible: false,
        ownerVisible: true,
        commitmentList: ["正品保障", "发货&售后", "七天退货", "先行赔付"]
      }
    },
    components: { productParams },
    methods: {
      // 收藏
      collection() {
        if(this.collectionVisible) {
          this.collectionVisible = false;
        }else if(!this.collectionVisible) {
          this.collectionVisible = true;
        }
      },
      // 分享商品
      shareProduct() {

      }
    },
    created() {
      let product = this.$route.query.product;
      // console.log(product);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
  .back-img {
    float: left;
    width: 18px;
    height: 37px;
    margin: 30px;
    transform: rotate(180deg);
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
    font-size: 26px;
    line-height: 59px;
    color: @bgMainColor;
    background-image: linear-gradient(to right, #db2295, #c457ac);
    .activity-text-one {
      margin-left: 42px;
    }
    .activity-text-two {
      flex: 1;
      text-align: right;
      margin-right: 20px;
    }
    .activity-text-three {
      margin-right: 31px;
    }
  }
  .product-prices {
    display: flex;
    .new-price {
      color: #333333;
      font-size: 38px;
      font-weight: bold;
      margin: 20px 20px;
    }
    .old-price {
      color: @grey;
      font-size: 28px;
      margin: 30px 0;
      text-decoration:line-through
    }
    .make-money {
      flex: 1;
      font-size: 38px;
      font-weight: bold;
      margin: 20px 20px;
      color: @mainColor;
      text-align: left;
    }
    .collection-share-img {
      width: 34px;
      height: 30px;
      margin: 30px 30px 0 0;
    }
  }
  .product-name {
    width: 561px;
    font-size: 32px;
    text-align: left;
    margin-left: 25px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
  }
  .product-buyer-quantity {
    color: @grey;
    font-size: 28px;
    text-align: left;
    margin: 29px 0 23px 22px;
  }
  .owner-price {
    height: 54px;
    display: flex;
    font-size: 26px;
    line-height: 54px;
    color: @bgMainColor;
    background-color: #b5c0dc;
    .owner-price-img {
      width: 28px;
      height: 28px;
      margin: 13px 8px 13px 45px;
    }
    .owner-price-one {
      flex: 1;
      text-align: left;
    }
    .owner-price-two {
      text-align: right;
      margin-right: 58px;
    }
  }
  .product-commitment {
    width: 21%;
    float: left;
    margin: 10px -2% 10px 5%;
    .commitment-img {
      width: 20px;
      height: 20px;
      float: left;
      margin: 5px 0;
    }
    .commitment-text {
      width: 130px;
    }
  }
  .product-activity-title {
    width: 100%;
    display: flex;
    .product-activity-name {
      color: @grey;
      font-size: 26px;
      margin: 25px 25px 10px 25px;
    }
    .product-activity-content {
      flex: 1;
      text-align: left;
      margin: 25px 0 10px 0;
      font-size: 28px;
      font-weight: bold;
      color: @greyColor;
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
</style>
