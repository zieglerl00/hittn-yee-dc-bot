import os
import requests
import json

API_KEY = os.environ.get("API_KEY")


def get_location(content):
    return str(content).split(" ")[1]


def get_weather(message):
    response_api = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={get_location(message.content)}&aqi=no")
    parse_json = json.loads(response_api.text)

    print(parse_json["current"]["condition"]["text"])

    return parse_json["current"]["condition"]["text"]
