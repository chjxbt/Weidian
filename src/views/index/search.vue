<template>
    <div class="m-search-html">
      <div class="m-search-box">
        <search></search>
        <span>搜索</span>
      </div>
      <div class="m-search-content">
        <p>热门搜索</p>
        <ul>
          <li>衬衣</li>
          <li>衬衣</li>
          <li>衬衣</li>
          <li>衬衣</li>
          <li>衬衣</li>
        </ul>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import search from '../../components/common/search';
    export default {
        data() {
            return {
                name: ''
            }
        },
        components: {
          search
        },
        methods: {},
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less">
  .m-search-html{
    height: 100%;
    background-color: #F1F1F1;
    .m-search-box{
      display: flex;
      flex-flow: row;
      justify-content: space-around;
      align-items: center;
      padding: 10px;
      font-size: 26px;
    }
    .m-search{
      background-color: #fff;
      border-radius: 10px;
      input{
        background-color: #fff;
        width: 560px;
      }
      .m-search-text{
        justify-content: flex-start;
      }
    }
    .m-search-content{
      padding: 18px;
      p{
        text-align: left;
      }
      ul{
        display: flex;
        flex-flow: row;
        justify-content: flex-start;
        align-items: center;
        flex-wrap: wrap;
        padding: 0;
        li {
          list-style: none;
          padding:  10px 30px;
          border-radius: 25px;
          color: #7499d7;
          background-color: #e5e5e5;
          margin-left: 30px;
          margin-top: 40px;
        }
      }
    }
  }
</style>
