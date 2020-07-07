import requests
from prettytable import PrettyTable

from bs4 import BeautifulSoup

url = 'https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Tue%20Jul%2007%202020%2015:39:28%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)'

source_code = requests.get(url,
                           headers = {
                               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                               'Referer':'https://www.cwb.gov.tw/V8/C/P/Warning/W29.html',
                               'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
                               })

html_sourcecode= BeautifulSoup(source_code.text, 'html.parser')

city_list = []
city = html_sourcecode.find_all('th')
for ele in city:
    city_list.append(ele.text)

temperature_list = []
temperature = html_sourcecode.find_all('span', class_='tem-C')
for ele in temperature:
    temperature_list.append(ele.text)

full_info = []
if len(temperature_list) == len(city_list):
    for i in range(len(temperature)):
        temp = []
        temp.append(city_list[i])
        temp.append(temperature_list[i])
        full_info.append(temp)
else:
    print('!error')

table = PrettyTable()
table.field_names = ['地區','氣溫']
for i in range(len(full_info)):
        table.add_row(full_info[i])

print(table)

