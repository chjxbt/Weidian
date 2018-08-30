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
          <img src="" class="m-img-l" alt="">
          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>1231</span>
                <span class="m-smile-icon"></span>
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
              src:'icon-share',
              name:'转发',
              url:'icon-share'
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
        tnid:{ type: String, default: null }
      },
      components: { iconList },
      methods: {
        iconClick(v){

        }
      },
      created() {

      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/discover";
</style>
