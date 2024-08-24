import requests
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit('More than one command line argument provided.')

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request failed")

    try:
        data = response.json()
        rate = data['bpi']['USD']['rate_float']
    except (KeyError, ValueError): 
         sys.exit("Invalid JSON")

    total_cost = bitcoin * rate
    print(f"${total_cost:,.4f}")


if __name__ == '__main__':
    main()
