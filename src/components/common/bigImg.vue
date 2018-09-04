<template>
  <img :src="src + myClass" alt=""/>
</template>

<script>
  export default {
    name: "bigImg",
    props: {
      src: {}
    },
    data: () => ({
      myClass: ''
    }),
    mounted () {}
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>

</style>
