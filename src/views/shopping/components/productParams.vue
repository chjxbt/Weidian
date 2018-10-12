<template>
  <div class="product-params">

    <div  class="product-params-choose" @click="productParams">
      <div class="product-params-text m-ft-26 m-grey tl" v-if="!selects">{{prompt}}</div>
      <div class="product-params-text m-ft-26 m-grey tl m-ml-0" v-if="selects">
        <template v-for="(item,index) in selects">
          <span class="product-params-detail  m-grey"> {{item.key}}:{{item.value}} </span>
        </template>
      </div>
      <img src="/static/images/icon-list-right.png" class="more-params">
    </div>

    <!--<div v-if="choose" class="product-params-show" @click="productParams">-->
      <!--<span class="product-params-detail m-ft-22 m-grey">尺寸：{{size}}</span><span class="product-params-detail">颜色：{{color}}</span>-->
      <!--<img v-if="popupVisible" src="/static/images/icon-list-down.png" class="list-right-down">-->
      <!--<img v-if="!popupVisible" src="/static/images/icon-list-right.png" class="list-right-down">-->
    <!--</div>-->
    <mt-popup v-model="popupVisible" position="bottom">
      <div class="product-params-content">
        <img src="/static/images/product1.png" class="product-img">
        <div class="product-params-center">
          <p class="product-price m-ft-20 m-red m-ft-b tl" v-if="surplus_value && surplus_value.length == 1">￥<span class="m-ft-34">{{surplus_value[0].pskprice}}</span></p>
          <p class="product-price m-ft-20 m-red m-ft-b tl" v-else>￥<span class="m-ft-34">{{price}}</span></p>
          <div class="choose-prompt m-ft-26 tl">{{prompt}}   库存：{{num}}</div>
        </div>
        <img src="/static/images/delete.png" class="close-popup" @click="closeModal">
      </div>
      <div class="line"></div>
      <div class="product-size-color" v-for="(opt, index) in option">
        <p class="product-size-color-text m-ft-30 tl">{{opt.key}}</p>
        <template v-for="(item, ind) in opt.values">
          <span :class="{select:colorSizeList[index]&& colorSizeList[index].vid == item.vid}" v-if="item.active"  @click="select(index, ind)">{{item.value}}</span>
          <span class="m-cancel"  v-else>{{item.value}}</span>
        </template>

      </div>
      <div class="line"></div>
      <div class="product-quantity">
        <div class="product-quantity-text m-ft-30 tl">购买数量</div>
        <product-quantity :quantity="quantity"   class="product-quantity-edit" @changeNum="changeNum"></product-quantity>
      </div>
      <div class="choose-done m-ft-28 m-bg-main-color" v-if="num" @click="chooseDone">确定</div>
      <div class="choose-done m-ft-28 m-choose-cancel" v-else >确定</div>
    </mt-popup>
  </div>
</template>

<script>
  import productQuantity from "../components/productQuantity";
  export default {
    data() {
      return {
        name: 'productParams',
        popupVisible: this.choose,
        prompt: "请选择规格",
        sel: [],
        colorSizeList: [],
        // options: [ {name: "颜色", items: [{id: 0, msg: "黄色"}, {id: 1, msg: "绿色"}, {id: 2, msg: "红色"}, {id:3, msg: "蓝色"}]},
        //   {name: "尺寸", items: [{id: 0, msg: "S"}, {id: 1, msg: "M"}, {id: 2, msg: "L"}, {id: 3, msg: "XL"}, {id: 4, msg: "2XL"}, {id: 5, msg: "3XL"}]} ],
       id: '',
        all_sku:null,
        surplus_value:null,
        select_num:this.quantity,
        option:null,
        num:null,
        show_num:false
      }
    },
    components: { productQuantity },
    props:{
      choose:{
        type: Boolean,
        default: false
      },
      size:{
        type: String,
        default: null
      },
      color:{
        type: String,
        default: null
      },
      quantity:{
        type: Number,
        default: 1
      },
      options:{
        type:Array,
        default:[]
      },
      selects:{
        type:Array,
        default:null
      },
      sku:{
        type:Array,
        default:null
      },
      price:{
        type:Number,
        default:null
      },
      item:{
        type:Number,
        default:null
      },
      number:{
        type:Number,
        default:null
      }
    },
    watch:{
      choose:function (val,oldValue) {
        this.popupVisible = val
      }
    },
    mounted(){
      // this.colorSizeList=new Array(this.options.length);
      // console.log(this.sku)
      let options_arr=this.options;
      for(let b=0;b<options_arr.length;b++){
        for(let c=0;c<options_arr[b].values.length;c++){
          options_arr[b].values[c].active = true;
        }
      }
      this.option =[].concat(options_arr);
       if(this.number){
         this.num = this.number;
         this.show_num = true;
       }
      if(this.selects){
        this.colorSizeList = [].concat(this.selects);

      }else{
        this.colorSizeList = new Array(this.option.length);
      }
      let _arr = this.sku;

      for(let i=0;i<_arr.length;i++){
        let _id = '';
        for(let j=0;j<_arr[i].pskproperkey.length;j++){
          _id = _id + _arr[i].pskproperkey[j].vid
        }
        _arr[i].id_arr = _id;
      }
      this.surplus_value = [].concat(_arr);
      this.all_sku = [].concat(_arr);
      if(this.selects){
        this.clickSku(0,this.selects[0].vid,true);
      }
    },
    methods: {
      closeModal(){
        this.popupVisible = false;
        this.$emit('closeModal')
      },
      // 判断选择商品类型的下部弹框是否弹出
      productParams() {
        if(this.popupVisible) {
          this.popupVisible = false;
        }else if(!this.popupVisible) {
          this.popupVisible = true;

          // 从购物车中调用时选中已确定的颜色和尺寸
          // for(let i = 0; i < this.options.length; i ++) {
          //   for(let j = 0; j < this.options[i].values.length; j ++) {
          //     if(this.color == this.options[i].values[j].value) {
          //       this.sel[0] = this.options[i].values[j].id;
          //       this.colorSizeList[0] = this.color;
          //     }
          //     if(this.size == this.options[i].values[j].value) {
          //       this.sel[1] = this.options[i].values[j].id;
          //       this.colorSizeList[1] = this.size;
          //     }
          //   }
          // }
          if(this.selects){
            for(let i = 0;i<this.selects.length;i++){
              for(let j = 0;j<this.option[i].values.length;j++){
                if(this.option[i].values[j].vid == this.selects[i].vid){
                  this.sel[i] = j;
                  continue;
                }
              }
            }
          }
          this.changePrompt();
        }
      },
      select(index, ind) {
        this.sel[index] = ind;                  // 让数组sel的第index+1的元素的值等于ind
        this.sel = this.sel.concat([]);         // 因为数组是引用类型，对其中一个变量直接赋值不会影响到另一个变量（并未操作引用的对象），使用concat（操作了应用对象）
        this.colorSizeList[index] = this.option[index].values[ind];         // 获取选中的id
        this.changePrompt();

        this.clickSku(index,this.option[index].values[ind],false,this.option[index].kid)
      },
      // 根据选择的商品参数来改变提示信息
      changePrompt() {
        for(let i=0;i<this.colorSizeList.length;i++){
          if(!this.colorSizeList[i]){
            this.prompt = "请选择 " + this.option[i].key;
            return false;
          }
        }
        let promptTemp = "";
        for(let i = 0; i < this.colorSizeList.length; i ++) {
          promptTemp = promptTemp + " " + this.option[i].key+':'+ this.colorSizeList[i].value;
        }
        this.prompt = promptTemp;
        // for(let a=0;a<this.sku.length;a++){
        //
        // }
        // if(this.colorSizeList[0] == "" && this.colorSizeList[1] != "") {
        //   this.prompt = "请选择 颜色"
        // }else if(this.colorSizeList[1] == "" && this.colorSizeList[0] != "") {
        //   this.prompt = "请选择 尺寸"
        // }else if(this.colorSizeList[0] != "" && this.colorSizeList[1] != "") {
        //   let promptTemp = "";
        //   for(let i = 0; i < this.colorSizeList.length; i ++) {
        //     promptTemp = promptTemp + " " + this.colorSizeList[i];
        //   }
        //   this.prompt = "已选择 " + promptTemp;
        // }
      },
      chooseDone() {
        for(let i=0;i<this.colorSizeList.length;i++){
          if(!this.colorSizeList[i] ){
            return false;
          }
        }
        this.popupVisible = false;
        if(this.item !=null){
          this.$emit('carChoose',this.surplus_value,this.select_num,this.item);
        }else{
          this.$emit('carChoose',this.surplus_value,this.select_num);
        }

      },
      clickSku(index,v,isFirst,kid){
        let arr =[];
        // if(!isFirst){
        //   for(let i =0;i<this.surplus_value.length;i++){
        //     if(this.surplus_value[i].pskproperkey[index].vid == v.vid){
        //       arr.push(this.surplus_value[i]);
        //     }
        //   }
        // }
        // console.log(this.all_sku,this.colorSizeList)
        // if(arr.length <1 ){
            let _id = '';
            for(let j=0;j<this.colorSizeList.length;j++){
              if(this.colorSizeList[j])
                _id = _id + this.colorSizeList[j].vid;
            }

          // for(let j=0;j<this.colorSizeList.length;j++){
              for(let i =0;i<this.all_sku.length;i++){
                  if(this.all_sku[i].id_arr.length == _id.length && this.all_sku[i].id_arr == _id ){
                    arr.push(this.all_sku[i]);
                  }else{
                    for(let a=0;a<this.all_sku[i].pskproperkey.length;a++){
                      if(this.all_sku[i].pskproperkey[a].vid == _id){
                        arr.push(this.all_sku[i]);
                      }
                    }
                  }
              }
          // }

        // }

        // if(arr.length != 1){
        //   let option_arr=this.options;
        //   for(let b=0;b<option_arr.length;b++){
        //     for(let c=0;c<option_arr[b].values.length;c++){
        //       option_arr[b].values[c].active = true;
        //     }
        //   }
        //   this.option =[].concat(option_arr);

          // let new_arr = [];
          // for(let y =0;y<arr[0].pskproperkey.length;y++){
          //   new_arr[y] = { kid:arr[0].pskproperkey[y].kid,key:arr[0].pskproperkey[y].key,values:[]};
          // }
          // for(let x=0;x<arr.length;x++){
          //   if(arr[x].pskproductnum == 0){
          //     for(let y =0;y<arr[x].pskproperkey.length;y++){
          //       new_arr[y].values.push({value:arr[x].pskproperkey[y].value,vid:arr[x].pskproperkey[y].vid})
          //     }
          //   }
          // }
          // let options_arr = this.option;
          // for(let m =0;m<options_arr.length;m++){
          //   if(options_arr[m].kid == kid ){
          //     continue;
          //   }else{
          //     for(let n=0;n<options_arr[m].values.length;n++){
          //       for(let b=0;b<new_arr.length;b++){
          //         if(new_arr[b].kid == kid){
          //           continue;
          //         }else{
          //           for(let c=0;c<new_arr[b].values.length;c++){
          //             if(new_arr[b].values[c].vid == options_arr[m].values[n].vid){
          //               options_arr[m].values[n].active = false;
          //             }
          //           }
          //         }
          //       }
          //     }
          //   }
          // }
          // this.option = [].concat(options_arr);
        // }
        if(arr.length ==1){
            this.num = arr[0].pskproductnum;
        }
        console.log(arr)
        this.surplus_value = [].concat(arr);
      },
      changeNum(num,i){
        // if(i == undefined && this.item != null){
        //   this.$emit('changeNum',num,this.item,'no');
        // }else{
        //   this.$emit('changeNum',num);
        // }
        this.select_num = num;
      }
    },
    created() {
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../../common/css/index";
  .m-cancel{
    color: #a4a4a4;
  }

  .product-params {
    .product-params-choose {
      width: 100%;
      display: flex;
      .product-params-text {
        flex: 1;
        margin: 15px 0 25px 35px;
        &.m-ml-0{
          margin: 15px 0;
        }
      }
      .more-params {
        width: 22px;
        height: 22px;
        margin: 22px 25px;
      }
    }
    .product-params-show {
      .product-params-detail {
        float: left;
        margin: 8px 20px 10px 0;
      }
      .list-right-down {
        width: 22px;
        height: 22px;
        margin-top: 14px;
        margin-left: -60px;
      }
    }
    .product-params-content {
      width: 750px;
      height: 160px;
      display: flex;
      .product-img {
        width: 220px;
        height: 220px;
        margin: -90px 0 0 40px;
      }
      .product-params-center {
        flex: 1;
        margin: 15px 0 0 35px;
        .product-price {
          margin: 20px 0;
        }
      }
      .close-popup {
        width: 34px;
        height: 34px;
        margin: 22px 22px;
      }
    }
    .product-size-color {
      height: 150px;
      .product-size-color-text {
        padding-left: 40px;
        margin-bottom: 20px;
      }
      .select {
        color: @bgMainColor;
        background-color: @mainColor;
      }
      span {
        display: inline-block;
        width: 90px;
        float: left;
        padding: 8px 0;
        font-size: 26px;
        border-radius: 10px;
        margin: 0 -20px 0 40px;
        background-color: #f4f3f9;
      }
    }
    .line {
      height: 2px;
      width: 696px;
      margin: 0 30px 20px 40px;
      background-color: @grey;
    }
    .product-quantity {
      .product-quantity-text {
        width: 535px;
        margin: 20px 0 40px 40px;
      }
      .product-quantity-edit {
        width: 205px;
        margin-top: 20px;
      }
    }
    .choose-done {
      padding: 30px;
      letter-spacing: 10px;
      background-color: @mainColor;
      &.m-choose-cancel{
        background-color: #f4f3f9;
        color: #a4a4a4;
      }
    }
  }
</style>
