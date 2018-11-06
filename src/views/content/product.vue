<template>
  <div class="m-weidians">
    <page-title :title="name"></page-title>
    <div class="m-weidian-contents">
      <div class="search-box">
        <div class="search-group">
          <div class="group-title">关键词：</div>
          <el-input class="search-input" v-model="keyword" placeholder="运营ID/单品名称/商家编码" size="mini"></el-input>
        </div>
        <div class="search-group">
          <div class="group-title">创建时间：</div>
          <el-date-picker v-model="createTime" type="datetimerange" start-placeholder="开始日期" range-separator="至"
                          end-placeholder="结束日期" value-format="yyyy-MM-dd HH:mm:ss" style="width: 3.2rem;" size="mini">
          </el-date-picker>
        </div>
        <div class="search-btn cancel-btn" @click="cancelSearch">取 消</div>
        <div class="search-btn" @click="searchProduct">搜 索</div>
      </div>

      <div class="content-table">
        <el-table :data="productList" border stripe style="width: 100%" v-loading="productLoading">
          <el-table-column prop="claimid" label="运营ID" width="160"></el-table-column>
          <el-table-column  prop="prtitle" label="单品名称" width="200"></el-table-column>
          <el-table-column prop="prmainpic" label="单品缩略图" width="100">
            <template slot-scope="scope">
              <img class="product-img" :src="scope.row.prmainpic">
            </template></el-table-column>
          <el-table-column prop="prTarget" label="所在模块" width="100">
            <template slot-scope="scope">
              <el-button class="blue-btn" type="text" size="small" @click="target(scope)">
                <div class="text-btn" v-for="item in scope.row.prTarget">{{item}}</div>
              </el-button>
            </template>
          </el-table-column>
          <el-table-column prop="prBaid" label="所在专题">
            <template slot-scope="scope">
              <el-button class="blue-btn" type="text" size="small" @click="baid(scope)">{{scope.row.prBaid}}</el-button>
            </template>
          </el-table-column>
          <el-table-column prop="zh_activitystatus" label="单品推文内容状态"></el-table-column>
          <el-table-column prop="productid" label="商家编码"></el-table-column>
          <el-table-column prop="" label="sku" width="80">
            <template slot-scope="scope">
              <el-button class="blue-btn" type="text" size="small" @click="sku(scope)">单品详情</el-button>
            </template>
          </el-table-column>
          <el-table-column prop="pv" label="pv"></el-table-column>
          <el-table-column prop="ortransform" label="转化" width="80"></el-table-column>
          <el-table-column prop="refundrate" label="退货率" width="80"></el-table-column>
          <el-table-column prop="prStatus" label="单品状态" width="80"></el-table-column>
          <el-table-column prop="isclaim" label="认领推文" width="80">
            <template slot-scope="scope">
              <el-button class="blue-btn" type="text" size="small" v-if="!scope.row.isclaim" :disabled="!scope.row.canclaim" @click="claimActivity(scope, '1')">认领</el-button>
              <el-button class="blue-btn" type="text" size="small" v-if="scope.row.isclaim" :disabled="!scope.row.canclaim" @click="claimActivity(scope, '0')">取消认领</el-button>
            </template>
          </el-table-column>
          <el-table-column prop="isbig" label="大礼包" width="70"></el-table-column>
          <el-table-column prop="prcreatetime" label="创建日期" width="100"></el-table-column>
          <el-table-column prop="" label="操作记录" width="80">
            <template slot-scope="scope">
              <el-button class="blue-btn" type="text" size="small" @click="searchRecord(scope, 1)">查看</el-button>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="管理" width="90">
            <template slot-scope="scope">
              <el-button type="text" size="small" v-if="scope.row.prstatus == '0'" @click="editProduct(scope, '1')">上架</el-button>
              <el-button type="text" size="small" v-if="scope.row.prstatus == '1'" @click="editProduct(scope, '0')">下架</el-button>
              <el-button type="text" size="small" @click="deleteProduct(scope)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
      </div>

      <!--单品所在模块-->
      <el-dialog title="单品所在模块" :visible.sync="targetDialog" width="6rem">
        <el-checkbox-group class="check-box-list" v-model="targetList" @change="checkBoxChange">
          <el-checkbox class="check-box" v-for="item in tabList" :key="item.tnname" :label="item.tnname"></el-checkbox>
        </el-checkbox-group>
        <el-radio class="radio-target" v-model="targetRadio" label="101" @change="radioChange">大礼包</el-radio>

        <div slot="footer" class="dialog-footer">
          <div class="dialog-text">注意：一个单品最多可同时存在于三个模块下，且模块与大礼包不共存</div>
          <el-button class="at-img-dialog-btn" @click="targetDialog = false">取消</el-button>
          <el-button class="at-img-dialog-btn btn-color" type="primary" @click="saveTarget">保存</el-button>
        </div>
      </el-dialog>

      <!--单品所属专题-->
      <el-dialog title="单品所属专题" :visible.sync="baidDialog" width="8rem">
        <div class="content-table" style="margin: -0.3rem 0 0 0">
          <el-table :data="baidList" stripe style="width: 100%" v-loading="baidLoading">
            <el-table-column prop="baid" label="专题ID" width="420">
              <template slot-scope="scope">
                <div v-if="scope.row.disabled == '0'">{{scope.row.baid}}</div>
                <el-select v-if="scope.row.disabled == '1' || scope.row.disabled == '2'" v-model="scope.row.baid" filterable placeholder="请选择专题" size="small" style="width: 2.8rem;">
                  <el-option v-for="item in baList" :key="item.baid" :label="item.baid" :value="item.baid"></el-option>
                </el-select>
              </template>
            </el-table-column>
            <!--<el-table-column prop="claimid" label="运营ID" width="290"></el-table-column>-->
            <el-table-column prop="clainname" label="运营名称"></el-table-column>
            <el-table-column prop="updatetime" label="操作时间"></el-table-column>
            <el-table-column fixed="right" label="管理" width="120">
              <template slot-scope="scope">
                <el-button type="text" size="small" @click="updateBa(scope, 3)" v-if="scope.row.disabled == '0'">编辑</el-button>
                <el-button type="text" size="small" @click="updateBa(scope, 0)" v-if="scope.row.disabled == '0'">删除</el-button>
                <el-button type="text" size="small" @click="updateBa(scope, 2)" v-if="scope.row.disabled == '1'">保存</el-button>
                <el-button type="text" size="small" @click="updateBa(scope, 1)" v-if="scope.row.disabled == '2'">添加</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div slot="footer" class="dialog-footer">
          <div class="dialog-text">注意：一个单品最多可同时存在于三个专题下</div>
          <el-button class="at-img-dialog-btn" @click="closeBaDialog">关闭</el-button>
          <el-button class="at-img-dialog-btn btn-color" type="primary" @click="addBaid" v-if="baidList.length < 3">添加绑定</el-button>
        </div>
      </el-dialog>

      <!--单品sku-->
      <el-dialog title="单品SKU" :visible.sync="skuDialog" width="8rem">
        <div class="content-table" style="margin: -0.3rem 0 0.1rem 0">
          <el-table :data="skuList" border stripe style="width: 100%" v-loading="skuLoading" :default-sort="{ prop: 'pskproperKey', order: 'ascending' }" height="400">
            <el-table-column prop="psskuid" label="SKUID" width="80"></el-table-column>
            <el-table-column prop="pskalias" label="SKU别名" width="100"></el-table-column>
            <el-table-column prop="pskpostfee" label="物流费" width="70"></el-table-column>
            <el-table-column prop="pskproductnum" label="库存" width="70"></el-table-column>
            <el-table-column prop="pskproperKey" label="SKU组合" sortable align="left" width="300"></el-table-column>
            <el-table-column prop="pskprice" label="售价" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.pskprice" v-if="scope.row.edit" placeholder="售价"></el-input>
                <div v-if="!scope.row.edit">{{scope.row.pskprice}}</div>
              </template>
            </el-table-column>
            <el-table-column prop="pskpurchase" label="进货价" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.pskpurchase" v-if="scope.row.edit" placeholder="售价"></el-input>
                <div v-if="!scope.row.edit">{{scope.row.pskpurchase}}</div>
              </template>
            </el-table-column>
            <el-table-column prop="pskprofict" label="利润" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.pskprofict" v-if="scope.row.edit" placeholder="售价"></el-input>
                <div v-if="!scope.row.edit">{{scope.row.pskprofict}}</div>
              </template>
            </el-table-column>
            <el-table-column fixed="right" label="管理" width="80">
              <template slot-scope="scope">
                <el-button type="text" size="small" v-if="!scope.row.edit" @click="updateSku(scope, 'edit')">编辑</el-button>
                <el-button type="text" size="small" v-if="scope.row.edit" @click="updateSku(scope, 'save')">保存</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-dialog>

      <!--单品操作记录-->
      <el-dialog title="单品操作记录" :visible.sync="recordDialog" width="8rem">
        <div class="content-table" style="margin: -0.3rem 0 0 0">
          <el-table :data="recordList" border style="width: 100%" v-loading="recordLoading">
            <el-table-column prop="poraction" label="操作内容"></el-table-column>
            <el-table-column prop="portarget" label="对应ID" width="290"></el-table-column>
            <el-table-column prop="suname" label="操作人"></el-table-column>
            <el-table-column prop="porcreatetime" label="操作时间"></el-table-column>
          </el-table>
          <Pagination class="page-box" :total="total_page" @pageChange="pageChangeR"></Pagination>
        </div>
      </el-dialog>

    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    name: "product",
    data() {
      return {
        name: '单品管理',
        isSearch: false,              // 是否正在搜索
        keyword: '',                  // 搜索关键词
        createTime: [],               // 创建时间
        productList: [],              // 单品管理的list
        productLoading: false,        // 单品管理表格加载中
        page_size: 4,                // 每页请求的数量
        page_num: 1,                  // 第几页
        total_page: 1,                // 总页数
        tabList: [],                  // 顶部所有导航list
        targetDialog: false,          // 所在模块的dialog
        targetList: [],               // 所在模块的list
        targetRadio: "",              // 为101是大礼包
        baidDialog: false,            // 所属专题的dialog
        baidList: [],                 // 所属专题的list
        baidLoading: false,           // 所属专题表格加载中
        baidValue: "",                // 选择的专题id
        baList: [],                   // 专题list
        skuDialog: false,             // 单品sku的dialog
        skuList: [],                  // 单品sku的list
        skuLoading: false,            // 单品sku的表格加载中
        recordDialog: false,         // 单品操作记录的dialog
        recordList: [],              // 单品操作记录的list
        recordLoading: false,        // 单品操作记录的表格加载中
        scope: { },                   // 暂存单品的scope
      }
    },
    components:{ pageTitle, Pagination },
    methods: {
      // 分页点击方法
      pageChange(v) {
        this.page_num = v;
        if(this.isSearch) {
          this.getProduct(this.page_num, 'search');      // 获取单品list
        }else {
          this.getProduct();      // 获取单品list
        }
      },
      // 单品操作记录分页点击方法
      pageChangeR(v) {
        this.searchRecord(this.scope, v);       // 查看单品操作记录
      },
      // 顶部查找单品的按钮
      searchProduct() {
        // console.log(this.keyword != "", this.createTime.length != 0);
        if(this.keyword != "" || this.createTime.length != 0) {
          this.isSearch = true;
          this.getProduct(1, 'search');      // 获取单品list
        }else {
          this.getProduct();      // 获取单品list
        }
      },
      // 顶部取消查找单品的按钮
      cancelSearch() {
        if(this.isSearch) {
          this.isSearch = false;
          this.keyword = "";
          this.createTime = [];
          this.getProduct(1, 'search');      // 获取单品list
        }
      },
      // 编辑单品所在的模块
      target(scope) {
        this.scope = scope;
        this.targetDialog = true;
        if(this.productList[scope.$index].prTarget[0] == "大礼包") {
          this.targetRadio = "101";
          this.targetList = [];
        }else {
          this.targetList = this.productList[scope.$index].prTarget;
          this.targetRadio = "";
        }
      },
      // CheckBox变化时
      checkBoxChange(v) {
        if(v.length != 0) {
          this.targetRadio = "";
        }
      },
      // radio变化时
      radioChange(v) {
        if(v == "101") {
          this.targetList = [];
        }
      },
      // 保存单品所绑定的模块
      saveTarget() {
        if(this.targetList.length > 3) {
          this.$message({ message: "一个单品最多可同时存在于三个模块下", type: 'warning' });
        }else {
          let prTarget = [];
          let params = { prid: this.scope.row.prid, prtarget: [] };
          if(this.targetRadio) {
            params.prtarget = [this.targetRadio];
            prTarget.push("大礼包");
          }else {
            for(let i = 0; i < this.targetList.length; i ++) {
              for(let j = 0; j < this.tabList.length; j ++) {
                if(this.targetList[i] == this.tabList[j].tnname) {
                  params.prtarget.push(this.tabList[j].tnid);
                  prTarget.push(this.tabList[j].tnname);
                }
              }
            }
          }
          // console.log(params);
          axios.post(api.update_p_p + "?token=" + localStorage.getItem("token"), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.targetDialog = false;
              this.productList[this.scope.$index].prTarget = prTarget;
              this.productList = this.productList.concat();
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }
      },
      // 编辑单品所绑定的专题
      baid(scope) {
        this.scope = scope;
        this.baidDialog = true;
        this.baidLoading = true;
        // 获取当前单品绑定的专题
        let params = { token: localStorage.getItem("token"), prid: scope.row.prid };
        axios.get(api.get_p_b, { params: params }).then(res => {
          if(res.data.status == 200) {
            // console.log(res.data.data);
            this.baidList = res.data.data;
            for(let i = 0; i < this.baidList.length; i ++) {
              this.baidList[i].disabled = "0";
            }
            this.baidLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });

        // 获取所有专题供添加专题绑定时选择
        axios.get(api.get_bigactivitys + "?token=" + localStorage.getItem("token")).then(res => {
          if(res.data.status == 200) {
            // console.log(res.data.data);
            this.baList = res.data.data;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 编辑或删除专题的绑定
      updateBa(scope, operate) {
        let params = { };
        if(operate == 0) {           // 删除专题的绑定
          this.$confirm("此操作将解除单品与该专题的绑定，是否继续?", '提示',
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            params = { pbid: scope.row.pbid, option: operate };
            axios.post(api.update_p_b + "?token=" + localStorage.getItem("token"), params).then(res=>{
              if(res.data.status == 200){
                this.baidList.splice(scope.$index, 1);
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              }else{
                this.$message({ message: res.data.message, type: 'error', duration: 1500 });
              }
            });
          }).catch(() => {  });
        }else if(operate == 1) {    // 添加专题绑定
          if(scope.row.baid == "") {
            this.$message({ message: "请选择专题再添加", type: 'warning', duration: 1500 });
          }else {
            params = { prid: this.scope.row.prid, baid: scope.row.baid, option: operate };
            axios.post(api.update_p_b + "?token=" + localStorage.getItem("token"), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.baidList[scope.$index].disabled = "0";
              }else{
                this.$message({ message: res.data.message, type: 'error', duration: 1500 });
              }
            });
          }
        }else if(operate == 2) {    // 保存编辑的专题绑定
          params = { pbid: scope.row.pbid, baid: scope.row.baid, option: operate };
          axios.post(api.update_p_b + "?token=" + localStorage.getItem("token"), params).then(res=>{
            if(res.data.status == 200){
              this.baidList[scope.$index].disabled = "0";
              this.baidList = this.baidList.concat();
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }else if(operate == 3) {    // 编辑专题按钮的点击事件
          scope.row.disabled = "1";
        }
      },
      // 编辑sku中的价格
      updateSku(scope, operate) {
        if(operate == "edit") {
          scope.row.edit = true;
          this.skuList = this.skuList.concat();
        }else if(operate == "save") {
          let params = {
            pskid: scope.row.pskid,
            pskprice: scope.row.pskprice,
            pskprofict: scope.row.pskprofict,
            pskpurchase: scope.row.pskpurchase
          };
          // console.log(params);
          axios.post(api.update_sku_price + "?token=" + localStorage.getItem("token"), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              scope.row.edit = false;
              this.skuList = this.skuList.concat();
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }
      },
      // 关闭绑定专题的dialog
      closeBaDialog() {
        this.baidDialog = false;
        this.productList[this.scope.$index].prBaid = this.baidList.length;
        this.productList = this.productList.concat();
      },
      // 添加专题按钮
      addBaid() {
        let index = this.baidList.length;
        this.baidList[index] = {};
        this.baidList[index].baid = "";
        this.baidList[index].disabled = "2";
        this.baidList = this.baidList.concat();
      },
      // 单品sku
      sku(scope) {
        // console.log(scope.row);
        this.skuDialog = true;
        this.skuLoading = true;
        let params = { token: localStorage.getItem("token"), prid: scope.row.prid };
        axios.get(api.get_one, { params: params }).then(res => {
          if(res.data.status == 200) {
            this.skuList = res.data.data.sku;

            for(let i = 0; i < this.skuList.length; i ++) {
              this.skuList[i].edit = false;
              this.skuList[i].pskproperKey = "";
              for(let j = 0; j < this.skuList[i].pskproperkey.length; j ++) {
                this.skuList[i].pskproperKey = this.skuList[i].pskproperKey + this.skuList[i].pskproperkey[j].key + "：" + this.skuList[i].pskproperkey[j].value;
                if(j < (this.skuList[i].pskproperkey.length - 1)) {
                  this.skuList[i].pskproperKey = this.skuList[i].pskproperkey[j].key + "：" + this.skuList[i].pskproperkey[j].value + "，";
                }
              }
            }
            this.skuLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 认领推文 - 取消认领
      claimActivity(scope, operate) {
        if(scope.row.canclaim) {
          let msg = "";
          let claim = "";
          if (operate == "1") {
            msg = "认领";
            claim = operate;
          } else if (operate == "0") {
            msg = "取消认领";
            claim = operate;
          }
          this.$confirm("此操作将" + msg + "该单品对应的推文，是否继续?", '提示',
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            let params = {prid: scope.row.prid, claim: claim};
            axios.post(api.shelf_product_or_claim_act + '?token=' + localStorage.getItem('token'), params).then(res => {
              if (res.data.status == 200) {
                this.$message({message: res.data.message, type: 'success', duration: 1500});

                // 改变认领推文 - 取消认领后要改变相应字段
                if (operate == "1") {
                  scope.row.isclaim = true;
                  scope.row.claimid = res.data.data.claimid;
                } else if (operate == "0") {
                  scope.row.isclaim = false;
                  scope.row.claimid = "无";
                }
              } else {
                this.$message({message: res.data.message, type: 'error', duration: 1500});
              }
            });
          }).catch(() => {  });
        }else {
          this.$message({message: "当前用户不可执行该操作", type: 'warning', duration: 1500});
        }
      },
      // 查看单品操作记录
      searchRecord(scope, page_num) {
        this.scope = scope;
        this.recordDialog = true;
        let params = {
          token: localStorage.getItem("token"),
          prid: scope.row.prid,
          page_num: page_num,
          page_size: 10
        };
        axios.get(api.get_product_record, { params: params }).then(res => {
          if(res.data.status == 200) {
            this.recordList = res.data.data;
            this.total_page = Math.ceil(res.data.count / 10);
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 编辑单品状态 - 上下架
      editProduct(scope, operate) {
        let msg = "";
        let shelf = "";
        if(operate == "1") {
          msg = "上架";
          shelf = operate;
        }else if(operate == "0") {
          msg = "下架";
          shelf = operate;
        }
        this.$confirm("此操作将" + msg + "该单品，是否继续?", '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          let params = { prid: scope.row.prid, shelf: shelf };
          axios.post(api.shelf_product_or_claim_act + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });

              // 改变单品状态后要改变相应字段
              if(operate == "1") {
                scope.row.prstatus = "1";
                scope.row.prStatus = "正常";
              }else if(operate == "0") {
                scope.row.prstatus = "0";
                scope.row.prStatus = "已下架";
              }
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }).catch(() => {  });
      },
      // 删除单品
      deleteProduct(scope) {
        console.log(scope.row);
        this.$confirm("此操作将删除该单品，是否继续?", '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          let params = { prid: scope.row.prid, prdel: "1" };
          axios.post(api.shelf_product_or_claim_act + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.productList.splice(scope.$index, 1);
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }).catch(() => {  });
      },
      // 获取单品list
      getProduct(page_num, operate) {
        this.productLoading = true;
        let params = {
          token: localStorage.getItem('token'),
          page_num: page_num || this.page_num,
          page_size: this.page_size,
        };
        // 搜索的拼接
        if(operate) {
          if(this.keyword != "") {
            params.kw = this.keyword;
          }
          if(this.createTime.length != 0) {
            params.time_start = this.createTime[0];
            params.time_end = this.createTime[1];
          }
        }
        // console.log(params);
        axios.get(api.get_list, { params: params }).then(res => {
          if(res.data.status == 200) {
            this.productList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);

            // 获取所有导航栏
            axios.get(api.get_all_topnav, { params: params }).then(res => {
              if(res.data.status == 200) {
                this.tabList = [];
                for(let i = 0; i < res.data.data.length; i ++) {
                  if(res.data.data[i].tnname == "素材圈") {
                    for(let j = 0; j < res.data.data[i].sub.length; j ++) {
                      this.tabList.push(res.data.data[i].sub[j]);
                    }
                  }else {
                    this.tabList.push(res.data.data[i]);
                  }
                }

                // 判断一些参数
                for(let i = 0; i < this.productList.length; i ++) {
                  // 所在模块
                  this.productList[i].prTarget = [];
                  if(this.productList[i].prtarget.length == 0) {
                    this.productList[i].prTarget = ["无"];
                  }
                  for(let j = 0; j < this.productList[i].prtarget.length; j ++) {

                    // 将拿到的tnid与tabList进行比对，获取汉字
                    for(let k = 0; k < this.tabList.length; k ++) {
                      if(this.productList[i].prtarget[j] == this.tabList[k].tnid) {
                        this.productList[i].prtarget[j] = this.tabList[k].tnname;
                      }
                      if(this.productList[i].prtarget[j] == "101") {
                        this.productList[i].prtarget[j] = "大礼包";
                      }
                    }
                    // 拼接所有模块
                    this.productList[i].prTarget.push(this.productList[i].prtarget[j])
                  }

                  // 所在专题id的条数
                  this.productList[i].prBaid = this.productList[i].prbaid.length;

                  // 如果还没有认领该单品推文，则运营id显示无
                  if(!this.productList[i].isclaim) {
                    this.productList[i].claimid = "无";
                  }
                  // 如果还没有认领该单品推文，则运营id显示无
                  if(this.productList[i].isbig) {
                    this.productList[i].isbig = "是";
                  }else if(!this.productList[i].isbig) {
                    this.productList[i].isbig = "否";
                  }
                  // 单品状态   0 下架, 1 正常, 2 禁用
                  if(this.productList[i].prstatus == "0") {
                    this.productList[i].prStatus = "已下架";
                  }else if(this.productList[i].prstatus == "1") {
                    this.productList[i].prStatus = "正常";
                  }else if(this.productList[i].prstatus == "2") {
                    this.productList[i].prStatus = "禁用中";
                  }
                }
                // 数据刷新，刷新视图
                this.productList = this.productList.concat();
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });

            this.productLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
    },
    mounted() {
      this.getProduct();      // 获取单品list
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  /*@import "../../common/css/weidian";*/
  @import "../../common/css/_variate";

  .m-weidians {
    background-color: #fff;
    .m-weidian-contents {
      padding: 0.25rem 0.3rem;
      .search-box {
        display: flex;
        flex-wrap: wrap;
        margin-top: -0.1rem;
        background-color: #f7f7f7;
        padding: 0.1rem 0.2rem;
        border-radius: 0.1rem;
        .search-group {
          display: flex;
          margin: 0.1rem 0.3rem 0 0;
          .group-title {
            width: 0.65rem;
            font-size: 0.12rem;
            line-height: 0.2rem;
          }
          .search-input {
            width: 2.3rem;
          }
        }
        .search-btn {
          width: 0.33rem;
          height: 0.18rem;
          line-height: 0.18rem;
          font-size: 0.12rem;
          white-space: nowrap;
          align-items: center;
          text-align: center;
          padding: 0.03rem 0.15rem;
          border-radius: 0.1rem;
          margin: 0.09rem 0 0 0.2rem;
          color: #ffffff;
          background-color: #9fd0bf;
        }
        .cancel-btn {
          color: #000000;
          background-color: #DBDCDC;
          margin-left: 0.5rem;
        }
      }

      .content-table {
        padding: 0.2rem 0 0 0;
        .product-img {
          width: 0.6rem;
          height: 0.6rem;
        }
        .blue-btn {
          color: #66B1FF;
          .text-btn {
            line-height: 0.15rem;
          }
        }
        .page-box {
          text-align: right;
          padding-top: 0.1rem;
        }
      }
    }
  }
  .check-box-list {
    display: flex;
    flex-wrap: wrap;
    margin: -0.2rem 0 0 0;
    .check-box {
      width: 25%;
      margin: 2% 0 0 8%;
    }
  }
  .radio-target {
    margin: 6% 0 0 8%;
  }
  .dialog-footer {
    display: flex;
    margin: 0.1rem 0.1rem 0 0;
    justify-content: flex-end;
    .dialog-text {
      flex: 1;
      text-align: left;
      font-size: 0.1rem;
      line-height: 0.22rem;
      letter-spacing: 0.4px;
    }
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
