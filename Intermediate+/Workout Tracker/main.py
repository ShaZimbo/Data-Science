""" Workout tracker """
from os import environ
import datetime as dt
import requests
from dotenv import load_dotenv

load_dotenv()

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

NIX_API_KEY = environ.get("NIX_API_KEY")
NIX_API_ID = environ.get("NIX_API_ID")
ADD_ENDPOINT = environ.get("SHEETY_ENDPOINT")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE = str(input("Which exercises did you do?\n"))
BEARER_CODE = environ.get("BEARER_CODE")


headers = {
    "x-app-id": NIX_API_ID,
    "x-app-key": NIX_API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": EXERCISE
}

try:
    add_ex = requests.post(
        ENDPOINT, headers=headers, json=parameters, timeout=10
        )
except requests.exceptions.Timeout:
    print("Timed out")

data = add_ex.json()

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_header = {
        "Authorization": BEARER_CODE,
    }

    try:
        add_to_sheet = requests.post(ADD_ENDPOINT, headers=bearer_header,
                                     json=sheet_inputs, timeout=10)
    except requests.exceptions.Timeout:
        print("Timed out")
