<template>
  <div class="m-cell" @click="cellClick(item)">
    <span class="m-cell-name" v-if="item.name">{{item.name}}</span>
    <span class="m-cell-nav" v-if="item.nav">
      <template v-for="(i,j) in item.nav">
              <span :class="i.click?'active':''" @click.stop="cellNav(j)">{{i.name}}</span>
      </template>

    </span>
    <span>
      <span v-if="item.value">{{item.value}}</span>

      <span class="m-cell-icon"></span>
    </span>
  </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        props:{
          item:{
            type:Object,
            default:null
          }
        },
        methods: {
          cellClick(v){
            if (v.url){
              this.$router.push('/'+v.url)
            }
          },
          cellNav(v){
            this.$emit('cellNav',v)
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";
  .m-cell{
    .flex-row(space-between);
    color: @grey;
    padding: 20px 32px;
    border-bottom: 1px solid @borderColor;
    .m-cell-nav{
      span{
        display: inline-block;
        padding: 0 20px;
        &.active{
          color: #666;
        }
      }
    }
    .m-cell-name{
      color: #666;
    }
    .m-cell-icon{
      display: inline-block;
      width: 26px;
      height: 26px;
      vertical-align: text-top;
      background: url("/static/images/icon-more.png") no-repeat right ;
      margin-left: 20px;
    }
  }
</style>
