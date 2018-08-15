<template>
  <div class="m-discover-announcement">
    <div class="m-section-one">
      <div class="m-section-content">

        <div class="m-section-title">
          <img class="m-section-img"/>
          <div>
            <span class="m-title">茉莉</span>
            <p class="m-fodder-time">昨天 13:54发布</p>
          </div>

        </div>

        <div class="m-section-text">
          <p><span class="m-mark">置顶</span>周周奖励发得完吗？不存在！</p>
          <p class="m-ft-30">新鲜出炉的周周奖现已发放，还不快去查收！</p>
          <img src="" class="m-img-l" alt="">
          <div class="m-section-bottom">
            <div>
              <div class="m-lookinfo-box">
                <span class="m-look-icon"></span>
                <span>1231</span>
                <span class="m-smile-icon"></span>
                <span>21231</span>
              </div>
            </div>
            <div>
              <icon-list></icon-list>
            </div>
          </div>

          <div class="m-comment-box">

            <div class="m-comment-content">
              <span class="m-comment-s"></span>
              <p><span class="m-comment-name">A玲珑服饰有限责任公司</span> : 感谢平台31个省市去均有店铺的
                库存</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script type="text/ecmascript-6">
  import iconList from'../../../components/common/iconList';
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {
          iconList
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  .m-discover-announcement{
    .m-section-one{
      padding: 30px 37px;
      display: flex;
      flex-flow: row;
      justify-content: flex-start;
      position: relative;
      border-bottom: 1px solid @borderColor;

      .m-section-img{
        width: 72px;
        height: 72px;
        border-radius: 10px;
        background-color: #666666;
        margin-right: 30px;
      }
      .m-section-content{
        width: 100%;
        .m-section-title{
          .flex-row(flex-start);
          line-height: 36px;
          text-align: left;
          .m-title{
            color: @blue;
            font-size: 26px;
          }
          .m-sale{
            color: #a4a4a4;
            font-size: 22px;
            margin-right: 40px;
          }
        }
        .m-fodder-time{
          color: @grey;
          text-align: left;
        }
        .m-section-text{
          text-align: left;
          font-size: 28px;
          .m-mark{
            display: inline-block;
            padding: 3px 10px;
            margin-right: 10px;
            text-align: center;
            background-color: @mainColor;
            color: #fff;
            border-radius: 10px;
            font-size: 20px;
          }
          p{
            text-indent: 0;
            margin: 10px 0;
          }
          .m-img-l{
            display: block;
            width: 182px;
            height: 400px;
            background-color: #666666;
            margin: 20px 0;
          }
          .m-section-bottom{
            margin: 10px 0;
            .flex-row(space-between);
            .m-lookinfo-box{
              color: @grey;
              font-size: 20px;
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
        }

        .m-comment-box{
          width: 100%;
          .m-comment-s{
            position: absolute;
            top: -30px;
            left: 30px;
            width: 0;
            height: 0;
            border-bottom: 15px solid #f0f0f0;
            border-top: 15px solid transparent;
            border-left: 15px solid transparent;
            border-right: 15px solid transparent;
            margin-left: 30px;

          }
          .m-comment-content{
            width: 100%;
            background-color: #f0f0f0;
            position: relative;
            padding: 20px 0;
            border-radius: 4px;
            p{
              margin: 12px;
              font-size: 20px;
              line-height: 26px;
              width: 90%;
              span.m-comment-name{
                color: #7499d7;
              }
            }
          }
        }
      }

    }
  }
</style>
