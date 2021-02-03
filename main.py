from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl


ssl._create_default_https_context = ssl._create_unverified_context 
##only way that worked for me to remove 
### urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>
finviz_url = 'https://finviz.com/quote.ashx?t='

tickers = ['AMZN', 'GME', 'AMC', 'NOK']


news_tables = {}
for ticker in tickers:
	url = finviz_url + ticker
	req = Request(url=url, headers={'user-agent': 'steven\'s macbook'})

	response = urlopen(req)

	html = BeautifulSoup(response, 'html')
	news_table = html.find(id='news-table')
	news_tables[ticker] = news_table

	break

amzn_data = news_tables['AMZN']
amzn_rows = amzn_data.findAll('tr')

for index, row in enumerate(amzn_rows): #enumerate() func returns the index and object of any list
	title = row.a.text
	print(title)