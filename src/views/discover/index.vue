<template>
    <div class="m-discover">
      <navbar :list="nav_list" @navClick="navClick"></navbar>

      <!--每日10荐-->
      <every v-if="nav_select == '0'" :tnid="nav_list[0].tnid"></every>
      <!--素材圈-->
      <fodder v-if="nav_select == '1'" :tnid="nav_list[1].tnid" @fodder="getData"></fodder>
      <!--公告-->
      <announcement v-if="nav_select == '2'" :tnid="nav_list[2].tnid"></announcement>
      <!--教程-->
      <course v-if="nav_select == '3'" :tnid="nav_list[3].tnid"></course>

      <div class="m-modal" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <img src="" class="m-modal-img">
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
  import { Toast } from 'mint-ui';

    export default {
      data() {
        return {
          show_modal: false,
          nav_list: [{ tnid: "1" }, { tnid: "1" },
            { tnid: "1" }, { tnid: "1" }],// 5ed4e908-a6db-11e8-b2ff-0cd292f93404
          nav_select: '1'
        }
      },
      components: { navbar, fodder, every, announcement, course, iconList },
      methods: {
        // 点击导航栏
        navClick(v){
          let arr = this.nav_list;
          for(let i = 0; i < arr.length; i ++){
            arr[i].click = false;
          }
          arr[v].click = true;
          this.nav_list = [].concat(arr);
          this.nav_select = v;
        },
        // 获取上部导航
        getTopnav() {
          axios.get(api.get_dp_topnav).then(res => {
            if(res.data.status == 200) {
              this.nav_list = res.data.data;
              this.nav_list[1].click = true;
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 接收子组件传的值
        getData(list) {
          this.nav_list = list;
          this.nav_list[1].click = true;
          // console.log(list);
        }
      },
      mounted() {
        // this.getTopnav();
        let token = "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzNTY2MzkyOCwiaWF0IjoxNTM1NTkxOTI4fQ.eyJtb2RlbCI6IlVzZXIiLCJpZCI6Impma3NhZGpmLWZkYXNsa2pmLTMyMTMtMzEyMzEiLCJ0aW1lIjoiMjAxOC0wOC0zMCAwOToxODo0OCJ9.lxgBU5RJ-wiVGoBFuDIhR9cz6RBvfcCf2MYmi-598Rk";
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
