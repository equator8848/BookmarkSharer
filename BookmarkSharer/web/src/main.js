// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'style/iconfont/iconfont.css'
import httpUtil from '@/utils/httpUtil'

Vue.config.productionTip = false
Vue.prototype.$httpUtil = httpUtil
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
