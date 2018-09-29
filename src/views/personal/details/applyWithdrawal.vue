<template>
    <div class="m-apply-withdrawal">
      <div class="m-amount">
        <div class="m-ft-30">提现金额</div>
        <div class="m-input-amount">
          <p class="m-border">
            <span class="m-ft-50 m-red m-ft-b">￥</span>
            <input type="money"  v-model="money" placeholder="最大可提现X元" class="m-input-amount-input">
            <span class="m-close-icon" @click="clearMoney"></span>
          </p>
          <p>
            <input type="text" placeholder="可用余额9.01元（仅支持大于10元的提现申请）">
          </p>
        </div>
      </div>
      <div class="m-apply-withdrawal-btn" v-if="bank_status">
        <span @click="applyClick">提现到银行卡</span></div>
      <div class="m-apply-withdrawal-btn m-apply-withdrawal-btn-two" v-else>
        <span class="active" @click="applyClick">提现到银行卡</span>
        <span @click="applyClick">提现到微信</span>
      </div>
      <div class="m-tel-info">
        <p>如果遇到问题，请随时联系我们！</p>
          <p>联系电话：12345678912</p>
      </div>

      <div class="m-modal" v-if="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-content">
            <img src="" class="m-apply-success" alt="">
            <p class="m-ft-30 m-ft-b">提交成功</p>
            <div class="m-apply-result-info">
              已成功提交提现申请，我们将在3个工作日内完成审核，请及时关注您的账户余额。
            </div>
            <div class="m-apply-result-btn">
              <span @click="knownClick">我知道了</span>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: '',
              show_modal:false,
              money:'',
              bank_status:true,
              bankcard:'',
            }
        },
        watch :{
          'money': function (curVal, oldVal) {
            if (!curVal) {
              this.money = ''
              return false
            }
            this.money = curVal.match(/\d/ig) ? curVal.match(/\d/ig).join('') : ''
          }
        },
        methods: {
          knownClick(){
            this.show_modal = false;
          },
          applyClick(){
            if(localStorage.getItem('level') == 'partner' && this.bankcard !=''){
              this.show_modal = true;
            }else{
              this.$router.push('/addBankCard')
            }
          },
          clearMoney(){
            console.log(this.money)
            this.money = '';
          },
          getInfo(){
            axios.get(api.get_account_info,{
              params:{
                token:localStorage.getItem('token')
              }
            }).then(res => {
              if(res.data.status == 200){
                this.bankcard = res.data.data.bankcard;
              }
            })
          },
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";
  @import "../../../common/css/modal";
.m-apply-withdrawal{
  .m-amount{
    padding: 33px 25px 0;
    box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.16);
    text-align: left;
    div{
      padding: 0 30px 0;
    }
    .m-input-amount{
      margin-top: 80px;
      input{
        border: none;
        padding: 30px;
        font-size: 24px;
        color: #c1c1c1;
        width: 90%;
      }
      .m-close-icon{
        display: inline-block;
        width: 60px;
        height: 60px;
        background: url("/static/images/icon-close-personal.png") no-repeat;
        background-size: 100%;
        vertical-align: text-bottom;
      }
      .m-input-amount-input{
        width: 400px;
        color: #333;
      }
      p.m-border{
        border-bottom: 1px solid #c1c1c1;
        height: 100px;
      }
    }
  }
  .m-apply-withdrawal-btn{
    margin-top: 60px;
    &.m-apply-withdrawal-btn-two{
      .flex-row(space-around);
      span{
        width: 300px;
      }
    }
    span{
      display: inline-block;
      width: 650px;
      height: 70px;
      line-height: 70px;
      background-color: @mainColor;
      color: #fff;
      border-radius: 50px;
      box-shadow: 2px 8px 8px 0 rgba(0, 0, 0, 0.16);
      &.active{
        background-color: #c1c1c1;
      }
    }
  }
  .m-tel-info{
    position: absolute;
    bottom: 71px;
    width: 100%;
    p{
      width: 100%;
      text-align: center;
      font-size: 24px;
      color: #666;
      line-height: 32px;
    }
  }
  .m-modal{
    .m-modal-state{
      width: 520px;
      height: 600px;
      border-radius: 30px;
      .m-modal-content{
        padding-top: 120px;
        p{
          color: #000;
        }
        .m-apply-success{
          display: inline-block;
          width: 85px;
          height: 85px;
          background: url("/static/images/icon-result-personal.png") no-repeat;
          background-size: 100%;
          margin-bottom: 36px;
        }
        .m-apply-result-info{
          margin: 40px 0;
          font-size: 24px;
          line-height: 35px;
        }
        .m-apply-result-btn{
          span{
            display: inline-block;
            width: 250px;
            height: 70px;
            line-height: 70px;
            background-color: @mainColor;
            color: #fff;
            border-radius: 50px;
            box-shadow: 2px 8px 8px 0 rgba(0, 0, 0, 0.16);
          }
        }
      }

    }
  }
}
</style>
