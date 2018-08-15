<template>
  <div class="m-discover-every">
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

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
              items: [{
                title: '你的名字',
                href: 'http://google.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }, {
                title: '我的名字',
                href: 'http://baidu.com',   url: 'http://www.baidu.com/img/bd_logo1.png'
              }]
            }
        },
        components: {},
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-discover-every{
    .m-swipe-box{
      margin-top: 30px;
      padding: 0 45px;
      border-radius: 10px;
      border: 1px solid @borderColor;
      .mint-swipe{
        width: 660px;
        height: 270px;
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
</style>
