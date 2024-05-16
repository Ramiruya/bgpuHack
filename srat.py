
import requests
from bs4 import BeautifulSoup
import json

def getArticleUrls(query):
    url = f'https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articleTitles = []
    for result in soup.find_all('div', class_='gs_r'):
        title = result.find('h3', class_='gs_rt')
        if title:
            titleText = title.text
            titleText = titleText.replace("[HTML]", "")
            titleText = titleText.replace("[PDF]", "")
            articleTitles.append(titleText)
            print(titleText)
        else:
            titleText = 'Заголовок не найден'
    
    return articleTitles

query = input('введите фио преподавателя: ')
query = query.replace(" ", "+")
articleUrls = getArticleUrls(query)
jsonData = json.dumps(articleUrls, indent=4, ensure_ascii=False)
with open('articles.json', 'w') as file:
    file.write(jsonData)
