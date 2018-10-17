<template>
  <div class="m-weidian">
    <page-title :title="name" ></page-title>
    <div class="m-weidian-content">
      <w-tab :list="tab_list"  @wTabClick="wTabClick"></w-tab>

      <p class="m-form-label" style="margin: 0.3rem 0 0.1rem 0">人员条件</p>
      <div class="num-list">
        <div class="num-box">
          <p class="m-form-label two-title">人数：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-input v-model="peopleNum" class="m-input-s" size="mini" placeholder="请输入人数条件">
                <template slot="append">人</template>
              </el-input>
            </div>
          </div>
        </div>
        <div class="num-box">
          <p class="m-form-label two-title">额度：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-input v-model="limitNum" class="m-input-s" placeholder="请输入额度条件">
                <template slot="append">元</template>
              </el-input>
            </div>
          </div>
        </div>
      </div>

      <p class="m-form-label" style="margin: 0.2rem 0 0.1rem 0">三级提点</p>
      <div class="num-list">
        <div class="num-box">
          <p class="m-form-label two-title">每单销售百分比：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-input v-model="salesPercentage" class="m-input-s" size="mini" placeholder="请输入佣金百分比">
                <template slot="append">%</template>
              </el-input>
            </div>
          </div>
        </div>
        <div class="num-box">
          <p class="m-form-label two-title">邀请普通合伙人大礼包金额：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-input v-model="giftAmount" class="m-input-s" placeholder="请输入大礼包金额">
                <template slot="append">元</template>
              </el-input>
            </div>
          </div>
        </div>
      </div>
      <div class="num-list">
        <div class="num-box">
          <p class="m-form-label two-title">团队月月奖时间：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-date-picker v-model="monthRewardTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
              </el-date-picker>
            </div>
          </div>
        </div>
      </div>
      <div class="num-list">
        <div class="num-box">
          <p class="m-form-label two-title">团队月月奖金额：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-input v-model="rewardAmount" class="m-input-s" size="mini" placeholder="请输入月月奖金额">
                <template slot="append">元</template>
              </el-input>
            </div>
          </div>
        </div>
      </div>
      <div class="num-list">
        <div class="num-box">
          <p class="m-form-label two-title">活动期间奖项时间：</p>
          <div class="m-item-content">
            <div class="m-item-row">
              <el-date-picker v-model="activityTime" type="datetimerange" range-separator="至" value-format="yyyy-MM-dd HH:mm:ss"
                              start-placeholder="开始日期" end-placeholder="结束日期" style="width: 4rem;">
              </el-date-picker>
            </div>
          </div>
        </div>
      </div>

      <div class="m-form-confirm-btn">
        <span @click="">保 存</span>
      </div>
    </div>
  </div>
</template>

<script>
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';

  export default {
    data(){
      return{
        name:'佣金管理',
        tab_list: [               // 顶部导航的list
          { active: true, name: "高级合伙人", tnid: "gaoji", url: "" },
          { active: false, name: "中级合伙人", tnid: "zhongji", url: "" },
          { active: false, name: "普通合伙人", tnid: "putong", url: "" }
        ],
        tnid: "",                 // tab栏的id
        peopleNum: "",            // 人数条件
        limitNum: "",             // 额度条件
        salesPercentage: "",      // 销售百分比
        giftAmount: "",           // 合伙人大礼包金额
        monthRewardTime: [],      // 团队月月奖时间
        rewardAmount: "",         // 团队月月奖金额
        activityTime: [],         // 活动期间奖项时间
      }
    },
    components:{ pageTitle, wTab },
    methods:{

      // 顶部tab栏的点击事件
      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a =0;a<arr.length;a++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.tab_list = [].concat(arr);

        this.tnid = this.tab_list[i].tnid;
        // this.getActivity(0, this.page_size);   // 获取首页活动/推文内容列表
      },
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/weidian";

  .num-list {
    display: flex;
    .num-box {
      margin-right: 0.5rem;
      .two-title {
        font-size: 0.12rem;
        margin-top: 0.05rem;
      }
    }
  }
</style>
