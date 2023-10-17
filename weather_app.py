# d= {
#         'consolidated_weather' : [
#         {
#             'id': 5756340131594240,
#             'weather_state_name': 'Heavy Cloud',
#             'weather_state_abbr': 'hc',
#             'wind_direction_compass': 'W',
#             'created': '2018-09-03T13:19:47.023710Z',
#             'applicable_date': '2018-09-03',
#             'min_temp': 13.7975,
#             'max_temp': 22.1725,
#             'the_temp': 14.47,
#             'wind_speed': 4.825861634719902,
#             'wind_direction': 269.0843199650456,
#             'air_pressure': 986.85,
#             'humidity': 77,
#             'visibility': 9.997862483098704,
#             'predictability': 71
#         }, {
#             'id': 6707457686503424,
#             'weather_state_name': 'Clear',
#             'weather_state_abbr': 'c',
#             'wind_direction_compass': 'W',
#             'created': '2018-09-03T13:19:50.520020Z',
#             'applicable_date': '2018-09-04',
#             'min_temp': 13.5025,
#             'max_temp': 25.685000000000002,
#             'the_temp': 24.23,
#             'wind_speed': 5.112756833426125,
#             'wind_direction': 270.2794344092529,
#             'air_pressure': 987.6,
#             'humidity': 64,
#             'visibility': 9.997862483098704,
#             'predictability': 68
#         }, {
#             'id': 6129188230660096,
#             'weather_state_name': 'Light Cloud',
#             'weather_state_abbr': 'lc',
#             'wind_direction_compass': 'W',
#             'created': '2018-09-03T13:19:53.914860Z',
#             'applicable_date': '2018-09-05',
#             'min_temp': 13.375,
#             'max_temp': 25.925,
#             'the_temp': 26.73,
#             'wind_speed': 5.52573398022217,
#             'wind_direction': 274.17536913320464,
#             'air_pressure': 987.2,
#             'humidity': 64,
#             'visibility': 9.997862483098704,
#             'predictability': 70
#         }, {
#             'id': 6028561710317568,
#             'weather_state_name': 'Light Cloud',
#             'weather_state_abbr': 'lc',
#             'wind_direction_compass': 'W',
#             'created': '2018-09-03T13:19:56.527170Z',
#             'applicable_date': '2018-09-06',
#             'min_temp': 13.7025,
#             'max_temp': 26.322499999999998,
#             'the_temp': 27.47,
#             'wind_speed': 5.296090166759458,
#             'wind_direction': 278.6409999622535,
#             'air_pressure': 989.74,
#             'humidity': 63,
#             'visibility': 9.997862483098704,
#             'predictability': 70
#         }, {
#             'id': 6695273375989760,
#             'weather_state_name': 'Heavy Cloud',
#             'weather_state_abbr': 'hc',
#             'wind_direction_compass': 'WNW',
#             'created': '2018-09-03T13:19:59.229340Z',
#             'applicable_date': '2018-09-07',
#             'min_temp': 14.6675,
#             'max_temp': 26.37,
#             'the_temp': 20.62,
#             'wind_speed': 5.071978578435272,
#             'wind_direction': 289.5,
#             'air_pressure': 1012.59,
#             'humidity': 57,
#             'visibility': 9.997862483098704,
#             'predictability': 71
#         }, {
#             'id': 5627284954284032,
#             'weather_state_name': 'Heavy Cloud',
#             'weather_state_abbr': 'hc',
#             'wind_direction_compass': 'NW',
#             'created': '2018-09-03T13:20:02.498590Z',
#             'applicable_date': '2018-09-08',
#             'min_temp': 14.755,
#             'max_temp': 26.11,
#             'the_temp': 19.47,
#             'wind_speed': 5.78301625175641,
#             'wind_direction': 305.0323351994134,
#             'air_pressure': 1010.77,
#             'humidity': 52,
#             'visibility': 9.997862483098704,
#             'predictability': 71
#         }
#     ],
# }

# for i in d['consolidated_weather']:
#     print(f"The humidity at this {i['applicable_date']} is {i['humidity']}")

# import requests

# API_ROOT = 'https://www.metaweather.com'
# API_LOCATION = '/api/location/search/?query='
# API_WEATHER = '/api/location/'  # + woeid

# def fetch_location(query):
#     return requests.get(API_ROOT + API_LOCATION + query).json()

# def fetch_weather(woeid):
#     return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

# def disambiguate_locations(locations):
#     print("Ambiguous location! Did you mean:")
#     for loc in locations:
#         print(f"\t* {loc['title']}")

# def display_weather(weather):
#     print(f"Weather for {weather['title']}:")
#     for entry in weather['consolidated_weather']:
#         date = entry['applicable_date']
#         high = entry['max_temp']
#         low = entry['min_temp']
#         state = entry['weather_state_name']
#         print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")

# def weather_dialog():
#     try:
#         where = ''
#         while not where:
#             where = input("Where in the world are you? ")
#         locations = fetch_location(where)
#         if len(locations) == 0:
#             print("I don't know where that is.")
#         elif len(locations) > 1:
#             disambiguate_locations(locations)
#         else:
#             woeid = locations[0]['woeid']
#             display_weather(fetch_weather(woeid))
#     except requests.exceptions.ConnectionError:
#         print("Couldn't connect to server! Is the network up?")

# if __name__ == '__main__':
#     while True:
#         weather_dialog()

import requests

# api_key = 'http://api.openweathermap.org/data/2.5/weather?q=New%20York&appid=b63bd79d425567bf4f8e90407d20bd61'
# r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=b63bd79d425567bf4f8e90407d20bd61')
# r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=5128581&appid=b63bd79d425567bf4f8e90407d20bd61')
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=New%20York&appid=b63bd79d425567bf4f8e90407d20bd61')

d = r.json()
print(d.keys())
# for i in d['list']:
#     print(i)
    # print(i['main']['humidity'])
    # print(i['max_temp'])