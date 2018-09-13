<template>
  <div class="m-modal m-share" >
    <div class="m-modal-state">
      <div class="m-modal-head">
        <span class="m-close" @click="closeModal('show_fixed')"> x </span>
      </div>
      <div class="m-modal-content">
        <h3>还差一步就可以转发内容啦</h3>
        <div>
          <img :src="src" class="m-share-img" alt="">
          <p>关注公众号获取</p>
        </div>
      </div>
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
        props: {
          src:{
            type:String,
            default:null
          }
        },
        methods: {
          closeModal(){
            this.$emit('closeModal');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../common/css/modal";
</style>
