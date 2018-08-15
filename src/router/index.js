import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../views/layout/index';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', component: Layout, hidden: true },
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

]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
