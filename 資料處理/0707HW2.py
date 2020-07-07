import requests
import json
import os
from prettytable import PrettyTable

class Searcher:
    def main(self):
        item_name = input('請輸入關鍵字 : ')
        print(item_name)
        url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={item_name}&page=1&sort=sale/dc'
        #print(url)

        json_file = requests.get(url)
        json_content = json.loads(json_file.text)
        max_page = int(json_content['totalPage'])
        while True:
            #print(url)
            json_file = requests.get(url)
            json_content = json.loads(json_file.text)

            goods_list = []
            goods_pagelist = json_content['prods']
            for i in range(len(goods_pagelist)):
                temp_list = []
                temp_list.append(goods_pagelist[i]["name"])
                temp_list.append(goods_pagelist[i]['price'])
                goods_list.append(temp_list)


            table = PrettyTable()
            table.field_names = ['名稱','價格']
            for i in range(len(goods_list)):
                table.add_row(goods_list[i])

            print(table)
            page_number = input('前往頁碼: ')
            if int(page_number) > max_page:
                print('頁碼超過範圍!')
                break
            url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+item_name+'&page='+page_number+'&sort=sale/dc'
            os.system('cls')

if __name__ == '__main__':
    a = Searcher()
    a.main()