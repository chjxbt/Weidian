<template>
  <div class="m-modal m-rule-modal" v-if="show_modal">
    <div class="m-modal-state">
      <div class="m-modal-head">
        <span class="m-close" @click="showModal(false)"> x </span>
      </div>
      <div class="m-modal-content">
        <h3>规则</h3>
        <div class="m-rule-scroll">
          <p>0000</p>

        </div>
      </div>
      <!--<div class="m-modal-foot">-->
      <!--<span class="m-modal-foot-btn">复制文案</span>-->
      <!--</div>-->
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
          show_modal:{
            type:Boolean,
            default:false
          },
          rule:{
            type:String,
            default:''
          }
        },
        methods: {
          showModal(v){
            this.$emit('showModal',v)
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/modal";
</style>
