from pprint import pprint
from pathlib import Path

# Функция чтения списка рецептов из файла
def read_cookbook(f_path):

    cook_book = {} # Пустой словарь для хранения рецептов
    
    with open(f_path, 'r', encoding='utf-8') as f:
        while True:
            # Читаем названия рецепта
            name_dish = f.readline().strip()
            
            # Проверяем, если название блюда
            if not name_dish:
                break
                
            # Получаем количество ингредиентов
            ingredient_count = int(f.readline())
            
            ingredients = [] # Список для хранения ингредиентов

            for _ in range(ingredient_count):
                # Считваем строки с ингредиентами
                ingredient_data = f.readline().strip().split(' | ')
                name, quantity, measure = ingredient_data
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            # Добавляем рецепт в словарь
            cook_book[name_dish] = ingredients
            
            f.readline() # Пропуск строки
    
    return cook_book

# Функция создания списка покупок
def get_shopping_list_by_dishes(dishes, person_count):

    shopping_list = {}
    
    for dish in dishes: # Проходимся по каждому блюду
        for ingredient in cook_book[dish]: # Проходимся по каждому ингредиенту в блюде
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name in shopping_list:
                shopping_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shopping_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    
    return shopping_list

f_path = Path(__file__).parent / 'recipes.txt'
cook_book = read_cookbook(f_path)

#---------------------------------------------------------------
# Добавить необходимые названия блюд
dishes = ['Запеченный картофель', 'Омлет']
# Добавить необходимое количество персон
person_count = 2
#---------------------------------------------------------------

shopping_list = get_shopping_list_by_dishes(dishes, person_count)

# Получаем
print('\n-----------------------------------------------------------------------------------------\n')
print('Имеющийся список блюд в словаре:\n')
pprint(cook_book)
print('\n-----------------------------------------------------------------------------------------\n')
print('Список индигриентов с выданным количеством:\n')
pprint(shopping_list)
print('\n')
