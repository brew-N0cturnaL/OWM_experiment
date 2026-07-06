import requests

from flag_parsing import parse
from weather_check import api_key, base_url, weather


def main():
    args = parse()
    params ={
        "q": args.city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params = params)
    if response.status_code == 200:
        weather_info = response.json()
        weather(weather_info)
    else:
        print(f"Error {response.status_code}")

if __name__ == "__main__":
    main()