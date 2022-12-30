import Vue from 'vue'
import VueRouter from 'vue-router'
// import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AxiosIndex from '@/components/AxiosIndex'

// Vue.use(Router)
Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/products/list',
      component: AxiosIndex
    }
  ]
})
