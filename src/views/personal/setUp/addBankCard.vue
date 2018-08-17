<template>
    <div class="m-add-bankCard">
        <div class="m-add-bankCard-content">
          <ul class="m-add-bankCard-form">
            <li>
              <span class="m-bankCard-label">姓名</span>
              <span class="m-bankCard-input">
                <input type="text" placeholder="输入姓名">
              </span>
            </li>
            <li>
              <span class="m-bankCard-label">卡号</span>
              <span class="m-bankCard-input">
                <input type="text" placeholder="输入卡号">
              </span>
            </li>
            <li>
              <span class="m-bankCard-label">银行</span>
              <span class="m-bankCard-select">
                <span>请选择银行</span>
                <span class="m-more-icon"></span>
              </span>
            </li>
          </ul>

          <div class="m-add-bankCard-btn">
            <span @click="addBankcard">下一步</span></div>
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
          addBankcard(){
            this.$router.push('/result');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../../common/css/index";
  .m-add-bankCard{
    background-color: #f2f5f7;
    height: 100%;
    width: 100%;
    .m-add-bankCard-content{
      padding-top: 20px;
      .m-add-bankCard-form{
        padding-left: 36px;
        background-color: #fff;
        border-bottom: 1px solid @borderColor;
        border-top: 1px solid @borderColor;
        li{
          height: 100px;
          line-height: 100px;
          .flex-row(flex-start);
          border-bottom: 1px solid @borderColor;
          &:last-child{
            border: none;
          }
          .m-bankCard-label{
            display: block;
            width: 170px;
            text-align: left;
            font-size: 30px;
          }
          .m-bankCard-input{
            width: 544px;
            input{
              width: 100%;
              font-size: 30px;
              border: none;
              height: 98px;
            }
          }
          .m-bankCard-select{
            width: 544px;
            text-align: right;
            color: @grey;
            font-size: 30px;
            .m-more-icon{
              display: inline-block;
              width: 16px;
              height: 31px;
              margin: 0 34px;
              background-color: #a3a3a3;
              vertical-align: middle;
            }
          }
        }
      }
      .m-add-bankCard-btn{
        text-align: center;
        span{
          display: inline-block;
          width: 706px;
          height: 97px;
          line-height: 97px;
          font-size: 36px;
          color: #fff;
          background-color: @mainColor;
          border-radius: 10px;
          margin-top: 300px;
        }
      }
    }
  }
</style>
