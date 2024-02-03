<template>
  <q-card>
    <q-card-section>{{ text }}</q-card-section>
  </q-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const text = ref<string>('Карточка блюда')
</script>
