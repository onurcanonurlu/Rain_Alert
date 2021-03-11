import requests
import os
from twilio.rest import Client

api_key = "YOUR API KEY HERE"
account_sid = "YOUR ACCOUNT SID HERE"
auth_token = "YOUR AUTH TOKEN HERE"
virtual_phone = 'YOUR VIRTUAL TWILIO NUMBER HERE'
my_phone="YOUR PHONE NUMBER HERE"
#Parameters for the API: (for Eskişehir)

parameters = {
    "lat" : 39.770771,
    "lon" :  30.517981,
    "appid" : api_key,
    "units" : "metric",
    "exclude" : "current,minutely,daily"
}
will_rain = False

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
first_12_hours_data = weather_data["hourly"][slice(0,13)]
for hour in first_12_hours_data:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Semsiyeni almayi unutma.☂",
        from_=virtual_phone,
        to=my_phone
    )

    print(message.status)
