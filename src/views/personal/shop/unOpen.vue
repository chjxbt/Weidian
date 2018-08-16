<template>
    <div class="m-unOpen">
      <div class="m-shop-top">
        <div class="m-flex-between">
          <span>账号设置</span>
          <span>等级规则</span>
        </div>
        <div class="m-flex-start m-shop">
          <img src="" class="m-shop-top-img" alt="">
          <div class="m-shop-content">
            <h3>小居居</h3>
            <div>
              <p class="m-red">123123</p>
              <p>1123</p>
            </div>
          </div>
        </div>
      </div>
      <div class="m-order-box">
        <div class="m-part-one">
         <cell :item="part_title" ></cell>
          <ul class="m-part-list">
            <li>
              <span class="m-part-list-icon"></span>
              <span>待支付</span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>待发货</span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>已发货</span>
            </li>
            <li>
              <span class="m-part-list-icon"></span>
              <span>已取消</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="m-cell-box">
        <template v-for="(item,index) in cell_list">
          <cell :item="item" ></cell>
        </template>

      </div>
      <div class="m-short-bannar">

      </div>
      <div class="m-high-bannar">

      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import cell from '../../../components/common/cell';
    export default {
        data() {
            return {
                name: '',
              part_title:{
                name:'我的订单',
                value:'更多',
                url:''
              },
                cell_list:[
                  {
                    name:'收藏夹',
                    value:'',
                    url:''
                  },
                  {
                    name:'快速投诉通道',
                    value:'',
                    url:''
                  },
                  {
                    name:'关注公众号',
                    value:'',
                    url:''
                  }
                ]
            }
        },
        components: {
          cell
        },
        methods: {
          cellClick(v){

          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-unOpen{
    .m-shop-top{
      padding: 28px;
      color: #a4a4a4;
      font-size: 26px;
      .m-shop{
        padding: 28px;
        .m-shop-top-img{
          display: block;
          width: 200px;
          height: 200px;
          background-color: #a4a4a4;
          border-radius: 50%;
          margin-right: 30px;
          /*border: 20px solid #fff;*/
        }
        .m-shop-content{
          height: 200px;
          text-align: left;
          p{
            line-height: 32px;
            font-size: 24px;
          }
          h3{
            font-size: 40px;
            margin-bottom: 43px;
            margin-top: 20px;
            color: #000;
          }
        }
      }
    }
    .m-order-box{
      background-color: #f2f5f7;
      padding: 10px 0;

    }
    .m-cell-box{
      padding: 20px 0;
    }
    .m-high-bannar{
      width: 100%;
      height: 400px;
      background-color: #a4a4a4;

    }

  }

</style>
