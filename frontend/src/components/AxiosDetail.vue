<template>
  <div id="app">
    <h1>AxiosDetail</h1>
    <br/><br/>
    <form submit.prevent="submit">
      <table border="1">
        <tr>
          <th>id</th>
          <th>name</th>
          <th>price</th>
          <th>編集</th>
          <th>削除</th>
        </tr>
        <tr>
          <td><input type="text" id="id" v-model="id" placeholder="edit me add name" /></td>
          <td><input type="text" id="name" v-model="name" placeholder="edit me add name" /></td>
          <td><input type="text" id="price" v-model="price" placeholder="edit me add name" /></td>
          <td><button type="submit" v-on:click="updateContents">編集</button></td>
          <td><button type="submit" v-on:click="deleteContents">削除</button></td>
        </tr>
      </table>

      <p v-if="errors.length">
        <b>以下の要件を満たす、フォームの入力をしてください。</b>
        <ul>
          <li v-for="(error, key) in errors" :key="key">{{ error }}</li>
        </ul>
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000/products/list/'
axios.defaults.headers.common['Accept'] = 'application/json'
axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080/products/list/'

export default {
  name: 'AxiosDetail',
  data () {
    return {
      productsUpdate: [],
      id: '',
      name: '',
      price: '',
      errors: []
    }
  },
  mounted () {
    axios.get(`http://localhost:8000/products/list/${this.$route.params.id}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      name: this.name,
      price: this.price
    })
      .then((res) => {
        this.id = res.data.id
        this.name = res.data.name
        this.price = res.data.price
      })
      .catch(error => console.log(error))
  },
  methods: {
    updateContents: function (res) {
      axios.put(`http://localhost:8000/products/list/${this.$route.params.id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(res),
        name: this.name,
        price: this.price
      })
        .then((res) => {
          this.productsUpdate = res.data
        })
        .catch((error) => {
          console.log(error)
          this.errors = []

          if (!this.name) {
            this.errors.push('名前は必須です。')
          }
          if (!this.price) {
            this.errors.push('価格は必須です。')
          } else if (typeof this.price !== 'number') {
            this.errors.push('価格は有効な整数を入力してください。')
          }

          if (!this.errors.length) {
            return true
          }
        })
    },
    deleteContents: function () {
      axios.post('http://localhost:8000/products/list/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        name: this.name,
        price: this.price
      })
        .then((res) => {
          this.productsUpdate = res.data
        })
        .catch((error) => {
          console.log(error)
          this.errors = []

          if (!this.name) {
            this.errors.push('名前は必須です。')
          }
          if (!this.price) {
            this.errors.push('価格は必須です。')
          } else if (typeof this.price !== 'number') {
            this.errors.push('価格は有効な整数を入力してください。')
          }

          if (!this.errors.length) {
            return true
          }
        })
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
table {
  margin: auto;
}
</style>
