<template>
  <div class="ui container" id="app">
    <h1>登録フォーム</h1>
    <br/><br/>
    <form>
      <div class="ui input">
        <input type="text" id="name" v-model="name"  placeholder="名前を入力してください" />
      </div><br/><br/>
      <div class="ui input">
        <input type="text" id="price" v-model="price"  placeholder="価格を入力してください" />
      </div><br/><br/>

      <p v-if="errors.length">
        <b>以下の要件を満たす、フォームの入力をしてください。</b>
        <ul>
          <li v-for="(error, key) in errors" :key="key">{{ error }}</li>
        </ul>
      </p>

      <sui-button color="blue" content="登録" icon="save outline" type="submit" v-on:click="addContents"></sui-button>
    </form>

    <h1>一覧テーブル</h1>
    <!-- {{ productsRes }} --><br/><br/>
    <sui-button color="grey" content="一覧取得" icon="eye" v-on:click="fetch"></sui-button><br/><br/>

    <table class="ui celled table">
      <thead>
        <th>項番</th>
        <th>名前</th>
        <th>価格</th>
        <th>詳細</th>
      </thead>
      <tbody>
        <tr v-for="(value, key) in productsRes" :key="key">
          <td>{{ value.id }}</td>
          <td>{{ value.name }}</td>
          <td>{{ value.price }}</td>
          <td>
            <sui-button basic icon="crosshairs">
              <router-link :to="{ name: 'AxiosDetail', params: { id: value.id }}">詳細</router-link>
            </sui-button>
          </td>
        </tr>
      </tbody>
      <router-view/>
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
      productsCreate: [],
      productsUpdate: [],
      id: '',
      name: '',
      price: '',
      errors: []
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
