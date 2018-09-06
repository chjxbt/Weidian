<template>
  <div>
    <navbar :list="nav_list" @navClick="navClick"></navbar>
    <div class="help-box">
      <div class="want-to-ask m-ft-26 m-grey-color tl">猜你想问</div>
      <div class="question-box" v-for="(item, index) in questions">
        <div class="question-line-one" @click="unfoldClick(index)">
          <div class="question-content m-ft-26 m-black tl">{{item.question}}</div>
          <img class="unfold-answer-img" :class="item.unfold?'active':''" src="/static/images/icon-list-down.png">
        </div>
        <div class="question-line-two m-ft-26 tl" v-if="item.unfold">{{item.answer}}</div>
      </div>
      <div class="question-bottom">
        <div class="bottom-left m-ft-20 tl">
          <div class="m-grey-color">拨打客服热线</div>
          <div class="bottom-left-text m-ft-24 m-blue">400-966-889 ></div>
          <div class="m-grey-color">服务时间：9:00-21:00</div>
        </div>
        <div class="bottom-right">
          <img class="bottom-right-img" src="/static/images/customer_service.png">
          <div class="m-ft-30 m-red">售后客服</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar';
  export default {
    name: "helpCenter",
    data(){
      return{
        nav_list: [
          { click: false, tnname: "常见问题" },
          { click: false, tnname: "物流问题" },
          { click: false, tnname: "购物问题" },
          { click: true, tnname: "售后问题" }
        ],
        questions: [
          { question: "如何体现？", unfold: true, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" },
          { question: "如何体现？", unfold: false, answer: "提现是免手续费的，在我的明细中，点击提现按钮，即可提现。" }
        ]
      }
    },
    components: { navbar },
    methods: {
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
      // 折叠
      unfoldClick(index) {
        if(this.questions[index].unfold) {
          this.questions[index].unfold = false;
        }else if(!this.questions[index].unfold) {
          this.questions[index].unfold = true;
        }
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .help-box {
    .want-to-ask {
      padding: 28px 0 20px 29px;
      background-color: #f2f5f7;
    }
    .question-box {
      border-bottom: 2px #E5E5E5 solid;
      .question-line-one {
        width: 100%;
        display: flex;
        .question-content {
          flex: 1;
          margin: 30px;
        }
        .unfold-answer-img {
          width: 30px;
          height: 30px;
          margin: 30px 50px 0 0;
          &.active {
            transform: rotate(180deg);
          }
        }
      }
      .question-line-two {
        color: #A5A5A5;
        margin-bottom: 30px;
        background-color: #FFFBFB;
        padding: 22px 74px 48px 28px;
      }
    }
    .question-bottom {
      width: 100%;
      display: flex;
      .bottom-left {
        flex: 1;
        margin: 50px;
        .bottom-left-text {
          margin: 10px 0;
        }
      }
      .bottom-right {
        margin: 50px;
        .bottom-right-img {
          width: 78px;
          height: 70px;
        }
      }
    }
  }
</style>
