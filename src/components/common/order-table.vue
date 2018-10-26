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
            <el-table-column align="center" prop="zh_status" label="订单商品状态" width="130"></el-table-column>
            <el-table-column align="center" prop="oiproductprice" label="单价"></el-table-column>
            <el-table-column align="center" prop="opiproductnum" label="数量"></el-table-column>
            <el-table-column align="center" prop="smalltotal" label="小计"></el-table-column>
            <el-table-column align="center" prop="pskproperKey" label="规格"></el-table-column>
            <!--<el-table-column align="center" prop="opilogisticssn" label="物流单号"></el-table-column>-->
            <!--<el-table-column align="center" prop="logistic_company" label="物流公司"></el-table-column>-->
            <!--<el-table-column align="center" prop="opilogisticstext" label="物流信息"></el-table-column>-->
            <el-table-column fixed="right" label="管理" width="150">
              <template slot-scope="scope">
                <el-button class="color-text" type="text" size="small" @click="productSend(scope, 'product')" v-if="scope.row.opistatus == 0">发货</el-button>
                <el-button class="color-text" type="text" size="small" @click="productReturn(scope, 'dialog')">退换货</el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column align="center" label="订单号" prop="oisn" width="220"></el-table-column>
      <el-table-column align="center" label="订单状态" prop="oipaystatusmsg" width="80"></el-table-column>
      <el-table-column align="center" label="总价" prop="oimount" width="80"></el-table-column>
      <el-table-column align="center" label="下单时间" prop="oicreatetime" width="140"></el-table-column>
      <el-table-column align="center" label="收货人" prop="oirecvname" width="140"></el-table-column>
      <el-table-column align="center" label="收货电话" prop="oirecvphone" width="120"></el-table-column>
      <el-table-column align="center" label="留言内容" prop="oileavetext"></el-table-column>
      <el-table-column fixed="right" label="管理" width="150">
        <template slot-scope="scope">
          <el-button class="color-text" type="text" size="small" @click="productSend(scope, 'order')" v-if="scope.row.oipaystatus == 4">发货</el-button>
          <el-button class="color-text" type="text" size="small" @click="cancelOrder(scope)" v-if="scope.row.oipaystatus == 1">取消</el-button>
          <el-button class="color-text" type="text" size="small" @click="deleteOrder(scope)" v-if="scope.row.oipaystatus == 1 || scope.row.oipaystatus == 6">删除</el-button>
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
          <el-button class="at-img-dialog-btn btn-color" type="primary" @click="productSend()">确 定</el-button>
        </div>
      </div>
    </el-dialog>

    <!--商品退换货再次发货-->
    <el-dialog title="商品发货" :visible.sync="againSendDialog" width="5rem">
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
        <div class="box-row">
          <div class="title-text">收货人：</div>
          <el-input class="search-input" v-model="consignee" size="small" clearable></el-input>
        </div>
        <div class="box-row">
          <div class="title-text">手机号：</div>
          <el-input class="search-input" v-model="telephone" size="small" clearable></el-input>
        </div>
        <div class="box-row">
          <div class="title-text">收货地址：</div>
          <el-input class="search-input" v-model="address" size="small" style="width: 3.2rem" clearable></el-input>
        </div>
        <div slot="footer" class="dialog-footer">
          <el-button class="at-img-dialog-btn" @click="dialogCancel">取 消</el-button>
          <el-button class="at-img-dialog-btn btn-color" type="primary" @click="againSend('save')">确 定</el-button>
        </div>
      </div>
    </el-dialog>

    <!--商品退款-->
    <el-dialog title="商品退换货" :visible.sync="productReturnDialog" width="5rem">
      <div class="return-box">
        <div class="dialog-title">订单编号： {{product.row.oisn}}</div>
        <div class="return-detail" v-if="product.row.resend">
          <div class="detail-row">
            <div class="row-label">退款金额：</div>
            <div class="row-value">{{product.row.product_resend.oprmount}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">描述：</div>
            <div class="row-value">{{product.row.product_resend.oprdesc}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">理由：</div>
            <div class="row-value">{{product.row.product_resend.oprreason}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">收货人：</div>
            <div class="row-value">{{product.row.product_resend.oprreceivername}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">收货手机号：</div>
            <div class="row-value">{{product.row.product_resend.oprreceiverphone}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">快递公司：</div>
            <div class="row-value">{{product.row.product_resend.zh_logistic_compnay}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">收货地址：</div>
            <div class="row-value">{{product.row.product_resend.oprreceiveraddress}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">退换货类型：</div>
            <div class="row-value">{{product.row.product_resend.zh_OPRtype}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">退换货进度：</div>
            <div class="row-value">{{product.row.product_resend.zh_OPRschedule}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">申请时间：</div>
            <div class="row-value">{{product.row.product_resend.oprcreatetime}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label">买家发货时间：</div>
            <div class="row-value">{{product.row.product_resend.oprresendlogistictime}}</div>
          </div>
          <div class="detail-row">
            <div class="row-label" style="padding: 0.15rem 0 0.2rem 0">申请凭证：</div>
            <div class="row-value">
              <img class="return-img" v-for="item in product.row.product_resend.oprimage" :src="item">
            </div>
          </div>
        </div>
        <div class="btn-box" v-if="product.row.resend">
          <div class="return-btn" v-if="product.row.product_resend.oprschedule == '0'" @click="returnStatus(1)">同意申请</div>
          <div class="return-btn" v-if="product.row.product_resend.oprschedule == '0'" @click="returnStatus(0)">拒绝申请</div>
          <div class="return-btn" v-if="product.row.product_resend.oprschedule == '2'" @click="solderConfirm">确认收货</div>
          <div class="return-btn" v-if="product.row.product_resend.oprschedule == '3'" @click="againSend('')">发 货</div>
        </div>
      </div>
    </el-dialog>

    <!--订单详情-->
    <el-dialog title="订单详情" :visible.sync="orderDetailDialog" width="9rem">
      <div class="order-box">
        <div class="detail-box">
          <div class="dialog-title">订单编号： {{order.oisn}}</div>
          <div class="box-row">
            <div class="row-label">订单总价：</div>
            <div class="row-value">{{order.oimount}} 元</div>
          </div>
          <div class="box-row">
            <div class="row-label">订单状态：</div>
            <div class="row-value">{{order.oipaystatusmsg}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">收货人：</div>
            <div class="row-value">{{order.oirecvname}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">收货电话：</div>
            <div class="row-value">{{order.oirecvphone}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">收货地址：</div>
            <div class="row-value">{{order.oiaddress}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">买家姓名：</div>
            <div class="row-value">{{order.user.usname}}</div>
          </div>
          <!--<div class="box-row">
            <div class="row-label">买家上级：</div>
            <div class="row-value">{{order.upper.usname}}</div>
          </div>-->
          <div class="box-row">
            <div class="row-label">留言：</div>
            <div class="row-value">{{order.oileavetext}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">下单时间：</div>
            <div class="row-value">{{order.oicreatetime}}</div>
          </div>
          <div class="box-row">
            <div class="row-label">支付时间：</div>
            <div class="row-value">{{order.oipaytime}}</div>
          </div>
        </div>
        <div class="detail-box">
          <!--<div class="dialog-title">订单编号： {{order.oisn}}</div>-->
          <div class="dialog-title">商品详情</div>
          <div class="product-box" v-for="product in order.productinfo">
            <div class="box-row">
              <div class="row-label">商品名称：</div>
              <div class="row-value">{{product.opiproductname}}</div>
            </div>
            <div class="box-row">
              <div class="row-label">订单商品状态：</div>
              <div class="row-value">{{product.zh_status}}</div>
            </div>
            <div class="box-row">
              <div class="row-label">商品单价：</div>
              <div class="row-value">{{product.oiproductprice}} 元</div>
            </div>
            <div class="box-row">
              <div class="row-label">商品数量：</div>
              <div class="row-value">{{product.opiproductnum}}</div>
            </div>
            <div class="box-row">
              <div class="row-label">价格小计：</div>
              <div class="row-value">{{product.smalltotal}} 元</div>
            </div>
            <div class="box-row">
              <div class="row-label">商品规格：</div>
              <div class="row-value">{{product.pskproperKey}}</div>
            </div>
          </div>
        </div>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button class="at-img-dialog-btn" @click="orderDetailDialog=false">取 消</el-button>
        <el-button class="at-img-dialog-btn btn-color" type="primary"  @click="orderDetailDialog=false">确 定</el-button>
      </div>
    </el-dialog>

    <div class="bottom-box">
      <!--<div class="export-btn" @click="exportClick">批量导出</div>-->
      <Pagination class="page-box" :total="total_page" @pageChange="pageChange" @changeNum="changeNum"></Pagination>
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
        expandAll: true,               // 表格是否默认展开行
        // orderLoading: true,          // 表格加载中
        statusnum: "",                  // 暂存订单状态
        orderOutList: [],               // 要导出的订单list
        orderDetailDialog: false,       // 订单详情的dialog
        productSendDialog: false,       // 商品发货的dialog
        productReturnDialog: false,     // 商品退款的dialog
        logisticsNo: "",                // 运单号
        logisticsCompany: "",           // 物流公司
        logisticsCompanyList: [],       // 物流公司list
        order: { user: { usname: "" } },                      // 暂存订单详情
        orderProduct: {},               // 暂存发货
        orderProductWhere: "",          // 暂存发货点击来源 - 订单/商品
        product: { row: { oisn: "" } }, // 暂存退款
        sendAgain: false,               // 是否是再次发货
        againSendDialog: false,         // 再次发货dialog
        consignee: "",                  // 收货人
        telephone: "",                  // 手机号
        address: "",                    // 收货地址
      }
    },
    props:{
      orderList:{ type: Array, default: [] },
      total_page:{ type: Number, default: 1 },
    },
    components: { Pagination },
    methods: {
      // 表格多选事件
      handleSelectionChange(value) {
        this.orderOutList = value;
      },
      // 批量导出
      exportClick(){
        console.log(this.orderOutList);
      },
      // 取消订单
      cancelOrder(scope) {
        this.$confirm("此操作将取消该订单，是否继续?", '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          this.order = scope.row;
          let params = { oiid: scope.row.oiid };
          axios.post(api.cancle_order + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.orderList.splice(scope.$index, 1);
              this.changeNum();       // 更新各状态订单的数量
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }).catch(() => {  });
      },
      // 删除订单
      deleteOrder(scope) {
        this.$confirm("此操作将删除该订单，是否继续?", '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          this.order = scope.row;
          let params = { oiid: scope.row.oiid };
          axios.post(api.delete_order + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.orderList.splice(scope.$index, 1);
              this.changeNum();       // 更新各状态订单的数量
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }).catch(() => {  });
      },
      // 订单详情
      orderDetail(scope, where) {
        this.orderDetailDialog = true;
        this.order = scope.row;

        console.log(scope.row.oipaystatus);
      },
      // 卖家确认收货(订单)
      solderConfirm() {
        let params = { opiid: this.product.row.opiid };
        axios.post(api.solder_confirm + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: res.data.message, type: 'success', duration: 1500 });
            this.product.row.product_resend.oprschedule = "3";
            this.product.row.product_resend.zh_OPRschedule = "卖家发货中";

            console.log(this.product.row.product_resend.oprschedule);
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 拒绝/同意退换货申请
      returnStatus(status) {
        let msg = "";
        let oprschedule = "";
        let zh_OPRschedule = "";
        let params = { opiid: this.product.row.opiid, agree: status };
        if(status == 1) {
          msg = "申请已同意";
          oprschedule = "1";
          zh_OPRschedule = "等待买家发货";
        }else if(status == 0) {
          msg = "申请已拒绝";
          oprschedule = "6";
          zh_OPRschedule = "拒绝申请";
        }
        axios.post(api.agree_refund + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: msg, type: 'success', duration: 1500 });
            this.product.row.product_resend.oprschedule = oprschedule;
            this.product.row.product_resend.zh_OPRschedule = zh_OPRschedule;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 商品发货取消按钮
      dialogCancel() {
        this.productSendDialog = false;
        this.againSendDialog = false;
        this.logisticsNo = "";
        this.logisticsCompany = "";
        this.consignee = "";
        this.telephone = "";
        this.address = "";
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
      // 商品退换货 - 再次发货
      againSend(where) {
        if(where) {
          let params = {
            opiid: this.product.row.opiid,
            opssendsn: this.logisticsNo,
            opssendlogisticcompany: this.logisticsCompany,
            opsreceivername: this.consignee,
            opsreceivephone: this.telephone,
            opsreceiveaddress: this.address
          };
          axios.post(api.solder_change_send + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "发货成功", type: 'success', duration: 1500 });

              // 发货成功后刷新视图
              this.againSendDialog = false;
              this.logisticsNo = "";
              this.logisticsCompany = "";

              this.product.row.product_resend.oprschedule = "4";
              this.product.row.product_resend.zh_OPRschedule = "卖家已发货";
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }else {
          this.getCompanies();        // 获取快递公司list

          this.consignee = this.product.row.oirecvname;
          this.telephone = this.product.row.oirecvphone;
          this.address = this.product.row.oiaddress;
          this.againSendDialog = true;
        }
      },
      // 商品退款
      productReturn(scope, where) {
        if(where) {
          this.productReturnDialog = true;
          this.product = scope;
          if(this.product.row.resend) {
            console.log(this.product.row);
          }
        }else {
          console.log(this.product.row);
        }
      },
      // 分页组件的提示
      pageChange(v) {
        this.$emit('pageChange', v);
      },
      // 更新各状态订单的数量
      changeNum() {
        this.$emit('changeNum');
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
    updated() {
      // 将订单中的收货信息写到每一个商品中
      for(let i = 0; i < this.orderList.length; i ++) {
        if(this.orderList[i].productinfo) {
          for(let j = 0; j < this.orderList[i].productinfo.length; j ++) {
            this.orderList[i].productinfo[j].oirecvname = this.orderList[i].oirecvname;
            this.orderList[i].productinfo[j].oirecvphone = this.orderList[i].oirecvphone;
            this.orderList[i].productinfo[j].oiaddress = this.orderList[i].oiaddress;
          }
        }
      }
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
      padding: 0 0.4rem 0.1rem 0.3rem;
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
    .return-detail {
      .detail-row {
        display: flex;
        font-size: 0.11rem;
        line-height: 0.23rem;
        text-align: center;
        align-items: center;
        .row-label {
          width: 30%;
          height: 0.23rem;
          background-color: #dbdcdc;
        }
        .row-value {
          width: 70%;
          min-height: 0.23rem;
          text-align: left;
          padding-left: 7%;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          background-color: #f1f1f1;
          .return-img {
            width: 0.5rem;
            height: 0.5rem;
          }
        }
      }
    }
    .btn-box {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      margin: 0.2rem 0 -0.2rem 0;
      .return-btn {
        padding: 0.03rem 0.1rem;
        margin-right: 0.1rem;
        border-radius: 0.05rem;
        color: #ffffff;
        background-color: #80a6b5;
      }
    }
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
    width: 90%;
    margin: -0.1rem auto;
    /*border: 1px red solid;*/
    display: flex;
    flex-wrap: wrap;
    .detail-box {
      width: 47.5%;
      overflow-y: auto;
      overflow-x: hidden;
      max-height: 4rem;
      &:first-child {
        margin-right: 5%;
      }
      .box-row {
        display: flex;
        font-size: 0.11rem;
        line-height: 0.23rem;
        text-align: center;
        align-items: center;
        &:last-child {
          .row-label {
            padding-bottom: 0.3rem;
          }
          .row-value {
            padding-bottom: 0.3rem;
          }
        }
        .row-label {
          width: 30%;
          height: 0.23rem;
          background-color: #dbdcdc;
        }
        .row-value {
          width: 70%;
          height: 0.23rem;
          text-align: left;
          padding-left: 7%;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          background-color: #f1f1f1;
        }
      }
    }
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
