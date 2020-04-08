import Vue from 'vue'
import Router from 'vue-router'
import Search from '@/pages/Search'
import Index from '@/pages/Index'
import Login from '@/pages/Login'
import Share from '@/pages/Share'
import SiteList from '@/pages/SiteList'
import WordCloudDetails from '@/pages/WordCloudDetails'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/siteList/:labelId',
      name: 'SiteList',
      component: SiteList
    },
    {
      path: '/wordCloudDetails/:pageId',
      name: 'WordCloudDetails',
      component: WordCloudDetails
    }
  ]
})
