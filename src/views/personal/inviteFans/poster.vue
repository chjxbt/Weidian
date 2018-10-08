<template>
    <div class="m-poster">
      <span class="m-poster-close">X</span>
      <h3>选择海报</h3>
      <div class="m-slider-box">
        <ul id="m-slider-ul" style="margin-left: 0px;" @touchstart='touchStart'
            @touchend='touchEnd'>
          <!--<li class="m-slider-left m-slider-side">-->
            <!--<img src="" class="m-slider-img" alt="">-->
          <!--</li>-->
          <!--<li class="m-slider-in">-->
            <!--<img src="" class="m-slider-img" alt="">-->
          <!--</li>-->
          <!--<li class="m-slider-right m-slider-side">-->
            <!--<img src="" class="m-slider-img" alt="">-->
          <!--</li>-->
          <template v-for="(item,index) in slider_list">
            <!--<li :class="(index == (slider_index -1) || (slider_index ==0 && index==slider_list.length -1) )? 'm-slider-left m-slider-side':(index == slider_index ? 'm-slider-in':((index == (slider_index +1 ) || (slider_list.length-1  == slider_index && index == 0))?'m-slider-right m-slider-side':''))">-->
              <!--<img src="" class="m-slider-img" alt="">-->
              <!--<div class="m-poster-content">-->
                <!--<div class="m-headPortrait-name">-->
                  <!--<span class="m-head-name">xxccccx</span>-->
                  <!--<img src="" class="m-head-portrait" />-->
                <!--</div>-->
                <!--<div class="m-poster-bottom">-->
                  <!--<div class="m-poster-code">-->
                    <!--<span class="m-code">邀请码: 872420</span>-->
                    <!--<img src="" class="m-poster-logo" alt="">-->
                  <!--</div>-->
                  <!--<img src="" class="m-poster-er" alt="">-->
                <!--</div>-->
              <!--</div>-->
            <!--</li>-->
            <li :class="(index == (slider_index -1) || (slider_index ==0 && index==slider_list.length -1) )? 'm-slider-left m-slider-side':(index == slider_index ? 'm-slider-in':((index == (slider_index +1 ) || (slider_list.length-1  == slider_index && index == 0))?'m-slider-right m-slider-side':''))">
              <img src="" :id="item.name" class="m-slider-img" alt="">
            </li>

          </template>
        </ul>
        <span class="m-slider-index">{{slider_index +1}}/{{slider_list.length}}</span>
      </div>
      <div class="m-poster-btn">
        <div class="m-btn">
          <span class="m-poster-btn-icon"></span>
          <p>保存图片</p>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
              slider_index:1,
                slider_list:[{
                  src:'',
                  url:'',
                  name:1
                },{
                  src:'',
                  url:'',
                  name:2
                },{
                  src:'',
                  url:'',
                  name:3
                },{
                  src:'',
                  url:'',
                  name:4
                }],
              startX:0,//开始触摸的位置
              endX:0,//结束触摸的位置
              interval:''

            }
        },
        components: {},
        mounted(){
            let that = this;
          for(let i=0;i<this.slider_list.length;i++){
            this.drawWay(this.slider_list[i].name)
          }
          this.interval = window.setInterval(that.animation,3000);
        },
        methods: {
          /*动画*/
          animation(v){
            v = v || 1;
            if(this.slider_index == this.slider_list.length -1){
              this.slider_index = 0;
            }else if(this.slider_index == 0 && v == -1){
              this.slider_index = this.slider_list.length -1;
            }else{
              this.slider_index = this.slider_index + v;
            }
          },
          /**/
          touchStart:function(ev) {
            ev = ev || event;
            ev.preventDefault();
//                      console.log(ev.targetTouches);
//                      console.log(ev.changedTouches);
            if(ev.touches.length == 1) {    //tounches类数组，等于1时表示此时有只有一只手指在触摸屏幕
              this.startX = ev.touches[0].clientX; // 记录开始位置
            }
            let that = this;
            window.clearInterval(that.interval);
          },
          touchEnd:function(ev){
            ev = ev || event;
            ev.preventDefault();
            if(ev.changedTouches.length == 1) {    //tounches类数组，等于1时表示此时有只有一只手指在触摸屏幕
              this.endX = ev.changedTouches[0].clientX; // 记录开始位置
            }
           if(this.endX < this.startX){
              this.animation(1);
           }else{
              this.animation(-1);
           }
           let that =this;
            this.interval = window.setInterval(that.animation,3000)
          },
          /*绘制图片*/
          drawWay(id){
            let canvas = document.createElement("canvas");
            let that = this;
            // let canvas = document.getElementById("m-canvas");
            let context = canvas.getContext("2d");
            canvas.height = 870;
            canvas.width = 580;

            context.rect(0, 0, canvas.width, canvas.height);
            context.fillStyle = "#efefef";
            context.fill();


            let bgImg = new Image();
            bgImg.crossOrigin = 'Anonymous';
            bgImg.src = "/static/images/poster/bg.jpg";

            bgImg.onload = function () {
              context.drawImage(bgImg, 0, 0,580,870);
              context.fillStyle="#c3c3c3";
              context.beginPath();
              // context.ellipse(180,83,62,26,0,0,Math.PI*2);
              that.drawRoundRect(context,110, 55, 140, 52, 25);
              context.fill();

              context.fillStyle = "#000";
              context.font = "normal 26px PingFang-SC";
              context.fillText("name", 153, 90);

              context.fillStyle="#fff";
              context.beginPath();
              context.lineWidth=5;
              context.arc(85,80,52,Math.PI*2,0,true);
              context.closePath();
              context.fill();
              let avatarImg = new Image();
              avatarImg.crossOrigin = 'Anonymous';
              avatarImg.src = "/static/images/poster/fans_img.png";

              avatarImg.onload = function () {
                context.drawImage(avatarImg, 40, 35,90,90);


                let logoImg = new Image();
                logoImg.crossOrigin = 'Anonymous';
                logoImg.src = "/static/images/poster/customer_service.png";

                logoImg.onload = function () {
                  context.drawImage(avatarImg, 100, 630, 200, 120);

                  let codeImg = new Image();
                  codeImg.crossOrigin = 'Anonymous';
                  codeImg.src = "/static/images/poster/fans_img.png";

                  codeImg.onload = function () {
                    context.drawImage(avatarImg, 390, 600, 145, 145);
                    let base64 = canvas.toDataURL("image/png");  //"image/png" 这里注意一下
                    let img = document.getElementById(id);

                    // document.getElementById('avatar').src = base64;
                    img.setAttribute('src', base64);
                  }
                }
              }

            }
          },
          drawRoundRect(cxt, x, y, width, height, radius){
            cxt.beginPath();
            cxt.arc(x + radius, y + radius, radius, Math.PI, Math.PI * 3 / 2);
            cxt.lineTo(width - radius + x, y);
            cxt.arc(width - radius + x, radius + y, radius, Math.PI * 3 / 2, Math.PI * 2);
            cxt.lineTo(width + x, height + y - radius);
            cxt.arc(width - radius + x, height - radius + y, radius, 0, Math.PI * 1 / 2);
            cxt.lineTo(radius + x, height +y);
            cxt.arc(radius + x, height - radius + y, radius, Math.PI * 1 / 2, Math.PI);
            cxt.closePath();
          }

        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  .m-poster{
    width: 100%;
    min-height: 100%;
    background: linear-gradient(to bottom, #362AC2, #FF7DD3);
    .m-poster-close {
      position: absolute;
      right: -20px;
      top: 10px;
      width: 120px;
      height: 50px;
      line-height: 50px;
      opacity: 0.7;
      border-radius: 29.5px;
      background-color: #333333;
      color: @grey;
      font-size: 30px;
    }
    h3{
      margin: 0;
      color: #fff;
      font-size: 30px;
      padding: 55px 0;
      font-weight: normal;
    }
    .m-slider-box{
      width: 100%;
      height: 910px;
      overflow: hidden;
      position: relative;
      ul{
        list-style-type:none;
        &:after{
          content: '';
          display: block;
          clear: both;
        }
        li{
          position: absolute;
          height: 870px;
          width: 580px;
          left:0;
          top:0;
          z-index: -1;
          &.m-slider-side{
            width: 86px;
            top:20px;
            z-index: 2;
          }
          &.m-slider-left{
            left:0;
            transition: all  1s;
          }
          &.m-slider-right{
            left:665px;
          }
          &.m-slider-in{
            z-index: 3;
            width: 580px;
            height: 910px;
            box-shadow: 0 8px 12px 0 rgba(66, 66, 66, 0.58);
            left:86px;
            transition: all 0.5s;
          }
          .m-slider-img{
           display: block;
            /*z-index:-1;*/
            width: 100%;
            height: 100%;
            background-color: #cfcfcf;
          }
          .m-poster-content{
            position: absolute;
            top:0;
            left: 0;
            z-index: 100;
            padding: 35px 40px;
            .m-headPortrait-name{
              position: relative;
              /*top:35px;*/
              /*left: 40px;*/
              .m-head-portrait{
                position: absolute;
                top:0;
                left:0;
                width: 95px;
                height: 95px;
                border: 2px solid #fff;
                border-radius: 50%;
                z-index: 200;
                background-color: #a4a4a4;
              }
              .m-head-name{
                position: absolute;
                top:22px;
                left:70px;
                z-index: 100;
                padding: 0 40px;
                height: 52px;
                line-height: 52px;
                background-color: #c3c3c3;
                border-radius: 25.3px;
                font-size: 26px;
              }
            }
            .m-poster-bottom{
              margin-top: 570px;
              .flex-row(flex-start);
              .m-poster-code{
                .m-code{
                  display: block;
                  font-size: 24px;
                  width: 208px;
                  height: 30px;
                  line-height: 30px;
                  background-color: #fff;
                  border-radius: 15px;
                  margin: 20px 0;
                }
                .m-poster-logo{
                  display: block;
                  width: 208px;
                  height: 100px;
                  background-color: #fff;
                }
              }
              .m-poster-er{
                display: block;
                width: 145px;
                height: 145px;
                background-color: #fff;
                margin-left: 150px;
              }
            }
          }
        }
      }
      .m-slider-index{
        position: absolute;
        bottom: 20px;
        left: 50%;
        z-index: 1001;
        width: 140px;
        height: 40px;
        line-height: 40px;
        font-size: 22px;
        background-color: @grey;
        border-radius: 20px;
        color: #666;
        transform: translateX(-70px);
      }
    }
    .m-poster-btn{
      .flex-row(center);
      margin-top: 40px;
      .m-btn{
        font-size: 22px;
        color: #666;
        .m-poster-btn-icon{
          display: inline-block;
          width: 80px;
          height: 80px;
          /*border: 1px solid #fff;*/
          border-radius: 50%;
          background: url("/static/images/icon-poster-download.png");
          background-size: 100% 100%;
        }
      }
    }
  }
</style>
