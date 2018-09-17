<template>
  <div class="m-section-one">
    <img v-if="list.suuser.suheader" :src="list.suuser.suheader" class="m-section-img"/>
    <div class="m-section-content">
      <div class="m-section-title">
        <span class="m-title">{{list.suuser.suname}}</span>
        <span class="m-sale">已售{{list.soldnum}}件</span>
      </div>
      <div class="m-section-text">
        <p  class="textP" :class="!list.show_text ? 'active':''">  {{list.actext}}</p>
        <span class="m-section-more" v-if="list.show_text" @click="showMoreText(false)">展开全文</span>
        <span class="m-section-more" v-if="list.actext.length >92 && !list.show_text" @click="showMoreText(true)">收起全文</span>
        <ul class="m-img-list">
          <template v-for="(item,index) in list.media">
            <li>
              <img v-if="item.amimage" :src="item.amimage" class="m-section-text-imgs" alt="">
              <video v-if="item.amvideo" :src="item.amvideo"></video>
            </li>
          </template>
        </ul>
        <div class="m-section-bottom">
          <div>
            <div>
              <span class="m-price-unit">￥</span>
              <span class="m-price " v-if="list.product != null && list.product.prprice" >{{list.product.prprice}}</span>
              <span class="m-red m-ft-30" v-if="list.product != null && list.product.prsavemonty">赚{{list.product.prsavemonty}}</span>
            </div>
            <div class="m-red m-ft-22">距活动结束仅剩{{list.remaintime[0] || '0'}}天{{list.remaintime[1] || '0'}}小时<span v-if="list.remaintime[0] == 0">{{list.remaintime[2] || '0'}}分钟</span> </div>
          </div>
          <div>
            <!--<icon-list :list="list.icon" :index="index" @iconClick="iconClick"></icon-list>-->
            <ul class="m-icon-list">
              <li v-for="(item,index) in list.icon" @click="iconClick(index)">
                <img v-if="!item.alreadylike" :src="'/static/images/' + item.src +'.png'" class="m-icon" alt="">
                <img v-else  :src="'/static/images/' + item.src +'-active.png'" class="m-icon" alt="">
                {{item.name}}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <m-label :name="list.tags[0].atname" v-if="list.tags[0]"></m-label>
  </div>
</template>

<script>
  import mLabel from '../../../components/common/mLabel';
  import iconList from '../../../components/common/iconList';
  import wxapi from '../../../common/js/mixins';
    export default {
      mixins: [wxapi],
      data(){
        return{

        }
      },
      props:{
        list:{
          type:Object,
          default:null
        },
        index:{
          type:Number,
          default:null
        }
      },
      components: {
        'm-label':mLabel,
        'icon-list':iconList
      },
      mounted(){
        let that = this;
        window.setInterval(that.getDJS,1000)
      },
      methods:{
        iconClick(v){
          this.$emit('iconClick',v,this.index)
        },
        showMoreText(v){
          this.$emit('showMoreText',v,this.index)
        },
        getDJS(){
          if(!this.list.acendtime){
            return false;
          }
          let EndTime= new Date(this.list.acendtime.slice(0,4),this.list.acendtime.slice(4,6)-1,this.list.acendtime.slice(6,8),this.list.acendtime.slice(8,10),this.list.acendtime.slice(10,12),this.list.acendtime.slice(12));//初始化结束日期2016年12月31日23点59分59秒

          let NowTime = new Date();
          let t =EndTime.getTime() - NowTime.getTime();

          if(t>0){
            let d=Math.floor(t/1000/60/60/24);
            let h=Math.floor(t/1000/60/60%24);
            let m=Math.floor(t/1000/60%60);
            let arr = [].concat(this.list.remaintime);
            arr[0] = d;
            arr[1] = h;
            arr[2] = m;

            this.list.remaintime = [].concat(arr);
          }
        }
      }
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
          white-space: nowrap;
          color: #a4a4a4;
          font-size: 22px;
          margin-right: 40px;
        }
      }
      .m-section-text{
        text-align: left;
        .textP{
          text-indent: 2em;
          margin: 10px 0;
          height: 160px;
          line-height: 42px;
          overflow: hidden;
          clear: both;
          &.active{
            height: auto;
          }
        }
        .m-section-more{
          color: @blue;
          font-size: 20px;
        }
        .m-img-list{
          .flex-row(flex-start);
          flex-wrap: wrap;
          .m-section-text-imgs{
            display: block;
            width: 180px;
            height: 180px;
            margin-right: 10px;
            margin-top: 10px;
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
  .m-icon-list{
    .flex-row(flex-end);
    li{
      margin-left: 10px;
      .flex-col(center);
      font-size: 22px;
      .m-icon{
        display: block;
        width: 30px;
        height: 25px;
      }
    }
  }
</style>
