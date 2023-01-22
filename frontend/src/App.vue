<template>
  <div id="app">
    <router-link to="/">トップページ</router-link><br/><br/>
    <router-link to="/products/list">一覧/登録 画面</router-link><br/><br/>
    <router-view/>
  </div>
</template>

<script>
import Vue from 'vue'
import AxiosIndex from './components/AxiosIndex.vue'
import AxiosDetail from './components/AxiosDetail.vue'
export default Vue.extend({
  name: 'App',
  components: {
    AxiosIndex,
    AxiosDetail
  }
})
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
a {
  text-decoration: none;
}
</style>
