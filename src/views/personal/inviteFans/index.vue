<template>
    <div class="m-fans" >
      <h3 class="m-fans-title">
        <!--邀请好友成为<span class="m-ft-60">专属粉丝</span>-->
      </h3>
      <div class="m-fans-border">
        <div class="m-fans-border-back">
          <div class="m-fans-img-box">
            <span class="m-fans-img"></span>
            <p class="m-fans-img-text">一次绑定 终生受益</p>
          </div>
          <p class="m-fans-info">每邀请1位专属粉丝预计收益 <span class="m-red m-ft-32">￥154</span> <span @click="fansClick">查看详情 ></span></p>
          <p class="m-fans-code-box">我的邀请码：<span class="m-ft-b m-ft-40"> 230232</span> <span class="m-fans-code-copy">复制</span></p>
        </div>

      </div>
      <div class="m-fans-share-box">
        <h3 class="m-fans-share-h3">立即邀请，赚取收益</h3>
        <p class="m-fans-share-p">好 友 将 获 得 20 元 新 衣 币</p>
        <div class="m-fans-share-btn">
          <span @click="sharePoster">分享海报</span>
          <span @click="copyText">分享链接</span>
        </div>
        <p class="m-fans-share-info">您已成功绑定5位粉丝  <span  @click="fansClick">&nbsp;&nbsp;&nbsp;点击查看></span></p>
      </div>
      <div class="m-fans-ranking-list-name">邀请排行榜</div>
      <div class="m-fans-ranking-list">
        <div class="m-fans-top-three">
          <div class="m-fans-top-one">
            <div class="m-fans-top-one-top m-fans-top-two">
              <img src="" class="m-fans-top-one-img" alt="">
              <span class="m-fans-crown"></span>
              <span class="m-fans-scarf">No 2</span>
            </div>
            <p class="m-golden m-fans-top-name">贝之店</p>
            <p>邀请<span  class="m-golden">4</span>个专属粉丝 </p>
          </div>
          <div class="m-fans-top-one">
            <div class="m-fans-top-one-top">
              <img src="" class="m-fans-top-one-img" alt="">
              <span class="m-fans-crown"></span>
              <span class="m-fans-scarf">No 1</span>
            </div>
            <p class="m-golden m-fans-top-name">贝之店</p>
            <p>邀请<span  class="m-golden">222</span>个专属粉丝 </p>
          </div>
          <div class="m-fans-top-one ">
            <div class="m-fans-top-one-top m-fans-top-three">
              <img src="" class="m-fans-top-one-img" alt="">
              <span class="m-fans-crown"></span>
              <span class="m-fans-scarf">No 3</span>
            </div>
            <p class="m-golden m-fans-top-name">贝之店</p>
            <p>邀请<span  class="m-golden">4</span>个专属粉丝 </p>
          </div>
        </div>
        <ul class="m-fans-ranking-ul">
          <li>
              <span>
                <span class="m-fans-ranking">4</span>
                <img src="" class="m-fans-portrait" alt="">
                <span class="m-fans-person-name">成成</span>
              </span>
            <span>邀请5个专属粉丝</span>
          </li>
          <li>
              <span>
                <span class="m-fans-ranking">5</span>
                <img src="" class="m-fans-portrait" alt="">
                <span class="m-fans-person-name">成成</span>
              </span>
            <span>邀请514个专属粉丝</span>
          </li>
        </ul>
      </div>
      <div class="m-modal m-copy-text" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal('show_modal')"> x </span>
          </div>
          <div class="m-modal-content">
            <h3>链接已经复制成功</h3>
            <p>您可以去分享给好友啦！
            </p>
          </div>
        <!--<div class="m-modal-foot">-->
        <!--<span class="m-modal-foot-btn">复制文案</span>-->
        <!--</div>-->
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: '',
              show_modal:false
            }
        },
        components: {},
        methods: {
          fansClick(){
            this.$router.push('/fansManagement')
          },
          sharePoster(){
            this.$router.push('/poster')
          },
          copyText(){
            let that =this;
            this.$copyText(window.location.origin + '/#/login').then(function (e) {
              that.show_modal = true;
            }, function (e) {

            })
          },
          closeModal(v){
            this[v] = false;
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  @import "../../../common/css/modal";
.m-fans{
  min-height: 100%;
  background: url("/static/images/invite_back.png") no-repeat;
  background-size: 100% 100%;
  padding: 40px 0;
  p{
    margin: 0;
  }
  .m-golden{
    color: #DCB276 ;
  }
  .m-fans-title{
    /*font-size: 50px;*/
    /*font-weight: bold;*/
    /*background:  linear-gradient(to bottom, #f0d9af, #ddab68) ;*/
    /*-webkit-background-clip: text;*/
    /*color: transparent;*/
    /*text-shadow: 8px 8px 5px rgba(0, 0, 0, 0.16);*/
    /*!*margin-bottom: 20px;*!*/
    /*span{*/
      /*font-size: 70px;*/
    /*}*/
    display: inline-block;
    width: 585px;
    height: 111px;
    background: url("/static/images/fans_name.png") no-repeat;
    background-size: 100% 100%;
  }
  .m-fans-border{
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: center;
    .m-fans-border-back{
      width: 652px;
      height: 530px;
      background: url("/static/images/fans_border.png") no-repeat;
      background-size: 100% 100%;
      margin-top: 20px;
      padding-top: 10px;
      .m-fans-img-box{
        position: relative;
        .m-fans-img{
          display: inline-block;
          width: 379px;
          height: 340px;
          background: url("/static/images/fans_img.png") no-repeat;
          background-size: 100% 100%;
        }
        .m-fans-img-text{
          position: absolute;
          bottom: 48px;
          left: 50%;
          transform: translateX(-123px);
          font-size: 30px;
          font-weight: bold;
          background:  linear-gradient(to bottom, #f0d9af, #ddab68) ;
          -webkit-background-clip: text;
          color: transparent;
          text-shadow: 8px 8px 5px rgba(0, 0, 0, 0.16);
        }
      }
      .m-fans-info{
        color: #ebcb8e;
        font-size: 28px;
        margin: 0;
      }
      .m-fans-code-box{
        color: #fff;
        font-size: 30px;
        .m-fans-code-copy{
          margin-left: 20px;
          margin-top: 40px;
          display: inline-block;
          width: 100px;
          height: 40px;
          border: 2px solid #fff;
          border-radius: 30px;
        }
      }
    }
  }
  .m-fans-share-box{
    margin-top: 30px;
    .m-fans-share-h3{
      font-size: 44px;
      color: #ebcb8e;
      line-height: 54.5px;
    }
    .m-fans-share-p{
      font-size: 32px;
      color: #ebcb8e;
      line-height: 54.5px;
    }
    .m-fans-share-btn{
      margin: 44px 0;
      span{
        display: inline-block;
        width: 168px;
        height: 40px;
        color: #7d3600;
        background:  linear-gradient(to bottom, #f0d9af, #ddab68) ;
        border-radius: 30px;
        line-height: 40px;
        &:last-child{
          margin-left: 70px;
        }
      }
    }
    .m-fans-share-info{
      color: #ebcb8e;
      font-size: 22px;
      line-height: 27px;
    }
  }
  .m-fans-ranking-list-name{
    width: 100%;
    height: 90px;
    line-height: 90px;
    font-size: 44px;
    color: #7d3600;
    background: url("/static/images/fans_ranking_list.png") no-repeat;
    background-size: 100% 100%;
    margin: 25px 0;
  }
  .m-fans-ranking-list{
    padding-top: 40px;
    .m-fans-top-three{
      .flex-row(space-around);
      font-size: 20px;
      color: #666;
      .m-fans-top-one{
        .m-fans-top-one-top{
          position: relative;
          /*margin-bottom: 20px;*/
          &.m-fans-top-two{
            margin-top: 20px;
            .m-fans-top-one-img{
              display: inline-block;
              width: 110px;
              height: 110px;
              border: 14px solid #dbcfc6;
              border-radius: 50%;
            }
            .m-fans-crown{
              position: absolute;
              top:-25px;
              right: 40px;
              width: 70px;
              height: 70px;
              background: url("/static/images/fans_two_crown.png") no-repeat;
              background-size: 100% 100%;
            }
            .m-fans-scarf{
              position: absolute;
              bottom: 0;
              left: 50%;
              transform: translateX(-60px);
              width: 120px;
              height: 40px;
              line-height: 40px;
              text-align: center;
              color: #dbcfc6;
              background: url("/static/images/fans_two_scarf.png") no-repeat;
              background-size: 100% 100%;
            }
          }
          &.m-fans-top-three{
            margin-top: 20px;
            .m-fans-top-one-img{
              display: inline-block;
              width: 110px;
              height: 110px;
              border: 14px solid #e3a357;
              border-radius: 50%;
            }
            .m-fans-crown{
              position: absolute;
              top:-25px;
              right: 40px;
              width: 70px;
              height: 70px;
              background: url("/static/images/fans_three_crown.png") no-repeat;
              background-size: 100% 100%;
            }
            .m-fans-scarf{
              position: absolute;
              bottom: -2px;
              left: 50%;
              transform: translateX(-60px);
              width: 120px;
              height: 40px;
              line-height: 40px;
              text-align: center;
              color: #e3a357;
              background: url("/static/images/fans_three_scarf.png") no-repeat;
              background-size: 100% 100%;
            }
          }
          .m-fans-top-one-img{
            display: inline-block;
            width: 130px;
            height: 130px;
            border: 14px solid #DCB276;
            border-radius: 50%;
          }
          .m-fans-crown{
            position: absolute;
            top:-25px;
            right: 40px;
            width: 70px;
            height: 70px;
            background: url("/static/images/fans_one-crown.png") no-repeat;
            background-size: 100% 100%;
          }
          .m-fans-scarf{
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-70px);
            width: 140px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            color: #AC8933;
            background: url("/static/images/fans_one_scarf.png") no-repeat;
            background-size: 100% 100%;
          }
        }
        .m-fans-top-name{
          font-size: 28px;
          margin: 20px 0 10px;
        }
      }
    }
    .m-fans-ranking-ul{
      li{
        .flex-row(space-between);
        margin: 0 50px;
        border-bottom: 1px solid #666;
        color: #666;
        font-size: 26px;
        padding: 20px 0;
        line-height: 80px;
        .m-fans-ranking{
          display: inline-block;
          width: 50px;
          height: 50px;
          line-height: 50px;
          vertical-align: middle;
          border-radius: 50%;
          background-color: #DCB276;
          color: #7d3600;
          font-size: 40px;
        }
        .m-fans-portrait{
          display: inline-block;
          width: 80px;
          height: 80px;
          border-radius: 50%;
          margin: 0 10px ;
          vertical-align: middle;
          background-color: #fff;
        }
        .m-fans-person-name{
          font-size: 28px;
          color: #DCB276;
        }
      }

    }
  }
}
</style>
