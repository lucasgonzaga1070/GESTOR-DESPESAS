<template>
  <h2>Transações</h2>
  
  <div class="table-cotainer">
    <table class="table table-hover">
      <thead>
          <tr>
            <th scope="col">Data</th>
            <th scope="col">Descrição</th>
            <th scope="col">Valor</th>
            <th scope="col">Categoria</th>
            <th scope="col">#</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transacao in store.transacoes" :key="transacao.id">
            <td>{{ transacao.data }}</td>
            <td>{{ transacao.descricao }}</td>
            <td>{{ transacao.valor }}</td>
            <td>{{ transacao.categoria }}</td>
            <td><button class="btn btn-danger" @click="deleteTransacao(transacao.id)"><i class="bi bi-trash"></i></button></td>
          </tr>
        </tbody>
    </table>
  </div>
  <form class="d-flex align-items-center">
    <input type="date" v-model="form.data" class="form-control me-2" placeholder="Data" required>
    <input type="text" v-model="form.descricao" class="form-control me-2" placeholder="Descrição" required>
    <input type="number" v-model.number="form.valor" class="form-control me-2" placeholder="Valor" required>
    <select v-model.number="form.categoria" class="form-control me-2" required>
      <option v-for="cat in store.categorias" :key="cat.id" :value="cat.id">
        {{ cat.nome }}
      </option>
    </select>
    <button type="submit" @click="enviarPost" class="btn btn-primary">Adicionar</button>
  </form>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useApiStore } from '@/stores/apis.js'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const store = useApiStore()

// Função para carregar as transações
const loadTransacoes = () => {
  store.getTransacoes()
}

const loadCategorias = () => {
  store.getCategorias()
}

onMounted(() => {
  loadTransacoes()
  loadCategorias()
})

// Função para adicionar uma nova transação
 const form = reactive({
  data: '',
  descricao: '',
  valor: 0,
  categoria: '',
});

const enviarPost = async () => {
  console.log('Enviando dados:', JSON.stringify(form))
  try {
    const response = await axios.post('http://localhost:8000/api/transacoes/', form)
    console.log('Resposta da API:', response.data)
      form.data = ''
      form.descricao = ''
      form.valor = 0
      form.categoria = ''
  } catch (error) {
    console.error('Erro ao enviar POST:', error)
  }
}

const id_delete = ref(null)

const deleteTransacao = async (id) => {
  try{
    const response = await axios.delete(`http://127.0.0.1:8000/api/transacoes/${id}/`)
    console.log('Transação deletada:', response.data)
    loadTransacoes() // Recarrega as transações após a exclusão
  } catch (error) {
    console.error('Erro ao deletar transação:', error)
  }
}
</script>

<style scoped>

.table-cotainer {
  height: 350px;
  max-height: 350px;
  overflow-y: auto;
}

</style>