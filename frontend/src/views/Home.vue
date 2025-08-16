<template>
    <div class="container d-flex justify-content-between align-items-center mt-3 mb-2">
        <h1 class="mb-0">Gestor de Despesas</h1>
        <AddCategoria/>
    </div>
    <div class="container py-4">
        <div class="row g-4">
            <!-- Coluna esquerda -->
            <div class="col-lg-8">
                <div class="row g-4 mb-4">
                    <div class="col-md-6">
                        <div class="p-4 bg-white rounded shadow">
                            <Saldo/>
                        </div>
                    </div>

                    <div class="col-md-6">
                        <div class="p-4 bg-white rounded shadow">
                            <Receita/>
                        </div>
                    </div>
                </div> 
                
                <div class="p-4 bg-white rounded shadow tabela">
                    <Tabela/>
                </div>
            </div>

            <!-- Coluna direita -->
            <div class="col-lg-4">
                <div class="p-4 bg-white rounded shadow mb-4">
                    <Donut/>
                </div>

                <div class="p-4 bg-white rounded shadow">
                    <Filters/>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import AddCategoria from '@/components/AddCategoria.vue';
import Tabela from '@/components/Tabela.vue';
import Donut from '@/components/Donut.vue';
import Receita from '@/components/Receita.vue';
import Filters from '@/components/Filters.vue';
import Saldo from '@/components/Saldo.vue';

</script>

<style scoped>

</style>