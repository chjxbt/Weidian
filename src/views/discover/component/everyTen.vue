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
  @import "../../../common/css/discover";
</style>
