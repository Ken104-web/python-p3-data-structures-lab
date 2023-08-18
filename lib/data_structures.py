spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for n in spicy_foods:
        names.append(n['name'])
    return names


def get_spiciest_foods(spicy_foods):
   return [n for n in spicy_foods if n["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get('cuisine')
        heat = food.get('heat_level') * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat}")
      
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    n = []
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
    return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = '🌶' * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    pass

def get_average_heat_level(spicy_foods):
    n = []
    for food in spicy_foods:
        n.append(food["heat_level"])
    value = (n[0] + n[1] + n[2]) / len(spicy_foods)
    return value
    pass

def create_spicy_food(spicy_foods, spicy_food):
    new_Arr = spicy_foods
    new_Arr.append({
                "name": spicy_food["name"],
                "cuisine": spicy_food["cuisine"],
                "heat_level": spicy_food["heat_level"],
            })
    return new_Arr
    pass
