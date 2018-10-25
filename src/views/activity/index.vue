<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">

      <!--<div class="title-img-box">
        <h3 class="m-title">发放优惠券</h3>
        <img v-if="handOut" class="table-close-img" src="../../assets/images/table_close.png" @click="handOutOpen">
        <img v-if="!handOut" class="table-close-img" src="../../assets/images/table_open.png" @click="handOutOpen">
      </div>
      <div class="hand-out-reward" v-if="!handOut">
        <p class="m-form-label" style="margin-bottom: 0.1rem">平台内发放优惠券</p>
        <div class="input-box">
          <div class="box-text">优惠券：</div>
          <div class="box-right">
            <el-select v-model="raid" placeholder="请选择优惠券" style="width: 2.3rem" size="mini" clearable>
              <el-option v-for="item in discountsList" :key="item.raid" :label="item.rewardstr" :value="item.raid"></el-option>
            </el-select>
          </div>
        </div>
      </div>-->

      <div class="coupons-box">
        <p class="m-form-label" style="margin-bottom: 0.1rem; flex: 1;">平台优惠</p>
        <el-select v-model="collectionS" filterable style="width: 2.3rem" placeholder="选择集合后可查看">
          <el-option v-for="item in collectionList" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
        <div class="coupons-btn">查 看</div>
      </div>
      <div class="content-table">
        <el-table :data="discountsList" border style="width: 100%" v-loading="discountsLoading">
          <el-table-column prop="raname" label="优惠名称"></el-table-column>
          <el-table-column prop="raType" label="优惠类型" width="120"></el-table-column>
          <el-table-column prop="rewardstr" label="优惠内容" width="140"></el-table-column>
          <el-table-column prop="rafilter" label="优惠门槛" width="80"></el-table-column>
          <el-table-column prop="raamount" label="优惠金额" width="80"></el-table-column>
          <el-table-column prop="raratio" label="上涨比率" width="80"></el-table-column>
          <el-table-column prop="ramaxholdnum" label="最大拥有数" width="95"></el-table-column>
          <el-table-column prop="ramaxusenum" label="可叠加张数" width="95"></el-table-column>
          <el-table-column prop="ratransfer" label="可否转赠" width="80"></el-table-column>
          <el-table-column prop="ratransfereffectivetime" label="转赠有效时长" width="110"></el-table-column>
          <el-table-column prop="num" label="集合"></el-table-column>
          <el-table-column prop="num" label="管理" width="160">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="editDiscount(scope)">编辑集合</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <p class="m-form-label" style="margin: 0.1rem 0; font-size: 0.14rem">优惠券编辑</p>
      <div class="input-boxs" v-if="!editDiscounts">
        <div class="input-box">
          <div class="box-text">优惠类型：</div>
          <div class="box-right">
            <el-select v-model="type" placeholder="请选择优惠类型" style="width: 2.3rem" size="mini" clearable>
              <el-option v-for="item in typeList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">优惠名称：</div>
          <div class="box-right">
            <el-input v-model="discountsName" style="width: 2.3rem" size="small" placeholder="请输入优惠名称" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">可叠加张数：</div>
          <div class="box-right">
            <el-input v-model="ramaxusenum" style="width: 2.3rem" size="small" placeholder="请输入允许叠加使用的张数" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">最大拥有数：</div>
          <div class="box-right">
            <el-input v-model="ramaxholdnum" style="width: 2.3rem" size="small" placeholder="请输入同种券最大可拥有数量" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">可否转赠：</div>
          <div class="box-right">
            <el-select v-model="giveToOne" placeholder="请选择是否允许转赠" style="width: 2.3rem" size="mini" clearable>
              <el-option v-for="item in giveToOneList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box" v-if="giveToOne">
          <div class="box-text">有效时长：</div>
          <div class="box-right">
            <el-input v-model="raendtime" style="width: 2.3rem" placeholder="请输入转赠有效时长" clearable>
              <template slot="append">小时</template>
            </el-input>
          </div>
        </div>
        <div class="input-box" v-if="type != 1">
          <div class="box-text">优惠金额：</div>
          <div class="box-right">
            <el-input v-model="amount" style="width: 2.3rem" placeholder="请输入优惠金额" clearable>
              <template slot="append">元</template>
            </el-input>
          </div>
        </div>
        <div class="input-box" v-if="type == 1">
          <div class="box-text">佣金加成：</div>
          <div class="box-right">
            <el-select v-model="bonus" placeholder="请选择佣金加成比率" style="width: 2.3rem" size="mini" clearable>
              <el-option v-for="item in bonusList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
        <div class="input-box" v-if="type != 2">
          <div class="box-text">优惠门槛：</div>
          <div class="box-right">
            <el-input v-model="threshold" style="width: 2.3rem" placeholder="请输入优惠门槛" clearable>
              <template slot="append">元</template>
            </el-input>
          </div>
        </div>
      </div>
      <div class="input-boxs">
        <div class="input-box">
          <div class="box-text">所属集合：</div>
          <div class="box-right">
            <el-select v-model="collection" filterable allow-create style="width: 2.3rem" placeholder="输入可创建新集合">
              <el-option v-for="item in collectionList" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </div>
        </div>
      </div>
      <div class="input-btns">
        <div class="input-btn" v-if="editDiscounts" @click="cancelDiscounts">取 消</div>
        <div class="input-btn" v-if="editDiscounts" @click="saveDiscounts">保 存</div>
        <div class="input-btn" v-if="!editDiscounts" @click="addDiscounts">保 存</div>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    data(){
      return{
        name:'活动中心',
        raid: "",                 // 平台内发放优惠券时选中的优惠券id
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
          { value: "3", label: "邀请粉丝券" },
          { value: "4", label: "开店大礼包专用" }
        ],
        giveToOne: "",            // 可否转赠
        giveToOneList: [          // 可否转赠list
          { value: true, label: "可转增" },
          { value: false, label: "不可转增" }
        ],
        amount: "",               // 优惠金额
        bonus: "",                // 佣金加成
        bonusList: [              // 佣金加成list
          { value: "10", label: "10%" }, { value: "20", label: "20%" }, { value: "30", label: "30%" }, { value: "40", label: "40%" }, { value: "50", label: "50%" },
          { value: "60", label: "60%" }, { value: "70", label: "70%" }, { value: "80", label: "80%" }, { value: "90", label: "90%" }, { value: "100", label: "100%" }
        ],
        threshold: "",            // 优惠门槛
        collection: "",           // 集合选中值
        collectionS: "",          // 头部查看 - 集合选中值
        collectionList: [],       // 集合list
      }
    },
    components:{ pageTitle },
    methods:{
      // 打开/关闭任务表格
      handOutOpen() {
        if(this.handOut) {
          this.handOut = false;
        }else if(!this.handOut) {
          this.handOut = true;
        }
      },
      // 获取所有优惠券
      getAllRaward() {
        this.discountsLoading = true;
        axios.get(api.get_all_raward + '?token=' + localStorage.getItem('token')).then(res => {
          if(res.data.status == 200){
            this.discountsList = res.data.data;
            for(let i = 0; i < this.discountsList.length; i ++ ){
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
      // 添加优惠券时编辑框的保存按钮
      addDiscounts() {

      },
      // 优惠券编辑框的保存按钮
      saveDiscounts() {

      },
      // 取消编辑优惠券的按钮
      cancelDiscounts() {
        this.editDiscounts = false;
      },
      // 编辑优惠券
      editDiscount(scope) {
        this.editDiscounts = true;
        console.log(scope.row);
      }
    },
    mounted() {
      this.getAllRaward();      // 获取所有优惠券
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .coupons-box {
    display: flex;
    margin-bottom: 0.1rem;
    .coupons-btn {
      color: #ffffff;
      font-size: 0.12rem;
      padding: 0.05rem 0.2rem;
      white-space: nowrap;
      background-color: #91aeb5;
      border-radius: 0.05rem;
      margin: 0.02rem 0 0.1rem 0.1rem;
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
</style>
