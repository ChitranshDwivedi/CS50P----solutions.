import requests
import sys

# Ensure exactly one command-line argument is provided
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Ensure the argument is a valid number
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Fetch current Bitcoin price from CoinCap API
try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=286b79726ab4a936f87cd1eee0a3b09cafdb113c66e2b1f4312b0d55bd3d8513")
    data = response.json()
    price = float(data["data"]["priceUsd"])   # Price is returned as a string, convert to float
except requests.RequestException:
    sys.exit("Error fetching data")

# Multiply number of bitcoins by current price and display result
total = n * price
print(f"${total:,.4f}")
