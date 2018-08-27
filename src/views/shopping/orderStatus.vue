<template>
  <div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: "orderStatus",
        order:{}
      }
    },
    // components: {  },
    methods: {

    },
    created() {
      this.order = this.$route.query.order;
      console.log("order", this.order);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";

</style>
