<template>
    <div class="m-service">
      <img :src="img_src" class="m-service-img" alt="">
    </div>

</template>

<script type="text/ecmascript-6">
  import axios from 'axios';
  import api from '../../api/api';
  import {Toast} from 'mint-ui';

    export default {
        data() {
            return {
                img_src:''
            }
        },
        components: {},
      mounted(){
          this.getRule(12)
      },
        methods: {
          getRule(type){
            axios.get(api.get_image_by_aitype,{
              params:{
                token:localStorage.getItem('token'),
                aitype:type
              }
            }).then(res => {
              if(res.data.status == 200){
                this.img_src = res.data.data.aiimage;
              }else{
                Toast({ message: res.data.message, className: 'm-toast-fail' });
              }
            },error => {
              Toast({ message: error.data.message, className: 'm-toast-fail' });            })
          },
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
.m-service{
  .m-service-img{
    width: 100%;
    height: 100%;
  }
}
</style>
