""" Questions for quizzler app """
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

try:
    response = requests.get(
        "https://opentdb.com/api.php", params=parameters, timeout=10
        )
except requests.exceptions.Timeout:
    print("Timed out")
response.raise_for_status()
data = response.json()
question_data = data["results"]
