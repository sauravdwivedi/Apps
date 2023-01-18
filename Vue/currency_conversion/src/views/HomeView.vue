<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <ApiCall/>
  </div>
</template>

<script>
import ApiCall from '@/components/ApiCall.vue'

export default {
  name: 'HomeView',
  components: {
    ApiCall
  }
}
</script>
