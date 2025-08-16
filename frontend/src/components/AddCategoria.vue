<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-outline-dark" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Adicionar Categoria
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
          <div class="modal-content">

            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Adicionar categoria</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
              <form class="d-flex align-items-center">
                <input v-model="form.nome" type="text" class="form-control me-2" placeholder="Nome" required>

                <select v-model="form.tipo" class="form-control me-2" required>
                  <option value="receita">Receita</option>
                  <option value="despesa">Despesa</option>
                </select>

                <button type="submit" @click="enviarPost" class="btn btn-primary">Adicionar</button>
              </form>
            </div>
          </div>
      </div>
    </div>
</template>

<script setup>

import { onMounted, reactive, ref } from 'vue'
import { useApiStore } from '@/stores/apis.js'
import axios from 'axios'

const myModalEl = ref(null)
const myInputEl = ref(null)

onMounted(() => {
  if (myModalEl.value) {
    myModalEl.value.addEventListener('shown.bs.modal', () => {
      myInputEl.value?.focus()
    })
  }
})

const store = useApiStore()

const loadCategorias = () => {
  store.getCategorias()
}

onMounted(() => {
  loadCategorias()
})

const form = reactive({
  nome: '',
  tipo: ''
})

const enviarPost = async () => {
  try {
    await axios.post('http://localhost:8000/api/categorias/', form)
    form.nome = ''
    form.tipo = ''
  } catch (error) {
    console.error('Erro ao enviar POST:', error)
  }
}

</script>