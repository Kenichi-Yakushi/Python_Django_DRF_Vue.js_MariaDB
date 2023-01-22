<template>
  <section class="container">
    <article class="book" v-for="book of bookList" :key="book.id">
      <figure>
        <img :src="book.thumbnail" :alt="book.name" class="thumbnail">
      </figure>
      <p class="book-category" :style="{ 'color': book.category.color }">
        {{ book.category.name }}
      </p>
      <h2 class="book-title">{{ book.name }}（著者: {{ book.author.name }} ／ 出版年月日: {{ book.publication_date }}）</h2>
      <p class="book-lead">{{ book.lead_text }}</p>
    </article>
  </section>
</template>
  
<script>
export default {
  name: 'BookList',
  data () {
    return {
      bookList: []
    }
  },
  created () {
    this.$http(this.$httpBooks)
      .then(response => {
        return response.json()
      })
      .then(data => {
        this.bookList = data
        console.log(this.bookList)
      })
  }
}
</script>
  
<style scoped>
  #lead {
    color: #999999;
  }
  section {
    margin-top: 80px;
  }
  .thumbnail {
    width: 100%;
    height: auto;
    vertical-align: bottom;
  }
  .book {
    text-decoration: none;
    color: #000;
    margin-bottom: 80px;
    display: block;
  }
  .book-category {
    margin-top: 25px;
    font-size: 12px;
  }
  .book-title {
    font-weight: bold;
    font-size: 14px;
    width: 100%
  }
  .book-lead {
    margin-top: 10px;
    width: 100%;
  }
  .divider {
    margin-top: 50px;
    margin-bottom: 25px;
    width: 100%;
    height: 1px;
    border: none;
    background-color: #ccc;
  }
  #page {
    color: #999;
  }
  #back {
    width: 44px;
    margin-right: 16px;
    display: inline-block;
  }
  #next {
    margin-left: 44px;
    width: 44px;
    display: inline-block;
  }
  @media (min-width: 768px) {
    section {
      display: grid;
      grid-template-columns: 340px 340px;
      column-gap: 20px;
      row-gap: 100px;
    }
    .thumbnail {
      width: 340px;
      height: 212px;
      object-fit: cover;
    }
    .book {
      margin-bottom: 0;
    }
    .book-title {
      width: 280px;
    }
    .book-lead {
      width: 280px;
    }
    .divider {
      width: 650px;
    }
  }
  @media (min-width: 1024px) {
    section {
      grid-template-columns: 480px 480px;
    }
    .thumbnail {
      width: 480px;
      height: 300px;
    }
    .book-title {
      width: 440px;
    }
    .book-lead {
      width: 440px;
    }
  }
</style>
  