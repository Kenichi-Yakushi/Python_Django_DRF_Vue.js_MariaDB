<template>
  <div id="app">
    <h1>AxiosIndex</h1>
    <h2>Essential Links</h2>
    {{ productsRes }}
    <br/><br/>
    <button v-on:click="fetch">Reverse json</button>

    <table border="1">
        <tr>
        <th>id</th>
        <th>name</th>
        <th>price</th>
        </tr>
        <tr v-for="(value, key) in productsRes" :key="key">
        <td>{{ value.id }}</td>
        <td>{{ value.name }}</td>
        <td>{{ value.price }}</td>
        </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000/products/list/'
axios.defaults.headers.common['Accept'] = 'application/json'
axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080/products/list/'

export default {
  name: 'AxiosIndex',
  data () {
    return {
      productsRes: []
    }
  },
  methods: {
    fetch: function (res) {
      axios.get('http://localhost:8000/products/list/', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(res)
      })
        .then((res) => {
          this.productsRes = res.data
        })
        .catch(error => console.log(error))
    }
  },
  compilerOptions: {
    delimiters: ['[[', ']]']
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
