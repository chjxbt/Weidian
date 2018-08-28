import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../views/layout/index';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', component: () => import('../views/login/login'), hidden: true },
  {path: '/register', component: () => import('../views/login/register'),hidden: true  },
  {
    path: '/',
    component: Layout,
    redirect: 'index',
    children: [{
      path: 'index',
      component: () => import('../views/index/index'),
      name: 'index',
      meta: { title: 'index', icon: 'index', noCache: true }
    }
    ],
  },
  {
    path: '/index',
    component: Layout,
    redirect: 'index',
    children: [{
      path: 'index',
      component: () => import('../views/index/index'),
      name: 'index',
      meta: { title: 'index', icon: 'index', noCache: true }
    }
    ],
  },
  {
    path: '/discover',
    component: Layout,
    redirect: 'discover/index',
    children: [{
      path: 'index',
      component: () => import('../views/discover/index'),
      name: 'index',
      meta: { title: 'index', icon: 'index', noCache: true }
    }
    ],

  },
  {
    path: '/service',
    component: Layout,
    redirect: 'service/index',
    children: [{
      path: 'index',
      component: () => import('../views/service/index'),
      name: 'service',
      meta: { title: 'service', icon: 'service', noCache: true }
    }
    ],

  },
  {
    path: '/shopping',
    component: Layout,
    redirect: 'shopping/index',
    children: [{
      path: 'index',
      component: () => import('../views/shopping/index'),
      name: 'shopping',
      meta: { title: 'shopping', icon: 'shopping', noCache: true }
    }
    ],

  },
  {
    path: '/personal',
    component: Layout,
    redirect: 'personal/index',
    children: [{
      path: 'index',
      component: () => import('../views/personal/index'),
      name: 'personal',
      meta: { title: 'personal', icon: 'personal', noCache: true }
    }
    ],
  },

//  我的
 /*账号设置*/
  { path: '/setUp', component: () => import('../views/personal/setUp/index'), hidden: true },
  { path: '/bankCard', component: () => import('../views/personal/setUp/bankCard'), hidden: true },
  { path: '/editAddress', component: () => import('../views/personal/setUp/editAddress'), hidden: true },
  { path: '/addBankCard', component: () => import('../views/personal/setUp/addBankCard'), hidden: true },
  { path: '/receiverAddress', component: () => import('../views/personal/setUp/receiverAddress'), hidden: true },
  { path: '/result', component: () => import('../views/personal/setUp/result'), hidden: true },
  /*邀请专属粉丝*/
  { path: '/inviteFans', component: () => import('../views/personal/inviteFans/index'), hidden: true },
  { path: '/fansManagement', component: () => import('../views/personal/inviteFans/fansManagement'), hidden: true },
  { path: '/poster', component: () => import('../views/personal/inviteFans/poster'), hidden: true },

  /*邀请开店*/
  { path: '/inviteStore', component: () => import('../views/personal/inviteStore/index'), hidden: true },
  { path: '/invitationLetter', component: () => import('../views/personal/inviteStore/invitationLetter'), hidden: true },

  /*收支明细*/
  { path: '/details', component: () => import('../views/personal/details/index'), hidden: true },
  { path: '/applyWithdrawal', component: () => import('../views/personal/details/applyWithdrawal'), hidden: true },
  { path: '/withdrawalDetail', component: () => import('../views/personal/details/withdrawalDetail'), hidden: true },

  /*订单*/
  { path: '/order', component: () => import('../views/personal/order/index'), hidden: true },
  /*投诉*/
  { path: '/complain', component: () => import('../views/personal/order/complain'), hidden: true },
  /*收藏*/
  { path: '/collect', component: () => import('../views/personal/collect'), hidden: true },

  // 商品详情
  { path: '/productDetail', component: () => import('../views/shopping/productDetail'), hidden: true },
  // 提交订单
  { path: '/submitOrder', component: () => import('../views/shopping/submitOrder'), hidden: true },
  // 订单支付成功
  { path: '/orderPayOK', component: () => import('../views/shopping/orderPayOK'), hidden: true },
  // 各种订单状态
  { path: '/orderStatus', component: () => import('../views/shopping/orderStatus'), hidden: true },
  // 物流信息
  { path: '/logisticsInfo', component: () => import('../views/shopping/logisticsInfo'), hidden: true },
]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
