<template>
  <div>
    returnProduct
  </div>
</template>

<script>
  export default {
    name: "returnProduct",
    data() {
      return {

      }
    },
    methods: {

    },
    created() {
      let type = this.$route.query.type;
      console.log("type", type);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

</style>
