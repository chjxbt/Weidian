<template>
    <div class="m-modal m-video-modal">
      <div class="m-video-box">
        <video :src="src" autoplay="true" x5-playsinline="true" x5-video-player-type="h5" x5-video-player-fullscreen="false"></video>
        <!--<video-player  class="video-player vjs-custom-skin"-->
                       <!--ref="videoPlayer"-->
                       <!--:playsinline="true"-->
                       <!--:options="playerOptions"-->
        <!--&gt;</video-player>-->
        <span class="m-close" @click="videoClose">X</span>
      </div>
    </div>
</template>

<script>
    export default {
        name: "video",
      data(){
          return {
            playerOptions: {
              playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
              autoplay: true, //如果true,浏览器准备好时开始回放。
              muted: false, // 默认情况下将会消除任何音频。
              loop: false, // 导致视频一结束就重新开始。
              preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
              language: 'zh-CN',
              aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
              fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
              sources: [{
                type: "",
                src: this.src//url地址
                // src: 'http://www.html5videoplayer.net/videos/madagascar3.mp4'//url地址
                // src: "" //url地址
              }],
              poster: "", //你的封面地址
              // width: document.documentElement.clientWidth,
              notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
              controlBar: {
                timeDivider: true,
                durationDisplay: true,
                remainingTimeDisplay: false,
                fullscreenToggle: true  //全屏按钮
              }
            }
          }
      },
      props:{
          src:{
            type:String,
            default:null
          }
      },
      mounted(){
        // document.getElementsByTagName("video")[0].play();
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
        width: 60px;
        height: 60px;
        line-height: 60px;
        border-radius: 50%;
        z-index: 10000;
      }
    }
  }


</style>
