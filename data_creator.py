import json
from bs4 import BeautifulSoup 
import requests
import csv




f = open('data/final_record.txt')

time_scale = 60
records = 24

final_record = int(f.readline())
url = 'https://chart.nobitex.ir/market/udf/history?symbol=ETHUSDT&resolution='+str(time_scale)+ \
        '&from='+str(final_record-144000)+'&to='+str(final_record)+'&countback='+str(records)+'&currencyCode=%EF%B7%BC'


f.close()


re = requests.get(url)

data = json.loads(re.text)



days = 500


for day in range(days):
    re = requests.get(url)
    data = json.loads(re.text)
    for price in range(len(data['o'])):
        price = -1*price-1
        price_info = [data['t'][price],data['o'][price],data['c'][price],data['h'][price],data['l'][price]]
        with open('data/eth_price.csv',newline='',mode='a') as csv_file:
            record_write = csv.writer(csv_file)
            record_write.writerow(price_info)



    final_record = data['t'][0]
    url = 'https://chart.nobitex.ir/market/udf/history?symbol=ETHUSDT&resolution='+str(time_scale)+ \
        '&from='+str(final_record-144000)+'&to='+str(final_record)+'&countback='+str(records)+'&currencyCode=%EF%B7%BC'
    f = open('data/final_record.txt',mode="w")
    f.write(str(final_record))
    f.close()
    print(str(day) + ' from today')



