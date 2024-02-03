<template>
  <q-card class="q-py-md" flat square style="height: 100vh">
    <q-toolbar-title class="q-pa-md text-center text-h4">Меню</q-toolbar-title>

    <q-card-section class="no-padding">
      <q-list class="rounded-borders">
        <q-expansion-item
          v-for="item in items"
          :key="item.id"
          :icon="item.icon"
          :label="item.label"
          header-class="text-primary"
        >
          <q-card>
            <q-card-section v-for="food in item.foods" :key="food.name">
              {{ `#${food.id} ${food.label} - ${food.name}` }}
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { FoodCategory } from '@/types/food.types'

const items = ref<FoodCategory[]>([
  {
    id: 1,
    label: 'Гриль',
    name: 'grill',
    icon: 'kebab_dining',
    foods: [
      { id: 1, label: 'Шашлык', name: 'shashlik' },
      { id: 2, label: 'Люля-кебаб', name: 'lula_kebab' }
    ]
  },
  {
    id: 2,
    label: 'Блюда',
    name: 'dishes',
    icon: 'restaurant_menu',
    foods: [
      { id: 1, label: 'Блюда', name: 'main_dishes' },
      { id: 2, label: 'Закуски', name: 'snacks' },
      { id: 3, label: 'Добавки', name: 'additives' },
      { id: 4, label: 'Денер', name: 'doner' }
    ]
  },
  {
    id: 3,
    label: 'Фастфуд',
    name: 'fast_food',
    icon: 'fastfood',
    foods: [
      { id: 5, label: 'Шаверма', name: 'shaverma' },
      { id: 1, label: 'Гамбургеры', name: 'hamburgers' },
      { id: 2, label: 'Чизбургеры', name: 'cheeseburgers' },
      { id: 3, label: 'Хот-доги', name: 'hot_dogs' },
      { id: 4, label: 'Комбо Сет', name: 'combo_set' }
    ]
  },
  {
    id: 4,
    label: 'Напитки',
    name: 'drinks',
    icon: 'local_drink',
    foods: [
      { id: 1, label: 'Алкогольные', name: 'alcoholic_drinks' },
      { id: 2, label: 'Безалкогольные', name: 'soft_drinks' }
    ]
  }
])
</script>
