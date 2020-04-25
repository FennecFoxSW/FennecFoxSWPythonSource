import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


CORONA_REGION_MAP = {
    "서울": 7,
    "부산": 8,
    "대구": 9,
    "인천": 10,
    "광주": 11,
    "대전": 12,
    "울산": 13,
    "세종": 14,
    "경기": 15,
    "강원": 16,
    "충북": 17,
    "충남": 18,
    "전북": 19,
    "전남": 20,
    "경북": 21,
    "경남": 22,
    "제주": 23,
    "검역": 24,
}

REMOVE_TAG_REGEXP = '<.+?>'

now = datetime.now()
url = "http://ncov.mohw.go.kr/"
request = requests.get(url)
print(f'{now} - {url} - {request.status_code} - {request.ok}')

soup = BeautifulSoup(request.text, 'html.parser')

livedate_html = soup.find('span', {'class': 'livedate'})
livedate = re.sub(REMOVE_TAG_REGEXP, "", str(livedate_html)).strip()  # 기준 날짜

numbers_html = soup.find_all('span', {'class': 'num'})
confirmed = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[0])).strip() + '명'  # 확진환자
recovered = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[1])).strip() + '명'  # 완치
quarantined = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[2])).strip() + '명'  # 치료중
deceased = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[3])).strip() + '명'  # 사망
tests_performed = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[4])).strip()  # 누적 검사수
tests_concluded = re.sub(REMOVE_TAG_REGEXP, "", str(numbers_html[5])).strip()  # 누적 검사완료수

daily_confirmed_html = soup.find('span', {'class': 'data1'})
daily_confirmed = re.sub(REMOVE_TAG_REGEXP, "", str(daily_confirmed_html)).strip()  # 일일 확진자

daily_recovered_html = soup.find('span', {'class': 'data2'})
daily_recovered = re.sub(REMOVE_TAG_REGEXP, "", str(daily_recovered_html)).strip()  # 일일 완치자

numbers = soup.find_all('span', {'class': 'before'})
confirmed_daily_change = re.sub(REMOVE_TAG_REGEXP, "", str(numbers[0])).strip().replace("전일대비 ", "")  # 확진환자 전일대비
recovered_daily_change = re.sub(REMOVE_TAG_REGEXP, "", str(numbers[1])).strip().replace("전일대비 ", "")  # 완치 전일대비
quarantined_daily_change = re.sub(REMOVE_TAG_REGEXP, "", str(numbers[2])).strip().replace("전일대비 ", "")  # 치료중 전일대비
deceased_daily_change = re.sub(REMOVE_TAG_REGEXP, "", str(numbers[3])).strip().replace("전일대비 ", "")  # 사망 전일대비

region = "서울"  # CORONA_REGION_MAP의 키
region_numbers = soup.find_all('span', {'class': 'num'})
region_confirmed = re.sub(REMOVE_TAG_REGEXP, "", str(region_numbers[region])).strip()  # 지역별 확진환자
