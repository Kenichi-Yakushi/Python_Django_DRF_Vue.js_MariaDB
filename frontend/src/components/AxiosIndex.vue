<template>
  <div id="app">
    <h1>AxiosIndex</h1>
    <h2>Essential Links</h2>
    [[ products_product ]]

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
export default {
  name: 'AxiosIndex',
  data () {
    return {
      products_product: []
    }
  },
  compilerOptions: {
    delimiters: ['[[', ']]']
  },
  mounted () {
    this.axios
      .get('http://localhost:8000/products/list')
      .then(response => (this.products_product = response.data))
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
