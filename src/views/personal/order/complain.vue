<template>
    <div class="m-complain">
      <div class="m-complain-form">
        <div class="m-complain-type">
          <span class="m-complain-type-btn">服务投诉</span>
          <span class="m-complain-type-btn">服务投诉</span>
        </div>
        <ul class="m-complain-checkbox">
          <li>
            <span class="m-checkbox active"></span>
            <span>客服态度差</span>
          </li>
          <li>
            <span class="m-checkbox active"></span>
            <span>商品质量问题</span>
          </li>
          <li>
            <span class="m-checkbox active"></span>
            <span>售后方案不合理</span>
          </li>
          <li>
            <span class="m-checkbox active"></span>
            <span>商品包装问题</span>
          </li>
        </ul>
        <div class="m-complain-textarea-box">
          <p><span>请详细描述您遇到的问题：</span><span class="m-complain">1/100</span></p>
          <textarea name="" id="" class="m-complain-textarea" placeholder="我们会尽快与您联系！"></textarea>
        </div>
        <div class="m-complain-submit">
          <span>提交</span>
        </div>
      </div>
      <div class="m-complain-line">自买订单</div>
      <div class="m-complain-order-list">
        <div class="m-no-complain-order">
          尚无相关订单...
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
  @import "../../../common/css/index";
.m-complain{
  .m-complain-form{
    padding: 20px 69px;
    .m-complain-type{
      .flex-row(space-between);
      .m-complain-type-btn{
        display: block;
        width: 264px;
        height: 60px;
        line-height: 60px;
        background-color: #666;
        color: #fff;
        font-size: 30px;
      }
    }
    .m-complain-checkbox{
      .flex-row(flex-start);
      flex-wrap: wrap;
      padding: 25px 0;
      li{
        width: 50%;
        font-size: 24px;
        color: #666;
        line-height: 32px;
        height: 41px;
        margin-bottom: 20px;
        &:nth-child(odd){
          text-align: left;
        }
        .m-checkbox{
          display: inline-block;
          width: 40px;
          height: 40px;
          background: url("/static/images/icon-check-personal.png") no-repeat center;
          background-size: 100% 100%;
          vertical-align: middle;
          margin-right: 30px;
          margin-left: 25px;
        }
      }
    }
    .m-complain-textarea-box{
      p{
        .flex-row(space-between);
        padding: 0 25px;
        font-size: 24px;
        .m-complain{
          color: #c1c1c1;
        }
      }
      .m-complain-textarea{
        margin: 14px 25px;
        width: 517px;
        height: 160px;
        border: 2px solid @borderColor;
        padding: 10px 20px;
        font-size: 21px;
      }
    }
    .m-complain-submit{
      padding: 0 25px;
      text-align: right;
      span{
        display: inline-block;
        width: 90px;
        height: 30px;
        line-height: 30px;
        text-align: center;
        background-color: @mainColor;
        color: #fff;
        border-radius: 30px;
        font-size: 21px;
      }
    }
  }
  .m-complain-line{
    width: 100%;
    height: 46px;
    line-height: 46px;
    font-size: 24px;
    background-color: @mainColor;
    color: #fff;
  }
  .m-complain-order-list{
    .m-no-complain-order{
      font-size: 30px;
      color: #c1c1c1;
      margin-top: 300px;
    }
  }
}
  .m-complain-textarea::-webkit-input-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea:-moz-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea::-moz-placeholder{
    color:#c1c1c1;
  }
  .m-complain-textarea:-ms-input-placeholder{
    color:#c1c1c1;
  }
</style>
