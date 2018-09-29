<template>

    <mt-tabbar v-model="selected" :fixed="true">
      <template v-for="(item,index) in tabbar" >
        <mt-tab-item :id="item.name" @click="tabbarClick(item)">
          <img slot="icon" :src="item.active_icon" v-if="item.name == selected">
          <img slot="icon" :src="item.icon" v-else>
          {{item.name}}
        </mt-tab-item>
      </template>
    </mt-tabbar>


</template>

<script type="text/ecmascript-6">
  import common from '../../common/js/common';
    export default {
        data() {
            return {
                name: '',
              selected:this.$store.state.tabbar_select,
              tabbar:this.$store.state.tabbar
            }
        },
        components: {},
        methods: {
          tabbarClick(v){

          }
        },
      mounted(){

      },
      computed:{
        select(){
          return this.$store.state.tabbar_select
        }
      },
      watch: {
        selected: function (val, oldVal) {
          this.$store.state.tabbar_select = val;
          common.changeTitle(val);
          switch(val){
            case '首页':
              this.$router.push('/index');
              break;
            case '客服':
              this.$router.push('/service');
              break;
            case '发现':
              if(this.$route.path == '/discover/index'){

                } else{
                this.$router.push('/discover');
              }


              break;
            case '购物车':
              this.$router.push('/shopping');
              break;
            case '我的':
              this.$router.push('/personal');
              break;
          }
        },
        select: function (val) {
          console.log((val,'asdasda'))
          this.selected = this.$store.state.tabbar_select
        }
      },

      created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
</style>
