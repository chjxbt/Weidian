import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../views/layout/index';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', component: Layout, hidden: true },
  {
    path: '/index',
    component: Layout,
    redirect: 'index/index',
    children: [{
      path: 'index',
      component: () => import('../views/index/index'),
      name: 'index',
      meta: { title: 'index', icon: 'index', noCache: true }
    }
    ],

  },

]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
