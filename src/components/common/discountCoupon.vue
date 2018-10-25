<template>
  <div class="m-already-used m-discountCoupon">
    <div class="m-new-info-left">
      <p class="m-red m-ft-b tc m-new-info-num">
        <span class="m-ft-30">￥</span>
        <span class="m-ft-60">{{card.reward_detail.raamount}}</span>
      </p>
      <p class="m-red m-center" v-if="card.reward_detail.ratype == 0">满{{card.reward_detail.rafilter}}元使用</p>
      <p class="m-red m-center" v-else>{{card.reward_detail.zh_ratype}}</p>
    </div>
    <div class="m-new-info-right">
      <p class="m-ft-24">{{card.reward_detail.raname}}</p>
      <p class="m-red">领取时间：{{card.urcreatetime}}</p>
      <div class="m-new-person-info">
        <img :src="card.usheader" v-if="card.usheader" class="m-new-info-img" alt="">
        <p>{{card.remarks}}</p>
      </div>
    </div>
  </div>

</template>

<script type="text/ecmascript-6" >
    export default {
        data() {
            return {
                name: ''
            }
        },
        props: {
          card:{
            type:Object,
            default:null
          },
          i:{
            type:Number,
            default:null
          }
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
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
