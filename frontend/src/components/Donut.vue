<template>
    <h2>Gastos por Categoria</h2>

    <canvas id="myDonutChart"></canvas>
</template>

<script setup>
import { onMounted } from 'vue'
import { Chart, DoughnutController, ArcElement, Tooltip, Legend } from 'chart.js'
import { useApiStore } from '@/stores/apis.js'

const store = useApiStore()

Chart.register(DoughnutController, ArcElement, Tooltip, Legend)

function gerarCores(qtd) {
  return Array.from({ length: qtd }, () =>
    `hsl(${Math.floor(Math.random() * 360)}, 70%, 50%)`
  )
}

onMounted(async () => {
  // Espera os dados chegarem
  await store.getGrafico()

  const categorias = store.grafico.map(item => item.categoria__nome)
  const totais = store.grafico.map(item => item.total)
  const cores = gerarCores(categorias.length)

  const ctx = document.getElementById('myDonutChart').getContext('2d')

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: categorias,
      datasets: [
        {
          label: 'Valores',
          data: totais,
          backgroundColor: cores,
          borderWidth: 1
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom'
        }
      }
    }
  })
})
</script>


<style scoped>

#myDonutChart {
  max-width: 300px;
  max-height: 300px;
  margin: auto;
  display: block;
}

</style>