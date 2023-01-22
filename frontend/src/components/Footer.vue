<template>
    <footer>
      <p>© 2022 henojiya.</p>
      <ul>
        <li><a href="https://qiita.com/YoshitakaOkada">Qiita</a></li>
        <li><a href="mailto:example@abc.com">Mail</a></li>
        <li><a href="https://github.com/duri0214">Github</a></li>
        <li><a href="#">Empty slot</a></li>
      </ul>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer'
  }
  </script>
  
  <style scoped>
    footer {
      background-color: #000;
      color: #fff;
      padding: 0 20px;
      margin-top: 160px;
    }
    ul > li {
      display: inline-block;
      margin-right: 2em;
    }
    ul a {
      color: #fff;
      text-decoration: none;
    }
    @media (min-width: 768px) {
      footer {
        padding: 0;
        height: 50px;
        display: grid;
        grid-template-columns: 1fr 700px 1fr;
        grid-template-rows: 1fr;
      }
      footer > * {
        grid-column: 2;
        grid-row: 1;
      }
      p {
        justify-self: start;
        align-self: center;
      }
      ul {
        justify-self: end;
        align-self: center;
      }
    }
    @media (min-width: 1024px) {
      footer {
        grid-template-columns: 1fr 980px 1fr;
      }
    }
  </style>
  