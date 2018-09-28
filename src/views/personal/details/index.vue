<template>
    <div class="m-details">
      <div class="m-total-money">
        <span class="m-help">帮助</span>
        <p>可提现金额数额</p>
        <p class="m-red">0.00</p>
        <span class="m-total-detail" @click="detailClick">提现明细</span>
        <span class="m-putforward-btn active" @click="putForwardClick">提现</span>
      </div>
      <div class="m-money-detail-type">
        <div class="m-money-type-one">
          <p>预估到账金额</p>
          <p class="m-red">0.00</p>
        </div>
        <div class="m-money-type-one">
          <p>预估到账金额</p>
          <p class="m-red">0.00</p>
        </div>
      </div>
      <p class="m-select-date" @click="showPicker">
        <span>{{date[0]}}年{{date[1]}}月</span>
        <span class="m-select-date-icon"></span>
      </p>
      <div class="m-money-details">
        <p class="m-money-type">
          <span :class="isIncome ? 'active':''" @click="moneyTypeClick(true)">我的收益</span>
          <span :class="!isIncome ? 'active':''" @click="moneyTypeClick(false)">新衣币</span>
        </p>

        <div v-if="isIncome">
          <p class="m-income-expenditure">
            <span :class="out ? 'active':''" @click="changeOut('out',true)">收入</span>
            <span :class="!out ? 'active':''" @click="changeOut('out',false)">支出</span>
          </p>
          <p class="m-income-expenditure-total">
            <span >本月总计</span>
            <span class="m-red">￥2.70</span>
          </p>
          <div class="m-scroll">
            <ul class="m-money-info" v-if="out">
              <li>
                <div>
                  <p>消费返现</p>
                  <p class="m-money-info-date">2018.07.30 19:27:15</p>
                </div>
                <div class="m-red">+1.35</div>
              </li>
              <li>
                <div>
                  <p>消费返现</p>
                  <p class="m-money-info-date">2018.07.30 19:27:15</p>
                </div>
                <div class="m-red">+1.35</div>
              </li>
            </ul>
            <ul class="m-money-info" v-else>
              <li>
                <div>
                  <p>消费返现</p>
                  <p class="m-money-info-date">2018.07.30 19:27:15</p>
                </div>
                <div class="m-red">-1.35</div>
              </li>
              <li>
                <div>
                  <p>邀请开店</p>
                  <p class="m-money-info-date">2018.07.30 19:27:15</p>
                </div>
                <div class="m-red">-1.35</div>
              </li>
            </ul>
          </div>
        </div>
        <div v-else>
          <p class="m-income-expenditure">
            <span :class="send ? 'active':''" @click="changeOut('send',true)">发出</span>
            <span :class="!send ? 'active':''" @click="changeOut('send',false)">收到</span>
          </p>
          <div class="m-total-share">
            <p>共9次贝币分享</p>
            <p>共<span class="m-red m-ft-30 m-ft-b">873</span>贝币</p>
          </div>

          <div class="m-scroll">
            <div class="m-new-info" v-if="send">
              <discount-coupon></discount-coupon>
            </div>
            <div class="m-new-info" v-else>
              <discount-coupon></discount-coupon>
              <discount-coupon></discount-coupon>
              <discount-coupon></discount-coupon>
            </div>
          </div>
        </div>
      </div>
      <picker :show_picker="show_picker" :slots="slots" @pickerSave="pickerSave"></picker>
    </div>

</template>

<script type="text/ecmascript-6">
   import discountCoupon from '../../../components/common/discountCoupon';
   import {Toast,MessageBox} from 'mint-ui';
   import picker from '../../../components/common/picker';
    export default {
        data() {
            return {
                name: '',
              isIncome:true,
              show_picker:false,
              date:['2018', '01'],
              slots: [
                {
                  flex: 1,
                  values: ['2017', '2018', '2019'],
                  className: 'slot1',
                  textAlign: 'right'
                }, {
                  divider: true,
                  content: '-',
                  className: 'slot2'
                }, {
                  flex: 1,
                  values: ['01', '02', '03', '04', '05', '06','07','08','09','10','11','12'],
                  className: 'slot3',
                  textAlign: 'left'
                }
              ],
              out:true,
              send:true
            }
        },
        components: {
          discountCoupon,
          picker
        },
      mounted(){
        let  myDate = new Date();
        let _arr = this.date;
        _arr[0] = myDate.getFullYear(); //获取完整的年份(4位,1970-????)
        _arr[1] = myDate.getMonth()>=9?(myDate.getMonth() +1): '0' +(myDate.getMonth() +1) ; //获取当前月份(0-11,0代表1月)
        this.date = [].concat(_arr)
      },
        methods: {
          detailClick(){
            this.$router.push('/withdrawalDetail');
          },
          putForwardClick(){
            this.$router.push('applyWithdrawal');
          },
          moneyTypeClick(v){
            this.isIncome = v;
          },
          pickerSave(v,i){
            this.show_picker = v;
            if(i)
              this.date = i;
          },
          showPicker(v){
            this.show_picker = v;
          },
          changeOut(v,bool){
            console.log(v)
            this[v] = bool;
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
@import "../../../common/css/index";
  .m-details{
    .m-total-money{
      height: 230px;
      text-align: center;
      font-size: 30px;
      border-bottom: 1px solid @borderColor;
      box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.16);
      position: relative;
      padding-top: 20px;
      .m-help{
        position: absolute;
        right: 20px;
        top: 40px;
        font-size: 24px;
        color: #a4a4a4;
      }
      p{
        margin: 20px 0;
        &.m-red{
          margin-top: 40px;
          font-size: 50px;
          font-weight: bold;
        }
      }
      .m-putforward-btn{
        position: absolute;
        width: 250px;
        height: 70px;
        line-height: 70px;
        text-align: center;
        border-radius: 50px;
        background-color: #c1c1c1;
        box-shadow: 2px 8px 8px 0 rgba(0, 0, 0, 0.16);
        color: #fff;
        left: 50%;
        bottom: -35px;
        transform: translateX(-125px);
        &.active{
          background-color: @mainColor;
          color: #fff;
        }
      }
      .m-total-detail{
        position: absolute;
        right: 23px;
        bottom: 14px;
        width: 129px;
        height: 40px;
        text-align: center;
        line-height: 40px;
        color: #888;
        border: 2px solid #888;
        border-radius: 30px;
        font-size: 24px;

      }
    }
    .m-money-detail-type{
      .flex-row(space-around);
      height: 180px;
      .m-money-type-one{
        p{
          margin-top: 20px;
          font-size: 30px;
          line-height: 40px;
          &.m-red{
            font-size: 40px;
            font-weight: bold;
            line-height: 53px;
          }
        }
      }
    }
    .m-select-date{
      text-align: center;
      font-size: 24px;
      line-height: 32px;
      color: #666666;
      margin-bottom: 10px;
      .m-select-date-icon{
        display: inline-block;
        width: 24px;
        height: 12px;
        background: url("/static/images/icon-select-date-personal.png") no-repeat;
        background-size: 100%;
        line-height: 32px;
      }
    }
    .m-money-details{
      height: 46px;
      .m-money-type{
        .flex-row(flex-start);
        span{
          display: block;
          width: 50%;
          height: 46px;
          line-height: 46px;
          font-size: 24px;
          background-color: #e9e9e9;
          color: #c1c1c1;
          &.active{
            background-color: @mainColor;
            color: #fff;
          }
        }
      }
      .m-income-expenditure{
        .flex-row(space-around);
        margin: 20px 0;
        span{
          display: block;
          font-size: 24px;
          line-height: 32px;
          color: #c1c1c1;
          padding: 0 10px;
          &.active{
            color: #666666;
            border-bottom: 4px solid @mainColor;
          }
        }
      }
      .m-income-expenditure-total{
        .flex-row(space-around);
        span{
          display: block;
          font-size: 24px;
          line-height: 32px;
          &.m-red{
            font-weight: bold;
          }
        }

      }
      .m-total-share{
        p{
          margin-bottom: 10px;
        }
      }
      .m-scroll{
        height: 620px;
        overflow-y: auto;
        padding-top: 10px;
        margin-right: 48px;
        .m-money-info{
          li{
            .flex-row(space-around);
            color: #666;
            font-size: 24px;
            line-height: 32px;
            margin-bottom: 20px;
            div{
              text-align: center;
              .m-money-info-date{
                font-size: 21px;
                line-height: 28px;
              }
            }
          }
        }
        .m-new-info{
          .flex-col(center);

        }
      }
    }
  }
/*滚动条样式*/
.m-scroll::-webkit-scrollbar {/*滚动条整体样式*/
  width: 9px;     /*高宽分别对应横竖滚动条的尺寸*/
  height: 9px;
  border-radius: 10px;
}
.m-scroll::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 5px #FBC6CC;
  background: #FBC6CC;
}
.m-scroll::-webkit-scrollbar-track {/*滚动条里面轨道*/
  -webkit-box-shadow: inset 0 0 5px #FDEAEC;
  border-radius: 10px;
  background: #FDEAEC;
}
</style>
