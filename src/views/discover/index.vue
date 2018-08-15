<template>
    <div class="m-discover">
      <navbar></navbar>

      <!--每日10荐-->
      <every></every>
      <!--素材圈-->
      <!--<fodder></fodder>-->
      <!--公告-->
      <!--<annoucement></annoucement>-->

      <div class="m-modal" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <img src="" class="m-modal-img" alt="">
          </div>
          <div class="m-modal-content">
            <h2>升级成为店主·方可使用此功能</h2>
            <ul class="m-modal-ul">
              <li>·<span>每日10荐 </span>精品推荐</li>
              <li>·<span>素&nbsp;&nbsp;材&nbsp;&nbsp;圈</span>时尚买家秀</li>
              <li>·<span>公&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;告</span>活动奖励不多，更多玩法</li>
              <li>·<span>教&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;程</span>精品专属教程</li>
            </ul>
          </div>
          <div class="m-modal-foot">
            <span class="m-modal-foot-btn grey">去首页逛逛</span>
            <span class="m-modal-foot-btn">我要成为店主</span>
          </div>
        </div>
      </div>

    </div>

</template>

<script type="text/ecmascript-6">
  import navbar from '../../components/common/navbar';
  import every from './component/everyTen';
  import fodder from './component/fodder';
  import annoucement from './component/announcement';
  import iconList from'../../components/common/iconList';
    export default {
        data() {
            return {
              show_modal:false
            }
        },
        components: {
          navbar,
          fodder,
          every,
          annoucement,
          iconList
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
.m-discover{


  .m-modal{
    .m-modal-state{
      height: 530px;
      .m-modal-head{
        padding: 0;
        .m-modal-img{
          display: block;
          width: 100%;
          height: 108px;
          background-color: #666666;
          border-top-left-radius: 10px;
          border-top-right-radius: 10px;
          border: 0;
        }
      }
      .m-modal-content{
        padding: 0 65px;
        h2{
          font-size: 26.5px;
          margin: 36px 0;
        }
        .m-modal-ul{
          li{
            padding-left: 60px;
            text-align: left;
            font-size: 20px;
            line-height: 46px;
            span{
              width: 110px;
              display: inline-block;
              margin-right: 20px;
            }
          }
        }
      }
      .m-modal-foot{
        position: absolute;
        bottom: 0;
        left: 0;
        .m-modal-foot-btn{
          width: 50%;
          border-right: 1px solid @borderColor;
          &:last-child{
            border-right: none;
          }
          &.grey{
            color: @grey;
          }
        }
      }
    }
  }
}
</style>
