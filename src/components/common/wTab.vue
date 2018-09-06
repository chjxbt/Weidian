<template>
  <ul class="m-weidian-tabbox m-no-margin">
    <template v-for="(item,index) in list">
      <li>
        <span class="m-tab-name" :class="item.active ? 'active':''" @click="wTabClick(index)">{{item.name}}</span>
        <span class="m-tab-line" v-if="index < list.length -1">/</span>
      </li>
    </template>

  </ul>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        props:{
          list:{
            type:Array,
            default: [],
          }
        },
        methods: {
          wTabClick(i){
            if(this.list[i].active){
              return false;
            }
            this.$emit('wTabClick',i)
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" >
@import "../../common/css/weidian";
</style>
