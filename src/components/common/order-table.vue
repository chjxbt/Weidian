<template>
  <div class="order-table">
    <table class="m-table">
      <thead>
       <tr>
         <th width="300">商品</th>
         <th width="100">订单状态</th>
         <th width="100">实付金额</th>
         <th width="100">总佣金</th>
         <th width="100">收件人</th>
         <th width="150">收件人联系方式</th>
         <th width="100">管理</th>
       </tr>
      </thead>
    </table>
    <table class="m-table m-row-table">
      <thead>
      <tr>
        <th width="300">订单编号</th>
        <th width="100"></th>
        <th width="100"></th>
        <th width="100"></th>
        <th width="100"></th>
        <th width="150"></th>
        <th width="100"></th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="m-table-flex">
          <img src="" class="m-table-img" alt="">
          <span>产品名称</span>
        </td>
        <td>商品</td>
        <td>商品</td>
        <td>商品</td>
        <td>商品</td>
        <td>商品</td>
        <td>
          <span class="m-table-link">详情</span>
          <span class="m-table-link" @click="returnClick">退款</span>
        </td>
      </tr>
      </tbody>
    </table>
    <div class="page-button">
      <Pagination :total="total_page" @pageChange="pageChange"></Pagination>
    </div>


  </div>
</template>

<script>
  // 0: "已取消", 7: "未支付", 14: "支付中", 21: "已支付",28: "已发货", 35: "已收货", 42: "已完成", 49: "已评价", 56: "退款中"
  import Pagination from "../../components/common/page";
  import {Message} from 'element-ui';
  export default {
    props: ["order"],
    name: "all-order-table",
    data() {
      return {
        expandAll: false,
        orderList: [],
        total_page: 0,
        current_page: 1,
        OMstatus: '',
        tableData6: [{
          id: '12987122',
          name: '王小虎',
          amount1: '234',
          amount2: '3.2',
          amount3: 10
        }, {
          id: '12987123',
          name: '王小虎',
          amount1: '165',
          amount2: '4.43',
          amount3: 12
        }, {
          id: '12987124',
          name: '王小虎',
          amount1: '324',
          amount2: '1.9',
          amount3: 9
        }, {
          id: '12987125',
          name: '王小虎',
          amount1: '621',
          amount2: '2.2',
          amount3: 17
        }, {
          id: '12987126',
          name: '王小虎',
          amount1: '539',
          amount2: '4.1',
          amount3: 15
        }]
      }
    },
    components: { Pagination },
    methods: {
      returnClick(){
        this.$emit('returnClick')
      },
      // 接收数据并赋值给 this.orderList
      getOrderList(data) {
        this.orderList = data.OrderMains
        // console.log(this.orderList)
        this.total_page = Math.ceil(data.count / data.page_size);
      },
      // 分页组件的提示
      pageChange(v){
        if(v == this.current_page){
          this.$message({ message: '这已经是第' + v + '页数据了', type: 'warning', duration: 1500 });
          return false;
        }
        this.current_page = v;
        this.$emit('toPage', v)
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";

  .order-table {
    .out-table {
      font-size: 14px;
    }
    .page-button {
      margin-top: 0.3rem;
    }
    .m-table{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 0.2rem;
      tr{
        border: 1px solid @borderColor;
      }
      &.m-row-table{
        th{
          background-color: #eeeeef;
        }
      }
      th{
        background-color: #dbdcdc;
        font-weight: normal;
      }
      th,td{
        padding: 5px 0;
        text-align: center;
      }
      td{
        padding: 15px 0;
      }
      .m-table-flex{
        display: flex;
        flex-flow: row;
        align-items: center;
        justify-content: center;
        .m-table-img{
          display: block;
          width: 1.05rem;
          height: 1.05rem;
          border-radius: 5px;
          background-color: #eeeeee;
          margin-right: 0.3rem;
        }
      }
      .m-table-link{
        display: inline-block;
        border-left: 1px solid @green;
        color: @green;
        padding: 0 0.12rem;
        cursor: pointer;
        &:first-child{
          border-left: none;
        }
        &.active{
          color: #b4b4b5;
        }
      }
    }
  }

</style>
