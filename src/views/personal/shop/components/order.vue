<template>
  <ul class="m-part-list">
    <template v-for="(item,index) in list">
      <li @click="navClick(item)">
        <img :src="item.src" class="m-part-list-icon" />
        <span>{{item.name}} <span> ({{item.value}})</span></span>
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
            default:null
          }
        },
        methods: {
          navClick(v){
            if(v.url) {
              this.$router.push(v.url);
            }
          },
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>

</style>
