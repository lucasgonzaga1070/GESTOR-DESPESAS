// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  // { path: '/filme/:id', name: 'Detalhes', component: Detalhes, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router