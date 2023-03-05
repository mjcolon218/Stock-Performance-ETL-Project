# Importing Modules/Libraries.
# Python Script to pull Data from Polygon and Write to CSV files.

import csv
import requests
import time
from config import key

stocks = ["AAPL","DIS","TSLA","SBUX","HMC"]
for stock in stocks:
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-05-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data = requests.get(url)
    json_data = data.json()
    results = json_data['results']


# Creating empty list to store target data.
# Filtering out necessary components from json structure
    stock_data = []
    for day in results:
        closing_price = day['c']
        time_price = day['t']
        real_time = time.strftime('%Y-%m-%d', time.localtime(time_price/1000))
    
    
        dic = {
            'Date': real_time,
            'Closing_Price': closing_price,
        }
        stock_data.append(dic)
    # CSV module to write the the file locally.
        with open(f"{stock}.csv", "w", newline = '') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['Date','Closing_Price'])
            writer.writeheader()
            writer.writerows(stock_data)