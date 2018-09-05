<template>
  <div>
    <div class="nav-span">
    <span class="nav-span-box" v-for="(item, index) in sub">
      <span class="nav-span-text m-ft-20 tc" :class="index == subClick?'active':''" @click="changeSubClick(item, index)">{{item}}</span>
    </span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "differentDays",
    data(){
      return{
        sub: ["今天", "7天", "15天", "30天"],
        subClick: 0
      }
    },
    methods: {
      changeSubClick(item, index) {
        this.subClick = index;
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";

  .nav-span {
    .nav-span-box {
      width: 25%;
      float: left;
      padding: 27px 0;
      background-color: #f2f5f7;
      .flex-row(space-around);
      .nav-span-text {
        padding: 5px;
        width: 120px;
        border: 1px solid @borderColor;
        background-color: #fff;
        border-radius: 20px;
        &.active{
          color: @mainColor;
          border: 1px solid @mainColor;
        }
      }
    }
  }
</style>
