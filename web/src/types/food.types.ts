interface Food {
  id: number
  label: string
  name: string
}

interface FoodCategory {
  id: number
  label: string
  name: string
  icon: string
  foods: Food[]
}

export type { FoodCategory, Food }
