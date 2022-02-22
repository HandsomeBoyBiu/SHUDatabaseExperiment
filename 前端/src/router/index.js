import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Dashboard', icon: 'dashboard' }
    }]
  },

  {
    path: '/reg',
    component: Layout,
    meta: { title: '登记', icon: 'form' },
    children: [
      {
        path: 'car_reg',
        name: '车辆登记',
        component: () => import("@/views/reg/car_reg"),
        meta: { title: '车辆登记', icon: 'el-icon-truck' }
      },
      {
        path: 'client_reg',
        name: '客户登记',
        component: () => import("@/views/reg/client_reg"),
        meta: { title: '客户登记', icon: 'el-icon-s-custom' }
      },
      {
        path: 'fix_reg',
        name: '维修委托登记',
        component: () => import('@/views/reg/fix_reg'),
        meta: { title: '维修委托登记', icon: 'el-icon-s-claim' }
      },
      {
        hidden: true,
        path: 'job_reg',
        name: ' 维修派工单',
        component: () => import('@/views/reg/job_reg'),
        meta: { title: ' 维修派工单', icon: 'el-icon-s-tools' }
      }
    ]
  },

  {
    path: '/manage',
    component: Layout,
    meta: { title: '管理', icon: 'el-icon-set-up' },
    children: [
      {
        path: 'car',
        name: '车辆管理',
        component: () => import('@/views/manage/car_mng'),
        meta: { title: '车辆管理', icon: 'el-icon-truck' }
      },
      {
        path: 'client',
        name: '客户管理',
        component: () => import('@/views/manage/client_mng'),
        meta: { title: '客户管理', icon: 'el-icon-s-custom' }
      },
      {
        path: 'fix',
        name: '维修委托管理',
        component: () => import('@/views/manage/fix_mng'),
        meta: { title: '维修委托管理', icon: 'el-icon-s-order' }
      },
      {
        hidden: true,
        path: 'report',
        name: '维修报告',
        component: () => import('@/views/manage/report'),
        meta: { title: '维修报告', icon: 'el-icon-s-custom' }

      }
    ]

  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
