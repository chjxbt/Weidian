<template>
    <div class="m-inviteStore" >
      <!--<div>-->
        <img src="" class="m-inviteStore-img" alt="">
      <!--</div>-->
        <div class="m-inviteStore-state">
          <div class="m-inviteStore-state-box">
            <ul class="m-inviteStore-type-ul">
              <li class="active">邀请记录</li>
              <li>礼包动态</li>
              <li>邀请排行榜</li>
            </ul>
            <div class="m-inviteStore-content">
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
                  <span >已购买16单</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="m-inviteStore-btn">立 即 邀 请</div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {},
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
.m-inviteStore{
  .m-inviteStore-img{
    display: block;
    width: 100%;
    height: 450px;
    background-color: #a3a3a3;
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
