<template>
    <div class="m-onOpen">
      <div class="m-shop-top">
        <div class="m-flex-between">
          <span>账号设置</span>
          <span>等级规则</span>
        </div>
        <div class="m-flex-start m-shop">
          <img src="" class="m-shop-top-img" alt="">
          <div class="m-shop-content">
            <h3>小居居</h3>
            <div>
              <p>您已成功超过 <span class="m-ft-30">80%</span> 的VIP</p>
              <p>离成功保级还差 <span class="m-ft-30">¥15000</span> 元</p>
            </div>
          </div>
        </div>
      </div>
      <div class="m-invite-box">
        <span class="m-invite-fans">邀请专属粉丝</span>
        <span class="m-invite-store">邀请购买开店大礼包</span>
      </div>
      <div>
        <div class="m-part-one">
          <div class="m-cell">
            <span class="m-cell-name">我的收益</span>
            <span>
              <span>查看更多</span>
              <span class="m-cell-icon"></span>
            </span>
          </div>
          <ul class="m-part-list">
            <li>
              <span>今日销售额</span>
              <span class="m-red m-num">1250</span>
            </li>
            <li>
              <span>今日赚</span>
              <span class="m-red m-num">250</span>
            </li>
            <li>
              <span>额外赚</span>
              <span class="m-red m-num">125</span>
            </li>
            <li>
              <span>新衣币</span>
              <span class="m-red m-num">234</span>
            </li>
          </ul>
          <p class="m-income-info">本月还差<span class="m-red m-ft-30">1520元</span>销售额即可获得奖励</p>
        </div>

        <div class="m-part-one">
          <div class="m-name">我的订单</div>
          <div class="m-cell">
            <span class="m-cell-nav">
              <span class="active">销售订单</span>
              <span>自买订单</span>
            </span>
            <span>
              <span>查看更多</span>
              <span class="m-cell-icon"></span>
            </span>
          </div>
          <ul class="m-part-list">
            <li>
              <span class="m-part-list-icon"></span>
              <span>待支付<span class="m-red">（1）</span></span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>待发货<span class="m-red">（1）</span></span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>已发货<span class="m-red">（1）</span></span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>已取消<span class="m-red">（0）</span></span>
            </li>
          </ul>
        </div>
      </div>

      <ul class="m-part-list">
        <li>
          <span class="m-part-list-icon"></span>
          <span>我的收藏</span>
        </li>
        <li>
          <span class="m-part-list-icon"></span>
          <span>赚钱学院</span>
        </li>
        <li>
          <span class="m-part-list-icon"></span>
          <span>我的导师</span>
        </li>
        <li>
          <span class="m-part-list-icon"></span>
          <span>我的导师</span>
        </li>
        <li>
          <span class="m-part-list-icon"></span>
          <span>快速投诉</span>
        </li>
      </ul>

      <div class="m-short-bannar">

      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {},
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-onOpen{
    color: #666;
    .m-shop-top{
      padding: 28px;
      font-size: 26px;
      background-color: #9fd0bf;
      color: #fff;
      .m-shop{
        padding: 28px;
        .m-shop-top-img{
          display: block;
          width: 200px;
          height: 200px;
          background-color: #a4a4a4;
          border-radius: 50%;
          margin-right: 30px;
          border: 10px solid #fff;
        }
        .m-shop-content{
          height: 200px;
          text-align: left;
          p{
            line-height: 32px;
            font-size: 24px;
            margin-bottom: 10px;
          }
          h3{
            font-size: 40px;
            margin-bottom: 43px;
            margin-top: 20px;
            color: #fff;
          }
        }
      }
    }
    .m-invite-box{
      .flex-row(space-around);
      span{
        display: block;
        width: 50%;
        height: 170px;
        line-height: 170px;
        text-align: center;
        color: #fff;
        &.m-invite-fans{
          background-color: #edb3b1;
        }
        &.m-invite-store{
          background-color: #799d74;
        }
      }
    }
    .m-part-one{
      border-bottom: 1px solid @borderColor;
    }
  }

</style>
