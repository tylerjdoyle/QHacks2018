from sys import argv
from urllib.request import urlopen

from bs4 import BeautifulSoup
import pandas
    
coin = argv[1]      # The coin that you would like data about.
start = argv[2]     # The first date (YYMMDD) that you would like data from.
end = argv[3]       # The last date (YYMMDD) that you would like data from.

url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start={}&end={}'.format(coin, start, end)
page = urlopen(url, timeout=10)
html = page.read()
soup = BeautifulSoup(html, 'html.parser')
    
dates = []
opens = []
highs = []
lows = []
closes = []

tables = soup.find_all('table', {'class': 'table'})
for table in tables:
    tbody = table.find('tbody')
    if tbody:
        if tbody.find('tr'):
            tr_tags = tbody.find_all('tr')
            
            for tr_tag in tr_tags:
                if tr_tag.find('td'):
                    
                    td_tags = tr_tag.find_all('td')
                    
                    dates.append(td_tags[0].text)
                    opens.append(td_tags[1].text)
                    highs.append(td_tags[2].text)
                    lows.append(td_tags[3].text)
                    closes.append(td_tags[4].text)

csv = '{}_from_{}_to_{}.csv'.format(coin, start, end)

dataframe = pandas.DataFrame()

dataframe['date'] = dates
dataframe['open'] = opens
dataframe['high'] = opens
dataframe['low'] = lows
dataframe['close'] = closes

dataframe.to_csv(csv, index=False)
