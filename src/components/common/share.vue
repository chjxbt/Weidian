<template>
  <div class="m-fixed" @click="fixedClick">
    <div class="m-fixed-state">
      <h3>转发到</h3>
      <ul class="m-share-list">
        <li v-if="num == 3" @click.stop="share">
          <img src="/static/images/icon-wei.png" class="m-share-icon" alt="">
          转发到微信好友
        </li>
        <li>
          <img src="/static/images/icon-peng.png" class="m-share-icon" alt="">
          转发到朋友圈
        </li>
        <li>
          <img src="/static/images/icon-link.png" class="m-share-icon" alt="">
          转发商品链接
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
    export default {
        name: "share",
      data(){
          return{

          }
      },
      props: {
          num: { type: Number, default: 3 }
      },
      methods:{
        fixedClick(){
          this.$emit('fixedClick')
        },
        share(){
          this.$emit('share')
        }
      },
      mounted() {
          // console.log(this.num)
      }
    }
</script>

<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";
  .m-fixed{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1001;
    .m-fixed-state{
      position: fixed;
      bottom: 0;
      left: 0;

      background-color: #fff;
      border-top: 1px solid @borderColor;
      border-top-left-radius: 20px;
      border-top-right-radius: 20px;
      box-shadow: 0 0 30px 0 rgba(66, 66, 66, 0.47);
      width: 100%;
      height: 288px;
      h3{
        font-size: 24px;
        color: #a4a4a4;
        margin: 20px 0 35px 30px;
      }
      ul.m-share-list{
        .flex-row(space-around);
        li{
          .flex-col(center);
          .m-share-icon{
            width: 97px;
            height: 97px;
            display: block;
            margin-bottom: 20px;
          }
        }
      }
    }

  }
</style>
