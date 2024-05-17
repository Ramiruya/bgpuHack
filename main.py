import os
import subprocess
import json_struct
import os.path
import shutil
import search_fio
import search_states
# Парсер сайта БГПУ для хакатона

# Запуск парсера сайта БГПУ
def run_spider(spider_name, json):
    process = subprocess.Popen(['scrapy', 'runspider', spider_name, '-o', json])
    process.wait()

def main():
    # Временный JSON
    json_tmp = './data_tmp.json'
    # Основной JSON с результатами с гугла по фио
    json_bspu = './data.json'

    try:
        os.remove(json_tmp)
    except FileNotFoundError:
        pass
    #Считываем пользовательский запрос, предлагая варианты действий
    if os.path.exists(json_bspu):
        print("\n\n\nДанные сотрудников БГПУ уже имеются\n"
              " 1 - Спарсить заново\n"
              " 2 - Продолжить с имеющимися данными"
              "\n Нажмите любую клавишу для продолжения с имеющимися данными")
        choose = input('1,2,Enter: ')
        match choose:
            case '1':
                # Запуск парсинга БГПУ
                run_spider('./spiders/bspu_spider.py', json_tmp)
                # Структурирование полученного json
                json_struct.struct(json_tmp)
                # Создание основного файла
                shutil.copyfile(json_tmp, json_bspu)
                main()
            case '2':
                print('\n\n\nВыберите тип поиска:'
                      '\n 1 - Поиск по ФИО, поулчение списка статей'
                      '\n 2 - Поиск по статье в локальной базе данных')
                choose = input('1,2: ')
                match choose:
                    case '1':
                        search_fio.select_fio(json_bspu)
                        main()
                    case '2':
                        search_states.select_states(json_bspu)
                        main()
                    case _:
                        main()
            case _:
                print('\n\n\nВыберите тип поиска:'
                      '\n 1 - Поиск по ФИО, поулчение списка статей'
                      '\n 2 - Поиск по статье в локальной базе данных')
                choose = input('1,2: ')
                match choose:
                    case '1':
                        search_fio.select_fio(json_bspu)
                        main()
                    case '2':
                        search_states.select_states(json_bspu)
                        main()
                    case _:
                        main()
                main()
main()