import requests
import bs4

url = 'https://api.coinbase.com/v2/currencies'
response = requests.get(url)
print(response.content)














#endpoints to know about
## https://api.coinbase.com/v2/time
## https://api.coinbase.com/v2/currencies