import json

# Загружаем JSON файл
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Функция для поиска и вывода значений
def find_and_print_values(data, search_state):
    for faculty in data.values():
        for department in faculty.values():
            for member in department:
                if 'states' in member:
                    for state in member['states']:
                        if state['state'] == search_state:
                            print(f"Post: {member.get('post')}")
                            print(f"FIO: {member.get('fio')}")
                            print(f"User Link: {member.get('user_link')}")
                            print("---")

# Искомое значение state
search_state = "Члены рабочей группы"

# Вызываем функцию для поиска и вывода
find_and_print_values(data, search_state)