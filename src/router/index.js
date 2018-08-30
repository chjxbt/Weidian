import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/** note: submenu only apppear when children.length>=1
 *   detail see  https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 **/

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']     will control the page roles (you can set multiple roles)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if true ,the page will no be cached(default is false)
  }
 **/
export const constantRouterMap = [
  { path: '/', component: () => import('../views/login/index'),   redirect: 'login', hidden: true },
  { path: '/login', component: () => import('../views/login/index'), hidden: true },
  { path: '/forgetPwd', component: () => import('../views/login/forgetPwd'), hidden: true },
  { path: '/error', component: () => import('../views/error/error'), hidden: true },
  {
    path: '/index',
    component: Layout,
    redirect: 'index/userIndex',
    children: [{
      path: 'userIndex',
      component: () => import('../views/index/userIndex'),
      name: 'userIndex',
      meta: { title: 'userIndex', icon: 'userIndex', noCache: true }
    },{
      path: 'adminIndex',
      component: () => import('../views/index/adminIndex'),
      name: 'adminIndex',
      meta: { title: 'adminIndex', icon: 'adminIndex', noCache: true }
    }
    ],

  },
  {
    path: '/jurisdiction',
    component: Layout,
    redirect: 'jurisdiction/admin',
    children: [{
      path: 'admin',
      component: () => import('../views/jurisdiction/admin'),
      name: 'admin',
      meta: { title: 'admin', icon: 'admin', noCache: true }
    },{
      path: 'user',
      component: () => import('../views/jurisdiction/user'),
      name: 'user',
      meta: { title: 'user', icon: 'user', noCache: true }
    }
    ],

  },
  {
    path: '/order',
    component: Layout,
    redirect: 'order/orderIndex',
    children: [{
      path: 'allOrder',
      component: () => import('../views/order/allOrder'),
      name: 'allOrder',
      meta: {title: 'allOrder', icon: 'allOrder', noCache: true}
    }, {
      path: 'orderIndex',
      component: () => import('../views/order/orderIndex'),
      name: 'orderIndex',
      meta: {title: 'orderIndex', icon: 'orderIndex', noCache: true}
    }, {
      path: 'orderDetails',
      component: () => import('../views/order/orderDetails'),
      name: 'orderDetails',
      meta: {title: 'orderDetails', icon: 'orderIndex', noCache: true}
    }, {
      path: 'refund',
      component: () => import('../views/order/refund'),
      name: 'refund',
      meta: {title: 'refund', icon: 'refund', noCache: true}
    }
    ]
  },{
    path: '/activity',
    component: Layout,
    redirect: 'activity/discountCoupon',
    children: [{
      path: 'productActivity',
      component: () => import('../views/activity/productActivity'),
      name: 'productActivity',
      meta: {title: 'productActivity', icon: 'productActivity', noCache: true}
    }, {
      path: 'discountCoupon',
      component: () => import('../views/activity/discountCoupon'),
      name: 'discountCoupon',
      meta: {title: 'discountCoupon', icon: 'discountCoupon', noCache: true}
    }, {
      path: 'storeActivity',
      component: () => import('../views/activity/storeActivity'),
      name: 'storeActivity',
      meta: {title: 'storeActivity', icon: 'storeActivity', noCache: true}
    }, {
      path: 'discountStoreStepOne',
      component: () => import('../views/activity/discountStoreStepOne'),
      name: 'discountStoreStepOne',
      meta: {title: 'discountStoreStepOne', icon: 'discountStoreStepOne', noCache: true}
    }, {
      path: 'discountProductStepOne',
      component: () => import('../views/activity/discountProductStepOne'),
      name: 'discountProductStepOne',
      meta: {title: 'discountProductStepOne', icon: 'discountProductStepOne', noCache: true}
    },{
      path: 'storeStepResult',
      component: () => import('../views/activity/storeStepResult'),
      name: 'storeStepResult',
      meta: {title: 'storeStepResult', icon: 'storeStepResult', noCache: true}
    }, {
      path: 'activityStoreStepOne',
      component: () => import('../views/activity/activityStoreStepOne'),
      name: 'activityStoreStepOne',
      meta: {title: 'activityStoreStepOne', icon: 'activityStoreStepOne', noCache: true}
    }, {
      path: 'activityStoreStepTwo',
      component: () => import('../views/activity/activityStoreStepTwo'),
      name: 'activityStoreStepTwo',
      meta: {title: 'activityStoreStepTwo', icon: 'activityStoreStepTwo', noCache: true}
    }, {
      path: 'activityStoreStepThree',
      component: () => import('../views/activity/activityStoreStepThree'),
      name: 'activityStoreStepThree',
      meta: {title: 'activityStoreStepThree', icon: 'activityStoreStepThree', noCache: true}
    }, {
      path: 'activityProductStepOne',
      component: () => import('../views/activity/activityProductStepOne'),
      name: 'activityProductStepOne',
      meta: {title: 'activityProductStepOne', icon: 'activityProductStepOne', noCache: true}
    }, {
        path: 'activityProductStepTwo',
        component: () => import('../views/activity/activityProductStepTwo'),
        name: 'activityProductStepTwo',
        meta: {title: 'activityProductStepTwo', icon: 'activityProductStepTwo', noCache: true}
      }, {
      path: 'activityProductStepThree',
      component: () => import('../views/activity/activityProductStepThree'),
      name: 'activityProductStepThree',
      meta: {title: 'activityProductStepThree', icon: 'activityProductStepThree', noCache: true}
    }
    ]
  }


]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

