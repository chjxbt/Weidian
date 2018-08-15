<template>
  <div class="m-section-one">
    <img class="m-section-img"/>
    <div class="m-section-content">
      <div class="m-section-title">
        <span class="m-title">拉夏贝尔La Chapelle</span>
        <span class="m-sale">已售1981件</span>
      </div>
      <div class="m-section-text">
        <p>    7月9日上午9:00开播99款，本次活动2天。
          La Chapelle她崇尚精神性的外在表达，探索
          真实的美，作为一个快速发展的时尚品牌，全
          国31个省市均有店铺存在，</p>
        <span class="m-section-more">展开全文</span>
        <ul class="m-img-list">
          <li>
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
            <div>
              <span class="m-price-unit">￥</span>
              <span class="m-price">58.00</span>
              <span class="m-red m-ft-30">赚12</span>
            </div>
            <div class="m-red m-ft-22">距活动结束仅剩2天10小时</div>
          </div>
          <div>
            <icon-list></icon-list>
          </div>
        </div>
      </div>
    </div>
    <m-label></m-label>
  </div>
</template>

<script>
  import mLabel from '../../../components/common/mLabel';
  import iconList from '../../../components/common/iconList';
    export default {
      data(){
        return{

        }
      },
      components: {
        'm-label':mLabel,
        'icon-list':iconList
      },
    }
</script>

<style lang="less" rel="stylesheet/less" >
  @import '../../../common/css/index';
  .m-section-one{
    padding: 14px 27px;
    display: flex;
    flex-flow: row;
    justify-content: flex-start;
    position: relative;
    .m-section-img{
      width: 72px;
      height: 72px;
      border-radius: 10px;
      background-color: #666666;
      margin-right: 30px;
    }
    .m-section-content{
      width: 570px;
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
      .m-section-text{
        text-align: left;
        p{
          text-indent: 2em;
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
</style>
