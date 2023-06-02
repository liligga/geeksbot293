"""Модуль для парсинга информации c сайта cars.kg"""
import requests
from bs4 import BeautifulSoup as BS


URL = 'https://cars.kg/offers'
page = 0
end = 'По заданным критериям не найдено ни одного предложения'
while True:
    page += 1
    url = URL + f'/{page}' 
    response = requests.get(url=URL, timeout=10)
    # print(f"{response.status_code=}")
    # print(f"{response.text[:270]=}")
    if response.status_code == 200:
        # проверка что не вышли за последнбб стр
        if response.text.find(end) > -1:
            break
        soup = BS(response.text, 'html.parser')
        cars_list = soup.find('div', class_='catalog-list')
        # print(cars_list.text[:200])
        for c in cars_list.find_all('a', class_='catalog-list-item'):
            model = c.find('span', class_='catalog-item-caption')
            year = model.find(class_='caption-year').text
            model = model.text.replace(f" , {year}", '').strip()
            print(model)