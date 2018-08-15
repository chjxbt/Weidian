<template>

      <mt-tabbar v-model="selected" :fixed="true">
        <mt-tab-item id="外卖">
          <img slot="icon" src="">
          外卖
        </mt-tab-item>
        <mt-tab-item id="订单">
          <img slot="icon" src="">
          订单
        </mt-tab-item>
        <mt-tab-item id="发现">
          <img slot="icon" src="">
          发现
        </mt-tab-item>
        <mt-tab-item id="我的">
          <img slot="icon" src="">
          我的
        </mt-tab-item>
      </mt-tabbar>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: '',
              selected:'我的'
            }
        },
        components: {},
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
</style>
