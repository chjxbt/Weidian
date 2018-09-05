<template>
  <div>
    <!--<div class="m-detail-navs">
      <ul class="m-detail-nav">
        <li>
          全部(158人)
        </li>
        <li>
          已开单(68人)
        </li>
        <li>
          未开单(90人)
        </li>
      </ul>
    </div>-->

    <navbar :list="nav_list" @navClick="navClick"></navbar>

    <div class="detail-prompt">
      <p class="detail-prompt-text">今日提示：</p>
      <p class="detail-prompt-text">你今日需要培训56人，分别是金金、小婷。。。。。</p>
      <p class="detail-prompt-text">等姓名颜色标红者。</p>
      <p class="detail-prompt-text">理由：累计订单超过20笔，持续上升幅度较高。</p>
    </div>
    <different-days></different-days>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  import differentDays from "../memberCenter/components/differentDays";

  export default {
    name: "memberDetail",
    data(){
      return{
        nav_list: [
          { click: true, tnname: "全部(158人)" },
          { click: false, tnname: "已开单(68人)" },
          { click: false, tnname: "未开单(90人)" }
        ]
      }
    },
    components: { navbar, differentDays },
    methods: {
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .m-detail-navs {
    width: 100%;
    border-bottom:#e3b6c1 2px dashed;
    .m-detail-nav{
      .flex-row(space-around);
      color: #000000;
      font-size: 26px;
      font-weight: 500;
      margin: 35px 40px;
    }
  }
  .detail-prompt {
    margin: 19px 0 40px 20%;
    .detail-prompt-text {
      font-size: 20px;
      text-align: left;
      color: @mainColor;
    }
  }
</style>
