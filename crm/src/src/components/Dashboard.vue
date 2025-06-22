<template>
  <div>
    <h2>Wheat Production Dashboard</h2>
    <!-- Use charting lib to visualize data -->
    <ProductionChart :data="productionData" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ProductionChart from './ProductionChart.vue'

const productionData = ref([])

onMounted(async () => {
  const res = await axios.get('/dashboard/production')
  productionData.value = res.data
})
</script>
