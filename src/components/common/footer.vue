<template>

    <mt-tabbar v-model="selected" :fixed="true">
      <template v-for="(item,index) in tabbar" >
        <mt-tab-item :id="item.name" @click.stop="tabbarClick(item)">
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
        // console.log(this.$store.state.tabbar,'asdasdasd');
      },
      computed:{
        select(){
          return this.$store.state.tabbar_select
        },
        tabbars(){
          return this.$store.state.tabbar;
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
          this.selected = this.$store.state.tabbar_select
        },
        $route: {
          handler: function(val, oldVal){
            switch (val.name){
              case 'index':
                this.selected = '首页';
                common.changeTitle('首页');
                break;
              case 'discover':
                this.selected = '发现';
                common.changeTitle('发现');
                break;
              case 'service':
                this.selected = '客服';
                common.changeTitle('客服');
                break;
              case 'shopping':
                this.selected = '购物车';
                common.changeTitle('购物车');
                break;
              case 'personal':
                this.selected = '我的';
                common.changeTitle('我的');
                break;

            }
          },
          // 深度观察监听
          deep: true
        },
        tabbars:function () {
          this.tabbar =this.$store.state.tabbar;
        }
      },

      created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
</style>
