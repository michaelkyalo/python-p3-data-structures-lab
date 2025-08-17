# lib/data_structures.py

# lib/data_structures.py

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

# 1. Return list of names
def get_names(foods):
    return [food["name"] for food in foods]

# 2. Return foods with heat_level > 5
def get_spiciest_foods(foods):
    return [food for food in foods if food["heat_level"] > 5]

# 3. Print foods in the required format
def print_spicy_foods(foods):
    for food in foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# 4. Find food by cuisine
def get_spicy_food_by_cuisine(foods, cuisine):
    for food in foods:
        if food["cuisine"] == cuisine:
            return food

# 5. Print only spiciest foods
def print_spiciest_foods(foods):
    spiciest = get_spiciest_foods(foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)

# 7. Add a new spicy food
def create_spicy_food(foods, new_food):
    foods.append(new_food)
    return foods
