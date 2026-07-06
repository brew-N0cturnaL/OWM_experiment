import requests, re

api_key = "099ed258adaefea61bc5772b732766cd"
base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&"

def read_ascii(file_path):
    with open(file_path, "r", encoding ="utf-8") as file:
        return file.read()

def display_weather(weather_info, ascii_art):
    ascii_lines = ascii_art.split("\n")
    info_lines = [f"Temperature: {weather_info['main']['temp']} ˚C\n",
          f"Pressure: {weather_info['main']['pressure']} hPa\n",
          f"Humidity: {weather_info['main']['humidity']} %\n",
          f"Wind: {weather_info['wind']['speed']} m/s {weather_info['wind']['deg']}˚\n",
          f'Description: {weather_info["weather"][0]["description"]}\n'
    ]

    max_length = max(len(line) for line in ascii_lines)
    for i in range(len(ascii_lines)):
        ascii_line = ascii_lines[i] if i < len(ascii_lines) else "\n"
        info_line = info_lines[i] if i < len(info_lines) else "\n"
        print(f"{ascii_line:<{max_length}}  {info_line}", end = "")

def weather(weather_info):
    weather_patterns = {
        r"thunderstorm|storm": "thunderstorm_ascii.txt",
        r"mist|fog|haze|smoke": "haze_ascii.txt",
        r"rain|drizzle": "rain_w_clouds.txt",
        r"clear|sunny": "clear_ascii.txt",
        r"snow|blizzard": "snow_ascii.txt",
        r"cloud": "cloudy_ascii.txt",
        r"overcast": "clouds_ascii.txt"
    }

    desc = weather_info["weather"][0]["description"].lower()
    for pattern, ascii_file in weather_patterns.items():
        if re.search(pattern, desc):
            ascii_art = read_ascii(ascii_file)
            return display_weather(weather_info, ascii_art)
    ascii_art = read_ascii("default_ascii.txt")
    return display_weather(weather_info, ascii_art)


def main():
    city = input("Enter city: ")
    params ={
        "q": city,
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
