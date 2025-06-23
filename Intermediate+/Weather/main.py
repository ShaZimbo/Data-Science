""" Send email if it will rain """
import os
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

perameters = {
    "lat": 53.4877,
    "lon": -2.2904,
    "appid": os.environ.get("APPID"),
    "units": "metric",
    "cnt": 3
    }
try:
    weather_data = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast",
        params=perameters, timeout=10
        )
except requests.exceptions.Timeout:
    print("Timed out")

weather = weather_data.json()
details = {entry["weather"][0]["id"]: entry["weather"][0]["description"]
           for entry in weather["list"]}

NEED_BROLLY = False
condition = []

for key, value in details.items():
    if key < 700:
        condition.append(value)
        NEED_BROLLY = True

if NEED_BROLLY is True:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Rain monitor\n\n"
            f"You need an umbrella for: {", ".join(condition)}"
            )
