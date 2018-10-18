<template>
  <div class="order-table">
    <el-table :data="orderList" style="width: 100%" class="outside-table" :default-expand-all="expandAll" stripe size="small" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="30"></el-table-column>
      <el-table-column type="expand" width="30">
        <template slot-scope="scope">
          <el-table class="inside-table" :data="scope.row.productinfo" border style="width: 100%" size="small">
            <el-table-column align="center" prop="opiproductimages" label="商品图片" width="100">
              <template slot-scope="scope">
                <img :src="scope.row.opiproductimages" class="product-img">
              </template>
            </el-table-column>
            <el-table-column align="center" prop="opiproductname" label="商品名称"></el-table-column>
            <el-table-column align="center" prop="zh_status" label="订单商品状态" width="100"></el-table-column>
            <el-table-column align="center" prop="oiproductprice" label="单价"></el-table-column>
            <el-table-column align="center" prop="opiproductnum" label="数量"></el-table-column>
            <el-table-column align="center" prop="pskproperKey" label="规格"></el-table-column>
            <!--<el-table-column align="center" prop="opilogisticssn" label="物流单号"></el-table-column>-->
            <!--<el-table-column align="center" prop="logistic_company" label="物流公司"></el-table-column>-->
            <!--<el-table-column align="center" prop="opilogisticstext" label="物流信息"></el-table-column>-->
            <el-table-column fixed="right" label="管理" width="150">
              <template slot-scope="scope">
                <el-button class="color-text" type="text" size="small" @click="productSend(scope, 'product')" v-if="scope.row.opistatus == 0">发货</el-button>
                <el-button class="color-text" type="text" size="small" @click="productReturn(scope, 'dialog')">查看退款</el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column align="center" label="订单号" prop="oiid" width="260"></el-table-column>
      <el-table-column align="center" label="订单状态" prop="oipaystatusmsg" width="80"></el-table-column>
      <el-table-column align="center" label="总价" prop="oimount" width="80"></el-table-column>
      <el-table-column align="center" label="下单时间" prop="oicreatetime" width="140"></el-table-column>
      <el-table-column align="center" label="收货人" prop="oirecvname" width="140"></el-table-column>
      <el-table-column align="center" label="收货电话" prop="oirecvphone" width="110"></el-table-column>
      <el-table-column align="center" label="留言内容" prop="oileavetext"></el-table-column>
      <el-table-column fixed="right" label="管理" width="150">
        <template slot-scope="scope">
          <el-button class="color-text" type="text" size="small" @click="productSend(scope, 'order')">发货</el-button>
          <!--<el-button class="color-text" type="text" size="small" @click="productSend(scope, 'order')" v-if="scope.row.opistatus == 4">发货</el-button>-->
          <el-button class="color-text" type="text" size="small" @click="orderDetail(scope, 'dialog')">详情</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--商品发货-->
    <el-dialog title="商品发货" :visible.sync="productSendDialog" width="3.4rem">
      <div class="send-box">
        <div class="box-row">
          <div class="title-text">运单号：</div>
          <el-input class="search-input" v-model="logisticsNo" size="small" clearable></el-input>
        </div>
        <div class="box-row">
          <div class="title-text">物流公司：</div>
          <el-select v-model="logisticsCompany" clearable filterable placeholder="请选择物流公司" size="small" class="search-input">
            <el-option v-for="item in logisticsCompanyList" :key="item.expresskey" :label="item.expressname" :value="item.expresskey"></el-option>
          </el-select>
        </div>
        <div slot="footer" class="dialog-footer">
          <el-button class="at-img-dialog-btn" @click="dialogCancel">取 消</el-button>
          <el-button class="at-img-dialog-btn btn-color" type="primary"  @click="productSend()">确 定</el-button>
        </div>
      </div>
    </el-dialog>

    <!--商品退款-->
    <el-dialog title="商品退款" :visible.sync="productReturnDialog" width="5rem">
      <div class="return-box">
        <div class="dialog-title">订单编号： {{product.row.oisn}}</div>
      </div>
    </el-dialog>

    <!--订单详情-->
    <el-dialog title="订单详情" :visible.sync="orderDetailDialog" width="6rem">
      <div class="order-box">
        <div class="dialog-title">订单编号： {{}}</div>
      </div>
    </el-dialog>

    <div class="bottom-box">
      <div class="export-btn" @click="exportClick">批量导出</div>
      <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
    </div>
  </div>
</template>

<script>
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    name: "all-order-table",
    data() {
      return {
        expandAll: true,                // 表格是否默认展开行
        // orderLoading: true,          // 表格加载中
        statusnum: "",                  // 暂存订单状态
        orderOutList: [],               // 要导出的订单list
        orderDetailDialog: false,       // 订单详情的dialog
        productSendDialog: false,       // 商品发货的dialog
        productReturnDialog: false,     // 商品退款的dialog
        logisticsNo: "",                // 运单号
        logisticsCompany: "",           // 物流公司
        logisticsCompanyList: [],       // 物流公司list
        orderProduct: {},               // 暂存发货
        orderProductWhere: "",          // 暂存发货点击来源 - 订单/商品
        product: { row: { oisn: "" } }  // 暂存退款
      }
    },
    props:{
      orderList:{ type: Array, default: [] },
      total_page:{ type: Number, default: 1 },
    },
    components: { Pagination },
    methods: {
      // 详情按钮
      detailClick(){
        this.$emit('detailClick')
      },

      // 退款按钮
      returnClick(){
        this.$emit('returnClick')
      },

      // 表格多选事件
      handleSelectionChange(value) {
        this.orderOutList = value;
      },

      // 批量导出
      exportClick(){
        console.log(this.orderOutList);
      },

      // 订单详情
      orderDetail(scope, where) {
        this.orderDetailDialog = true;
      },

      // 商品发货取消按钮
      dialogCancel() {
        this.productSendDialog = false;
        this.logisticsNo = "";
        this.logisticsCompany = "";
      },
      // 商品发货
      productSend(scope, where) {
        if(where) {
          this.productSendDialog = true;
          this.orderProduct = scope;
          this.orderProductWhere = where;

          this.getCompanies();        // 获取快递公司list
        }else {
          // console.log(this.orderProduct);
          if(this.logisticsNo == "" || this.logisticsCompany == "") {
            this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
          }else {
            let params = { send_infos: [] };
            if(this.orderProductWhere == "product") {
              params = {send_infos: [
                { opiid: this.orderProduct.row.opiid, opilogisticssn: this.logisticsNo, kdcompany: this.logisticsCompany }
              ]};
            }else if(this.orderProductWhere == "order") {
              for(let i = 0; i < this.orderProduct.row.productinfo.length; i ++) {
                params.send_infos.push({ opiid: this.orderProduct.row.productinfo[i].opiid, opilogisticssn: this.logisticsNo, kdcompany: this.logisticsCompany })
              }
            }
            axios.post(api.send_order + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: "发货成功", type: 'success', duration: 1500 });

                // 发货成功后刷新视图
                this.logisticsNo = "";
                this.logisticsCompany = "";
                this.productSendDialog = false;
              }else{
                this.$message({ message: res.data.message, type: 'error', duration: 1500 });
              }
            });
          }
        }
      },

      // 商品退款
      productReturn(scope, where) {
        if(where) {
          this.productReturnDialog = true;
          this.product = scope;
        }else {
          console.log(this.product);
        }
      },

      // 分页组件的提示
      pageChange(v){
        this.$emit('pageChange', v)
      },

      // 获取快递公司list
      getCompanies() {
        axios.get(api.get_kd_list + "?kw=").then(res => {
          if(res.data.status == 200) {
            this.logisticsCompanyList = res.data.kd_list;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      }
    },
    mounted() {


    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .order-table {
    .outside-table {
      .inside-table {
        .product-img {
          width: 0.4rem;
          height: 0.4rem;
        }
      }
    }
  }
  .bottom-box {
    display: flex;
    justify-content: space-between;
    margin-top: 0.1rem;
    .page-box {

    }
    .export-btn {
      /*width: 0.5rem;*/
      height: 0.2rem;
      line-height: 0.2rem;
      font-size: 0.12rem;
      white-space: nowrap;
      align-items: center;
      text-align: center;
      padding: 0.03rem 0.15rem;
      border-radius: 0.05rem;
      color: #ffffff;
      background-color: #9fd0bf;
    }
  }
  .color-text {
    color: #91aeb5;
  }
  .send-box {
    .box-row {
      display: flex;
      padding: 0 0.5rem 0.1rem 0.3rem;
      .title-text {
        width: 0.8rem;
        line-height: 0.23rem;
        white-space: nowrap;
      }
      .search-input {
        width: 2rem;
      }
    }
  }
  .return-box {
    margin: -0.1rem 0 0.2rem 0;
  }
  .dialog-title {
    padding-left: 0.2rem;
    font-size: 0.12rem;
    height: 0.3rem;
    line-height: 0.3rem;
    color: #ffffff;
    background-color: #80a6b5;
  }
  .order-box {
  }
  .dialog-footer {
    text-align: right;
    margin: 0.2rem 0.2rem 0 0;
    .at-img-dialog-btn {
      padding: 0.05rem 0.1rem;
      font-size: 14px;
    }
    .btn-color {
      border-color: @btnActiveColor;
      background-color: @btnActiveColor;
    }
  }
</style>
