# Bitcoin Price Index
# Gets current Bitcoin price using requests library

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
    total = amount * rate
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")
