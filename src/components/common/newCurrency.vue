<template>
  <div>
    <div class="new-currency" @click="chooseNewCurrency">
      <span class="user-new-content">优惠：5元新衣币</span>
      <img src="/static/images/icon-list-right.png" class="user-new-more">
    </div>

    <!--底部弹框-->
    <mt-popup v-model="popupVisible" position="bottom" class="new-currency-popup">
      <div class="popup-title">新衣币</div>
      <mt-navbar v-model="selected">
        <mt-tab-item id="1" @click="tabName">可使用</mt-tab-item>
        <mt-tab-item id="2" @click="tabName">不可用</mt-tab-item>
      </mt-navbar>
      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="1">

          <div class="m-scroll">
            <ul class="m-new-info">
              <li class="m-already-back">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">
                    <img src="" class="m-new-info-img" alt="">
                    <p>乌冬冬领取后24小时未
                      使用还回</p>
                  </div>
                </div>
                <div class="new-currency-choose-img">
                  <img v-if="chooseNewVisible" src="/static/images/icon-complain-check-active.png" class="new-currency-choose" @click="chooseNew">
                  <img v-if="!chooseNewVisible" src="/static/images/icon-complain-check.png" class="new-currency-choose" @click="chooseNew">
                </div>
              </li>
              <li class="m-already-back">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">
                    <img src="" class="m-new-info-img" alt="">
                    <p>乌冬冬领取后24小时未
                      使用还回</p>
                  </div>
                </div>
                <div class="new-currency-choose-img">
                  <img v-if="chooseNewVisible" src="/static/images/icon-complain-check-active.png" class="new-currency-choose" @click="chooseNew">
                  <img v-if="!chooseNewVisible" src="/static/images/icon-complain-check.png" class="new-currency-choose" @click="chooseNew">
                </div>
              </li>
              <li class="m-already-back">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">
                    <img src="" class="m-new-info-img" alt="">
                    <p>乌冬冬领取后24小时未
                      使用还回</p>
                  </div>
                </div>
                <div class="new-currency-choose-img">
                  <img v-if="chooseNewVisible" src="/static/images/icon-complain-check-active.png" class="new-currency-choose" @click="chooseNew">
                  <img v-if="!chooseNewVisible" src="/static/images/icon-complain-check.png" class="new-currency-choose" @click="chooseNew">
                </div>
              </li>
            </ul>
          </div>

          <div class="line"></div>
          <div class="m-un-use">
            <div class="un-use-text">不使用</div>
            <img v-if="chooseNewVisible" src="/static/images/icon-complain-check-active.png" class="un-use-img" @click="chooseNew">
            <img v-if="!chooseNewVisible" src="/static/images/icon-complain-check.png" class="un-use-img" @click="chooseNew">
          </div>
          <div class="line-black"></div>
          <div class="m-scroll-close" @click="closeScroll">关闭</div>

        </mt-tab-container-item>
        <mt-tab-container-item id="2">

          <div class="m-un-scroll">
            <ul class="m-new-info">
              <li class="m-already-used">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">
                    <img src="" class="m-new-info-img" alt="">
                    <p>乌冬冬领取后24小时未
                      使用还回</p>
                  </div>
                </div>
              </li>
              <li class="m-already-back">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">
                    <img src="" class="m-new-info-img" alt="">
                    <p>乌冬冬已使用</p>
                  </div>
                </div>
              </li>
              <li class="m-Unavailable">
                <div class="m-new-info-left">
                  <p class="m-red m-ft-b tc m-new-info-num">
                    <span class="m-ft-30">￥</span>
                    <span class="m-ft-60">5</span>
                  </p>
                  <p class="m-red">满6元使用</p>
                </div>
                <div class="m-new-info-right">
                  <p class="m-ft-24">限时分享贝币</p>
                  <p class="m-red">退回时间：2017.12.11 20:40</p>
                  <div class="m-new-person-info">

                  </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="line-black"></div>
          <div class="m-scroll-close" @click="closeScroll">关闭</div>

        </mt-tab-container-item>
      </mt-tab-container>
    </mt-popup>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'newCurrency',
        popupVisible: false,
        selected: "1",
        chooseNewVisible: false
      }
    },
    methods: {
      // 判断选择新衣币的下部弹框是否弹出
      chooseNewCurrency() {
        if(this.popupVisible) {
          this.popupVisible = false;
        }else if(!this.popupVisible) {
          this.popupVisible = true;
        }
      },
      // 勾选新衣币
      chooseNew() {
        // console.log(this.chooseNewVisible);
        if(this.chooseNewVisible) {
          this.chooseNewVisible = false;
        }else if(!this.chooseNewVisible) {
          this.chooseNewVisible = true;
        }
      },
      // 获取点击的tab 可使用、不可用
      tabName() {
        console.log(this.selected)
      },
      // 关闭选择新衣币的下部弹框
      closeScroll () {
        this.popupVisible = false;
        this.selected = "1";
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .new-currency {
    .user-new-content {
      color: @black;
      font-size: 26px;
    }
    .user-new-more {
      width: 22px;
      height: 22px;
      margin: 0 10px 0 10px;
    }
  }
  .new-currency-popup {
    width: 750px;
    height: 830px;
    .popup-title {
      color: @black;
      font-size: 36px;
      margin: 20px 25px 0 25px;
      text-align: left;
    }
    .m-scroll{
      height: 440px;
      overflow-y: auto;
      margin-top: 20px;
    }
    .m-un-scroll {
      height: 540px;
      overflow-y: auto;
      margin-top: 20px;
      margin-left: 60px;
      margin-bottom: 20px;
    }
    .m-new-info{
      li{
        .flex-row(flex-start);
        width: 545px;
        height: 220px;
        margin-left: 34px;
        &.m-already-used{
          display: flex;
          background: url("/static/images/bg-use.png") no-repeat;
          background-size: 100% 100%;
        }
        &.m-already-back{
          display: flex;
          background: url("/static/images/bg-back.png") no-repeat;
          background-size: 100% 100%;
        }
        &.m-Unavailable{
          display: flex;
          background: url("/static/images/bg-unavailable.png") no-repeat;
          background-size: 100% 100%;
          p{
            color: #888!important;
          }
        }
        .m-new-info-left{
          width: 130px;
          font-size: 24px;
          .m-new-info-num{
            margin-bottom: 20px;
          }
        }
        .m-new-info-right{
          padding-left: 60px ;
          padding-top: 20px;
          font-size: 21px;
          text-align: left;
          color: #fff;
          line-height: 32px;
          .m-new-person-info{
            margin-top: 35px;
            height: 65px;
            display: flex;
            flex-flow: row;
            align-content: end;
            .m-new-info-img{
              display: block;
              width: 60px;
              height: 60px;
              border-radius: 50%;
              background-color: #a4a4a4;
              margin-right: 20px;
            }
            p{
              width: 250px;
            }
          }
        }
        .new-currency-choose-img {
          flex: 1;
          .new-currency-choose {
            width: 49px;
            height: 49px;
            margin-right: -100px;
          }
        }
      }
    }
    /*滚动条样式*/
    ::-webkit-scrollbar {/*滚动条整体样式*/
      width: 9px;     /*高宽分别对应横竖滚动条的尺寸*/
      height: 9px;
      border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
      border-radius: 10px;
      -webkit-box-shadow: inset 0 0 5px #FBC6CC;
      background: #FBC6CC;
    }
    ::-webkit-scrollbar-track {/*滚动条里面轨道*/
      -webkit-box-shadow: inset 0 0 5px #FDEAEC;
      border-radius: 10px;
      background: #FDEAEC;
    }
    .line {
      width: 701px;
      height: 1px;
      opacity: 0.3;
      margin: 25px;
      background-color: @mainColor;
    }
    .m-un-use {
      display: flex;
      .un-use-text {
        flex: 1;
        font-size: 30px;
        color: @greyColor;
        text-align: left;
        margin: 0 0 30px 42px;
      }
      .un-use-img {
        width: 43px;
        height: 43px;
        margin: 0 50px;
      }
    }
    .line-black {
      width: 750px;
      opacity: 0.3;
      border: solid 1px @grey;
    }
    .m-scroll-close {
      margin: 22px 0;
      font-size: 30px;
      color: @mainColor;
      text-align: center;
    }
  }
</style>
