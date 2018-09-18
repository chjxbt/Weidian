<template>
  <div>
    <!--<img src="/static/images/order_pay_OK.png" class="m-ok-img">
    <p class="m-ft-40 m-black m-ft-b">订单支付成功</p>
    <p class="price-text m-black m-ft-b">￥<span class="m-ft-34">159.00</span></p>
    <p class="order-text m-ft-30 m-grey">仓库正为您备货中</p>
    <div class="m-btn">
      <div class="m-btn-text m-ft-28 m-grey-color" @click="orderDetail">查看订单</div>
      <div class="m-btn-text m-ft-28 m-grey-color" @click="returnHome">返回首页</div>
    </div>-->



    <div class="m-btn">
      <div class="m-btn-text m-ft-28 m-grey-color"  @click="shareImg()">查看订单</div>
    </div>
    <canvas id="myCanvas" width="1431" height="1209" style="border: 1px #d3d3d3 solid;">
      Your browser does not support the HTML5 canvas tag.
    </canvas>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "orderPayOK",
        order: {}
      }
    },
    // components: {  },
    methods: {
      // 合成图片
      shareImg() {

        let list = ["/static/images/share/product.png", "/static/images/share/product.png", "/static/images/share/product.png", "/static/images/share/product.png"];

        let canvas = document.getElementById("myCanvas");
        let context = canvas.getContext("2d");

        context.font="30px PingFang-SC";
        context.fillText("商品标题商品标题商品标题", 40, 900);
        context.fillText("商品标题商品标题商品...", 40, 940);

        let img1 = new Image();
        img1.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
        img1.src = "/static/images/share/bg_test.png";    //背景图，本地图片或者在线图片

        img1.onload = function(){

          let img2 = new Image();
          img2.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
          img2.src = "/static/images/share/product.jpg";   //本地图片或者在线图片
          img2.onload = function(){
            context.drawImage(img2 , 0 , 0 , 814 , 814);

            let img3 = new Image();
            img3.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
            img3.src = "/static/images/share/product.jpg";   //本地图片或者在线图片
            img3.onload = function(){
              context.drawImage(img3 , 839 , 0 , 592 , 592);

              let img4 = new Image();
              img4.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
              img4.src = "/static/images/share/product.jpg";   //本地图片或者在线图片
              img4.onload = function(){
                context.drawImage(img4 , 839 , 617 , 592 , 592);

                let img5 = new Image();
                img5.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
                img5.src = "/static/images/share/share.jpg";   //本地图片或者在线图片
                img5.onload = function(){
                  context.drawImage(img5 , 560 , 850 , 250 , 250);

                };
              };
            };
          };

          let base64 = canvas.toDataURL("image/png");  //"image/png" 这里注意一下
          let img = document.getElementById('myCanvas');

          img.setAttribute('src', base64);
          // window.location.href = base64;   // 下载-无后缀名
          // console.log(base64);
        }
      },
      // 查看订单
      orderDetail() {
        let order = this.order;
        this.$router.push({path: "/orderStatus", query: { order }});
      },
      // 返回首页
      returnHome() {
        this.$router.push('/index');
      }
    },
    mounted() {

    },
    created() {
      this.order = this.$route.query.order;
      // console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .m-ok-img {
    width: 198px;
    height: 191px;
    margin: 260px 0 70px 0;
  }
  .price-text {
    margin-top: 60px;
  }
  .order-text {
    margin: 20px 0 80px 0;
  }
  .m-btn {
    display: flex;
    .m-btn-text {
      width: 115px;
      margin: 0 65px;
      padding: 26px 63px;
      border-radius: 4px;
      white-space: nowrap;
      border: 2px solid @grey;
    }
  }
</style>
