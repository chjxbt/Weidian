<template>
    <div class="m-discover">
      <mt-loadmore :top-method="loadTop" ref="loadmore">
        <navbar :list="nav_list" @navClick="navClick"></navbar>

        <!--<template v-for="(item,index) in nav_list">-->
          <!--每日10荐-->
          <every v-if="nav_select == '每日10荐'" :tnid="nav_list[select_index].tnid" ref="every"></every>
          <!--素材圈-->
          <fodder v-if="nav_select == '素材圈'" :tnid="nav_list[select_index].tnid" :sub="sub" ref="fodder"></fodder>
          <!--公告-->
          <announcement v-if="nav_select == '公告'" :tnid="nav_list[select_index].tnid " ref="announcement"></announcement>
          <!--教程-->
          <course v-if="nav_select == '教程'" :tnid=" nav_list[select_index].tnid" ref="course"></course>
        <!--</template>-->
      </mt-loadmore>

      <div class="m-modal" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head m-modal-store">
            <img src="http://cdn2.55haitao.com/bbs/data/attachment/forum/201411/20/132745toqfxf1r19k3y333.jpg" class="m-modal-img">
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
            <span class="m-modal-foot-btn grey" @click="toPage('index')">去首页逛逛</span>
            <span class="m-modal-foot-btn" @click="toPage('partner')">我要成为店主</span>
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
          /*nav_list: [{ tnid: "1" }, { tnid: "1" },
            { tnid: "1" }, { tnid: "1" }],// 5ed4e908-a6db-11e8-b2ff-0cd292f93404*/
          nav_list: [{ tnid: "1" }],// 5ed4e908-a6db-11e8-b2ff-0cd292f93404
          nav_select: '',
          sub: [],
          select_index:0
        }
      },
      components: { navbar, fodder, every, announcement, course, iconList },
      computed:{
        name(){
          return this.$route.query.name
        }
      },
      watch: {
        name: function (val) {
          this.getTopnav(this.$route.query.name)
        },
      },
      mounted(){
        if(localStorage.getItem('user_level') == 0){
          this.show_modal = true
        }
        if(this.$route.query.name){

          this.getTopnav(this.$route.query.name)

        }else{
          this.getTopnav();
        }

      },
      methods: {
        loadTop() {
          if(this.nav_select == '每日10荐') {
            this.$refs.every.loadTop();
          }else if(this.nav_select == '素材圈') {
            this.$refs.fodder.loadTop();
          }else if(this.nav_select == '公告') {
            this.$refs.announcement.loadTop();
          }else if(this.nav_select == '教程') {
            this.$refs.course.loadTop();
          }
          this.$refs.loadmore.onTopLoaded();
        },
        // 点击导航栏
        navClick(v){
          let arr = this.nav_list;
          for(let i = 0; i < arr.length; i ++){
            arr[i].click = false;
          }
          arr[v].click = true;
          this.nav_list = [].concat(arr);
          this.nav_select = this.nav_list[v].tnname;
          this.select_index = v;
        },
        // 获取上部导航
        getTopnav(name) {
          let _index = 0;
          axios.get(api.get_dp_topnav).then(res => {
            if(res.data.status == 200) {
              this.nav_list = res.data.data;
              for(let j=0;j<this.nav_list.length;j++){
                if(this.nav_list[j].tnname == '素材圈'){
                  this.sub = this.nav_list[j].sub;
                }
              }
              for(let i=0;i<this.nav_list.length;i++){
                if(this.nav_list[i].tnname == name){
                  _index = i;
                }else if(name == '赚钱学院' && this.nav_list[i].tnname == '教程'){
                  _index = i
                }
              }
              this.nav_list[_index].click = true;
              this.select_index = _index;
              this.nav_select = this.nav_list[_index].tnname;
            }else{
              Toast({ message: res.data.message, className: 'm-toast-fail' });
            }
          })
        },
        // 跳转页面
        toPage(page) {
          if(page == "index") {
            this.$store.state.tabbar_select = '首页';
            this.$router.push('/index');
          }else if(page == "partner") {
            this.$router.push('/invitationLetter');
            // this.show_modal = false;
          }
        }
      },
      created() {

      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/modal";
.m-discover{

  .m-modal{
    .m-modal-state{
      height: 530px;
      .m-modal-head{
        padding: 10px 20px;
        margin: -1px;
        &.m-modal-store{
          width: 100%;
          padding: 0;
        }
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
        border-top: 1px solid @borderColor;
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
