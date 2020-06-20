import sys
import os

url = sys.argv[-1]
if url[-1] != '28廖勛仕homework2.py':
    print(f'開啟網址: {url}')
    os.system(f'"C:/Program Files/Internet Explorer/iexplore.exe" {url}')