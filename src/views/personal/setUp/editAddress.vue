<template>
    <div class="m-editAddress">
      <div class="m-editAddress-form">
        <div class="m-editAddress-row">
          <span class="m-editAddress-row-name">收货人</span>
          <div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="form.uaname" class="m-editAddress-input" placeholder="输入收货人姓名">
            </div>
             <div class="m-editAddress-input-box">
               <input type="text" v-model="form.uaphone" class="m-editAddress-input" placeholder="输入收货人联系方式">
             </div>
          </div>
        </div>
        <div class="m-editAddress-row">
          <span class="m-editAddress-row-name">收货地址</span>
          <div>
            <div class="m-editAddress-input-box">
              <input type="text" class="m-editAddress-input" placeholder="选择省、市、区（县）">
            </div>
            <div class="m-editAddress-input-box">
              <input type="text" v-model="form.uaphone" class="m-editAddress-input" placeholder="输入详情街道地址">
            </div>
          </div>
        </div>
      </div>
      <div class="m-editAddress-switch">
        <span>设为默认</span>
        <span class="m-radio" :class="form.uadefault ? 'active':''" @click="radioChange"></span>
      </div>
      <div class="m-editAddress-switch">
        <span class="m-red">删除收货地址</span>
      </div>

      <div class="m-address-btn" >保存</div>

    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                radio_select:true,
               form:{
                 uadefault: false,
                 uaname:'',
                 uaphone:'',
                 uatext:'',
                 uaid:''
               }
            }
        },
        components: {},
        methods: {
          radioChange(){
            this.form.uadefault = !this.form.uadefault;
          }
        },
      mounted(){
          if(this.$route.query){
            this.form = this.$route.query;
          }
      },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
.m-editAddress{
  background-color: #f2f5f7;
  height: 100%;
  width: 100%;
  .m-editAddress-form{
    width: 100%;
    border-top: 20px solid #f2f5f7;
    .m-editAddress-row{
      background-color: #fff;
      display: flex;
      flex-flow: row;
      justify-content: flex-start;
      font-size: 30px;
      border-bottom: 2px solid @borderColor;
      &:last-child{
        border-bottom: none;
      }
      .m-editAddress-row-name{
        width: 190px;
        text-align: center;
        line-height: 85px;
      }
      .m-editAddress-input-box{
        width: 560px;
        border-bottom: 2px solid @borderColor;
        input{
          width: 100%;
          border: none;
          height: 85px;
          line-height: 85px;
          font-size: 30px;
        }
        &:last-child{
          border-bottom: none;
        }
      }
    }
  }
  .m-editAddress-switch{
    .flex-row(space-between);
    height: 80px;
    line-height: 80px;
    font-size: 30px;
    background-color: #fff;
    padding: 0 36px;
    margin: 20px 0;
    .m-radio{
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
}
</style>
