<template>
    <div class="m-register">
      <img src="" class="m-register-logo" alt="">
      <h3 >欢迎你</h3>
      <div class="m-register-form">
        <mt-field placeholder="手机号" v-model="captcha">
        </mt-field>
        <mt-field placeholder="验证码" v-model="captcha">
          <span class="m-register-code">获取验证码</span>
        </mt-field>
      </div>
      <div class="m-register-btn">
        <span>确定</span>
      </div>
    </div>
</template>

<script>
  import common from '../../common/js/common';
    export default {
        name: "register",
      data(){
          return{
            captcha:''
          }
      },
      mounted(){
        common.changeTitle('注册');
      },
      methods:{

      }

    }
</script>

<style lang="less" rel="stylesheet/less" >
.m-register{
  padding: 50px 35px 50px 50px;
  text-align: left;
  .m-register-logo{
    display: block;
    width: 160px;
    height: 100px;
    border: 1px solid #a3a3a3;
  }
  h3{
    font-size: 56px;
    font-weight: bold;
    margin: 70px 0 150px;
  }
  .m-register-code{
    display: inline-block;
    width: 210px;
    height: 70px;
    line-height: 70px;
    background-color: #a4a4a4;
    color: #fff;
    text-align: center;
    font-size: 28px;
    border-radius: 10px;
  }
  .m-register-btn{
    text-align: center;
    margin-top: 400px;
    span{
      display: inline-block;
      background-color: #f43b51;
      color: #fff;
      width: 660px;
      height: 80px;
      line-height: 80px;
      border-radius: 40px;
      font-size: 32px;
    }
  }
}
  .mint-cell{
    border-bottom: 2px solid #a4a4a4;
    margin-bottom: 10px;
  }
</style>
