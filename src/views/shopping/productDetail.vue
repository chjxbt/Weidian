<template>
  <div>
    <img src="/static/images/icon-more.png" class="back-img" @click="backPage">
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
    <div class="product-evaluation">
      <div class="evaluation-title">商品评价（99+）</div>
      <div class="applause-rate">好评率99.8%</div>
    </div>
    <div class="evaluation-tabs" v-for="item in evaluationTabs">
      <div class="evaluation-tab" @click="getEvaluation">{{item}}</div>
    </div>
    <div class="one-evaluation">
      <div class="evaluator">
        <img src="http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg" class="evaluator-img">
        <div class="evaluator-name">欣**3</div>
      </div>
      <div class="evaluation-text">一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺</div>
      <span class="evaluation-pictures" v-for="item in evaluationPictures">
        <img :src="item" class="evaluation-picture">
      </span>
      <div class="more-evaluation" @click="moreEvaluation">查看更多>></div>
    </div>
    <div class="recommended">
      <div class="recommended-title">—— 配套推荐 ——</div>
      <div class="recommended-imgs">
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name">太阳帽女防晒防太阳帽女防晒防</p>
          <p class="recommended-price">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name">太阳帽女防晒防</p>
          <p class="recommended-price">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name">太阳帽女防晒防</p>
          <p class="recommended-price">￥160</p>
        </div>
        <div class="recommended-box">
          <img src="http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg" class="recommended-img">
          <p class="recommended-name">太阳帽女防晒防</p>
          <p class="recommended-price">￥160</p>
        </div>
      </div>
    </div>
    <div class="product-detail-text">—— 详情 ——</div>
    <ul>
      <li v-for="brand in brandList">
        <img v-lazy="brand.img" class="detail-img">
      </li>
    </ul>
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
        commitmentList: ["正品保障", "发货&售后", "七天退货", "先行赔付"],
        evaluationTabs: ["衣服不错(50)", "面料好(30)", "穿着舒服(30)"],
        evaluationPictures: ["http://image2.suning.cn/content/catentries/00000000010295/000000000102956200/fullimage/000000000102956200_8f.jpg", "http://image4.suning.cn/content/catentries/00000000010292/000000000102925077/fullimage/000000000102925077_6f.jpg",
                             "http://img0.imgtn.bdimg.com/it/u=12035839,3404122673&fm=26&gp=0.jpg", "http://image3.suning.cn/content/catentries/00000000010295/000000000102955143/fullimage/000000000102955143_2f.jpg"],
        brandList: [{img: "http://pic1.win4000.com/wallpaper/8/599d1d60036a2.jpg"}, {img: "http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201804/25/145712qjc3gwcbtvgoct9w.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/57eb314a3c143.jpg"}, {img: "http://pic1.win4000.com/wallpaper/8/57eb322625b50.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc06f60ecf.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc080092c6.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc07478a17.jpg"}, {img: "http://pic1.win4000.com/wallpaper/6/59bcc08474821.jpg"}]
      }
    },
    components: { productParams },
    methods: {
      // 返回上一页
      backPage() {
        this.$router.push('/shopping/index');
      },
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

      },
      // 获取单个评论
      getEvaluation() {

      },
      // 查看更多评论
      moreEvaluation() {

      }
    },
    created() {
      let product = this.$route.query.product;
      // console.log(product);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/discover";
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
    margin: 20px -2% 10px 5%;
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
  .product-evaluation {
    display: flex;
    .evaluation-title {
      color: @greyColor;
      font-size: 26px;
      font-weight: bold;
      margin: 19px 24px;
    }
    .applause-rate {
      flex: 1;
      color: @grey;
      font-size: 26px;
      font-weight: bold;
      margin: 19px 26px;
      text-align: right;
    }
  }
  .evaluation-tabs {
    width: 100%;
    .evaluation-tab {
      float: left;
      color: #f1f1f1;
      margin: 10px 3%;
      font-size: 18px;
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
        color: @grey;
        font-size: 20px;
        margin-top: 30px;
      }
    }
    .evaluation-text {
      font-size: 20px;
      color: @greyColor;
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
      font-size: 20px;
      color: @greyColor;
      background-color: #f2f5f7;
    }
  }
  .recommended {
    .recommended-title {
      width: 750px;
      margin: 7px 0 53px 0;
      font-size: 22px;
      color: @greyColor;
      text-align: center;
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
          font-size: 20px;
          margin: 10px 0 10px 30px;
          color: @greyColor;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .recommended-price {
          font-size: 22px;
          color: @mainColor;
          margin-bottom: 43px;
        }
      }
    }
  }
  .product-detail-text {
    font-size: 22px;
    color: @greyColor;
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
    background: url("/static/images/commitment.png") no-repeat fixed center;
  }
</style>
