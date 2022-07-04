import requests
from twilio.rest import Client

my_lat = -2.849691
my_lng = 108.172126
api_key = "sign in to https://openweathermap.org and get your api"

parameters = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": api_key,
    "exclude": "daily,minutely"
}

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"

response = requests.get(api_endpoint, params=parameters)

# ----------------------------LONG WAY----------------------------
# -------------------------NOT RECOMMENDED------------------------

# data_hourly = response.json()["hourly"]
# print(data_hourly)
#
# weather = []
# for data in data_hourly:
#     for key, value in data.items():
#         if key == "weather":
#             data[key] = value
#             weather.append(data[key])
#
# print(weather)
#
# list_id_48h = []
# for data in weather:
#     for dictionary in data:
#         for key, value in dictionary.items():
#             if key == "id":
#                 main_value = dictionary[key]
#                 list_id_48h.append(main_value)
#
# print(list_id_48h)
#
# rain = False
# for items in range(0, len(list_id_48h)-24):
#     if list_id_48h[items] < 700:
#         rain = True
#
# if rain:
#     print("Don't forget your umbrella")


weather_data_in_12hour = response.json()["hourly"][0:12]

will_rain = False
for data in weather_data_in_12hour:
    weather_status_code = data["weather"][0]["id"]
    if weather_status_code < 700:
        will_rain = True


account_sid = "sign in to https://www.twilio.com/ and get your personal account sid"
auth_token = 'sign in to https://www.twilio.com/ and get your personal auth token'

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body="Hii, boss. I'm your online assistance. Don't forget to bring umbrella "
                     "it's going to rain today",
                from_='you can get this number from twilio',
                to='add your personal number to receive message')

    print(message.status)

else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body="Hii, boss. I'm your online assistance. Just for information "
                     "It's sunny today",
                from_='you can get this number from twilio',
                to='add your personal number to receive message')

    print(message.status)
