<template>
  <ul class="m-icon-list">


    <li v-for="(item,index) in list" @click="iconClick(index)">
      <img :src="'/static/images/' + item.src +'.png'" class="m-icon" alt="">
      {{item.name}}
    </li>

  </ul>
</template>

<script>
    export default {
        data(){
          return{

          }
        },
      props:{
          list:{
            type:Array,
            default: [
                  {
                    src:'icon-like',
                    name:'1',
                    url:'icon-like'
                  },
                  {
                    src:'icon-lian',
                    name:'复制链接',
                    url:'icon-lian'
                  },
                  {
                    src:'icon-share',
                    name:'转发',
                    url:'icon-share'
                  }
                ]
          }
      },
      methods:{
        iconClick(v){
          this.$emit('iconClick',v)
        }
      }
    }
</script>

<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";
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
