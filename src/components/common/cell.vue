<template>
  <div class="m-cell">
    <span class="m-cell-name">收藏夹</span>
    <span>
      <span class="m-cell-icon"></span>
    </span>
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
  @import "../../common/css/index";
  .m-cell{
    .flex-row(space-between);
    color: @grey;
    padding: 20px 32px;
    border-bottom: 1px solid @borderColor;
    .m-cell-name{
      color: #000;
    }
    .m-cell-icon{
      display: inline-block;
      width: 20px;
      height: 26px;
      vertical-align: middle;
      background-color: #666666;
      margin-left: 20px;
    }
  }
</style>
