import requests

API_ROOT = 'http://api.openweathermap.org'
API_LOCATION = '/data/2.5/weather?q='
API_WEATHER = '/data/2.5/forecast?id='  # + woeid
APPID_STR = '&appid='
APPID = 'b63bd79d425567bf4f8e90407d20bd61'

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query + APPID_STR + APPID ).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)  + APPID_STR + APPID ).json()

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['name']}")

def display_weather(weather):
    print(f"Weather for {weather['city']['name']}:")
    for entry in weather['list']:
        date = entry['dt_txt']
        high = entry['main']['temp_max']
        low = entry['main']['temp_min']
        print(f"{date}\t\thigh {high:2.1f}°C\tlow {low:2.1f}°C")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you? ")
        locations = fetch_location(where)
        # print(locations)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) < 5:
            disambiguate_locations(locations)
        else:
            woeid = locations['id']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?")

if __name__ == '__main__':
    while True:
        weather_dialog()