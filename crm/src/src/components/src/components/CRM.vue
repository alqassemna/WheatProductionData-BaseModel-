<template>
  <div>
    <h2>Stakeholder CRM</h2>
    <StakeholderList :stakeholders="stakeholders" />
    <!-- Add forms to add/edit stakeholders -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import StakeholderList from './StakeholderList.vue'

const stakeholders = ref([])

onMounted(async () => {
  const res = await axios.get('/crm/stakeholders')
  stakeholders.value = res.data
})
</script>
