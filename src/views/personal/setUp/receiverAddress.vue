<template>
    <div class="m-receiverAddress">
      <div v-if="have_address">
        <div class="m-one-address" @click="addressClick">
          <span class="m-check-icon active"></span>
          <div class="m-address-info">
            <div class="m-address-row m-address-row1 ">
              <span>小白</span>
              <span>18210036741</span>
            </div>
            <div class="m-address-row">
              <div class="tl m-address">
                <span class="m-mo">[ 默认地址 ]</span>
                <span>上京新航线304楼4单元702室上京新航线4楼4单元702室内</span>
              </div>
              <span class="m-edit">编辑</span>
            </div>
          </div>
        </div>
        <div class="m-one-address">
          <span class="m-check-icon"></span>
          <div class="m-address-info">
            <div class="m-address-row m-address-row1 ">
              <span>小白</span>
              <span>18210036741</span>
            </div>
            <div class="m-address-row">
              <div class="tl m-address">
                <span>上京新航线304楼4单元702室上京新航线4楼4单元702室内</span>
              </div>
              <span class="m-edit">编辑</span>
            </div>
          </div>
        </div>
        <div class="m-one-address">
          <span class="m-check-icon"></span>
          <div class="m-address-info">
            <div class="m-address-row m-address-row1 ">
              <span>小白</span>
              <span>18210036741</span>
            </div>
            <div class="m-address-row">
              <div class="tl m-address">
                <span>上京新航线304楼4单元702室上京新航线4楼4单元702室内</span>
              </div>
              <span class="m-edit">编辑</span>
            </div>
          </div>
        </div>
      </div>
      <div class="m-no-address" v-else>
        <img src="/static/images/icon-no-address.png" class="m-no-address-img" alt="">
        <p>您还没有收货地址哦</p>
      </div>

      <div class="m-address-btn" @click="addressClick">添加新地址</div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
              have_address:true
            }
        },
        components: {},
        methods: {
          addressClick(){
            this.$router.push('/editAddress')
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../../common/css/index";
  .m-receiverAddress{
    font-size: 28px;
    margin-bottom: 110px;
    .m-one-address{
      .flex-row(flex-start);
      height: 180px;
      border-bottom: 1px solid @borderColor;
      .m-check-icon{
        display: block;
        width: 50px;
        height: 50px;
        background: url("/static/images/icon-radio.png") no-repeat;
        background-size: 100%;
        margin: 30px;
        &.active{
          background: url("/static/images/icon-radio-active.png") no-repeat;
          background-size: 100%;
        }
      }
      .m-address-info{
        .m-address-row{
          margin-bottom: 10px;
          .flex-row(flex-start);
          &.m-address-row1{
            .flex-row(space-between);
            padding-right: 120px;
            width: 530px;
            span{
              display: block;
            }
          }
          .m-address{
            width: 530px;
            color: @grey;
            .m-mo{
              color: @mainColor;
            }
          }
          .m-edit{
            display: block;
            padding: 0 15px;
            border-left: 1px solid @borderColor;
            text-align: center;
            color: @grey;
          }
        }
      }

    }
    .m-address-btn{
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      text-align: center;
      height: 100px;
      line-height: 100px;
      background-color: @mainColor;
      color: #fff;
      font-size: 34px;
    }
    .m-no-address{
      height: 890px;
      background-color: #f1f1f1;
      padding-top: 332px;
      text-align: center;
      font-size: 26px;
      color: @grey;
      .m-no-address-img{
        display: inline-block;
        width: 218px;
        height: 123px;
      }
      p{
        margin-top: 20px;
      }
    }
  }
</style>
