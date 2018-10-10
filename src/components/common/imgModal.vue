<template>
    <div class="m-img-modal">
      <div class="m-modal-state">
        <!--<span class="m-close" @click="closeModal">X</span>-->
        <!--<img :src="src"  alt="">-->
        <mt-popup
          class="help-popup"
          v-model="helpPopupVisible"
          popup-transition="popup-fade">
          <img class="close-img" @click="closeModal" src="static/images/delete.png" alt="">
          <img style="width: 100%;height: 100%;" :src="src" alt="">
        </mt-popup>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: '',
              helpPopupVisible:true
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
    height: 750px;
    top:50%;
    left: 50%;
    transform: translate(-300px,-375px);
    /*img{*/
      /*width: 600px;*/
      /*height: 750px;*/
      /*background-color: #fff;*/
    /*}*/
    .m-close{
      position: absolute;
      top: 20px;
      right: 20px;
    }
  }
}
.help-popup{
  height: 750px;
  width: 600px;

  .close-img{
    position: absolute;
    top: 10px;
    right: 10px;
    width: 25px;
    height: 25px;
  }
}
</style>
