import requests
from bs4 import BeautifulSoup
import json_struct
def scholar_search(fio,json_path):
    # Указываем url
    query = fio.replace(" ", "+")
    url = f'https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q={query}'

    # Отправляем GET-запрос по указанной ссылке
    response = requests.get(url)

    # Парсим HTML-разметку с помощью BS
    soup = BeautifulSoup(response.content, 'html.parser')

    #Находим все заголовки результатов
    results = soup.find_all('h3', class_='gs_rt')

    # Извлекаем названия и ссылки из заголовков
    articles = []
    for result in results:
        link = result.find('a')['href']
        title = result.text
        title = title.replace("[HTML]", "")
        title = title.replace("[PDF]", "")
        articles.append({'title': title, 'link': link})
    # print(articles)
    print("Были найденны и записаны статьи:")
    for article in articles:
        print("     Название", article["title"])
        print("         Ссылка", article["link"])
        # print(f'<a href="{article["link"]}">{article["title"]}</a>')
        json_struct.add_state(json_path,fio,article["title"],article["link"])
