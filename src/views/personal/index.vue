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
                isOpen:false
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

</style>
