<template>
    <div>
      <div class="m-shop-top">
        <div class="m-flex-between">
          <span>账号设置</span>
          <span>等级规则</span>
        </div>
        <div class="m-flex-start m-shop">
          <img src="" class="m-shop-top-img" alt="">
          <div class="m-shop-content">
            <h3>小居居</h3>
            <div>
              <p>123123</p>
              <p>1123</p>
            </div>
          </div>
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
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-shop-top{
    padding: 28px;
    font-size: 26px;
    background-color: #9fd0bf;
    color: #fff;
    .m-shop{
      padding: 28px;
      .m-shop-top-img{
        display: block;
        width: 200px;
        height: 200px;
        background-color: #a4a4a4;
        border-radius: 50%;
        margin-right: 30px;
        border: 10px solid #fff;
      }
      .m-shop-content{
        height: 200px;
        text-align: left;
        p{
          line-height: 32px;
          font-size: 24px;
          margin-bottom: 10px;
        }
        h3{
          font-size: 40px;
          margin-bottom: 43px;
          margin-top: 20px;
          color: #fff;
        }
      }
    }
  }
</style>
