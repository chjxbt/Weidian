<template>
  <div class="m-modal m-share" >
    <div class="m-modal-state">
      <div class="m-modal-head">
        <span class="m-close" @click="closeModal('show_fixed')"> x </span>
      </div>
      <div class="m-modal-content" v-if="!is_sub">
        <h3 class="h3-text">还差一步就可以转发内容啦</h3>
        <div>
          <img :src="wximg" class="m-share-img" alt="">
          <p class="grey-text">关注公众号获取</p>
        </div>
      </div>

      <div class="m-modal-content" v-if="is_sub">
        <img id="avatar" class="canvas-img">
        <p class="grey-text">长按图片分享您的专属二维码</p>
      </div>
    </div>
  </div>

</template>

<script type="text/ecmascript-6">
  import wxapi from '../../common/js/mixins';
  export default {
    mixins: [wxapi],
    data() {
      return {
        name: '',
        wximg:localStorage.getItem('wximg'),
        is_sub:localStorage.getItem('subscribe')
      }
    },
    props: {
      src: { type: String, default: null },
      show_fixed: { type: Boolean, default: false },
      shareParams: { type: Object, default: {} }
    },
    methods: {
      // 关闭modal
      closeModal(){
        this.$emit('closeModal');
      },
      // 合成图片
      shareImg() {
        let productImgList = [];
        for(let i = 0; i < this.shareParams.media.length; i ++) {
          productImgList.push(this.shareParams.media[i].amimage);
        }
        // productImgList = ["/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product4.png"];
        // productImgList = ["/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product2.png", "/static/images/share/product4.png", "/static/images/share/product5.png", "/static/images/share/product.jpg"];

        let canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");

        // 小集合图、大集合图
        canvas.height = 1275;
        if(productImgList.length == 4) {
          canvas.width = 1525;
        }else if(productImgList.length == 6) {
          canvas.width = 2150;
        }

        context.rect(0, 0, canvas.width, canvas.height);
        context.fillStyle = "#fff";
        context.fill();

        // 处理商品标题的字间距
        context.fillStyle = "#000000";
        context.font="30px PingFang-SC";
        let name = this.shareParams.product.prname;
        let col = 12;
        if(name.length < 12 || name.length == 12) {
          for(let i = 0; i < name.length; i ++) {
            context.fillText(name[i], (90 + 34 * i), 970);
            // console.log(name[i])
          }
        }
        if(name.length > 12) {
          for(let i = col; i < (2 * col - 1); i ++) {
            context.fillText(name[i], (90 + 34 * (i - col)), 1015);
            if(i == (2 * col - 2)) {
              context.fillText("...", 90 + 34 * (i - col + 1), 1015);
            }
          }
        }

        // 添加价格文字
        let price = this.shareParams.product.prprice.split(".");
        context.fillStyle = "#f43b51";
        context.font="bold 30px PingFang-SC";
        context.fillText("￥", 90, 1150);
        context.font="bold 58px PingFang-SC";
        context.fillText(price[0], 120, 1150);
        context.font="bold 30px PingFang-SC";
        context.fillText(". " + price[1], 230, 1150);

        // 添加原价文字
        context.fillStyle = "#a4a4a4";
        context.font="30px PingFang-SC";
        context.fillText("原价：￥" + this.shareParams.product.prprice, 90, 1200);

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

                              let base64 = canvas.toDataURL("image/png");  //"image/png" 这里注意一下
                              let img = document.getElementById('avatar');

                              // document.getElementById('avatar').src = base64;
                              img.setAttribute('src' , base64);
                            }
                          }
                        }
                        // 小集合图
                        if(productImgList.length == 4) {
                          let base64 = canvas.toDataURL("image/png");  //"image/png" 这里注意一下
                          let img = document.getElementById('avatar');

                          // document.getElementById('avatar').src = base64;
                          img.setAttribute('src' , base64);
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        };
      }
    },
    mounted() {
      // this.src = "/static/images/share/Qrcode.png";

      this.shareImg();
      // console.log(this.show_fixed);
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/modal";

  .m-modal-state {
    width: 640px !important;
    min-height: 530px;
    .m-modal-head {
      width: 92% !important;
    }
    .m-modal-content {
      width: 100%;
      border-bottom: 0 !important;
      padding: 0 !important;
      .h3-text {
        margin-top: -20px;
        margin-bottom: 40px !important;
        white-space: nowrap;
      }
      .m-share-img {
        border: 1px red solid;
      }
      .canvas-img {
        /*width: 640px;*/
        height: 380px;
        margin-top: 10px;
        margin-bottom: -20px;
      }
      .grey-text {
        margin-top: 20px;
        /*border-top: 1px #d3d3d3 solid;*/
        line-height: 80px;
        letter-spacing: 1.2px;
      }
    }
  }
</style>
