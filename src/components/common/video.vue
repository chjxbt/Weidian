<template>
    <div class="m-modal m-video-modal">
      <div class="m-video-box">
        <video :src="src" autoplay="true"></video>
        <span class="m-close" @click="videoClose">X</span>
      </div>
    </div>
</template>

<script>
    export default {
        name: "video",
      props:{
          src:{
            type:String,
            default:null
          }
      },
      methods:{
        videoClose(){
          this.$emit('videoClose')
        }
      }
    }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/modal";
  .m-video-modal{
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: center;
    background-color: #000;
    .m-video-box{
      height: 450px;
      width: 100%;
      background-color: #fff;
      position: relative;
      video{
        width: 100%;
        height: 450px;
      }
      .m-close{
        position: absolute;
        top: 0;
        right:0;
        background-color: rgba(0,0,0,0.3);
        color: #fff;
        width: 40px;
        height: 40px;
        line-height: 40px;
        border-radius: 50%;
      }
    }
  }


</style>
