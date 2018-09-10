<template>
    <div>
      <on-open v-if="isOpen"></on-open>
      <un-open v-else></un-open>
    </div>

</template>

<script type="text/ecmascript-6">
  import onOpen from './shop/onOpen';
  import unOpen from './shop/unOpen';
    export default {
        data() {
            return {
                isOpen: false
            }
        },
        components: {
          onOpen,
          unOpen
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";
  .m-part-one{
    background-color: #fff;

    .m-name{
      text-align: left;
      font-size: 24px;
      line-height: 32px;
      margin-top: 20px;
      margin-left: 32px;
    }
    .m-income-info{
      padding-bottom: 30px;
      text-align: center;
    }
  }
  .m-part-list{
    .flex-row(space-around);
    padding: 46px 0;
    li{
      .flex-col(center);
      .m-part-list-icon{
        display: block;
        width: 50px;
        height: 50px;
        margin-bottom: 15px;
      }
      .m-num{
        font-size: 40px;
        margin-top: 30px;
        /*line-height: 1.33;*/
        font-weight: bold;
      }
    }

  }
  .m-short-bannar{
    width: 100%;
    height: 100px;
    background-color: #a4a4a4;
    margin: 16px 0;
  }
</style>
