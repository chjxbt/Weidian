<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <p class="m-form-label" style="margin-bottom: 0.2rem">任务等级奖励 </p>

      <p class="m-form-label" style="margin-bottom: 0.1rem">任务等级奖励方式管理</p>
      <!--<div class="content-table">
        <el-table :data="hiddenList" border style="width: 100%" v-loading="hiddenLoading">
          <el-table-column prop="name" label="板块" width="260"></el-table-column>
          <el-table-column prop="content" label="隐藏内容" width="500"></el-table-column>
          <el-table-column prop="show" label="是否显示" width="300">
            <template slot-scope="scope">
              <div @click="rowClick(scope.$index)">
                <el-switch v-model="scope.row.show" active-text="展示" inactive-text="隐藏" @change="hiddenRow"></el-switch>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </div>-->

      <div class="coupons-box">
        <p class="m-form-label" style="margin-bottom: 0.1rem; flex: 1;">平台优惠</p>
        <div class="add-coupons-btn">添加优惠券</div>
      </div>
      <div class="content-table">
        <el-table :data="discountsList" border style="width: 100%" v-loading="discountsLoading">
          <el-table-column prop="type" label="优惠类型"></el-table-column>
          <el-table-column prop="status" label="状态"></el-table-column>
          <el-table-column prop="discounts" label="优惠"></el-table-column>
          <el-table-column prop="num" label="已领取"></el-table-column>
          <el-table-column prop="num" label="管理">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="">编辑</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>


      <p class="m-form-label" style="margin-bottom: 0.1rem; font-size: 0.14rem">优惠编辑</p>
      <div class="input-box">
        <div class="box-text">优惠类型</div>
        <div class="box-right">
          <el-select v-model="type" placeholder="请选择" style="width: 2rem" size="mini">
            <el-option v-for="item in typeList" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </div>
      </div>

      <div class="input-box" v-if="type != 2">
        <div class="box-text">优惠金额</div>
        <div class="box-right">
          <el-input v-model="amount" style="width: 2rem" size="small" placeholder="请输入"></el-input>
        </div>
        <div class="box-text">元</div>
      </div>

      <div class="input-box" v-if="type == 2">
        <div class="box-text">佣金加成</div>
        <div class="box-right">
          <el-select v-model="bonus" placeholder="请选择" style="width: 2rem" size="mini">
            <el-option v-for="item in bonusList" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </div>
      </div>

      <div class="input-box" v-if="type != 3">
        <div class="box-text">优惠门槛</div>
        <div class="box-right">
          <el-input v-model="threshold" style="width: 2rem" size="small" placeholder="满减"></el-input>
        </div>
        <div class="box-text">元</div>
      </div>

      <div class="input-box">
        <div class="box-text">使用时间</div>
        <div class="box-right">
          <el-date-picker v-model="time" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                          start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
          </el-date-picker>
        </div>
      </div>

      <div class="input-btns">
        <div class="input-btn">删 除</div>
        <div class="input-btn">删 除</div>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  export default {
    data(){
      return{
        name:'佣金管理',
        discountsList: [  // 平台优惠list
          { type: "满减",status: "领取中", discounts: "满100-20元", time: "2018/08/05  至  2018/09/05", num: "100" },
          { type: "佣金加成",status: "暂停", discounts: "佣金+20%", time: "2018/08/05  至  2018/09/05", num: "200" },
          { type: "无门槛",status: "已结束", discounts: "减50元", time: "2018/08/05  至  2018/09/05", num: "300" }
        ],
        discountsLoading: false,  // 平台优惠list加载中
        type: "",         // 优惠类型
        typeList: [       // 优惠类型list
          { value: "1", label: "满减" },
          { value: "2", label: "佣金加成" },
          { value: "3", label: "无门槛" }
        ],
        amount: "",       // 优惠金额
        bonus: "",        // 佣金加成
        bonusList: [      // 佣金加成list
          { value: "1", label: "10%" },
          { value: "2", label: "20%" },
          { value: "3", label: "30%" },
          { value: "4", label: "40%" },
          { value: "5", label: "50%" }
        ],
        threshold: "",    // 优惠门槛
        time: "",         // 使用时间

      }
    },
    components:{ pageTitle },
    methods:{

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .coupons-box {
    display: flex;
    .add-coupons-btn {
      color: #ffffff;
      font-size: 0.12rem;
      padding: 0.05rem 0.3rem;
      white-space: normal;
      background-color: #91aeb5;
      border-radius: 0.1rem;
      margin-bottom: 0.05rem;
    }
  }

  .input-box {
    display: flex;
    padding-bottom: 0.2rem;
    .box-text {
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
      width: 0.3rem;
      color: #ffffff;
      font-size: 0.12rem;
      padding: 0.05rem 0.3rem;
      white-space: normal;
      background-color: #91aeb5;
      border-radius: 0.1rem;
      margin-bottom: 0.05rem;
      margin-left: 1rem;
    }
  }
</style>
