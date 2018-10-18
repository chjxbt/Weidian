<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <div class="coupons-box">
        <p class="m-form-label" style="margin-bottom: 0.1rem; flex: 1;">平台优惠</p>
        <div class="add-coupons-btn">添加优惠券</div>
      </div>
      <div class="content-table">
        <el-table :data="discountsList" border style="width: 100%" v-loading="discountsLoading">
          <el-table-column prop="type" label="优惠名称"></el-table-column>
          <el-table-column prop="type" label="优惠类型"></el-table-column>
          <el-table-column prop="status" label="状态"></el-table-column>
          <el-table-column prop="discounts" label="优惠"></el-table-column>
          <el-table-column prop="discounts" label="使用时间"></el-table-column>
          <el-table-column prop="num" label="已领取"></el-table-column>
          <el-table-column prop="num" label="集合"></el-table-column>
          <el-table-column prop="num" label="管理" width="120">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <p class="m-form-label" style="margin: 0.1rem 0; font-size: 0.14rem">优惠编辑</p>
      <div class="input-boxs">
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
            <el-input v-model="discountsName" style="width: 2.3rem" size="small" placeholder="请输入优惠门槛" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">叠加张数：</div>
          <div class="box-right">
            <el-input v-model="ramaxusenum" style="width: 2.3rem" size="small" placeholder="请输入允许叠加使用的张数" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">最大拥有量：</div>
          <div class="box-right">
            <el-input v-model="ramaxholdnum" style="width: 2.3rem" size="small" placeholder="请输入同种券最大可拥有数量" clearable></el-input>
          </div>
        </div>
        <div class="input-box">
          <div class="box-text">可否转赠：</div>
          <div class="box-right">
            <el-select v-model="giveToOne" placeholder="请选择优惠类型" style="width: 2.3rem" size="mini" clearable>
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
            <el-input v-model="threshold" style="width: 2.3rem" placeholder="请输入优惠金额" clearable>
              <template slot="append">元</template>
            </el-input>
          </div>
        </div>
      </div>

      <div class="input-btns">
        <div class="input-btn">删 除</div>
        <div class="input-btn">保 存</div>
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
        discountsList: [          // 平台优惠list
          { type: "满减",status: "领取中", discounts: "满100-20元", time: "2018/08/05  至  2018/09/05", num: "100" },
          { type: "佣金加成",status: "暂停", discounts: "佣金+20%", time: "2018/08/05  至  2018/09/05", num: "200" },
          { type: "无门槛",status: "已结束", discounts: "减50元", time: "2018/08/05  至  2018/09/05", num: "300" }
        ],
        discountsLoading: false,  // 平台优惠list加载中
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
          { value: "true", label: "可转增" },
          { value: "false", label: "不可转增" }
        ],
        amount: "",               // 优惠金额
        bonus: "",                // 佣金加成
        bonusList: [              // 佣金加成list
          { value: "10", label: "10%" }, { value: "20", label: "20%" }, { value: "30", label: "30%" }, { value: "40", label: "40%" }, { value: "50", label: "50%" },
          { value: "60", label: "60%" }, { value: "70", label: "70%" }, { value: "80", label: "80%" }, { value: "90", label: "90%" }, { value: "100", label: "100%" }
        ],
        threshold: "",            // 优惠门槛
      }
    },
    components:{ pageTitle },
    methods:{

    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .coupons-box {
    display: flex;
    .add-coupons-btn {
      width: 0.6rem;
      color: #ffffff;
      font-size: 0.12rem;
      padding: 0.05rem 0.2rem;
      white-space: nowrap;
      background-color: #91aeb5;
      border-radius: 0.1rem;
      margin-bottom: 0.1rem;
    }
  }

  .input-boxs {
    display: flex;
    flex-wrap: wrap;
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
</style>
