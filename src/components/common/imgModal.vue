<template>
    <div class="m-img-modal">
      <div class="m-modal-state">
        <span class="m-close" @click="closeModal">X</span>
        <img src="" alt="">
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
        methods: {
          closeModal(){
            this.$emit('closeModal','show_img')
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
.m-img-modal{
  position: fixed;
  top:0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: rgba(0,0,0,0.4);
  z-index: 10001;
  .m-modal-state{
    position: absolute;
    width: 600px;
    height: 600px;
    top:50%;
    left: 50%;
    transform: translate(-300px,-300px);
    img{
      width: 600px;
      height: 600px;
    }
    .m-close{
      position: absolute;
      top: 20px;
      right: 20px;
    }
  }
}
</style>
