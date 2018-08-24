<template>
    <div class="m-index">
      <div class="m-suspend-btn" @click.stop="showModal('show_task')">
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
            <span class="m-close" @click="closeModal('show_modal')"> x </span>
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
      <div class="m-modal" v-if="show_task">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <span class="m-close" @click="closeModal('show_task')"> x </span>
          </div>
          <div class="m-modal-content">
            <h3 class="m-modal-award-title">
              <span>奖励任务</span>
              <span class="m-modal-award-info">15元新衣币*2张</span>
            </h3>
            <div class="m-scroll">
              <ul class="m-modal-award-ul">
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn active">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span><span class="m-red">首单佣金翻倍</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
                <li>
                  <div class="m-modal-award-img-box">
                    <img src="" class="m-modal-award-img" alt="">
                    <div>
                      <h3>观看视频1</h3>
                      <p class="m-modal-award-complete"><span>完成 0/1</span> </p>
                    </div>
                  </div>
                  <span class="m-modal-award-btn">做任务</span>
                </li>
              </ul>
            </div>
            <div class="m-modal-award-rule">
              <h3>规则</h3>
              <p class="m-modal-award-rule-info">
                完成任务领取奖励balbalalabanal
                bababa
              </p>
            </div>
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
              show_task:false,
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
          closeModal(v){
            this[v]  = false;
          },
          showModal(v){
            this[v] = true;
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
.m-index{
  .m-modal{
    .m-modal-state{
      /*height: auto;*/
      width: 620px;
      height: 1000px;
      .m-modal-head{
        padding: 0 20px;
      }
      .m-modal-content{
        padding: 0;
        .m-modal-award-title{
          .flex-row(space-between);
          color: #333;
          padding: 10px 33px 30px;
          font-size: 30px;
          font-weight: normal;
          border-bottom: 1px solid @borderColor;
          margin-bottom: 20px;
          .m-modal-award-info{
            color: @grey;
            font-size: 24px;
          }
        }
        .m-scroll{
          height: 620px;
          overflow-y: auto;
          .m-modal-award-ul{
            li{
              .flex-row(space-between);
              margin: 0 25px;
              border-bottom: 1px solid @borderColor;
              padding: 30px 0;
              .m-modal-award-img-box{
                .flex-row(flex-start);
                text-align: left;
                .m-modal-award-img{
                  display: block;
                  width: 77px;
                  height: 77px;
                  background-color: #a3a3a3;
                  border-radius: 50%;
                  margin-right: 30px;
                }
                h3{
                  font-size: 26px;
                  line-height: 30px;
                }
                .m-modal-award-complete{
                  font-size: 22px;
                  .m-red{
                    margin-left: 20px;
                  }
                }
              }
              .m-modal-award-btn{
                display: block;
                width: 137px;
                height: 46px;
                line-height: 46px;
                text-align: center;
                border-radius: 23px;
                background:  linear-gradient(to right, #ff3146, #ff7044);
                -webkit-background-clip: text;
                color: transparent;
                border: 2px solid #ff3146;
                &.active{
                  color: #fff;
                  border: solid 2px transparent;
                  background-image: linear-gradient(to right, #ff3146, #ff7044), linear-gradient(to right, #ff3146, #ff7044);
                  background-origin: border-box;
                  background-clip: content-box, border-box;
                }
              }
            }
          }
        }
        .m-modal-award-rule{
          text-align: left;
          h3{
            margin: 0 33px 20px;
            font-size: 30px;
          }
          .m-modal-award-rule-info{
            padding: 10px 80px;
            font-size: 20px;
            line-height: 24px;
          }
        }
      }
    }

  }
}

</style>
