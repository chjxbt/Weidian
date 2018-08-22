<template>
    <div class="m-setUp">
      <div class="m-setUp-logo">
        <img src="" class="m-logo" alt="">
      </div>
      <div class="m-setUp-form">
        <div class="m-row">
          <span class="m-form-label">昵称</span>
          <input type="text" class="m-setUp-input" placeholder="小居居">
        </div>
        <div class="m-row">
          <span class="m-form-label">微信号</span>
          <input type="text" class="m-setUp-input" placeholder="xiaojujuxiaokeai2018">
        </div>
        <div class="m-row">
          <span class="m-form-label">手机号</span>
          <input type="text" class="m-setUp-input" placeholder="12345678912">
        </div>
        <div class="m-row" @click="addressClick">
          <span class="m-form-label">地址</span>
          <input type="text" class="m-setUp-input" placeholder="杭州市萧山区宁围镇XX号">
        </div>
        <div class="m-row">
          <span class="m-form-label">银行卡</span>
          <input type="text" class="m-setUp-input" placeholder="6222222222222222222">
          <!--<router-link to="/bankCard" tag="span">-->
            <span class="m-row-btn" @click="barkChange">更换</span>
          <!--</router-link>-->
        </div>
      </div>

      <div class="m-setUp-btn">
        <span>退出登录</span>

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
          addressClick(){
            this.$router.push('/receiverAddress');
          },
          barkChange(){
            // this.$router.push('/bankCard');
            this.$router.push('/addBankCard');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../../common/css/index";
.m-setUp{
  .m-setUp-logo{
    width: 100%;
    padding: 76px 0;
    text-align: center;
    .m-logo{
      display: inline-block;
      width: 200px;
      height: 200px;
      border-radius: 50%;
      background-color: #a3a3a3;
    }
  }
  .m-setUp-form{
    margin-top: 30px;
    .m-row{
      .flex-row(flex-start);
      border-bottom: 1px solid @borderColor;
      padding: 20px 0;
      font-size: 24px;
      line-height: 32px;
      .m-form-label{
        width: 145px;
        display: inline-block;
        text-align: right;
        color: #c1c1c1;
        margin-right: 45px;
      }
      .m-setUp-input{
        border: none;
        font-size: 24px;
        width: 400px;
        &:focus{
          border: none;
        }
      }
      .m-row-btn{
        display: inline-block;
        height: 40px;
        line-height: 40px;
        width: 120px;
        text-align: center;
        background-color: @mainColor;
        color: #fff;
      }
    }
  }
  .m-setUp-btn{
    margin-top: 225px;
    span{
      display: inline-block;
      width: 690px;
      height: 80px;
      line-height: 80px;
      background-color: @mainColor;
      color: #fff;
      font-size: 30px;
    }

  }
}
</style>
