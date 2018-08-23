<template>
    <div>
      <div class="m-suspend-btn">
        <span>开始转发</span>
      </div>
      <div class="m-top">
        <search></search>
        <navbar :list="nav_list" @navClick="navClick"></navbar>
      </div>

      <mt-swipe :auto="2000">
        <mt-swipe-item v-for="item in items" :key="item.id">
          <a :href="item.href" rel="external nofollow" >
            <img :src="item.url" class="img"/>
            <span class="desc"></span>
          </a>
        </mt-swipe-item>
      </mt-swipe>
      <div class="m-recommend">
        <span class="m-recommend-label">热文</span>
        <span>全新鞋面设计，阿迪新款首发，先到先得</span>
      </div>

      <div class="m-index-section">
        <ctx :icon="icon_list" @iconClick="iconClick"></ctx>
        <ctx></ctx>
      </div>


      <div class="m-modal" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal"> x </span>
          </div>
          <div class="m-modal-content">
            <h3>文案、图片已保存成功</h3>
            <p>图片已保存完成，复制文案即可
              一键发圈。
            </p>
          </div>
          <div class="m-modal-foot">
            <span class="m-modal-foot-btn">复制文案</span>
          </div>
        </div>
      </div>
      <div class="m-modal" v-if="!show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal"> x </span>
          </div>
          <div class="m-modal-content">
            <h3 class="m-modal-award-title">
              <span>奖励任务</span>
              <span class="m-modal-award-info">15元新衣币*2张</span>
            </h3>
            <ul>
              <li>

              </li>
            </ul>
          </div>
          <div class="m-modal-foot">

          </div>
        </div>
      </div>

      <share v-if="show_fixed" @fixedClick="fixedClick"></share>
    </div>

</template>

<script type="text/ecmascript-6">
  import navbar from '../../components/common/navbar';
  import search from '../../components/common/search';
  import ctx from './components/ctx';
  import share from '../../components/common/share';
    export default {
        data() {
            return {
              show_modal: false,
              show_fixed:false,
              items: [{
                title: '你的名字',
                href: 'http://google.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }, {
                title: '我的名字',
                href: 'http://baidu.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }],
              nav_list:[
                {
                  name:'上新',
                  url:'',
                  dot:false,
                  click:true
                },{
                  name:'特卖',
                  url:'',
                  dot:false,
                  click:false
                },{
                  name:'爆款',
                  url:'',
                  dot:true,
                  click:false
                },{
                  name:'预告',
                  url:'',
                  dot:true,
                  click:false
                }
              ],
              icon_list:[
                {
                  src:'icon-like',
                  name:'123123',
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
              ]
            }
        },
        components: {
          navbar,
          search,
          ctx,
          share
        },
        methods: {
          closeModal(){
            this.show_modal = false;
          },
          fixedClick(){
            this.show_fixed = false;
          },
          navClick(v){
            for(let i=0;i<this.nav_list.length;i++){
              this.nav_list[i].click = false;
            }
            this.nav_list[v].click = true;
          },
          iconClick(v){
            switch (v){
              case 0:
                break;
              case 1:
                this.show_modal = true;
                break;
              case 2:
                this.show_fixed = true;
                break;
            }
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
  @import "../../common/css/modal";
.m-top{
  margin-top: 10px;
}
  .m-recommend{
    width: 100%;
    background-color: #F9F9F9;
    height: 44px;
    line-height: 44px;
    font-size: 22px;
    .flex-row(center);
    .m-recommend-label{
      display: inline-block;
      padding: 0 10px;
      height: 27px;
      line-height: 27px;
      font-size: 20px;
      color: @mainColor;
      border: 1px solid @mainColor;
      border-radius: 4px;
      margin-right: 12px;
    }
  }
  .m-index-section{

  }
.m-suspend-btn{
  position: fixed;
  bottom: 211px;
  right: 5px;
  width: 113px;
  height: 113px;
  box-shadow: 0 7px 13px rgba(245, 78, 100, 0.83) ;
  background-color: rgba(245, 78, 100, 0.83);
  color: rgba(248, 248, 249, 0.8);
  border-radius: 50%;
  z-index: 1001;
  vertical-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}
  .m-modal{
    .m-modal-state{
      .m-modal-content{
        padding: 0;
        .m-modal-award-title{
          .flex-row(space-between);
          color: #333;
          padding: 20px 33px 30px;
          font-size: 30px;
          font-weight: normal;
          border-bottom: 1px solid @borderColor;
          .m-modal-award-info{
            color: @grey;
            font-size: 24px;
          }
        }
      }
    }

  }
</style>
