import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import os

# 清空畫面
os.system('cls')

# 取得相關參數
filename = input('請輸入圖片檔名: ')
watermark_content  = input('請輸入浮水印內容: ')
watermark_size = input('請輸入浮水印尺寸(px): ')

# 從cv2讀圖
image0 = cv2.imread(filename, 1)

# 把圖丟進cv2
PIL_image = Image.fromarray(image0)

# 加入文字
ImageDraw.Draw(PIL_image).text((0,0), watermark_content, (0,0,255), ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', int(watermark_size)))

# 轉回cv2資料型別
image0 = np.array(PIL_image)

# 印出圖片尺寸
print(image0.shape[0])

# 顯示出圖片!
cv2.imshow('Image: test', image0)
cv2.waitKey(0)
cv2.destroyAllWindows()