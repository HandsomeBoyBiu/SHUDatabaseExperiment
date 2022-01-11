<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import Axios from 'axios'
Axios.defaults.baseURL='127.0.0.1:8000/polls'
export default {
  name: 'App'
}
</script>
