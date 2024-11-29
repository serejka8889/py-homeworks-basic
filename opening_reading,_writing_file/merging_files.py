import os
from pathlib import Path

def merging_files(output_file, input_files):

    list_info = []  # Список для хранения информации

    for filename in input_files: 
        with open(Path(__file__).parent / filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
        list_info.append((filename, len(content), content))
    
    # Сортируем файлы по количеству строк
    sorted_files = sorted(list_info, key=lambda x: x[1])  # сортировка по второму элементу
    
    # Открываем output_file и записываем туда данные, последовательно.
    with open(Path(__file__).parent / output_file, 'w') as f:
        for filename, line_count, content in sorted_files:
            f.write(f'{filename}\n')
            f.write(f'{line_count}\n')
            f.writelines(f'{content}\n')
            f.write('\n')  

# Выполняем объединение
files_input = ['1.txt', '2.txt', '3.txt']  # Список файлов для объединения

file_output = 'all.txt'

merging_files(file_output, files_input)

# Отображаем на экране монитора
opens = open(Path(__file__).parent / "all.txt", "r")

files = opens.read()

print(files)

