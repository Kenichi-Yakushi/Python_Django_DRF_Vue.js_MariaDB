<template>
  <div id="app">
    <h1>AxiosIndex</h1>
    <h2>Essential Links</h2>
    {{ products_product }}
    <br/><br/>
    <button v-on:click="fetch">Reverse json</button>

    <table border="1">
        <tr>
        <th>id</th>
        <th>name</th>
        <th>price</th>
        </tr>
        <tr v-for="(value, key) in products_product" :key="key">
        <td>{{ value.id }}</td>
        <td>{{ value.name }}</td>
        <td>{{ value.price }}</td>
        </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AxiosIndex',
  data () {
    return {
      products_product: []
    }
  },
  methods: {
    fetch: function () {
      axios.get('http://localhost:8000/products/list')
        .then((res) => {
          this.products_product = res.data
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
