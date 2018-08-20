<template>
    <div class="m-apply-withdrawal">
      <div class="m-amount">
        <div class="m-ft-30">提现金额</div>
        <div class="m-input-amount">
          <p class="m-border">
            <span class="m-ft-50 m-red m-ft-b">￥</span>
            <input type="text" placeholder="最大可提现X元" class="m-input-amount-input">
            <span class="m-close-icon"></span>
          </p>
          <p>
            <input type="text" placeholder="可用余额9.01元（仅支持大于10元的提现申请）">
          </p>
        </div>
      </div>
      <div class="m-apply-withdrawal-btn">
        <span>提现到银行卡</span></div>
      <div class="m-apply-withdrawal-btn m-apply-withdrawal-btn-two">
        <span class="active">提现到银行卡</span>
        <span>提现到微信</span>
      </div>
      <div class="m-tel-info">
        <p>如果遇到问题，请随时联系我们！</p>
          <p>联系电话：12345678912</p>
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
  @import "../../../common/css/index";
.m-apply-withdrawal{
  .m-amount{
    padding: 33px 25px 0;
    box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.16);
    text-align: left;
    div{
      padding: 0 30px 0;
    }
    .m-input-amount{
      margin-top: 80px;
      input{
        border: none;
        padding: 30px;
        font-size: 24px;
        color: #c1c1c1;
        width: 90%;
      }
      .m-close-icon{
        display: inline-block;
        width: 60px;
        height: 60px;
        background-color: #a4a4a4;
        vertical-align: text-bottom;
      }
      .m-input-amount-input{
        width: 400px;
      }
      p.m-border{
        border-bottom: 1px solid #c1c1c1;
        height: 100px;
      }
    }
  }
  .m-apply-withdrawal-btn{
    margin-top: 60px;
    &.m-apply-withdrawal-btn-two{
      .flex-row(space-around);
      span{
        width: 300px;
      }
    }
    span{
      display: inline-block;
      width: 650px;
      height: 70px;
      line-height: 70px;
      background-color: @mainColor;
      color: #fff;
      border-radius: 50px;
      &.active{
        background-color: #c1c1c1;
      }
    }
  }
  .m-tel-info{
    position: absolute;
    bottom: 71px;
    width: 100%;
    p{
      width: 100%;
      text-align: center;
      font-size: 24px;
      color: #666;
      line-height: 32px;
    }
  }
}
</style>
