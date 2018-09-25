<template>
  <div class="m-picker-status" v-if="show_picker">
    <div class="m-picker-box" >
      <p class="m-picker-text">
        <span class="cancel" @click="cancelSave(false)">取消</span>
        <span class="m-picker-btn" @click="pickerSave(false)">确定</span>
      </p>
      <mt-picker :slots="slots"  @change="onValuesChange"></mt-picker>
    </div>
  </div>
</template>

<script>
    export default {
        data(){
          return {
            select:''
          }
        },
      props:{
          slots:{
            type:Array,
            default:null
          },
          show_picker:{
              type:Boolean,
            default:false
          },
        params:{
            type:String,
            default:''
        }
      },
      methods:{
        onValuesChange(picker, values) {
          this.select= values;
        },
        pickerSave(v){
          this.$emit('pickerSave',v,this.select,this.params);
        },
        cancelSave(v){
          this.$emit('pickerSave',v);
        }
      }
    }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  .m-picker-status{
    position: fixed;
    top: 0;
    left:0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    .m-picker-box{
      position: fixed;
      bottom: 0;
      left: 0;
      height: 450px;
      width: 100%;
      background-color: #fff;
      text-align: right;
      .m-picker-text{
        display: flex;
        flex-flow: row;
        align-items: center;
        justify-content: space-between;
        font-size: 30px;
        padding: 10px;
        span.cancel{
          color: #a4a4a4;
        }
      }
  }

  }
</style>
