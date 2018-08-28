<template>
    <div class="m-login">
      <img src="" class="m-login-logo" alt="">
      <div class="m-login-btn">
        <span>微信登录</span></div>
      <div class="m-login-bottom">
        <span class="m-login-check-box">
          <span class="m-login-check"></span>
          <span>我已阅读并同意《用户使用协议》</span>
        </span>
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
.m-login{
  background-color: #9fd0bf;
  min-height: 100%;
  .m-login-logo{
    display: inline-block;
    width: 400px;
    height: 200px;
    border: 1px solid #a4a4a4;
    margin: 300px 0;
  }
  .m-login-btn{
    margin-top: 150px;
    span{
      display: inline-block;
      width: 630px;
      height: 97px;
      line-height: 97px;
      color: #fff;
      font-size: 32px;
      border-radius: 48.5px;
      background-color: #09bb07;
      box-shadow: 0px 13px 22px 0 rgba(9, 187, 7, 0.35);
    }
  }
  .m-login-bottom{
    margin-top: 40px;
    font-size: 22px;
    color: #666;
    line-height: 25px;
    .m-login-check{
      display: inline-block;
      width: 23px;
      height: 23px;
      border: 1px solid #a4a4a4;
      vertical-align: bottom;

    }
  }
}
</style>
