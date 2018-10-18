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
    redirect: 'order/allOrder',
    children: [
      {
        path: 'allOrder',
        component: () => import('../views/order/allOrder'),
        name: 'allOrder',
        meta: {title: 'allOrder', icon: 'allOrder', noCache: true}
      }
    ]
  },
  {
    path: '/activity',
    component: Layout,
    redirect: 'activity/index',
    children: [
      {
        path: 'index',
        component: () => import('../views/activity/index'),
        name: 'index',
        meta: {title: 'index', icon: 'index', noCache: true}
      }
    ]
  },
  {
    path: '/control',
    component: Layout,
    redirect: 'control/index',
    children: [{
      path: 'index',
      component: () => import('../views/control/index'),
      name: 'control',
      meta: { title: 'control', icon: 'control', noCache: true }
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
    path: '/commission',
    component: Layout,
    redirect: 'commission/index',
    children: [
      {
        path: 'index',
        component: () => import('../views/commission/index'),
        name: 'commission',
        meta: { title: 'commission', icon: 'commission', noCache: true }
      },
      {
        path: 'set',
        component: () => import('../views/commission/set'),
        name: 'set',
        meta: { title: 'set', icon: 'set', noCache: true }
      }
    ],
  },
  {
    path: '/content',
    component: Layout,
    redirect: 'content/index',
    children: [{
      path: 'index',
      component: () => import('../views/content/index'),
      name: 'content',
      meta: { title: 'content', icon: 'content', noCache: true }
    },{
      path: 'discovery',
      component: () => import('../views/content/discovery'),
      name: 'discovery',
      meta: { title: 'discovery', icon: 'discovery', noCache: true }
    },{
      path: 'modal',
      component: () => import('../views/content/modal'),
      name: 'modal',
      meta: { title: 'modal', icon: 'modal', noCache: true }
    }
    ],
  },


]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

