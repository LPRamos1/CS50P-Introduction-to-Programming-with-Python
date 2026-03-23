import requests
import sys


def get_price():
    # Search for the actual bitcoin price in USD
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])

    # sys.exit avoid main receiving an string
    except (requests.RequestException, KeyError, ValueError) as e:
        sys.exit(f"Cannot request data: {e}")


def main():
    # Validation for Command-line (expect: bitcoin.py x
    # x expected to be a int from the user
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Command-line argument too large")
    # Converting to float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # Getting owned in current bitcoin usd price
    price = get_price()
    total = amount * price
    # Total with 4 decimals
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
