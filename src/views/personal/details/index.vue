<template>
    <div class="m-details">
      <div class="m-total-money">
        <p>可提现金额数额</p>
        <p class="m-red">0.00</p>
        <span class="m-total-detail" @click="detailClick">提现明细</span>
        <span class="m-putforward-btn active" @click="putForwardClick">提现</span>
      </div>
      <div class="m-money-detail-type">
        <div class="m-money-type-one">
          <p>预估到账金额</p>
          <p class="m-red">0.00</p>
        </div>
        <div class="m-money-type-one">
          <p>预估到账金额</p>
          <p class="m-red">0.00</p>
        </div>
      </div>
      <p class="m-select-date">
        <span>2018年8月</span>
        <span class="m-select-date-icon"></span>
      </p>
      <div class="m-money-details">
        <p class="m-money-type">
          <span class="active">我的收益</span>
          <span>新衣币</span>
        </p>
        <p class="m-income-expenditure">
          <span class="active">收入</span>
          <span>支出</span>
        </p>
        <p class="m-income-expenditure-total">
          <span >本月总计</span>
          <span class="m-red">￥0.00</span>
        </p>
        <div class="m-scroll">
          <ul class="m-money-info">
            <li>
              <div>
                <p>消费返现</p>
                <p class="m-money-info-date">2018.07.30 19:27:15</p>
              </div>
              <div class="m-red">-1.35</div>
            </li>
          </ul>
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
        methods: {
          detailClick(){
            this.$router.push('/withdrawalDetail');
          },
          putForwardClick(){
            this.$router.push('applyWithdrawal');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../../common/css/index";
  .m-details{
    .m-total-money{
      height: 230px;
      text-align: center;
      font-size: 30px;
      border-bottom: 1px solid @borderColor;
      box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.16);
      position: relative;
      padding-top: 20px;
      p{
        margin: 20px 0;
        &.m-red{
          margin-top: 40px;
          font-size: 50px;
          font-weight: bold;
        }
      }
      .m-putforward-btn{
        position: absolute;
        width: 250px;
        height: 70px;
        line-height: 70px;
        text-align: center;
        border-radius: 50px;
        background-color: #c1c1c1;
        box-shadow: 2px 8px 8px 0 rgba(0, 0, 0, 0.16);
        color: #fff;
        left: 50%;
        bottom: -35px;
        transform: translateX(-125px);
        &.active{
          background-color: @mainColor;
          color: #fff;
        }
      }
      .m-total-detail{
        position: absolute;
        right: 23px;
        bottom: 14px;
        width: 129px;
        height: 40px;
        text-align: center;
        line-height: 40px;
        color: #888;
        border: 2px solid #888;
        border-radius: 30px;
        font-size: 24px;

      }
    }
    .m-money-detail-type{
      .flex-row(space-around);
      height: 180px;
      .m-money-type-one{
        p{
          margin-top: 20px;
          font-size: 30px;
          line-height: 40px;
          &.m-red{
            font-size: 40px;
            font-weight: bold;
            line-height: 53px;
          }
        }
      }
    }
    .m-select-date{
      text-align: center;
      font-size: 24px;
      line-height: 32px;
      color: #666666;
      margin-bottom: 10px;
      .m-select-date-icon{
        display: inline-block;
        width: 24px;
        height: 12px;
        background-color: #edb3b1;
        line-height: 32px;
      }
    }
    .m-money-details{
      height: 46px;
      .m-money-type{
        .flex-row(flex-start);
        span{
          display: block;
          width: 50%;
          height: 46px;
          line-height: 46px;
          font-size: 24px;
          background-color: #e9e9e9;
          color: #c1c1c1;
          &.active{
            background-color: @mainColor;
            color: #fff;
          }
        }
      }
      .m-income-expenditure{
        .flex-row(space-around);
        margin: 20px 0;
        span{
          display: block;
          font-size: 24px;
          line-height: 32px;
          color: #c1c1c1;
          padding: 0 10px;
          &.active{
            color: #666666;
            border-bottom: 4px solid @mainColor;
          }
        }
      }
      .m-income-expenditure-total{
        .flex-row(space-around);
        span{
          display: block;
          font-size: 24px;
          line-height: 32px;
          &.m-red{
            font-weight: bold;
          }
        }

      }
      .m-scroll{
        height: 460px;
        overflow-y: auto;
        padding-top: 40px;
        margin-right: 48px;
        .m-money-info{
          li{
            .flex-row(space-around);
            color: #666;
            font-size: 24px;
            line-height: 32px;
            margin-bottom: 20px;
            div{
              text-align: center;
              .m-money-info-date{
                font-size: 21px;
                line-height: 28px;
              }
            }
          }
        }
      }
    }
  }
/*滚动条样式*/
.m-scroll::-webkit-scrollbar {/*滚动条整体样式*/
  width: 9px;     /*高宽分别对应横竖滚动条的尺寸*/
  height: 9px;
  border-radius: 10px;
}
.m-scroll::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 5px #FBC6CC;
  background: #FBC6CC;
}
.m-scroll::-webkit-scrollbar-track {/*滚动条里面轨道*/
  -webkit-box-shadow: inset 0 0 5px #FDEAEC;
  border-radius: 10px;
  background: #FDEAEC;
}
</style>
