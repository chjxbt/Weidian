<template>
  <div class="m-discover-announcement">
    <div class="m-section-one">
      <div class="m-section-content">

        <div class="m-section-title">
          <img class="m-section-img"/>
          <div>
            <span class="m-title">茉莉</span>
            <p class="m-fodder-time">昨天 13:54发布</p>
          </div>

        </div>

        <div class="m-section-text">
          <p><span class="m-mark">置顶</span>周周奖励发得完吗？不存在！</p>
          <p class="m-ft-30">新鲜出炉的周周奖现已发放，还不快去查收！</p>
          <div class="m-video-box">
            <img src="" class="m-video-img" alt="">
            <video class="m-video" controls="controls" type="video/mp4" preload="auto">
              <!--<source src="../video/data/1.mp4" autostart="false">-->
              Your browser does not support the video tag.
            </video>
          </div>

          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>1231</span>
                <span class="m-good-icon"></span>
                <span>21231</span>
              </div>
            </div>
            <div>
              <icon-list :list="icon_list" @iconClick="iconClick"></icon-list>
            </div>
          </div>

          <div class="m-comment-box">

            <div class="m-comment-content">
              <span class="m-comment-s"></span>
              <p><span class="m-comment-name">A玲珑服饰有限责任公司</span> : 感谢平台31个省市去均有店铺的
                库存</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script type="text/ecmascript-6">
  import iconList from'../../../components/common/iconList';
  export default {
    data() {
      return {
        icon_list:[
          {
            src:'icon-down',
            name:'保存',
            url:'icon-down'
          },
          {
            src:'icon-message',
            name:'评论',
            url:'icon-message'
          }
        ]
      }
    },
    props:{
      tnid: { type: String, default: null }
    },
    components: { iconList },
    methods: {
      iconClick(v){

      }
    },
    mounted() {
      console.log(this.tnid);
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/discover";
</style>
