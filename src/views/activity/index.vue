<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">

      <div class="title-img-box">
        <h3 class="m-title">发放优惠券</h3>
        <img v-if="!handOut" class="table-close-img" src="../../assets/images/table_close.png" @click="handOutOpen">
        <img v-if="handOut" class="table-close-img" src="../../assets/images/table_open.png" @click="handOutOpen">
      </div>
      <div class="hand-out-reward" v-if="handOut">
        <p class="m-form-label" style="margin-bottom: 0.1rem">给个人发放优惠券</p>
        <div class="input-box">
          <div class="box-text" style="width: 0.4rem">用 户：</div>
          <div class="box-right">
            <el-select v-model="usid" placeholder="请输入手机号或用户名搜索" style="width: 2.3rem"
                       filterable remote :remote-method="remoteMethod" :loading="loading" clearable>
              <el-option v-for="item in userList" :key="item.usid" :label="item.usname" :value="item.usid">
                <span style="float: left">{{item.usname}}</span>
                <span style="float: right; margin-right: 0.2rem">{{item.usphone}}</span>
              </el-option>
            </el-select>
          </div>
          <div class="box-text" style="width: 0.4rem; margin-left: 0.2rem">优惠券：</div>
          <div class="box-right">
            <el-select v-model="raid" placeholder="请选择优惠券" style="width: 2.3rem" filterable clearable>
              <el-option v-for="item in discountsList" :key="item.raid" :label="item.rewardstr" :value="item.raid"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text" style="width: 0.4rem">数 量：</div>
          <div class="box-right">
            <el-input v-model="discountNum" style="width: 2.3rem" placeholder="请输入赠送的数量" clearable>
              <template slot="append">张</template>
            </el-input>
          </div>
          <div class="coupons-btn" style="margin-left: 1rem" @click="giveDiscount">赠 送</div>
          <div class="blue-btn coupons-text" @click="getGrantRecord">赠券记录</div>
        </div>

        <!--运营赠券记录-->
        <el-dialog title="运营赠券记录" :visible.sync="recordDialog" width="7rem">
          <div class="content-table" style="margin-bottom: -0.2rem">
            <el-table :data="recordList" border style="width: 100%" v-loading="recordLoading">
              <el-table-column prop="usname" label="用户名"></el-table-column>
              <el-table-column prop="rewardname" label="优惠券"></el-table-column>
              <el-table-column prop="ranumber" label="数量（张）" width="100"></el-table-column>
              <el-table-column prop="susername" label="操作人"></el-table-column>
              <el-table-column prop="rgrcreatetime" label="操作时间" width="160"></el-table-column>
            </el-table>
            <Pagination class="page-box" :total="total_page" @pageChange="pageChangeR"></Pagination>
          </div>

          <div slot="footer" class="dialog-footer">
            <el-button class="at-img-dialog-btn btn-color" type="primary" @click="recordDialog = false">关闭</el-button>
          </div>
        </el-dialog>
      </div>

      <div class="coupons-box">
        <p class="m-form-label" style="margin-bottom: 0.1rem; flex: 1;">平台优惠</p>
        <el-select v-model="collectionS" filterable style="width: 2.3rem" placeholder="选择集合后可查看" clearable @clear="getAllRaward">
          <el-option v-for="item in collectionList" :key="item.rptid" :label="item.rptname" :value="item.rptid"></el-option>
        </el-select>
        <div class="coupons-btn" @click="searchDiscounts">查 看</div>
      </div>
      <div class="content-table">
        <el-table :data="discountsList" border style="width: 100%" v-loading="discountsLoading">
          <el-table-column prop="raname" label="优惠名称" width="120"></el-table-column>
          <el-table-column prop="raType" label="优惠类型" width="120"></el-table-column>
          <el-table-column prop="rewardstr" label="优惠内容" width="160"></el-table-column>
          <el-table-column prop="rptname" label="集合名称"></el-table-column>
          <el-table-column prop="rafilter" label="优惠门槛" width="80"></el-table-column>
          <el-table-column prop="raamount" label="优惠金额" width="80"></el-table-column>
          <el-table-column prop="raratio" label="加成比率" width="80"></el-table-column>
          <el-table-column prop="ramaxholdnum" label="最大拥有数" width="95"></el-table-column>
          <el-table-column prop="ramaxusenum" label="可叠加张数" width="95"></el-table-column>
          <el-table-column prop="racreatetime" label="创建时间" width="155"></el-table-column>
          <el-table-column prop="raendtime" label="到期时间" width="155"></el-table-column>
          <el-table-column prop="ratransfers" label="可否转赠" width="80"></el-table-column>
          <el-table-column prop="ratransfereffectivetime" label="转赠时长" width="80"></el-table-column>
          <el-table-column prop="num" fixed="right" label="管理" width="160">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="editDiscount(scope, 'update')">编辑集合</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="editDiscount(scope, 'delete')">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
      </div>

      <p class="m-form-label" style="margin: 0.1rem 0; font-size: 0.14rem">优惠券编辑</p>
      <div class="input-boxs" v-if="!editDiscounts">
        <div class="input-box">
          <div class="box-text">优惠券名称：</div>
          <div class="box-right">
            <el-input v-model="discountsName" style="width: 2.3rem" size="small" placeholder="请输入优惠名称"></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">优惠类型：</div>
          <div class="box-right">
            <el-select v-model="type" placeholder="请选择优惠类型" style="width: 2.3rem" size="mini">
              <el-option v-for="item in typeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box" v-if="type == 0">
          <div class="box-text">优惠门槛：</div>
          <div class="box-right">
            <el-input v-model="threshold" style="width: 2.3rem" placeholder="请输入优惠门槛">
              <template slot="append">元</template>
            </el-input>
          </div>
        </div>
        <div class="input-box" v-if="type != 1">
          <div class="box-text">优惠金额：</div>
          <div class="box-right">
            <el-input v-model="amount" style="width: 2.3rem" placeholder="请输入优惠金额">
              <template slot="append">元</template>
            </el-input>
          </div>
        </div>
        <div class="input-box" v-if="type == 1">
          <div class="box-text">佣金加成：</div>
          <div class="box-right">
            <el-select v-model="bonus" placeholder="请选择佣金加成比率" style="width: 2.3rem" size="mini">
              <el-option v-for="item in bonusList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">可叠加张数：</div>
          <div class="box-right">
            <el-input v-model="ramaxusenum" style="width: 2.3rem" size="small" placeholder="请输入允许叠加使用的张数"></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">最大拥有数：</div>
          <div class="box-right">
            <el-input v-model="ramaxholdnum" style="width: 2.3rem" size="small" placeholder="请输入同种券最大可拥有数量"></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">到期时间：</div>
          <div class="box-right">
            <el-date-picker v-model="endTime" style="width: 2.3rem" type="datetime" value-format="yyyy-MM-dd HH:mm:ss"
                            placeholder="请选择到期时间" :picker-options="pickerOptions"></el-date-picker>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">可否转赠：</div>
          <div class="box-right">
            <el-select v-model="giveToOne" placeholder="请选择是否允许转赠" style="width: 2.3rem" size="mini">
              <el-option v-for="item in giveToOneList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box" v-if="giveToOne">
          <div class="box-text">有效时长：</div>
          <div class="box-right">
            <el-input v-model="raendtime" style="width: 2.3rem" placeholder="请输入转赠有效时长">
              <template slot="append">小时</template>
            </el-input>
          </div>
        </div>
      </div>
      <div class="input-boxs">
        <div class="input-box">
          <div class="box-text">所属集合：</div>
          <div class="box-right">
            <el-select v-model="collection" style="width: 2.3rem" placeholder="请选择集合" clearable>
              <el-option v-for="item in collectionList" :key="item.rptid" :label="item.rptname" :value="item.rptid"></el-option>
            </el-select>
          </div>
          <div class="admin-btn" @click="addCollection('')">管理</div>
        </div>
      </div>
      <!--添加集合-->
      <el-dialog title="新建优惠券集合" :visible.sync="addDialog" width="5rem">
        <div class="send-box">
          <el-table :data="collectionList" border style="width: 100%; margin-bottom: 0.1rem;" v-loading="discountsLoading">
            <el-table-column prop="rptname" label="集合名称">
              <template slot-scope="scope">
                <el-input class="search-input" v-model="scope.row.rptname" :disabled="scope.row.disabled"></el-input>
              </template>
            </el-table-column>
            <el-table-column prop="rptid" label="管理" width="160">
              <template slot-scope="scope">
                <el-button type="text" v-if="!scope.row.disabled" @click="addCollection('save', scope)">保存</el-button>
                <el-button type="text" v-if="scope.row.disabled" @click="deleteCollection(scope)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="add-btn" @click="addCollection('add')">+</div>

          <div slot="footer" class="dialog-footer">
            <el-button class="at-img-dialog-btn" @click="closeDialog">关 闭</el-button>
            <!--<el-button class="at-img-dialog-btn" @click="closeDialog">取 消</el-button>-->
            <!--<el-button class="at-img-dialog-btn btn-color" type="primary" @click="closeDialog">确 定</el-button>-->
          </div>
        </div>
      </el-dialog>

      <div class="input-btns">
        <div class="input-btn" v-if="!editDiscounts" @click="addDiscounts">保 存</div>
        <div class="input-btn" v-if="editDiscounts" @click="cancelDiscounts">取 消</div>
        <div class="input-btn" v-if="editDiscounts" @click="saveDiscounts">保 存</div>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    data(){
      return{
        name:'活动中心',
        raid: "",                 // 给个人发放优惠券时选中的优惠券id
        usid: "",                 // 给个人发放优惠券时选中的用户id
        userList: [],             // 给个人发放优惠券时供选择的用户list
        discountNum: "",          // 给个人发放优惠券时选中的用户id
        recordDialog: false,      // 运营赠券记录
        recordList: [],           // 运营赠券记录表格
        recordLoading: false,     // 运营赠券记录表格加载中
        discountsList: [],        // 平台优惠list
        discountsLoading: false,  // 平台优惠list加载中
        editDiscounts: false,     // 编辑优惠
        handOut: true,           // 平台内发放优惠券
        discountsName: "",        // 优惠名称
        ramaxusenum: "",          // 允许叠加使用的张数
        ramaxholdnum: "",         // 同种券最大可拥有数量
        raendtime: "",            // 转赠券的有效时长
        type: "",                 // 优惠类型
        typeList: [               // 优惠类型list
          { value: "0", label: "满减" },
          { value: "1", label: "佣金加成" },
          { value: "2", label: "无门槛" },
          // { value: "3", label: "邀请粉丝券" },
          // { value: "4", label: "开店大礼包专用" }
        ],
        endTime: "",              // 优惠券的到期时间
        giveToOne: false,         // 可否转赠
        giveToOneList: [          // 可否转赠list
          { value: true, label: "可转增" },
          { value: false, label: "不可转增" }
        ],
        bonus: "",                // 佣金加成
        bonusList: [              // 佣金加成list
          { value: "10", label: "10%" }, { value: "20", label: "20%" }, { value: "30", label: "30%" }, { value: "40", label: "40%" }, { value: "50", label: "50%" },
          { value: "60", label: "60%" }, { value: "70", label: "70%" }, { value: "80", label: "80%" }, { value: "90", label: "90%" }, { value: "100", label: "100%" }
        ],
        threshold: "",            // 优惠门槛
        amount: "",               // 优惠金额
        collection: "",           // 集合选中值
        collectionS: "",          // 头部查看 - 集合选中值
        collectionList: [],       // 集合list
        addDialog: false,         // 添加集合的dialog
        saveCollection: true,     // 判断是否已保存集合名
        discount: {},             // 暂存优惠券
        page_size: 10,            // 每页请求的数量
        page_num: 1,              // 第几页
        total_page: 1,            // 总页数
        pickerOptions: {          // 到期时间不可选择之前时间
          disabledDate(time) {
            return time.getTime() < Date.now() - 8.64e7;
          }
        },
        loading: false,           // 远程查找用户
      }
    },
    components:{ pageTitle, Pagination },
    methods:{
      // 打开/关闭任务表格
      handOutOpen() {
        if(this.handOut) {
          this.handOut = false;
        }else if(!this.handOut) {
          this.handOut = true;
        }
      },
      // 分页点击方法
      pageChange(v) {
        this.page_num = v;
        this.getAllRaward();      // 获取所有优惠券
      },
      // 分页点击方法 - 运营赠券记录
      pageChangeR(v) {
        this.page_num = v;
        this.getGrantRecord();    // 运营赠券记录
      },
      // 输入值发生变化时调用 - 查找用户
      remoteMethod(query) {
        if(query != "") {
          this.loading = true;
          axios.get(api.search_user + '?token=' + localStorage.getItem('token') + "&keywords=" + query).then(res => {
            if(res.data.status == 200){
              this.loading = false;
              this.userList = res.data.data;
            }else{
              this.$message({ type: 'error', message: res.data.message, duration: 1500 });
            }
          });
        }else {
          this.userList = [];
        }
      },
      // 获取运营赠券记录
      getGrantRecord() {
        this.recordDialog = true;
        this.recordLoading = true;
        axios.get(api.get_grant_record + '?token=' + localStorage.getItem('token') + "&page_num=" + this.page_num + "&page_size=" + this.page_size).then(res => {
          if(res.data.status == 200){
            this.recordList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);
            this.recordLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 给个人发放优惠券
      giveDiscount() {
        if(this.usid == "" || this.raid == "" || this.discountNum == "") {
          this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
        }else {
          let params = { usid: this.usid, raid: this.raid, ranumber: this.discountNum };
          console.log(params);
          axios.post(api.admin_giving_reward + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.usid = "";
              this.raid = "";
              this.discountNum = "";
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }
      },
      // 按集合查找优惠券
      searchDiscounts() {
        this.discountsLoading = true;
        axios.get(api.get_r_p_detail + '?token=' + localStorage.getItem('token') + "&rptid=" + this.collectionS).then(res => {
          if(res.data.status == 200){
            this.discountsList = [];
            for(let i = 0; i < res.data.data.length; i ++) {
              this.discountsList.push(res.data.data[i].reward_detail);
            }

            for(let i = 0; i < this.discountsList.length; i ++ ){
              // 判断是否可转增
              if(this.discountsList[i].ratransfer) {
                this.discountsList[i].ratransfers = "是";
              }else if(!this.discountsList[i].ratransfer) {
                this.discountsList[i].ratransfers = "否";
              }
              for(let j = 0; j < this.typeList.length; j ++) {
                if(this.discountsList[i].ratype == this.typeList[j].value) {
                  this.discountsList[i].raType = this.typeList[j].label;
                }
              }
            }
            this.discountsLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 获取所有优惠券
      getAllRaward() {
        this.discountsLoading = true;
        axios.get(api.get_all_raward + '?token=' + localStorage.getItem('token') + "&page_num=" + this.page_num + "&page_size=" + this.page_size).then(res => {
          if(res.data.status == 200){
            this.discountsList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);

            for(let i = 0; i < this.discountsList.length; i ++ ){
              // 判断是否可转增
              if(this.discountsList[i].ratransfer) {
                this.discountsList[i].ratransfers = "是";
              }else if(!this.discountsList[i].ratransfer) {
                this.discountsList[i].ratransfers = "否";
              }
              for(let j = 0; j < this.typeList.length; j ++) {
                if(this.discountsList[i].ratype == this.typeList[j].value) {
                  this.discountsList[i].raType = this.typeList[j].label;
                }
              }
            }
            this.discountsLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 获取所有优惠券集合名
      getRewardPackets() {
        axios.get(api.get_reward_packets + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.collectionList = res.data.data;
            for(let i = 0; i < this.collectionList.length; i ++) {
              this.collectionList[i].disabled = true;
            }
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },
      // 添加优惠券时编辑框的保存按钮
      addDiscounts() {
        if(this.discountsName == "" || this.type == "" || this.ramaxusenum == "" || this.ramaxholdnum == "") {
          this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
        }else {
          let params = {
            ratype: this.type,              // 优惠类型
            ramaxusenum: this.ramaxusenum,  // 可叠加张数
            ramaxholdnum: this.ramaxholdnum,// 最大持有数
            raname: this.discountsName,     // 优惠名称
            ratransfer: this.giveToOne,     // 是否允许转赠
          };
          if(this.raendtime) {          // 允许转赠时设置失效时长，为空时默认24小时
            params.ratransfereffectivetime = this.raendtime;
          }
          if(this.endTime) {            // 设置优惠券的到期时间，为空时默认30天
            params.raendtime = this.endTime;
          }
          if(this.collection) {         // 集合id
            params.rptid = this.collection;
          }
          if(this.type == "0") {       // 满减
            if(this.threshold == "" || this.amount == "") {
              this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
            }else {
              params.rafilter = this.threshold;
              params.raamount = this.amount;
              this.addDiscount(params);     // 保存添加的优惠券
            }
          }else if(this.type == "1") { // 佣金加成
            if(this.bonus == "") {
              this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
            }else {
              params.raratio = this.bonus;
              this.addDiscount(params);     // 保存添加的优惠券
            }
          }else if(this.type == "2") { // 无门槛
            if(this.amount == "") {
              this.$message({ message: "请完整填写", type: 'warning', duration: 1500 });
            }else {
              params.raamount = this.amount;
              this.addDiscount(params);     // 保存添加的优惠券
            }
          }
        }
      },
      // 保存添加的优惠券
      addDiscount(params) {
        console.log(params);

        axios.post(api.create_reward + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: res.data.message, type: 'success', duration: 1500 });
            this.getAllRaward();          // 获取所有优惠券

            this.type = "";
            this.ramaxusenum = "";
            this.ramaxholdnum = "";
            this.raendtime = "";
            this.discountsName = "";
            this.giveToOne = false;
            this.collection = "";
            this.threshold = "";
            this.amount = "";
            this.endTime = "";
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 添加优惠券
      addCollection(where, scope) {
        if(where == "") {
          this.addDialog = true;
        }else if(where == "add") {    // 新建优惠券集合
          this.saveCollection = false;
          let index = this.collectionList.length;
          this.collectionList[index] = {};
          this.collectionList[index].rptname = "";
          this.collectionList[index].disabled = false;
          this.collectionList = this.collectionList.concat();
        }else if(where == "save") {
          let params = { name: scope.row.rptname };
          axios.post(api.create_rewardpacket + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.getRewardPackets();      // 获取所有优惠券集合名

              this.saveCollection = true;
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }else if(where == "close") {

        }
      },
      // 删除优惠券
      deleteCollection(scope) {
        this.$confirm("此操作将删除该优惠券集合，是否继续?", '提示',
          {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
          let params = { rptid: scope.row.rptid };
          axios.post(api.del_rewardpacket + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: res.data.message, type: 'success', duration: 1500 });
              this.collectionList.splice(scope.$index, 1);
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }).catch(() => {  });
      },
      // 关闭dialog
      closeDialog() {
        if(!this.saveCollection) {
          this.collectionList.splice(this.collectionList.length - 1, 1);
          this.addDialog = false;
        }else {
          this.addDialog = false;
        }
      },
      // 保存优惠券 - 编辑优惠券所属集合
      saveDiscounts() {
        let params = { raid: this.discount.row.raid, rptid: this.collection };
        axios.post(api.update_reward + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: res.data.message, type: 'success', duration: 1500 });

            // 回显数据
            if(this.collection) {
              for(let i = 0; i < this.collectionList.length; i ++) {
                if(this.collection == this.collectionList[i].rptid) {
                  this.discountsList[this.discount.$index].rptname = this.collectionList[i].rptname;
                }
              }
            }else {
              this.discountsList[this.discount.$index].rptname = "";
            }
            this.discountsList = this.discountsList.concat();
            this.collection = "";
            this.editDiscounts = false;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
          }
        });
      },
      // 取消编辑优惠券的按钮
      cancelDiscounts() {
        this.editDiscounts = false;
        this.collection = "";
      },
      // 编辑优惠券
      editDiscount(scope, operate) {
        this.discount = scope;
        let params = { raid: scope.row.raid };
        if(operate == "update") {         // 编辑优惠券的集合
          this.editDiscounts = true;
          this.collection = scope.row.rptname;
        }else if(operate == "delete") {   // 删除优惠券
          params.raisdelete = true;
          this.$confirm("此操作将删除该优惠券，是否继续?", '提示',
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            axios.post(api.update_reward + '?token=' + localStorage.getItem('token'), params).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: res.data.message, type: 'success', duration: 1500 });
                this.discountsList.splice(scope.$index, 1);
              }else{
                this.$message({ message: res.data.message, type: 'error', duration: 1500 });
              }
            });
          }).catch(() => {  });
        }
      }
    },
    mounted() {
      this.getAllRaward();          // 获取所有优惠券
      this.getRewardPackets();      // 获取所有优惠券集合名
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .coupons-box {
    display: flex;
    margin-bottom: 0.1rem;
  }
  .coupons-text {
    margin: 0.07rem 0 0 0.7rem;
  }
  .coupons-btn {
    color: #ffffff;
    font-size: 0.12rem;
    padding: 0.05rem 0.2rem;
    white-space: nowrap;
    background-color: #91aeb5;
    border-radius: 0.05rem;
    margin: 0.02rem 0 0.1rem 0.1rem;
  }
  .content-table {
    padding-bottom: 0 !important;
    .page-box {
      text-align: right;
      margin-top: 0.1rem;
    }
  }

  .input-boxs {
    display: flex;
    flex-wrap: wrap;
  }
  .input-box {
    display: flex;
    padding: 0 0.5rem 0.2rem 0;
    .box-text {
      width: 0.65rem;
      white-space: nowrap;
      font-size: 0.12rem;
      line-height: 0.3rem;
      margin-right: 0.2rem;
    }
    .box-right {
      margin-right: 0.1rem;
    }
  }
  .admin-btn {
    color: #4169E1;
    font-size: 0.12rem;
    margin: auto 0.1rem;
  }
  .add-btn {
    font-size: 0.18rem;
    margin: auto 0.1rem;
  }

  .input-btns {
    display: flex;
    flex-flow: row;
    .input-btn {
      width: 0.4rem;
      white-space: nowrap;
      text-align: center;
      color: #ffffff;
      font-size: 0.12rem;
      padding: 0.05rem 0.3rem;
      background-color: #91aeb5;
      border-radius: 0.1rem;
      margin: 0.2rem 0 0.05rem 1.5rem;
    }
  }
  .title-img-box {
    display: flex;
    justify-content: flex-start;
    .m-title{
      font-size: 18px;
      margin-bottom: 0.1rem;
    }
    .table-close-img {
      width: 0.18rem;
      height: 0.12rem;
      padding: 0.02rem 0 0 0.2rem;
    }
  }
  .hand-out-reward {
    margin: 0 0 0.1rem 0.1rem;
  }
  .send-box {
    .box-row {
      display: flex;
      padding: 0.1rem 0.4rem 0.1rem 0.3rem;
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
  .dialog-footer {
    text-align: right;
    margin: 0.1rem 0.1rem 0 0;
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
