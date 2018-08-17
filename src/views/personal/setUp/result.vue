<template>
    <div class="m-add-result">
      <img src="" class="m-add-result-img" alt="">
      <p>恭喜，绑定成功！</p>
      <span class="m-result-btn" @click="returnBack">返回</span>
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
          returnBack(){
            this.$router.push('/bankCard');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
.m-add-result{
  text-align: center;
  p{
    font-size: 40px;
    font-weight: 500;
  }
  .m-add-result-img{
    display: inline-block;
    width: 200px;
    height: 200px;
    background-color: #a3a3a3;
    margin: 250px 0 58px;
  }
  .m-result-btn{
    display: inline-block;
    width: 690px ;
    height: 90px;
    line-height: 90px;
    background-color: @mainColor;
    color: #fff;
    border-radius: 10px;
    margin-top: 160px;
    font-size: 38px;
  }
}
</style>
