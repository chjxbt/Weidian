<template>
  <div class="m-discover-fodder">
    <div class="m-filtrate-box">
      <span class="m-filtrate active">精选</span>
      <span class="m-filtrate">心灵鸡汤</span>
      <span class="m-filtrate">店主招募</span>
      <span class="m-filtrate">新手必发</span>
    </div>
    <div class="m-discover-fodder-content">
      <div class="m-section-one">
        <img class="m-section-img"/>
        <div class="m-section-content">
          <div class="m-section-title">
            <span class="m-title">茉莉</span>
          </div>
          <p class="m-fodder-time">昨天 13:54发布</p>
          <div class="m-section-text">
            <p>7月9日上午9:00开播99款，本次活动2天。</p>
            <ul class="m-img-list">
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li> <li>
              <img src="" class="m-section-text-img" alt="">
            </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
            </ul>
            <div class="m-section-bottom">
              <div>
                <div>805人已发圈</div>
              </div>
              <div>
                <icon-list :list="icon_list" @iconClick="iconClick"></icon-list>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <share v-if="show_fixed"  @fixedClick="fixedClick"></share>
  </div>

</template>

<script type="text/ecmascript-6">
  import iconList from '../../../components/common/iconList';
  import share from '../../../components/common/share';
    export default {
        data() {
            return {
              show_fixed:false,
              icon_list:[
                {
                  src:'icon-share',
                  name:'转发',
                  url:'icon-share'
                }
              ]
            }
        },
        components: {
          'icon-list':iconList,
          share
        },
        methods: {
          iconClick(v){
              this.show_fixed = true;
          },
          fixedClick(){
            this.show_fixed = false;
          },
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/discover";

</style>
