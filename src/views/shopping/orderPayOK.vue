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
    <canvas id="myCanvas" style="border: 1px #d3d3d3 solid;">
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

        let productImgList = ["/static/images/share/product1.png", "/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product4.png"];
        // let productImgList = ["/static/images/share/product1.png", "/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product4.png", "/static/images/share/product5.png", "/static/images/share/product.jpg"];

        let canvas = document.getElementById("myCanvas");
        let context = canvas.getContext("2d");

        // 小集合图、大集合图
        canvas.height = 1275;
        if(productImgList.length == 4) {
          canvas.width = 1525;
        }else if(productImgList.length == 6) {
          canvas.width = 2150;
        }

        // 处理商品标题的字间距
        context.font="30px PingFang-SC";
        let name = "商品标题商品标题商品标题商品标题商品标题商品标题商品标题商品标题商品标题商";
        let col = 12;
        for(let i = 0; i < col; i ++) {
          context.fillText(name[i], (90 + 34 * i), 970);
        }
        for(let i = col; i < (2 * col - 1); i ++) {
          context.fillText(name[i], (90 + 34 * (i - col)), 1015);
          if(i == (2 * col - 2)) {
            context.fillText("...", 90 + 34 * (i - col + 1), 1015);
          }
        }
        // 添加价格文字
        context.fillStyle = "#f43b51";
        context.font="bold 30px PingFang-SC";
        context.fillText("￥", 90, 1140);
        context.font="bold 58px PingFang-SC";
        context.fillText("129", 120, 1140);
        context.font="bold 30px PingFang-SC";
        context.fillText(". 50", 230, 1140);

        // 添加原价文字
        context.fillStyle = "#a4a4a4";
        context.font="30px PingFang-SC";
        context.fillText("原价：￥298.50", 90, 1200);

        // 创建要添加到canvas上的image对象
        let img0 = new Image();
        img0.crossOrigin = 'Anonymous';   // 设置图像的跨域属性-允许跨域
        img0.src = "/static/images/share/bg_test.png";  // 背景图

        // 依次往canvas上填充
        img0.onload = function(){

          let img1 = new Image();
          img1.crossOrigin = 'Anonymous';
          img1.src = "/static/images/share/sweep.png";    // 扫码下单
          img1.onload = function(){
            context.drawImage(img1 , 560 , 1190 , 260 , 60);

            let img2 = new Image();
            img2.crossOrigin = 'Anonymous';
            img2.src = "/static/images/share/Qrcode.png";    // 二维码
            img2.onload = function(){
              context.drawImage(img2 , 560 , 920 , 260 , 260);

              let img3 = new Image();
              img3.crossOrigin = 'Anonymous';
              img3.src = "/static/images/share/commitment.png";   // 三个背景为红色的承诺
              img3.onload = function(){
                context.drawImage(img3 , 50 , 825 , 800 , 55);

                let img4 = new Image();
                img4.crossOrigin = 'Anonymous';
                img4.src = productImgList[0];
                img4.onload = function(){
                  context.drawImage(img4 , 50 , 25 , 800 , 800);

                  let img5 = new Image();
                  img5.crossOrigin = 'Anonymous';
                  img5.src = productImgList[1];
                  img5.onload = function(){
                    context.drawImage(img5 , 875 , 25 , 600 , 600);

                    let img6 = new Image();
                    img6.crossOrigin = 'Anonymous';
                    img6.src = productImgList[2];
                    img6.onload = function(){
                      context.drawImage(img6 , 875 , 650 , 600 , 600);

                      let img9 = new Image();
                      img9.crossOrigin = 'Anonymous';
                      img9.src = "/static/images/share/delete.png";
                      img9.onload = function(){
                        context.drawImage(img9 , 175 , 1180 , 150 , 20);

                        // 大集合图
                        if(productImgList.length == 6) {

                          let img7 = new Image();
                          img7.crossOrigin = 'Anonymous';
                          img7.src = productImgList[3];
                          img7.onload = function(){
                            context.drawImage(img7 , 1500 , 25 , 600 , 600);

                            let img8 = new Image();
                            img8.crossOrigin = 'Anonymous';
                            img8.src = productImgList[4];
                            img8.onload = function(){
                              context.drawImage(img8 , 1500 , 650 , 600 , 600);
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
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
