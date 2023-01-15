import Vue from 'vue'
import VueRouter from 'vue-router'
// import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AxiosIndex from '@/components/AxiosIndex'
import AxiosDetail from '@/components/AxiosDetail'

// Vue.use(Router)
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/products/list',
      name: 'AxiosIndex',
      component: AxiosIndex
    },
    {
      path: '/products/list/:id',
      name: 'AxiosDetail',
      component: AxiosDetail
    }
  ]
})
