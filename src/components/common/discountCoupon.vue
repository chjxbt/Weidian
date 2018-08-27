<template>
  <div class="m-already-used m-discountCoupon">
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
<style lang="less" rel="stylesheet/less" >
  .m-discountCoupon{
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: flex-start;
    width: 545px;
    height: 220px;
    margin-top: 15px;
    &.m-already-used{
      background: url("/static/images/bg-use.png") no-repeat;
      background-size: 100% 100%;
    }
    &.m-already-back{
      background: url("/static/images/bg-back.png") no-repeat;
      background-size: 100% 100%;
    }
    &.m-Unavailable{
      background: url("/static/images/bg-unavailable.png") no-repeat;
      background-size: 100% 100%;
      p{
        color: #888!important;
      }
    }
    .m-new-info-left{
      width: 157px;
      font-size: 24px;
      .m-new-info-num{
        margin-bottom: 20px;
      }
    }
    .m-new-info-right{
      padding-left: 25px ;
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
  }
</style>
