<template>
  <div class="m-withdrawal-details">
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
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  .m-withdrawal-details{
    .m-income-expenditure-total{
      .flex-row(space-around);
      margin-top: 65px;
      span{
        display: block;
        font-size: 30px;
        line-height: 40px;
        &.m-red{
          font-weight: bold
        }
      }

    }
    .m-scroll{
      height: 980px;
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

</style>
