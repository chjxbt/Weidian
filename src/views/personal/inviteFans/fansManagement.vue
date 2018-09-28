<template>
    <div class="m-fansManagement">
      <div class="m-fans-code-box">
        <div class="m-fans-code">
          <div>
            <span>我的邀请码：</span>
            <span class="m-red">345678</span>
            <span class="m-fans-red-border">复制</span>
          </div>
          <p>规则</p>
        </div>
        <p class="m-fans-code-info">被邀请好友填写你的邀请码即可</p>
      </div>
      <div class="m-fans-img-box"></div>
      <div class="m-fans-type">
        <span :class=" fans_type == 'exclusive' ? 'active':''" @click="fansChange('exclusive')">专属粉丝 (15人) </span>
        <!--<span :class=" fans_type == 'invite' ? 'active':''" @click="fansChange('invite')">邀请潜在粉丝（125人）</span>-->
      </div>
      <div class="m-flex-between m-ft-b m-fans-total-money">
        <span>专属粉丝累计收益</span>
        <span class="m-red m-ft-28">￥400</span>
      </div>
      <div class="m-fans-content" v-if="fans_type == 'exclusive'">
        <div class="m-one">
          <img src="" class="m-one-img" alt="">
          <div class="m-one-right">
            <div class="m-one-right-row">
              <p>微信名：茉莉<span class="m-fans-red-border">专属粉丝</span></p>
              <p class="m-red m-ft-b m-ft-28">￥200</p>
            </div>
            <p>日期：2018.8.2</p>
            <p>粉丝期限:永久</p>
            <p>建议：分享商品，保持粉丝活性</p>
          </div>
        </div>
        <div class="m-one">
          <img src="" class="m-one-img" alt="">
          <div class="m-one-right">
            <div class="m-one-right-row">
              <p>微信名：茉莉<span class="m-fans-red-border">专属粉丝</span></p>
              <p class="m-red m-ft-b m-ft-28">￥200</p>
            </div>
            <p>日期：2018.8.2</p>
            <p>粉丝期限:永久</p>
            <p>建议：分享商品，保持粉丝活性</p>
          </div>
        </div>
      </div>
      <div class="m-fans-content m-fans-invite-content" v-else>
        <div class="m-one">
          <img src="" class="m-one-img" alt="">
          <div class="m-one-right">
            <p>微信名：茉莉</p>
            <p>日期：2018.8.2</p>
            <p>粉丝期限:永久</p>
            <p>建议：分享商品，保持粉丝活性</p>
          </div>
          <span class="m-fans-btn">邀请</span>
        </div>
        <div class="m-one">
          <img src="" class="m-one-img" alt="">
          <div class="m-one-right">
            <p>微信名：茉莉</p>
            <p>日期：2018.8.2</p>
            <p>粉丝期限:永久</p>
            <p>建议：分享商品，保持粉丝活性</p>
          </div>
          <span class="m-fans-btn doing">邀请中</span>
        </div>
        <div class="m-one">
          <img src="" class="m-one-img" alt="">
          <div class="m-one-right">
            <p>微信名：茉莉</p>
            <p>日期：2018.8.2</p>
            <p>粉丝期限:永久</p>
            <p>建议：分享商品，保持粉丝活性</p>
          </div>
          <span class="m-fans-btn done">已邀请</span>
        </div>
      </div>
    </div>
</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
               fans_type:'exclusive'
            }
        },
        components: {},
        methods: {
          fansChange(v){
            this.fans_type = v;
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  .m-fansManagement{
    .m-fans-code-box{
      padding: 15px 30px 25px;
      font-size: 30px;
      text-align: left;
      line-height: 40px;
      .m-fans-code{
        .flex-row(space-between);
        font-weight: bold;
        p{
          color: #666;
        }
      }
      .m-fans-code-info{
        color: @grey;
        font-size: 22px;
        margin-top: 10px;
      }
    }
    .m-fans-img-box{
      width: 100%;
      height: 275px;
      background-color: #a3a3a3;
      margin-bottom: 20px;
    }
    .m-fans-type{
      .flex-row(space-around);
      border-bottom: 1px solid @borderColor;
      margin-bottom: 10px;
      span{
        display: block;
        font-size: 26px;
        color: #727272;
        font-weight: bold;
        line-height: 38px;
        padding: 10px 0;
        &.active{
          color: @mainColor;
          border-bottom: 3px solid @mainColor;
        }
      }
    }
    .m-fans-total-money{
      padding: 30px;
      background-color: #f1f1f1;
      font-size: 30px;
    }
    .m-fans-content{
      .m-one{
        padding: 20px 30px 30px;
        border-bottom: 1px solid @borderColor;
        display: flex;
        flex-flow: row;
        justify-content: flex-start;
        font-size: 26px;
        color: @grey;
        text-align: left;
        .m-one-img{
          display: block;
          width: 88px;
          height: 88px;
          background-color: #a3a3a3;
          border-radius: 10px;
          margin-right: 25px;
        }
        .m-one-right{
          width: 88%;
          .m-one-right-row{
            .flex-row(space-between);
            .m-fans-red-border{
              font-size: 16px;
              padding: 5px;
            }
          }
          p{
            margin-top: 10px;
          }
        }
        .m-fans-btn{
          display: block;
          width: 25px;
          background-color: @mainColor;
          color: #fff;
          border-radius: 10px;
          font-size: 26px;
          padding:  35px 18px;
          text-align: center;
          margin-top: 30px;
          &.doing{
            background-color: @grey;
            padding:  17px 18px;
          }
          &.done{
            background-color: #f1f1f1;
            color: #666;
            padding:  17px 18px;
          }
        }
      }
    }
    .m-fans-red-border{
      display: inline-block;
      padding: 5px 10px;
      color: @mainColor;
      border: 2px solid @mainColor;
      border-radius: 6px;
      font-size: 20px;
      margin-left: 20px;
      line-height: 27px;
      vertical-align: top;
    }
  }
</style>
