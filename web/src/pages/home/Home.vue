<template>
  <q-card flat square class="q-pa-md" style="height: 100vh">
    <q-toolbar-title class="q-pa-md text-center text-h4">Меню</q-toolbar-title>

    <q-card-section>
      <q-list bordered class="rounded-borders">
        <q-expansion-item
            v-for="item in items"
            :key="item.id"
            expand-separator
            header-class="text-primary"
            :label="item.label"
            :icon="item.icon"
        >
          <q-card>
            <q-card-section>
              {{ `#${item.id} ${item.label} - ${item.name}` }}
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-list>
    </q-card-section>
  </q-card>

</template>

<script setup lang="ts">
//


const items = [
  {
    id: 1,
    label: 'Шашлык',
    name: 'shashlik',
    icon: 'kebab_dining',
  },
  {
    id: 2,
    label: 'Люля-кебаб',
    name: 'lula_kebab',
    icon: 'kebab_dining',
  },
  {
    id: 3,
    label: 'Блюда',
    name: 'dishes',
    icon: 'food',
  },
  {
    id: 4,
    label: 'Закуски',
    name: 'snacks',
    icon: 'food',
  },
  {
    id: 5,
    label: 'Добавки',
    name: 'additives',
    icon: 'food',
  },
  {
    id: 6,
    label: 'Шаверма в лаваше',
    name: 'shawarma',
    icon: 'food',
  },
  {
    id: 7,
    label: 'Денер',
    name: 'doner',
    icon: 'food',
  },
  {
    id: 8,
    label: 'Гамбургеры',
    name: 'hamburgers',
    icon: 'food',
  },
  {
    id: 9,
    label: 'Чизбургеры',
    name: 'cheeseburgers',
    icon: 'food',
  },
  {
    id: 10,
    label: 'Хот-доги',
    name: 'hot_dogs',
    icon: 'food',
  },
  {
    id: 11,
    label: 'Комбо Сет',
    name: 'combo_set',
    icon: 'food',
  },
  {
    id: 12,
    label: 'Напитки',
    name: 'drinks',
    icon: 'food',
  }
];

</script>
