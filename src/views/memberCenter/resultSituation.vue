<template>
  <div>
    <navbar :list="nav_list" @navClick="navClick"></navbar>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  export default {
    name: "resultSituation",
    data(){
      return{
        nav_list: [
          { click: true, tnname: "全部(158人)" },
          { click: false, tnname: "已开单(68人)" },
          { click: false, tnname: "未开单(90人)" }
        ],
      }
    },
    components: { navbar },
    methods: {
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

</style>
