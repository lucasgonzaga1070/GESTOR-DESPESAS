<template>
    <h2>Filtros</h2>
    <form>
        <div class="d-flex align-items-center">
            <input type="date" v-model="store.filtroDataInicio" class="form-control me-2 mb-2" placeholder="Data" required>
            <input type="date" v-model="store.filtroDataFim " class="form-control mb-2" placeholder="Data" required>
        </div>

        <select v-model.number="store.filtroCategoria" class="form-control me-2 mb-2" required>
            <option value="" disabled selected>Categoria</option>
            <option v-for="cat in store.categorias" :key="cat.id" :value="cat.id">
                {{ cat.nome }}
            </option>
        </select>

        <button type="submit" @click="filtrar" class="btn btn-primary">Filtrar</button>
    </form>
</template>

<script setup>

import { onMounted, reactive } from 'vue'
import { useApiStore } from '@/stores/apis.js'

const store = useApiStore()

const loadCategorias = () => {
  store.getCategorias()
}

const form = reactive({
  data_min: '',
  data_max: '',
  categoria: '',
})

onMounted(() => {
  loadCategorias()
})

const filtrar = async () => {
    store.getTransacoesComFiltro()
}


</script>

<style></style>