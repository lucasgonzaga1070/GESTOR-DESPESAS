<template>
    <h3>Saldo</h3>
    <h2>R$ {{ store.resumo.saldo.toFixed(2) }}</h2>
</template>

<script setup>

import { onMounted } from 'vue'
import { useApiStore } from '@/stores/apis.js'

const store = useApiStore()

// Função para carregar as transações
const loadResumo = () => {
  store.getResumo()
}

onMounted(() => {
  loadResumo()
})

</script>

<style scoped>

h3{
    color: #585757;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

</style>