<template>
    <div @click="fansClick">邀请专属粉丝

    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {},
        methods: {
          fansClick(){
            this.$router.push('/fansManagement')
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>

</style>
