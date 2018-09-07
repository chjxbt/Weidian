<template>
  <div class="all-order">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="all-order-content">
      <div class="all-order-search">
        <div class="order-search">
          <div class="search-text-input">
            <div class="search-text">订单类型：</div>
            <el-input v-model="OMidSearch" size="mini" placeholder="请输入订单类型" clearable></el-input>
          </div>
          <div class="search-text-input" style="width: 48%">
            <div class="search-text">下单时间：</div>
            <div class="block">
              <el-date-picker v-model="OMtime" type="daterange" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"
                              :picker-options="pickerOptions2" size="mini" value-format="yyyy-MM-dd">
              </el-date-picker>
            </div>
          </div>
          <div class="search-text-input">
            <div class="search-text">物流方式：</div>
            <el-select v-model="OMlogisticsNameSearch" placeholder="请选择" size="mini" clearable>
              <div v-for="item in OMlogisticsNameList">
                <el-option :label="item" :value="item"></el-option>
              </div>
            </el-select>
          </div>
        </div>
        <div class="order-search">
          <div class="search-text-input">
            <div class="search-text">商品名称：</div>
            <el-input v-model="PRnameSearch" size="mini" placeholder="请输入商品名称" clearable></el-input>
          </div>
          <div class="search-text-input" style="width: 48%">
            <div class="search-text" >订单类型：</div>
            <el-input v-model="OMidSearch" size="mini" placeholder="请输入订单类型" clearable></el-input>
          </div>
          <div class="search-text-input">
            <div class="search-text" >订单类型：</div>
            <el-input v-model="OMidSearch" size="mini" placeholder="请输入订单类型" clearable></el-input>
          </div>
        </div>
        <div class="search-buttons">
          <el-button class="search-button" size="mini" @click="topSearch">搜索</el-button>
        </div>
      </div>
      <div class="all-order-tabs">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <div v-for="item in tabList">
            <el-tab-pane :label="item" :name="item.slice(0, 3)" :lazy="lazyStatus">
              <all-order-table ref="child" :order="order" @toPage="getData" @returnClick="returnClick"></all-order-table>
            </el-tab-pane>
          </div>
        </el-tabs>
      </div>
    </div>
    <div class="m-modal" v-if="show_return">
      <div class="m-modal-state">
        <div class="m-modal-head m-flex-end m-no-border">
          <span class="m-close" @click="changeModal('show_return')">x</span>
        </div>
        <div class="m-modal-content">
          <p class="m-order-no">订单编号：E256487897456161456</p>
          <table class="m-table">
            <thead>
            <tr>
              <th width="100">订单类型</th>
              <th width="100">申请退款</th>
              <th width="100">退款</th>
              <th width="150" class="m-grey">退货状态</th>
              <th width="150">换货状态</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>111</td>
              <td class="m-table-select">
                <el-select v-model="value" placeholder="请选择">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </td>
              <td>
                <span class="m-table-btn">退款</span>
              </td>
              <td class="m-grey">111</td>
              <td>111</td>
            </tr>
            </tbody>
          </table>
          <table class="m-table">
            <thead>
            <tr>
              <th width="350">备注</th>
              <th >货物状态</th>
              <th>订单状态</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>颜色发错发黑色颜色发错发黑色颜色发错发黑色</td>
              <td>
                <span class="m-table-btn active ">退款</span>
              </td>
              <td >111</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="m-modal" v-if="show_details">
      <div class="m-modal-state">
        <div class="m-modal-head m-flex-end m-no-border">
          <span class="m-close" @click="changeModal('show_details')">x</span>
        </div>

        <div class="m-modal-content ">
          <p>订单详情</p>
          <div class="m-detail-content">
            <div class="m-one-detail">
              <p class="m-order-no">订单编号：E256487897456161456</p>
              <table class="m-detail-table">
                <tr>
                  <td width="170">商品名称</td>
                  <td >产品名称</td>
                </tr>
                <tr>
                  <td>买家会员名</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>新衣币抵扣金额</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>付款总金额</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>退款金额</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>级别总佣金</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>订单状态</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>买家备注</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>发货物流公司</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>发货物流单号</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>退换货类型</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>退回物流公司</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>退回物流单号</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>二次物流单号</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>供应商订单号</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>供应商编号</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>商家编码</td>
                  <td>小西几</td>
                </tr>

                <tr>
                  <td>收货人姓名</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>收货地址</td>
                  <td>杭州市萧山区宁围镇包神实际中心</td>
                </tr>
                <tr>
                  <td>联系电话</td>
                  <td>小西几</td>
                </tr>
                <tr>
                  <td>订单创建时间</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>订单付款时间</td>
                  <td>￥5.0</td>
                </tr>
                <tr>
                  <td>店主ID</td>
                  <td>小西几</td>
                </tr>
              </table>
              <div class="m-modal-btn">
                <span>导出</span>
              </div>
            </div>
            <div class="m-one-detail">
              <p class="m-order-no">订单编号：E256487897456161456</p>
              <table class="m-detail-table">
                <tr>
                  <td width="170">订单类型</td>
                  <td >订单类型</td>
                </tr>
                <tr class="m-grey">
                  <td>申请退款</td>
                  <td>同意</td>
                </tr>
                <tr>
                  <td>退款</td>
                  <td>发起中</td>
                </tr>
                <tr class="m-grey">
                  <td>退货状态</td>
                  <td>顺丰（25478951112）</td>
                </tr>
                <tr>
                  <td>换货状态</td>
                  <td>顺丰（25478951112）
                    顺丰（25478951112）</td>
                </tr>
                <tr>
                  <td>备注</td>
                  <td>颜色发错发黑色颜色发错发黑色颜色发错发黑色</td>
                </tr>
                <tr>
                  <td>货物状态</td>
                  <td>确认退货</td>
                </tr>
              </table>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import allOrderTable from '../../components/common/order-table';
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  import index from "../../router";
  export default {
    data() {
        return {
          name: '所有订单',
          activeName: '全 部',
          pickerOptions2: {
            shortcuts: [
              {
                text: '最近一周',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                  picker.$emit('pick', [start, end]);
                }
              },
              {
                text: '最近一个月',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                  picker.$emit('pick', [start, end]);
                }
              },
              {
                text: '最近三个月',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                  picker.$emit('pick', [start, end]);
                }
              }
            ]
          },
          OMtime: null,
          OMlogisticsNameSearch: '',
          OMlogisticsNameList: [],
          lazyStatus: false,
          PRnameSearch: '',
          OMidSearch: '',
          orderList: [],
          search: {},
          order: {},
          page_size: 10,
          OMstatus: '',
          OMstartTime: '',
          OMendTime: '',
          tabList: ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中'],
          index: 0,
          show_return:false,
          show_details:true,
          options: [{
            value: '选项1',
            label: '黄金糕'
          }, {
            value: '选项2',
            label: '双皮奶'
          }, {
            value: '选项3',
            label: '蚵仔煎'
          }, {
            value: '选项4',
            label: '龙须面'
          }, {
            value: '选项5',
            label: '北京烤鸭'
          }],
          value: ''
        }
    },
    components: { pageTitle, allOrderTable },
    methods: {
      returnClick(){
        this.show_return = true;
      },
      changeModal(v){
        this[v] = false;
      },
      // 页面刷新
      freshClick(){
        console.log('fresh');
      },
      // 获取点击tab的label
      handleClick(tab) {
        // 判断要调用哪个子组件的方法
        if(tab.index == 9) {
          this.index = 0
        }else {
          this.index = parseInt(tab.index) + 1
        }
        // 判断需要的订单状态
        if(tab.name == '全 部') {
          this.OMstatus = ''
        }else {
          this.OMstatus = tab.name
        }
        // this.tabList = ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中']
        // tab.label含"0"则不调用接口
        if(tab.label.indexOf("0") == -1) {
          this.getData(1)
        }
      },
      // 获取订单数据
      getData(v){
        let params = {
          token: localStorage.getItem('token'),
          OMstatus: this.OMstatus,
          page_num: v,
          page_size: this.page_size,
          OMid: '',
          OMlogisticsName: '',
          PRname: '',
          OMstartTime: '',
          OMendTime: ''
        }
        if(this.search != '') {
            params.OMid =  this.search.OMid
            params.OMlogisticsName =  this.search.OMlogisticsName
            params.PRname =  this.search.PRname
            params.OMstartTime = this.search.OMstartTime
            params.OMendTime =  this.search.OMendTime
        }
        axios.get(api.get_all_order,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.orderList = res.data.data.OrderMains;
            this.order = res.data.data
            // 仅在查询和点击“全部”Tab标签时，对tabList进行一次添加数量操作
            if(this.tabList[0].length == 3) {
              this.getTabs(this.order.OMcount)
            }
          }else{
            this.$message.error(res.data.message);
          }
        })
      },
      // 获取订单的各个状态及对应的数量，并添加到tabList中
      getTabs(OMcount) {
        let i = 0
        this.tabList[0] = this.tabList[0]+'('+this.orderList.length+')'
        for(let j=1;j<this.tabList.length;j++) {
          i = (j-1)*7
          this.tabList[j] = this.tabList[j]+'('+OMcount[i]+')'
        }
      },
      // 头部查询条件
      topSearch() {
        this.OMstatus = ''
        // 完善头部查询条件去除后获取数据的逻辑
        if(this.OMtime != null || this.PRnameSearch != '' || this.OMidSearch != '' || this.OMlogisticsNameSearch != '') {
          if(this.OMtime != null) {
            this.OMstartTime = this.OMtime[0]+' 00:00:00'
            this.OMendTime = this.OMtime[1]+' 23:59:59'
          }else if (this.OMtime == null) {
            this.OMstartTime = ''
            this.OMendTime = ''
          }
        }
        this.search = {
          OMid: this.OMidSearch,
          OMlogisticsName: this.OMlogisticsNameSearch,
          PRname: this.PRnameSearch,
          OMstartTime: this.OMstartTime,
          OMendTime: this.OMendTime
        }
        this.tabList = ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中']
        this.getData(1)
      },
      getOMlogisticsNameList() {
        axios.get(api.get_omfilter).then(res => {
          if(res.data.status == 200) {
            for(let i=0;i<res.data.data.length;i++) {
              if(res.data.data[i].key == "OMlogisticsName") {
                this.OMlogisticsNameList = res.data.data[i].value
              }
            }
          }else{
            this.$message.error(res.data.message);
          }
        })
      }
    },
    created() {
      this.getData(1)
      this.getOMlogisticsNameList()
    },
    watch: {
      // 依据order变化来传递对应的新的order给对应的this.index的子组件，并调用该子组件的getOrderList方法
      order(newValue, oldValue) {
        this.$refs.child[this.index].getOrderList(newValue)
      }
    }
  }
</script>
<style lang="less" rel="stylesheet/less">
  @import "../../common/css/_variate.less";
  @import "../../common/css/modal";
  .all-order {
    background-color: @bgMainColor;
    .all-order-content {
      background-color: @bgMainColor;
      .all-order-search {
        padding: 0.2rem 0;
        margin: 0.15rem 0.2rem 0 0.2rem;
        border-radius: 0.1rem;
        background-color: @borderColor;
        .order-search{
          display: flex;
          flex-flow: row;
          flex-wrap: wrap;
          align-items: center;
        }
        .search-buttons {
          /*margin-top: -0.3rem;*/
          display: flex;
          flex-flow: row;
          flex-wrap: wrap;
          align-items: center;
          justify-content: flex-end;
          margin-right: 0.4rem;
          .search-button {
            background-color: @btnActiveColor;
            color: @bgMainColor;
            font-size: 14px;
          }
          .el-button:active {
            color: @sectionBgColor;
            border-color: @sectionBgColor;
            outline: 0;
          }
        }
      }
      .all-order-tabs {
        width: 100%;
        background-color: @bgMainColor;
        .el-tabs {
          padding: 0.2rem;
        }
      }
    }
    .m-modal{
      .m-modal-state{
        width: 10rem;
        height: 92%;
        .m-no-border{
          border: none;
        }
        .m-modal-content{
          padding: 0 0.2rem 0.1rem;
          .m-order-no{
            background-color: #80a6b5;
            color: #fff;
            padding: 0.08rem 0.4rem;
          }
          .m-detail-content{
            display: flex;
            flex-flow: row;
            justify-content: space-between;
            margin-top: 0.1rem;
            .m-one-detail{
              width: 45%;
              .m-modal-btn{
                text-align: center;
                span{
                  display: inline-block;
                  width: 0.9rem;
                  height: 0.36rem;
                  line-height: 0.36rem;
                  background-color: #9fd0bf;
                  color: #fff;
                  border-radius: 5px;
                  cursor: pointer;
                }
              }
            }
            .m-detail-table{
              width: 100%;
              border-collapse: collapse;
              margin-bottom: 0.2rem;
              td{
                background-color: #f1f1f1;
                padding: 0.02rem 0;
              }
              tr{
                td:first-child{
                  background-color: #dbdcdc;
                  text-align: center;
                }
                td:last-child{
                  padding-left: 0.6rem;
                  padding-right: 0.4rem;
                }
              }
            }
          }
        }

      }
    }
  }
  .search-text-input {
    width: 26%;
    margin-bottom: 0.2rem;
    .search-text {
      float: left;
      margin-left: 0.2rem;
      line-height: 0.22rem;
      font-size: 14px;
    }
    .search-text-middle {
      font-size: 14px;
      line-height: 0.22rem;
      margin: 0 0.1rem 0 0.1rem;
    }
    .el-input {
      float: left;
      width: 1.6rem;
    }

  }
  .m-table{
    width: 100%;
    border-collapse: collapse;
    margin: 0.2rem 0;
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
      padding: 0.05rem 0;
      text-align: center;
    }
    td{
      padding: 0.1rem 0;
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
    .m-grey{
      color: #ababab;
    }
    .m-table-btn{
      display: inline-block;
     padding: 0 0.2rem;
      height: 0.27rem;
      line-height: 0.27rem;
      background-color: #80a6b5;
      color: #fff;
      border-radius: 10px;
      font-size: 14px;
      &.active{
        background-color: #dbdcdc;
        color: #b4b4b5;
      }
    }
  }
</style>
