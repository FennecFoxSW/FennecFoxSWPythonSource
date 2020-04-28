import requests
from bs4 import BeautifulSoup as bsoup

baseurl = 'https://datalab.naver.com/keyword/realtimeList.naver?'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
req = requests.get(baseurl, headers={'User-Agent': ua})

html = req.text
soup = bsoup(html, 'html.parser')

titles = soup.select('li.ranking_item span.item_title')
print(titles)
