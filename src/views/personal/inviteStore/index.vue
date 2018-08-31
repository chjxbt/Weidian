<template>
    <div class="m-inviteStore">
      <span class="m-inviteStore-rule m-ft-20 m-bg-main-color tr" @click="show_rule = true">规 则</span>
      <div class="m-modal" v-if="show_rule">
        <div class="m-modal-state">
          <div class="m-modal-head">
            <img src="http://img1.imgtn.bdimg.com/it/u=1767479973,4078045028&fm=26&gp=0.jpg" class="m-modal-img">
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
            <span class="modal-foot-btn" @click="show_rule = false">我 已 知 晓</span>
          </div>
        </div>
      </div>

      <div class="m-inviteStore-img-box">
        <img src="http://d6.yihaodianimg.com/N00/M00/FE/31/CgMBmVNv9WCAWLTNAAXxZghPNoo13800.jpg" class="m-inviteStore-img">
      </div>
      <div class="m-inviteStore-state">
        <div class="m-inviteStore-state-box">
          <ul class="m-inviteStore-type-ul">
            <template v-for="(item,index) in nav_list">
              <li :class="item.name == now.name ?'active':''" @click="navChange(item)">{{item.name}}</li>
            </template>
          </ul>
          <div class="m-inviteStore-content" v-if="now.name == '邀请记录'">
            <div class="m-inviteStore-progress">
              <p class="m-inviteStore-content-have">已成功邀请<span class="m-red">1</span>人，再邀请<span class="m-red">19</span>人可晋升，加油！</p>
              <mt-progress :value="20" :bar-height="5"></mt-progress>
            </div>
            <ul class="m-inviteStore-content-ul m-inviteStore-content-prepaid">
              <li>
                <div class="m-inviteStore-content-img-box">
                  <img src="" class="m-inviteStore-content-img" alt="">
                  <div>
                    <h3>乌东东</h3>
                    <p class="m-inviteStore-content-complete"><span>2018-08-08</span> </p>
                  </div>
                </div>
                <span >已支付</span>
              </li>
            </ul>

            <p class="m-inviteStore-content-info">邀请以下好友开店的概率更大哦，快行动吧~</p>
            <ul class="m-inviteStore-content-ul">
              <li>
                <div class="m-inviteStore-content-img-box">
                  <img src="" class="m-inviteStore-content-img" alt="">
                  <div>
                    <h3>乌东东</h3>
                    <p class="m-inviteStore-content-complete"><span>2018-08-08</span> </p>
                  </div>
                </div>
                <span >已购买16单</span>
              </li>
              <li>
                <div class="m-inviteStore-content-img-box">
                  <img src="" class="m-inviteStore-content-img" alt="">
                  <div>
                    <h3>乌东东</h3>
                    <p class="m-inviteStore-content-complete"><span>2018-08-08</span> </p>
                  </div>
                </div>
                <span >已购买16单</span>
              </li>
              <li>
                <div class="m-inviteStore-content-img-box">
                  <img src="" class="m-inviteStore-content-img" alt="">
                  <div>
                    <h3>乌东东</h3>
                    <p class="m-inviteStore-content-complete"><span>2018-08-08</span> </p>
                  </div>
                </div>
                <span>已购买16单</span>
              </li>
            </ul>
          </div>
          <div class="m-inviteStore-content" v-else-if="now.name == '礼包动态'">
              <ul class="m-inviteStore-dynamic-ul">
                <li>
                  <img src="http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=20a7d1b16163f62408503140ef2d818d/6a600c338744ebf8c8f43eb7d3f9d72a6159a7b5.jpg" class="m-inviteStore-dynamic-img">
                  <p class="m-inviteStore-dynamic-name">商品名称商品名称商品名称</p>
                  <p><span class="m-red">￥136</span></p>
                </li>
                <li>
                  <img src="http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=20a7d1b16163f62408503140ef2d818d/6a600c338744ebf8c8f43eb7d3f9d72a6159a7b5.jpg" class="m-inviteStore-dynamic-img">
                  <p class="m-inviteStore-dynamic-name">商品名称商品名称商品名称</p>
                  <p><span class="m-red">￥136</span></p>
                </li>
                <li>
                  <img src="http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=20a7d1b16163f62408503140ef2d818d/6a600c338744ebf8c8f43eb7d3f9d72a6159a7b5.jpg" class="m-inviteStore-dynamic-img">
                  <p class="m-inviteStore-dynamic-name">商品名称商品名称商品名称</p>
                  <p><span class="m-red">￥136</span></p>
                </li>
                <li>
                  <img src="http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=20a7d1b16163f62408503140ef2d818d/6a600c338744ebf8c8f43eb7d3f9d72a6159a7b5.jpg" class="m-inviteStore-dynamic-img">
                  <p class="m-inviteStore-dynamic-name">商品名称商品名称商品名称</p>
                  <p><span class="m-red">￥136</span></p>
                </li>
              </ul>

          </div>
          <div class="m-inviteStore-content" v-else-if="now.name == '邀请排行榜'">
              <h3 class="m-inviteStore-ranking-h3">-8月8日邀请开店排行榜-</h3>
            <p class="m-inviteStore-ranking-info">每日更新排行，请加油哦</p>
            <div class="m-fans-ranking-list">
              <div class="m-fans-top-three">
                <div class="m-fans-top-one">
                  <div class="m-fans-top-one-top m-fans-top-two">
                    <img src="" class="m-fans-top-one-img" alt="">
                    <span class="m-fans-crown"></span>
                    <span class="m-fans-scarf">No 2</span>
                  </div>
                  <p class="m-golden m-fans-top-name">贝之店</p>
                  <p class="m-ft-20">邀请数：<span  class="m-golden">212424</span></p>
                </div>
                <div class="m-fans-top-one">
                  <div class="m-fans-top-one-top">
                    <img src="" class="m-fans-top-one-img" alt="">
                    <span class="m-fans-crown"></span>
                    <span class="m-fans-scarf">No 1</span>
                  </div>
                  <p class="m-golden m-fans-top-name">贝之店</p>
                  <p class="m-ft-20">邀请数：<span  class="m-golden">212424</span></p>
                </div>
                <div class="m-fans-top-one ">
                  <div class="m-fans-top-one-top m-fans-top-three">
                    <img src="" class="m-fans-top-one-img" alt="">
                    <span class="m-fans-crown"></span>
                    <span class="m-fans-scarf">No 3</span>
                  </div>
                  <p class="m-golden m-fans-top-name">贝之店</p>
                  <p class="m-ft-20">邀请数：<span  class="m-golden">212424</span></p>
                </div>
              </div>
              <ul class="m-fans-ranking-ul">
                <li>
            <span>
              <span class="m-fans-ranking">4</span>
              <span class="m-fans-person-name">成成</span>
            </span>
                  <span class="m-ft-22">邀请5143个专属粉丝</span>
                </li>
                <li>
                  <span>
                    <span class="m-fans-ranking">5</span>

                    <span class="m-fans-person-name">成成</span>
                  </span>
                  <span class="m-ft-22">邀请5143个专属粉丝</span>
                </li>

              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="m-inviteStore-btn" @click="showModal(true)">立 即 邀 请</div>

      <div class="m-inviteStore-modal" v-if="show_modal">
        <div class="m-inviteStore-modal-state">
          <span class="m-inviteStore-modal-close" @click="showModal(false)"> X</span>
          <span class="m-inviteStore-modal-logo"></span>

          <div class="m-inviteStore-modal-content">
            <h3 class="m-inviteStore-modal-content-h3">选择赠与的新衣币</h3>
            <ul class="m-inviteStore-modal-content-ul">
              <li>
                <span class="m-check"></span>
                <discount-coupon></discount-coupon>
              </li>
              <li>
                <span class="m-check active"></span>
                <discount-coupon></discount-coupon>
              </li>
            </ul>
          </div>
          <div class="m-inviteStore-modal-foot">
            <div class="m-flex-start">
              <span class="m-check"></span>
              <span>不使用新衣币</span>
            </div>
            <span class="m-inviteStore-modal-btn">确定</span>
          </div>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import discountCoupon from '../../../components/common/discountCoupon'
    export default {
      data() {
        return {
          now:{
            url:'record',
            name:'礼包动态'
          },
          nav_list:[
            {
              url:'record',
              name:'邀请记录'
            },
            {
              url:'dynamic',
              name:'礼包动态'
            },
            {
              url:'ranking',
              name:'邀请排行榜'
            }
          ],
          show_modal:false,
          show_rule: true
        }
      },
      components: { discountCoupon },
      methods: {
        navChange(v){
          this.now = v
        },
        showModal(v){
            this.show_modal = v;
        }
      },
      mounted(){

      },
      created() {

      }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
  @import "../../../common/css/modal";
.m-inviteStore{
  .m-inviteStore-rule {
    width: 45%;
    position: fixed;
    padding: 13px;
  }
  .m-inviteStore-img-box {
    background-color: #CF2A2A;
    .m-inviteStore-img{
      margin: 60px 13px 0 13px;
      width: 724px;
      height: 424px;
      border-radius: 10px;
    }
  }
  .m-modal{
    .m-modal-state{
      height: 530px;
      .m-modal-head{
        padding: 0;
        margin: -1px;
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
        .modal-foot-btn{
          width: 100%;
          /*&:last-child{
            border-right: none;
          }*/
        }
      }
    }
  }
  .m-inviteStore-state{
    padding: 13px;
    background-color: #CF2A2A;
    .m-inviteStore-state-box{
     background-color: #fff;
      border-radius: 10px;
      .m-inviteStore-type-ul{
        .flex-row(space-around);
        border-bottom: 1px solid @borderColor;
        color: @grey;
        li{
          height: 76px;
          line-height: 76px;
          font-size: 32px;
          &.active{
            color: #333;
            border-bottom: 3px solid @mainColor;
            margin-bottom: -3px;
          }
        }
      }
      .m-inviteStore-content{
        padding: 34px;
        min-height: 800px;
        .m-inviteStore-progress{
          padding: 0 47px;
          .m-inviteStore-content-have{
            font-size: 21px;
            line-height: 28px;
            color: #c1c1c1;
          }
        }
        .m-inviteStore-content-ul{
          &.m-inviteStore-content-prepaid{
            border-bottom: 1px solid @borderColor;
            li{
              .m-inviteStore-content-img-box{
                .m-inviteStore-content-img{
                  width: 100px;
                  height: 100px;
                  margin-right: 36px;
                  margin-left: 0;
                }
              }
            }
          }
          li{
            .flex-row(space-between);
            margin: 0 25px;
            padding: 30px 0;
            color: #666;
            .m-inviteStore-content-img-box{
              .flex-row(flex-start);
              text-align: left;
              .m-inviteStore-content-img{
                display: block;
                width: 80px;
                height: 80px;
                background-color: #a3a3a3;
                border-radius: 50%;
                margin-right: 46px;
                margin-left: 10px;
              }
              h3{
                font-size: 24px;
                line-height: 30px;
              }
              .m-inviteStore-content-complete{
                font-size: 21px;
                margin-top: 20px;
              }
            }
          }
        }
        .m-inviteStore-content-info{
          font-size: 24px;
          color: #666;
          margin: 15px 0;
        }
        .m-inviteStore-dynamic-ul{
          .flex-row(flex-start);
          flex-wrap: wrap;
          margin-bottom: 80px;
          li{
            width: 318px;
            margin-bottom: 20px;
            &:nth-child(odd){
              margin-right: 20px;
            }
            text-align: left;
            .m-inviteStore-dynamic-img{
              display: block;
              width: 318px;
              height: 318px;
              background-color: #a4a4a4;
            }
            .m-inviteStore-dynamic-name{
              font-size: 24px;
              width: 318px;
              overflow: hidden;
              text-overflow:ellipsis;
              white-space: nowrap;
            }
          }
        }
        .m-inviteStore-ranking-h3{
          font-size: 30px;
          font-weight: bold;
        }
        .m-inviteStore-ranking-info{
          font-size: 21px;
          margin: 20px 0;
          color: #666;
        }
        .m-fans-ranking-list{
          padding-top: 40px;
          .m-fans-top-three{
            .flex-row(space-around);
            font-size: 20px;
            color: #666;
            .m-fans-top-one{
              .m-fans-top-one-top{
                position: relative;
                /*margin-bottom: 20px;*/
                &.m-fans-top-two{
                  margin-top: 20px;
                  .m-fans-top-one-img{
                    display: inline-block;
                    width: 110px;
                    height: 110px;
                    border: 14px solid #dbcfc6;
                    border-radius: 50%;
                  }
                  .m-fans-crown{
                    position: absolute;
                    top:-25px;
                    right: 20px;
                    width: 70px;
                    height: 70px;
                    background: url("/static/images/fans_two_crown.png") no-repeat;
                    background-size: 100% 100%;
                  }
                  .m-fans-scarf{
                    position: absolute;
                    bottom: 0;
                    left: 50%;
                    transform: translateX(-60px);
                    width: 120px;
                    height: 40px;
                    line-height: 40px;
                    text-align: center;
                    color: #dbcfc6;
                    background: url("/static/images/fans_two_scarf.png") no-repeat;
                    background-size: 100% 100%;
                  }
                }
                &.m-fans-top-three{
                  margin-top: 20px;
                  .m-fans-top-one-img{
                    display: inline-block;
                    width: 110px;
                    height: 110px;
                    border: 14px solid #e3a357;
                    border-radius: 50%;
                  }
                  .m-fans-crown{
                    position: absolute;
                    top:-25px;
                    right: 20px;
                    width: 70px;
                    height: 70px;
                    background: url("/static/images/fans_three_crown.png") no-repeat;
                    background-size: 100% 100%;
                  }
                  .m-fans-scarf{
                    position: absolute;
                    bottom: -2px;
                    left: 50%;
                    transform: translateX(-60px);
                    width: 120px;
                    height: 40px;
                    line-height: 40px;
                    text-align: center;
                    color: #e3a357;
                    background: url("/static/images/fans_three_scarf.png") no-repeat;
                    background-size: 100% 100%;
                  }
                }
                .m-fans-top-one-img{
                  display: inline-block;
                  width: 130px;
                  height: 130px;
                  border: 14px solid #DCB276;
                  border-radius: 50%;
                }
                .m-fans-crown{
                  position: absolute;
                  top:-25px;
                  right: 20px;
                  width: 70px;
                  height: 70px;
                  background: url("/static/images/fans_one-crown.png") no-repeat;
                  background-size: 100% 100%;
                }
                .m-fans-scarf{
                  position: absolute;
                  bottom: 0;
                  left: 50%;
                  transform: translateX(-70px);
                  width: 140px;
                  height: 40px;
                  line-height: 40px;
                  text-align: center;
                  color: #AC8933;
                  background: url("/static/images/fans_one_scarf.png") no-repeat;
                  background-size: 100% 100%;
                }
              }
              .m-fans-top-name{
                font-size: 28px;
                margin: 20px 0 10px;
              }
            }
          }
          .m-fans-ranking-ul{
            li{
              .flex-row(space-between);
              margin: 0 20px;
              color: #666;
              font-size: 24px;
              /*padding: 5px 0;*/
              line-height: 80px;
              .m-fans-ranking{
                display: inline-block;
                width: 44px;
                height: 44px;
                line-height: 44px;
                vertical-align: middle;
                border-radius: 50%;
                background-color: #b2c4d7;
                color: #fff;
                font-size: 30px;
                margin-right: 20px;
              }
              .m-fans-person-name{
                font-size: 28px;
              }
            }

          }
        }
      }
    }
  }
  .m-inviteStore-btn{
    width: 460px;
    height: 80px;
    text-align: center;
    line-height: 80px;
    font-size: 30px;
    text-shadow: 5px 5px 5px rgba(0, 0, 0, 0.16);
    background-color: @mainColor;
    color: #fff;
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
    border-radius: 50px;
    position: fixed;
    left: 50%;
    bottom: 44px;
    transform: translateX(-230px);
    animation:myMove 1s infinite;//循环
    -webkit-animation:myMove 1s infinite;
    -moz-animation:myMove 1s infinite;
    -o-animation:myMove 1s infinite;
  }
  .m-inviteStore-modal{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0,0,0,0.2);
    z-index: 1001;
    transition: opacity .5s;
    .m-inviteStore-modal-state{
      background-color: #fff;
      position: absolute;
      width: 100%;
      height: 786px;
      left: 0;
      bottom:0;
      .m-inviteStore-modal-close{
        position: absolute;
        top:0;
        right: 10px;
        font-size: 30px;
        color: #a4a4a4;
        padding: 20px;
        touch-action: none;
      }
      .m-inviteStore-modal-logo{
        position: absolute;
        top:-75px;
        left: 50%;
        transform: translateX(-75px);
        width: 148px;
        height: 148px;
        border: 2px solid #fff;
        border-radius: 50%;
        background: url("/static/images/icon-invitateStore-logo.png") no-repeat;
        background-size: 100%;
      }
      .m-inviteStore-modal-content{
        padding: 34px;
        margin-top: 90px;
        .m-inviteStore-modal-content-h3{
          font-size: 28px;
          font-weight: bold;
        }
        .m-inviteStore-modal-content-ul{
          li{
            .flex-row(flex-start);
          }
        }
      }
      .m-inviteStore-modal-foot{
        .flex-row(space-between);
        font-size: 34px;
        color: #666;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 110px;
        line-height: 110px;
        background-color: #f5f5f5;
        border-top: 1px solid @borderColor;
        .m-inviteStore-modal-btn{
          display: block;
          width: 247px;
          height: 80px;
          line-height: 80px;
          color: #fff;
          background-color: @mainColor;
          border-radius: 6px;
          margin-right: 36px;
          font-size: 32px;
        }
      }
      .m-check{
        display: inline-block;
        width: 46px;
        height: 46px;
        margin: 0 38px;
        background: url("/static/images/icon-complain-check.png") no-repeat center;
        background-size: 100% 100%;
        &.active{
          background: url("/static/images/icon-complain-check-active.png") no-repeat center;
          background-size: 100% 100%;
        }
      }
    }
  }
}
  @keyframes  myMove{
    0%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform: translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px)scale(1,1);
    }
    50%{
      transform:translateX(-230px) scale(1.2,1.2);
      -moz-transform:translateX(-230px) scale(1.2,1.2);
      -webkit-transform:translateX(-230px) scale(1.2,1.2);
      -o-transform:translateX(-230px) scale(1.2,1.2);
      -ms-transform:translateX(-230px) scale(1.2,1.2);
    }
    100%{
      transform: translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
  }
  @-webkit-keyframes  myMove{
    0%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
    50%{
      transform:translateX(-230px) scale(1.2,1.2);
      -moz-transform:translateX(-230px) scale(1.2,1.2);
      -webkit-transform:translateX(-230px) scale(1.2,1.2);
      -o-transform:translateX(-230px) scale(1.2,1.2);
      -ms-transform:translateX(-230px) scale(1.2,1.2);
    }
    100%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
  }
  @-moz-keyframes  myMove{
    0%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
    50%{
      transform:translateX(-230px) scale(1.2,1.2);
      -moz-transform:translateX(-230px) scale(1.2,1.2);
      -webkit-transform:translateX(-230px) scale(1.2,1.2);
      -o-transform:translateX(-230px) scale(1.2,1.2);
      -ms-transform:translateX(-230px) scale(1.2,1.2);
    }
    100%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
  }
  @-o-keyframes  myMove{
    0%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
    50%{
      transform:translateX(-230px) scale(1.2,1.2);
      -moz-transform:translateX(-230px) scale(1.2,1.2);
      -webkit-transform:translateX(-230px) scale(1.2,1.2);
      -o-transform:translateX(-230px) scale(1.2,1.2);
      -ms-transform:translateX(-230px) scale(1.2,1.2);
    }

    100%{
      transform:translateX(-230px) scale(1,1);
      -moz-transform:translateX(-230px) scale(1,1);
      -webkit-transform:translateX(-230px) scale(1,1);
      -o-transform:translateX(-230px) scale(1,1);
      -ms-transform:translateX(-230px) scale(1,1);
    }
  }
</style>
