<template>
    <div class="m-collect">
      <div class="m-collect-one">
        <img src="" class="m-collect-img" alt="">
        <div class="m-collect-text">
          <div>
            <span class="m-check active"></span>
            <span class="m-red">下架商品</span>
          </div>
          <span>已有122人发圈</span>
        </div>
      </div>
      <div class="m-collect-one">
        <img src="" class="m-collect-img" alt="">
        <div class="m-collect-text">
          <div>
            <span class="m-check"></span>
            <span class="m-red">下架商品</span>
          </div>
          <span>已有122人发圈</span>
        </div>
      </div>
      <div class="m-collect-one">
        <img src="" class="m-collect-img" alt="">
        <div class="m-collect-text">
          <div>
            <span class="m-check"></span>
            <span class="m-red">下架商品</span>
          </div>

          <span>已有122人发圈</span>
        </div>
      </div>
      <div class="m-collect-fixed">
        <div class="m-left">
          <span class="m-check active"></span>
          <span>全选</span>
        </div>
        <span class="m-right">删除</span>
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
.m-collect{
  display: flex;
  flex-flow: row;
  align-items: center;
  justify-content: flex-start;
  flex-wrap: wrap;
  padding: 30px 55px;
  .m-collect-one{
    margin-bottom: 20px;
    &:nth-child(odd){
      margin-right: 40px;
    }
    .m-collect-img{
      display: block;
      width: 300px;
      height: 300px;
      box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
      margin-bottom: 20px;
    }
    .m-collect-text{
      font-size: 21px;
      line-height: 28px;
      display: flex;
      flex-flow: row;
      align-items: center;
      justify-content: space-between;
      .m-red{
        color: #f53b52;
      }

    }
  }
  .m-check{
    display: inline-block;
    width: 24px;
    height: 24px;
    background: url("/static/images/icon-complain-check.png") no-repeat;
    background-size: 100% 100%;
    &.active{
      background: url("/static/images/icon-complain-check-active.png") no-repeat;
      background-size: 100% 100%;
    }
  }
  .m-collect-fixed{
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 100;
    width: 100%;
    height: 100px;
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 -3px 6px 0 rgba(0, 0, 0, 0.16);
    .m-check{
      margin: 0 28px 0 55px;
    }
    .m-right{
      margin-right: 55px;
    }
  }
}
</style>
