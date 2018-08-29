<template>
    <div class="m-discover">
      <navbar :list="nav_list" @navClick="navClick"></navbar>

      <!--每日10荐-->
      <every v-if="nav_select == 'every'"></every>
      <!--素材圈-->
      <fodder v-if="nav_select == 'fodder'"></fodder>
      <!--公告-->
      <announcement v-if="nav_select == 'announcement'"></announcement>
      <!--教程-->
      <course v-if="nav_select == 'course'"></course>

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
  import announcement from './component/announcement';
  import course from './component/course';
  import iconList from'../../components/common/iconList';

  import api from '../../api/api';
  import axios from 'axios';

    export default {
      data() {
        return {
          show_modal:false,
          nav_list:[
            {
              tnname:'每日10荐',
              url:'every',
              dot:false,
              click:true
            },{
              tnname:'素材圈',
              url:'fodder',
              dot:false,
              click:false
            },{
              tnname:'公告',
              url:'announcement',
              dot:true,
              click:false
            },{
              tnname:'教程',
              url:'course',
              dot:true,
              click:false
            }
          ],
          nav_select:'every'
        }
      },
      components: {
        navbar,
        fodder,
        every,
        announcement,
        course,
        iconList
      },
      methods: {
        navClick(v){
          for(let i=0;i<this.nav_list.length;i++){
            this.nav_list[i].click = false;
          }
          this.nav_list[v].click = true;
          this.nav_select = this.nav_list[v].url
        }
      },
      created() {

        let token = "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzNTU4NDU2NywiaWF0IjoxNTM1NTEyNTY3fQ.eyJtb2RlbCI6IlVzZXIiLCJpZCI6Impma3NhZGpmLWZkYXNsa2pmLTMyMTMtMzEyMzEiLCJ0aW1lIjoiMjAxOC0wOC0yOSAxMToxNjowNyJ9._LSlRme_ktLk35dcuIGNVrze7xmdK-VtqPaXO-ZLmkc";
        localStorage.setItem('token', token);
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
