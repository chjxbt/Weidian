<template>
    <div class="m-discover">
      <navbar></navbar>
      <div class="m-discover-content">
        <div class="m-swipe-box">
          <mt-swipe :auto="2000">
            <mt-swipe-item v-for="item in items" :key="item.id">
              <a :href="item.href" rel="external nofollow" >
                <img :src="item.url" class="img"/>
                <span class="desc"></span>
              </a>
            </mt-swipe-item>
          </mt-swipe>
          <div class="m-scroll">
            <ul class="m-img-list">
              <li>
                <img src="" class="m-img-list-img" alt="">
                <p><span class="m-price">￥169</span><span class="m-red">赚12</span></p>
              </li>
              <li>
                <img src="" class="m-img-list-img" alt="">
                <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
              </li>
              <li>
                <img src="" class="m-img-list-img" alt="">
                <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
              </li>
              <li>
                <img src="" class="m-img-list-img" alt="">
                <p><span class="m-price">￥69</span><span class="m-red">赚12</span></p>
              </li>
            </ul>
          </div>

        </div>
        <div class="m-item-one">
          <div class="m-title">
            <div>
              <img src="" class="m-item-title-img" alt="">
              <span>拉夏贝尔La Chapelle</span>
            </div>
            <div class="m-lookinfo-box">
              <span class="m-look-icon"></span>
              <span>1231</span>
              <span class="m-smile-icon"></span>
              <span>21231</span>
            </div>
          </div>
          <ul class="m-item-img-list">
            <li>
              <img src="" class="m-item-img m-item-img-l" alt="">
            </li>
            <li>
              <img src="" class="m-item-img" alt="">
            </li>
            <li>
              <img src="" class="m-item-img" alt="">
            </li>
            <li>
              <img src="" class="m-item-img" alt="">
            </li>
          </ul>
        </div>
      </div>


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
    export default {
        data() {
            return {
              show_modal:true,
              items: [{
                title: '你的名字',
                href: 'http://google.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }, {
                title: '我的名字',
                href: 'http://baidu.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }]
            }
        },
        components: {
          navbar
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
.m-discover{
  .m-discover-content{
    .m-swipe-box{
      margin-top: 30px;
      padding: 0 45px;
      border-radius: 10px;
      border: 1px solid @borderColor;
      .mint-swipe{
        width: 660px;
      }
      .m-scroll{
        min-height: 330px;
        .m-img-list {
          /*.flex-row(flex-start);*/
          margin: 10px 0;
          width: 100%;
          display: inline;
          white-space: nowrap;
          overflow-x: scroll;
          float: left;
          overflow-y: hidden;
          li {
            display: inline-block;
            /*width: 210px;*/
            margin-right: 4px;
            /*text-align: center;*/
            .m-img-list-img {
              display: block;
              width: 210px;
              height: 210px;
              background-color: #666;
              border-radius: 10px;
            }
            .m-price {
              color: #a4a4a4;
              margin-right: 10px;
            }
          }
        }
      }

    }
    .m-item-one{
      .m-title{
        .flex-row(space-between);
        border-bottom: 1px solid @borderColor;
        padding: 10px 45px;
        color: #a3a3a3;
        font-size: 20px;
        line-height: 36px;
        .m-item-title-img{
          display: inline-block;
          width: 34px;
          height: 34px;
          margin-right: 10px;
          border-radius: 10px;
          background-color: #666666;
          vertical-align:middle;
        }
        .m-lookinfo-box{
          .m-look-icon{
            display: inline-block;
            width: 25px;
            height: 34px;
            background: url("/static/images/icon-look.jpg")no-repeat center;
            background-size: 100%;
            vertical-align:middle;
          }
          .m-smile-icon{
            display: inline-block;
            width: 25px;
            height: 34px;
            background: url("/static/images/icon-smile.jpg")no-repeat center;
            background-size: 100%;
            margin-left: 20px;
            vertical-align:middle;
            &.active{
              background: url("/static/images/icon-smile-active.jpg")no-repeat center;
              background-size: 100%;
            }
          }
        }
      }
      .m-item-img-list{
        padding: 20px 45px ;
        .flex-row(flex-start);
        flex-wrap: wrap;
        .m-item-img{
          width: 210px;
          height: 210px;
          display: block;
          margin-right: 10px;
          background-color: #666666;
          border-radius: 10px;
          margin-bottom: 10px;
        }
        .m-item-img-l{
          width: 653px;
          height: 260px;
          display: block;
          margin-right: 10px;
          background-color: #666666;
          border-radius: 10px;
        }
      }
    }
  }

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
