// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import router from './router'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.headers.common['Accept'] = 'application/json'
axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080/products/list'
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

Vue.prototype.$http = (url, opts) => fetch(url, opts)
Vue.prototype.$httpBooks = 'http://127.0.0.1:8000/book_management/api/books/'


/* eslint-disable */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
