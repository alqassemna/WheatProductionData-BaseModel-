<template>
  <div>
    <h2>Impact Pathway</h2>
    <!-- Visualize nodes/edges as a graph (use vis.js, cytoscape, etc.) -->
    <ImpactGraph :nodes="nodes" :edges="edges" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ImpactGraph from './ImpactGraph.vue'

const nodes = ref([])
const edges = ref([])

onMounted(async () => {
  nodes.value = (await axios.get('/impact/pathway/nodes')).data
  edges.value = (await axios.get('/impact/pathway/edges')).data
})
</script>
