<template>
    <div style="margin-bottom: 115px;">
      <div class="m-swipe-box">
        <mt-swipe :auto="2000">
          <mt-swipe-item v-for="item in items" :key="item.id">
            <a :href="item.href" rel="external nofollow">
              <img :src="item.url" class="img"/>
              <span class="desc"></span>
            </a>
          </mt-swipe-item>
        </mt-swipe>
      </div>
      <div class="m-store-order" v-for="item in orderList" :key="item.id">
        <div class="m-store-name">
          <img src="/static/images/store-img.png" class="store-img">
          <div class="store-name m-ft-28 tl">{{item.storeName}}</div>
          <div class="product-send m-ft-28">{{item.productSend}}</div>
        </div>
        <div class="m-order-discounts m-ft-20">
          <div class="reduce-title m-bg-main-color">{{item.reduceTitle}}</div>
          <div class="reduce-number m-grey tl">{{item.reduceNumber}}</div>
          <div class="to-reduce m-red">{{item.toReduce}}</div>
        </div>
        <div class="m-order-product">
          <div class="one-product" v-for="product in item.productList" :key="product.id">
            <img v-if="product.choose" src="/static/images/check_box_on.png" class="check-box-img" @click="chooseProduct(product)">
            <img v-if="!product.choose" src="/static/images/check_box_un.png" class="check-box-img" @click="chooseProduct(product)">
            <img :src="product.productImg" class="product-img" @click="toDetail(product)">
            <div class="one-product-three">
              <div class="product-name m-ft-24 tl m-ft-b" @click="toDetail(product)">{{product.productName}}</div>
              <product-params :choose="true" :size="product.size" :color="product.color" :quantity="product.quantity"></product-params>
              <product-quantity :quantity="product.quantity"></product-quantity>
            </div>
            <div class="one-product-four">
              <p class="one-product-price m-red m-ft-20 m-ft-b">￥<span class="product-price-number">{{product.productPrice}}</span></p>
              <div class="product-failure m-ft-24 m-grey"></div>
              <img src="/static/images/delete.png" class="delete-product-img" @click="deleteProduct(product)">
            </div>
          </div>
        </div>
        <div class="failure-product">
          <div class="one-product" v-for="failure in item.failureList" :key="failure.id">
            <img src="/static/images/check_box_disabled.png" class="check-box-img">
            <img :src="failure.productImg" class="product-img">
            <div class="one-product-three">
              <div class="product-name m-ft-24 tl m-ft-b">{{failure.productName}}</div>
              <div class="tl">尺寸：{{failure.size}} 颜色：{{failure.color}}</div>
              <!--<product-params :size="failure.size" :color="failure.color"></product-params>-->
              <!--<product-quantity :quantity="failure.quantity"></product-quantity>-->
            </div>
            <div class="one-product-four">
              <p class="one-product-price m-red m-ft-20 m-ft-b">￥<span class="product-price-number">{{failure.productPrice}}</span></p>
              <div class="product-failure m-ft-24 m-grey">失效</div>
              <img src="/static/images/delete.png" class="delete-product-img">
            </div>
          </div>
        </div>
      </div>
      <div class="guess-product">
        <div class="guess-product-border">
          <div class="guess-product-title">
            <img src="/static/images/guess_product_left.png" class="guess-product-left">
            <img src="/static/images/guess_product_center.png" class="guess-product-center">
            <div class="guess-product-title-text m-ft-30 m-red">你可能还喜欢</div>
            <img src="/static/images/guess_product_right.png" class="guess-product-left">
          </div>
          <div class="guess-product-detail" v-for="item in guessProductList" :key="item.id">
            <img :src="item.productImg" class="guess-product-img">
            <div class="guess-product-name m-ft-24 tl m-ft-b">{{item.productName}}</div>
            <p class="guess-product-price m-ft-20 m-red m-ft-b">￥<span class="m-ft-34">{{item.productPrice}}</span></p>
            <div class="guess-product-buy m-ft-24 m-red">购买</div>
          </div>
        </div>
      </div>
      <div class="pay-price">
        <img v-if="ifChooseAll" src="/static/images/check_box_on.png" class="choose-all-img" @click="chooseAll()">
        <img v-if="!ifChooseAll" src="/static/images/check_box_un.png" class="choose-all-img" @click="chooseAll()">
        <div class="choose-all-text m-ft-30" @click="chooseAll()">全 选</div>
        <div class="pay-price-detail tr">
          <p class="pay-price-text m-ft-30">总 价：
            <span class="m-ft-20 m-red m-ft-b">￥</span>
            <span class="m-ft-34 m-red">{{totalPrice}}</span>
          </p>
          <div class="pay-price-reduce m-grey m-ft-20">已减 30 元</div>
        </div>
        <div class="to-pay m-ft-34 m-bg-main-color" @click="toOrder">去结算</div>
      </div>
    </div>
</template>

<script type="text/ecmascript-6">
  import productParams from "../../components/common/productParams";
  import productQuantity from "../../components/common/productQuantity";
  import { MessageBox } from 'mint-ui';

  export default {
    data() {
      return {
        name: '',
        items: [{ title: '你的名字', href: 'http://baidu.com',   url: 'http://d6.yihaodianimg.com/N03/M02/1E/8B/CgQCs1Kyi3yABkF6AAEMkxApUWk35400.jpg' },
                { title: '你的名字', href: 'http://baidu.com',   url: 'http://img006.hc360.cn/m1/M03/91/1F/wKhQb1RRIZuEaFdwAAAAAKhAlYA086.jpg' }],
        orderList: [
          { storeName: "衣衣旗舰店", productSend: "已免运费", reduceTitle: "满 300 减 30", reduceNumber: "还差 30 元", toReduce: "去凑单 >",
            productList: [
              { choose: false, productImg: "/static/images/product1.png", productName: "18年版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版", size: "XL", color: "黄色", quantity: 2, productPrice: "106" },
              { choose: false, productImg: "/static/images/product1.png", productName: "18年版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版",  size: "2XL", color: "蓝色", quantity: 1,productPrice: "99" }
            ],
            failureList: [
              { productImg: "/static/images/product1.png", productName: "18年版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版安耐晒金瓶防晒霜60ml同款温和清洁澳洲版", size: "M", color: "红色", quantity: 3, productPrice: "106" }
            ]
          }
        ],
        guessProductList: [
          {productImg: "/static/images/product1.png", productName: "商品名称商品名称商品名称商品名称商品名称", productPrice: "199"},
          {productImg: "/static/images/product1.png", productName: "商品名称商品名称商品名称商品名称商品名称", productPrice: "199"}
        ],
        ifChooseAll: false,
        totalPrice: 0,
        order: []
      }
    },
    components: { productParams, productQuantity },
    methods: {
      // 单独勾选产品
      chooseProduct(product) {
        if(product.choose) {
          product.choose = false;
          this.totalPrice = 0;
          this.order = [];
        }else if(!product.choose) {
          product.choose = true;
          // 勾选后把该商品加入到可以结算的 list 中
          for(let i = 0; i < this.orderList.length; i++) {
            for(let j = 0; j < this.orderList[i].productList.length; j++) {
              if(this.orderList[i].productList[j].choose) {
                this.order.push(this.orderList[i].productList[j]);
                // 计算单价商品的总价
                this.totalPrice = this.orderList[i].productList[j].productPrice * this.orderList[i].productList[j].quantity;
              }
            }
          }
        }
      },
      // 结算时的全选
      chooseAll() {
        let price;
        let quantity;
        if(this.ifChooseAll) {
          this.ifChooseAll = false;
          this.totalPrice = 0;
          for(let i = 0; i < this.orderList.length; i++) {
            for(let j = 0; j < this.orderList[i].productList.length; j++) {
              this.orderList[i].productList[j].choose = false;
              this.order = [];
            }
          }
        }else if(!this.ifChooseAll) {
          this.ifChooseAll = true;
          for(let i = 0; i < this.orderList.length; i++) {
            for(let j = 0; j < this.orderList[i].productList.length; j++) {
              this.orderList[i].productList[j].choose = true;
              // console.log(this.orderList[i].productList[j]);
              // 单价、数量
              price = parseFloat(this.orderList[i].productList[j].productPrice);
              quantity = parseInt(this.orderList[i].productList[j].quantity);
              // 计算总价
              this.totalPrice = this.totalPrice + price * quantity;
              // 勾选后把该商品加入到可以结算的 list 中
              this.order.push(this.orderList[i].productList[j]);
            }
          }
        }
      },
      // 删除商品
      deleteProduct(product) {
        MessageBox({
          title: '提示',
          message: '确定删除该商品？',
          showCancelButton: true
        }).then(action => {
          if(action == "confirm") {
            console.log("deleteProduct", product);
          }
        });
      },
      // 跳转商品详情页
      toDetail(product) {
        // console.log(product)
        this.$router.push({path: "/productDetail", query: { product }});
      },
      // 去结算
      toOrder() {
        let order = this.order;
        this.$router.push({path: "/submitOrder", query: { order }});
      }
    },
    created() {}
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  .m-swipe-box {
    .mint-swipe{
      width: 750px;
      height: 120px;
    }
    .mint-swipe .img {
      height: 120px;
    }
  }
  .m-store-order {
    .m-store-name {
      display: flex;
      width: 100%;
      height: 100px;
      border-bottom: 2px solid #EDEDED;
      border-top: 4px solid #EDEDED;
      .store-img {
        width: 40px;
        height: 41px;
        margin: 31px 7px 0 21px;
      }
      .store-name {
        flex: 1;
        margin: 33px 0;
        padding: 0 10px;
      }
      .product-send {
        margin: 33px 30px;
      }
    }
    .m-order-discounts {
      height: 80px;
      display: flex;
      width: 100%;
      .reduce-title {
        height: 30px;
        margin: 25px;
        padding: 0 20px;
        border-radius: 4px;
        background-color: @mainColor;
      }
      .reduce-number {
        flex: 1;
        margin: 25px 0;
      }
      .to-reduce {
        margin: 25px 30px;
      }
    }
    .m-order-product {
      width: 720px;
      margin: 15px;
      border-radius: 10px;
      box-shadow: 0 0 10px 0 rgba(66, 66, 66, 0.3);
    }
    .failure-product {
      opacity: 0.6;
      padding: 0 15px;
    }
    .one-product {
      display: flex;
      width: 100%;
      .check-box-img {
        width: 45px;
        height: 45px;
        padding: 92px 10px;
      }
      .product-img {
        width: 150px;
        height: 150px;
        padding: 40px 12px;
      }
      .one-product-three {
        width: 321px;
        padding: 40px 22px;
        .product-name {
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 2;
          overflow: hidden;
        }
      }
      .one-product-four {
        display: flex;
        flex-flow: column;
        padding: 40px 15px;
        .one-product-price {
          margin: 0;
          .product-price-number {
            font-size: 34px;
          }
        }
        .product-failure {
          flex: 1;
          line-height: 90px;
        }
        .delete-product-img {
          width: 21px;
          height: 21px;
          padding-left: 30px;
        }
      }
    }
  }
  .guess-product {
    padding: 25px;
    background-color: #f2f5f7;
    .guess-product-border {
      width: 700px;
      height: 540px;
      border-radius: 10px;
      background-color: @bgMainColor;
      .guess-product-title {
        display: flex;
        padding: 40px 0;
        margin-left: 120px;
        .guess-product-left {
          width: 60px;
          height: 10px;
          padding: 15px;
        }
        .guess-product-center {
          width: 40px;
          height: 40px;
          padding: 0 5px;
        }
        .guess-product-title-text {
          padding: 0 10px;
          letter-spacing: 5px;
        }
      }
      .guess-product-detail {
        padding: 0 25px;
        width: 300px;
        float: left;
        .guess-product-img {
          width: 300px;
          height: 300px;
        }
        .guess-product-name {
          padding: 5px 0;
          display: -webkit-box;
          -webkit-box-orient: vertical;
          -webkit-line-clamp: 1;
          overflow: hidden;
        }
        .guess-product-price {
          margin: 0;
          float: left;
          padding: 15px 0;
        }
        .guess-product-buy {
          float: right;
          margin-top: 5px;
          padding: 10px 30px;
          letter-spacing: 5px;
          border: 2px solid @mainColor;
          border-radius: 30px;
        }
      }
    }
  }
  .pay-price {
    display: flex;
    position: fixed;
    bottom: 100px;
    background-color: @bgMainColor;
    .choose-all-img {
      width: 50px;
      height: 49px;
      padding: 30px 15px;
    }
    .choose-all-text {
      padding: 32px 0;
    }
    .pay-price-detail {
      width: 365px;
      .pay-price-text {
        margin: 0;
        padding: 10px 20px;
      }
      .pay-price-reduce {
        padding: 0 20px;
      }
    }
    .to-pay {
      height: 48px;
      white-space: nowrap;
      overflow: hidden;
      padding: 30px 60px;
      letter-spacing: 5px;
      background-color: @mainColor;
    }
  }
</style>
