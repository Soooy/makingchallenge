import requests
from bs4 import BeautifulSoup
import random

data = requests.get('https://www.subway.co.kr/menuView/sandwich?menuItemIdx=1444')
soup = BeautifulSoup(data.text, 'html.parser')

# table = soup.find_all('table')
table = soup.find('table').text
table = soup.select('#content > div > div.menu_content > div.component_chart > div > div.board_list_wrapper > table > tbody > tr')

for t in table:

    print(t)

# data = soup.select_one('#content > div > div.menu_content > div.component_chart > div > div.board_list_wrapper > table > thead > tr').text
# cal = soup.select_one('#content > div > div.menu_content > div.component_chart > div > div.board_list_wrapper > table > tbody > tr').text
#
# print(data, cal)

# for d in data:
#     table = d.li.select_one
#     print(table)
#
