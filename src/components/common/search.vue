<template>
  <div class="m-search" >
    <div class="m-search-text" v-if="search" @click="inputClick">
      <span class="m-search-icon" @click="inputClick"></span>
      <span @click="inputClick">搜索商品、品牌</span>
    </div>
    <div class="m-input" v-if="!search" >
      <input type="text" v-model="value" autofocus="!search" placeholder="" />
      <span @click.stop="searchClick">搜索</span>
    </div>

  </div>
</template>

<script>
    export default {
        name: "search",
      data(){
          return{
            value:''
          }
      },
      props:{
        search:{
          type:Boolean,
          default:true
        }
      },
      methods:{
        inputClick(e){
          e.preventDefault();
          this.$emit('inputClick')
        },
        searchClick(){
          this.$emit('searchClick',this.value)
        }
      }
    }
</script>

<style lang="less" rel="stylesheet/less">
  .m-search{
    /*width: 100%;*/
    padding: 0 18px;
    position: relative;
    height: 72px;
    input{
      width: 94%;
      height: 72px;
      line-height: 72px;
      font-size: 26px;
      border: none;
      background-color: #f1f1f1;
      border-radius: 10px;
      padding: 0 20px;
      &::-webkit-input-placeholder{
        text-align: center;
      }
    }
    .m-search-text{
      position: absolute;
      top:0;
      left: 28px;
      height: 72px;
      line-height: 72px;
      text-align: center;
      color: #a4a4a4;
      font-size: 26px;
      display: flex;
      flex-flow: row;
      align-items: center;
      justify-content: center;
      width: 94%;
      border: none;
      background-color: #f1f1f1;
      border-radius: 10px;
      .m-search-icon{
        display: inline-block;
        width: 34px;
        height: 34px;
        background: url("/static/images/icon-search.png") no-repeat;
        background-size: 100%;
        vertical-align: middle;
      }
    }
    .m-input{
      display: flex;
      flex-flow: row;
      justify-content: flex-start;
      align-items: center;
      input{
        width: 83%;
        margin-right: 10px;
      }
    }
  }
</style>
