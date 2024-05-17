import json
import logging


def struct(json_path):
    # Чтение данных из JSON файла
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Создание структурированного файла
    structured_data = {}
    for item in data:
        faculty_name = item['faculty_name']
        department = item['department']

        if faculty_name not in structured_data:
            structured_data[faculty_name] = {}

        if department not in structured_data[faculty_name]:
            structured_data[faculty_name][department] = []

        structured_data[faculty_name][department].append({
            'post': item['post'],
            'user_link': item['user_link'],
            'fio': item['fio']
        })

    # Запись структурированных данных в новый файл
    with open(json_path, 'w') as file:
        json.dump(structured_data, file, ensure_ascii=False, indent=4)

def add_state(json_path,fio,state,url):

    # Открываем файл и загружаем данные
    with open(json_path, 'r') as file:
        data = json.load(file)

    for faculty in data.values():
        for department in faculty.values():
            for obj in department:
                if obj['fio'] == fio:
                    try:
                        states = obj['states']
                        logging.warning(states)
                        states_add = ({'state': state, 'url': url})
                        states.append(states_add)
                        logging.warning(states)
                        obj['states'] = states

                    except KeyError:
                        obj['states'] = [{'state':state, 'url': url}]

    # Записываем измененные данные обратно в файл
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)