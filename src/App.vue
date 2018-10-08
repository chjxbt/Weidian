<template>
  <div id="app">
    <!--<span class="m-return" @click.stop="returnClick">返回</span>-->
    <router-view/>
  </div>
</template>

<script>
  import common from './common/js/common'
export default {

  name: 'App',
  methods:{
    returnClick(){
      this.$router.go(-1);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;

}
.m-return{
  position: fixed;
  left: 10px;
  top: 10px;
  width: 80px;
  height: 40px;
  line-height: 44px;
  border-radius: 15px;
  background-color: rgba(0,0,0,0.2);
  color: #f7f7f7;
  z-index: 10000;
}
</style>
