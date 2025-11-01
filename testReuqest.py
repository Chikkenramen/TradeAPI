from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# API endpoint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

# Define your API key and headers
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '006873f7872d457e9c17d56619533561',  # 🔑 Replace with your CoinMarketCap API key
}

# Optional parameters
parameters = {
    'limit': '10',       # how many trending coins to return
    'sort': 'cmc_rank'     # convert all prices to USD
}

# Create a session
session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = response.json()   # parse JSON directly
    print(json.dumps(data, indent=2))  # nicely formatted output
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
