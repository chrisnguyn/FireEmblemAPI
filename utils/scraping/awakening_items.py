import requests
from bs4 import BeautifulSoup
from collections import defaultdict

item_dict = defaultdict(str)
response = requests.get('https://fireemblem.fandom.com/wiki/List_of_items_in_Fire_Emblem_Awakening')
data = BeautifulSoup(response.content, features='html.parser')
items = data.find_all('tr')

for item in items:
    info = item.text.split('\n')

    if not info[0]:
        key, desc = info[1], info[7]

        if key == 'Name':
            continue
        else:
            item_dict[key] = desc

for k, v in item_dict.items():
    print(f'{k} - {v}')
    print('\n')
