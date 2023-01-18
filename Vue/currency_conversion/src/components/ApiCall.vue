<template>
  <div class="container">
      <h1>{{ selectedOne }} to {{ selectedTwo }} conversion rate</h1>
      <p>1 <select v-model="selectedOne">
            <option :value="null">select currency</option>
            <option 
              v-for="(currency, index) in currencies" 
              :value="index"
              :key="currency">{{ index }}: {{ currency }}</option>
        </select>
       = <b>{{ rate }}</b> <select v-model="selectedTwo" @change="apiCall">
            <option :value="null">select currency</option>
            <option 
              v-for="(currency, index) in currencies" 
              :value="index"
              :key="currency">{{ index }}: {{ currency }}</option>
        </select> at {{ time }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import moment from "moment"

export default {
  data() {
    return {
      title: 'SEK to INR conversion rate',
      rate: 'NULL',
      time: 'NULL',
      selectedOne: null,
      selectedTwo: null,
      currencies: {
        "SEK": "Swedish Krona",
        "INR": "Indian Rupee",
      },
    }
  },
  methods: {
    async apiCall() {
      await axios.get(`https://api.apilayer.com/currency_data/convert?to=${this.selectedTwo}&from=${this.selectedOne}&amount=1`, 
        {
          headers: {'apikey': 'lWHgvT1oGQVVxprbrVswsTroUUG2DYYj'}
        })
      .then((response) => {
        console.log(response);
        const res = response.data;
        this.rate = res.info.quote;
        this.time = moment(res.info.timestamp * 1000).format("MMMM Do YYYY, h:mm:ss a");
      })
      .catch((errors) => {
        console.log(errors);
      });
    },
    async loadCurrencies() {
      await axios.get('https://api.apilayer.com/currency_data/list', 
        {
          headers: {'apikey': 'lWHgvT1oGQVVxprbrVswsTroUUG2DYYj'}
        })
      .then((response) => {
        console.log(response);
        const res = response.data;
        this.currencies = res.currencies;
      })
      .catch((errors) => {
        console.log(errors);
      });
    },
    async onClick() {
      await this.apiCall();
    }
  },
  mounted() {
    this.loadCurrencies();
  }
} 
</script>