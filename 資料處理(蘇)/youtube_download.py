import pytube

#url = input('輸入youtube網址: ')
url = 'https://www.youtube.com/watch?v=E0z6jzd1uwY'
yt = pytube.YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


print('下載完成')