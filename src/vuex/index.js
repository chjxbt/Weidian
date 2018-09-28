import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);

let store= new Vuex.Store({
  state: {
    route: null,
    now:null,
    token:'',
    tabbar:[{
      name:'首页',
      icon:'',
      active_icon:'',
      url:'index'
    },{
      name:'客服',
      icon:'',
      active_icon:'',
      url:'service'
    },{
      name:'发现',
      icon:'',
      active_icon:'',
      url:'discover'
    },{
      name:'购物车',
      icon:'',
      active_icon:'',
      url:'shopping'
    },{
      name:'我的',
      icon:'',
      active_icon:'',
      url:'personal'
    }],
    tabbar_select:'首页'
  },
  mutations: {
    add(state,route) {
      state.tabbar_select=route;
    },
    remove(state,name){
      Vue.delete(state.route,name)
      // delete state.route[name]


      // this.$store.commit('remove',name)调用此方法
    }
  }
})


export default store
