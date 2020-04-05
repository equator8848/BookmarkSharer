import Vue from 'vue'
import Router from 'vue-router'
import Hot from '@/pages/Hot'
import Index from '@/pages/Index'
import Login from '@/pages/Login'
import Share from '@/pages/Share'
import SiteList from '@/pages/SiteList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/hot',
      name: 'Hot',
      component: Hot
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/share',
      name: 'Share',
      component: Share
    },
    {
      path: '/siteList/:labelId',
      name: 'SiteList',
      component: SiteList
    }
  ]
})
