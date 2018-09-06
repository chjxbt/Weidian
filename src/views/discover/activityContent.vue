<template>
  <div>
    <img class="activity-img" :src="activity.rbimage">

    <mt-loadmore :top-method="loadTop" ref="loadmore">
      <div class="m-index-section">
        <template v-for="(item,index) in activity_list">
          <ctx :icon="icon_list" :list="item" :index="index" @iconClick="iconClick" @showMoreText="showMoreText"></ctx>
        </template>
      </div>
    </mt-loadmore>
    <share v-if="show_fixed" @fixedClick="fixedClick"></share>

    <m-footer></m-footer>
  </div>
</template>

<script>
  import mFooter from '../../components/common/footer';
  import ctx from '../index/components/ctx';
  import share from '../../components/common/share';
  export default {
    name: "activityContent",
    data() {
      return {
        activity: {},
        activity_list: [],
        icon_list:[
          {
            src:'icon-like',
            name:'收藏',
            url:'icon-like'
          },
          {
            src:'icon-lian',
            name:'复制链接',
            url:'icon-lian'
          },
          {
            src:'icon-share',
            name:'转发',
            url:'icon-share'
          }
        ],
        show_fixed: false
      }
    },
    components: { mFooter, ctx, share },
    methods: {
      // 下拉刷新
      loadTop() {
        for(let i=0;i<this.nav_list.length;i++){
          if(this.nav_list[i].click){
            this.getActivity(this.nav_list[i].tnid);
          }
        }
        this.$refs.loadmore.onTopLoaded();
      },
      /*每个活动icon点击*/
      iconClick(v, list){
        switch (v){
          case 0:
            this.changeLike(list);
            break;
          case 1:
            this.show_modal = true;
            break;
          case 2:
            this.show_fixed = true;
            break;
        }
      },
      // 展开全文、收齐全文
      showMoreText(bool,v){
        let arr = [].concat(this.activity_list);
        arr[v] = Object.assign({}, arr[v], { show_text: bool });
        this.activity_list = [].concat(arr);
      },
    },
    created() {
      this.activity = this.$route.query.activity;
      console.log(this.activity);
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .activity-img {
    width: 750px;
    height: 280px;
  }
</style>
