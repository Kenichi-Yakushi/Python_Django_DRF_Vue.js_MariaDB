<template>
  <div id="app">
    <h1>AxiosCreate</h1>
    <br/><br/>
    <form submit.prevent="submit">
      <input type="text" id="name" v-model="name"  placeholder="edit me add name" /><br/><br/>
      <input type="text" id="price" v-model="price"  placeholder="edit me add price" /><br/><br/>

      <button type="submit" v-on:click="addContents">Add Contents</button>
    </form>

    <h1>AxiosIndex</h1>
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
      productsRes: [],
      productsCreate: []
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
    },
    addContents: function () {
      axios.post('http://localhost:8000/products/list/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        name: this.name,
        price: this.price
      })
        .then((res) => {
          this.productsCreate = res.data
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
