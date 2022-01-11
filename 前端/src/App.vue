<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import Axios from 'axios'
Axios.defaults.baseURL='http://127.0.0.1:8000'
export default {
  name: 'App'
}
</script>
