""" Email if ISS is close and it is dark """
from datetime import datetime
from time import sleep
import smtplib
import requests

MY_LAT =  # Your latitude
MY_LONG =  # Your longitude
MY_EMAIL =  # Your email (change SMTP)
PASSWORD =  # Your app password


def close(iss_lat, iss_long):
    """ Check if ISS near me """
    if (
        iss_lat >= MY_LAT - 5 and iss_lat <= MY_LAT + 5 and
        iss_long >= MY_LONG - 5 and iss_long <= MY_LONG + 5
    ):
        return True


def dark(sd, su):
    """ Check if it is dark """
    if (
        time_now.hour <= 24 and time_now.hour >= sd
        or time_now.hour >= 0 and time_now.hour <= su
    ):
        return True


try:
    response = requests.get(
        url="http://api.open-notify.org/iss-now.json",
        timeout=10)
except requests.exceptions.Timeout:
    print("Timed out")

response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

try:
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters,
        timeout=10
    )
except requests.exceptions.Timeout:
    print("Timed out")

response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position and it is dark
while True:
    sleep(60)
    if (
        close(iss_latitude, iss_longitude) is True
        and dark(sunset, sunrise) is True
    ):
        # Send email to look up
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS overhead\n\nLook up!"
                )
