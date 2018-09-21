<template>
    <div class="m-modal m-video-modal">
      <div class="m-video-box">
        <video :src="src"></video>
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
      }
    }
</script>

<style lang="less" rel="stylesheet/less">
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
      video{
        width: 100%;
        height: 450px;
      }
    }
  }


</style>
