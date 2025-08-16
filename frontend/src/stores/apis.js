import { defineStore } from 'pinia'
import axios from 'axios'

export const useApiStore = defineStore('api', {
  state: () => ({
    transacoes: [],
    categorias: [],
    resumo: { saldo: 0, total_receitas: 0, total_despesas: 0 },
    grafico: {},  
    loading: false,
    error: null,

    // filtros
    filtroDataInicio: null,
    filtroDataFim: null,
    filtroCategoria: null,
  }),
  
  actions: {
    async getTransacoes() {
      this.loading = true
      this.error = null
      try {
        const resposta = await axios.get(`http://localhost:8000/api/transacoes/`)
        this.transacoes = resposta.data
      } catch (err) {
        this.error = 'Erro ao buscar transações'
        this.transacoes = null
      } finally {
        this.loading = false
      }
    },

    async getCategorias() {
      this.loading = true
      this.error = null
      try {
        const resposta = await axios.get(`http://localhost:8000/api/categorias/`)
        this.categorias = resposta.data
      } catch (err) {
        this.error = 'Erro ao buscar transações'
        this.categorias = null
      } finally {
        this.loading = false
      }
    },

    async getResumo() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get(`http://localhost:8000/api/transacoes/resumo/`)
        this.resumo = response.data
      } catch (err) {
        this.error = 'Erro ao buscar transações'
        this.categorias = null
      } finally {
        this.loading = false
      }
    },

    async getGrafico() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get(`http://localhost:8000/api/transacoes/por_categoria/`)
        this.grafico = response.data
      } catch (err) {
        this.error = 'Erro ao buscar grafico'
        this.categorias = null
      } finally {
        this.loading = false
      }
    },

    async getTransacoesComFiltro() {
      this.loading = true
      this.error = null
      try {
        // monta parâmetros de query com os filtros
        const params = {}
        if (this.filtroDataInicio) params.data_inicio = this.filtroDataInicio
        if (this.filtroDataFim) params.data_fim = this.filtroDataFim
        if (this.filtroCategoria) params.categoria = this.filtroCategoria

        const resposta = await axios.get(`http://localhost:8000/api/transacoes/`, { params })
        this.transacoes = resposta.data
      } catch (err) {
        this.error = 'Erro ao buscar transações'
        this.transacoes = []
      } finally {
        this.loading = false
      }
    },
  }
})