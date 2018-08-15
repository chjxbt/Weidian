<template>
  <div class="m-discover-fodder">
    <div class="m-filtrate-box">
      <span class="m-filtrate active">精选</span>
      <span class="m-filtrate">心灵鸡汤</span>
      <span class="m-filtrate">店主招募</span>
      <span class="m-filtrate">新手必发</span>
    </div>
    <div class="m-discover-fodder-content">
      <div class="m-section-one">
        <img class="m-section-img"/>
        <div class="m-section-content">
          <div class="m-section-title">
            <span class="m-title">茉莉</span>
          </div>
          <p class="m-fodder-time">昨天 13:54发布</p>
          <div class="m-section-text">
            <p>7月9日上午9:00开播99款，本次活动2天。</p>
            <ul class="m-img-list">
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li> <li>
              <img src="" class="m-section-text-img" alt="">
            </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
              <li>
                <img src="" class="m-section-text-img" alt="">
              </li>
            </ul>
            <div class="m-section-bottom">
              <div>
                <div>805人已发圈</div>
              </div>
              <div>
                <icon-list></icon-list>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script type="text/ecmascript-6">
  import iconList from '../../../components/common/iconList';
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {
          'icon-list':iconList
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../../common/css/index";
  .m-discover-fodder{
    .m-filtrate-box{
      width: 100%;
      padding: 30px 0;
      background-color: #f1f1f1;
      .flex-row(space-around);
      .m-filtrate{
        display: block;
        width: 130px;
        height: 36px;
        text-align: center;
        line-height: 36px;
        border: 1px solid @borderColor;
        background-color: #fff;
        border-radius: 20px;
        font-size: 20px;
        &.active{
          border: 1px solid @mainColor;
          color: @mainColor;
        }
      }
    }
    .m-discover-fodder-content{
      .m-section-one{
        padding: 14px 27px;
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
          width: 85%;
          font-size: 28px;
          .m-section-title{
            .flex-row(space-between);
            line-height: 36px;
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
            margin: 10px 0;
          }
          .m-section-text{
            text-align: left;
            p{
              text-indent: 0;
              margin: 10px 0;
            }
            .m-section-more{
              color: @blue;
              font-size: 20px;
            }
            .m-img-list{
              .flex-row(flex-start);
              flex-wrap: wrap;
              .m-section-text-img{
                display: block;
                width: 180px;
                height: 180px;
                margin-right: 10px;
                margin-top: 10px;
                background-color: #666666;
                &:nth-child(3n){
                  margin-right: 0;
                }
              }
            }
            .m-section-bottom{
              margin: 10px 0;
              .flex-row(space-between);
              .m-price-unit{
                font-size: 22px;
              }
              .m-price{
                font-size: 32px;
              }

            }
          }
        }

      }
    }
  }
</style>
