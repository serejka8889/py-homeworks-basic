from pathlib import Path
from pprint import pprint

def read_cookbook(file_path):
    cook_book = {}
    
    with open(file_path, "r", encoding='utf-8') as file:
        while True:
            # Чтение названия рецепта
            dish_name = file.readline().strip()
            
            if not dish_name:
                break
                
            # Чтение количества ингредиентов
            ingredient_count = int(file.readline())
            
            ingredients = []
            for _ in range(ingredient_count):
                # Чтение строки с ингредиентом
                ingredient_data = file.readline().strip().split(' | ')
                name, quantity, measure = ingredient_data
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            # Добавление рецепта в словарь
            cook_book[dish_name] = ingredients
            
            # Пропуск пустой строки между рецептами
            file.readline()
    
    return cook_book


file_path = Path(__file__).parent / 'recipes.txt'  # Путь к вашему файлу с рецептами
cook_book = read_cookbook(file_path)
pprint(cook_book)