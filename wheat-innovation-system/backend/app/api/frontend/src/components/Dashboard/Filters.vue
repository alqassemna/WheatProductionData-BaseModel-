<template>
  <div>
    <DatePicker v-model="start" label="Start Date"/>
    <DatePicker v-model="end" label="End Date"/>
    <SelectType v-model="selectedTypes" :options="typeOptions"/>
    <button @click="apply">Apply Filters</button>
  </div>
</template>
<script setup lang="ts">
import { ref, defineEmits } from 'vue'
const emit = defineEmits(['update:filters'])
const start = ref<Date|null>(null)
const end = ref<Date|null>(null)
const selectedTypes = ref<string[]>([])
const typeOptions = ['Yield', 'Import', 'Planted Area', 'Harvested Area']
function apply() {
  emit('update:filters', {start: start.value, end: end.value, types: selectedTypes.value})
}
</script>
