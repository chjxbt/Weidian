<template>
  <div>
    <div class="m-navbar" >
      <ul class="ul-four">
        <li v-for="(item,index) in list" :class="item.click?'active':''" @click="navClick(index)">
          <span class="m-navbar-text">{{item.tnname}}</span>
          <span class="m-dot" v-if="item.dot"></span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import common from '../../common/js/common';
    export default {
      name: "navbar",
      data(){
        return{

        }
      },
      props:{
        list:{ type:Array, default:null }
      },
      methods:{
        navClick(v){
          if(this.list[v].click){
            return false;
          }
          common.changeTitle(this.list[v].tnname);
          this.$emit('navClick',v)
        }
      },
      mounted() {

      }
    }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  .m-navbar{
    margin-top: 10px;
    padding: 0 18px;
    border-bottom: 1px solid @borderColor;
    .ul-four{
      display: flex;
      flex-flow: row;
      align-items: center;
      font-size: 32px;
      white-space: nowrap;
      justify-content: space-around;
      li{
        padding: 10px 0;
        /*width: 25%;*/
        position: relative;
        span.m-navbar-text{
          padding: 10px 20px;
          font-weight: 600;
        }
        &.active{
          span.m-navbar-text{
            color: @mainColor;
            border-bottom: 3px solid @mainColor;
          }
        }
        .m-dot{
          position: absolute;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background-color: @mainColor;
        }
      }
    }


  }
</style>
