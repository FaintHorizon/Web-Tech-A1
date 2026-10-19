# =========================
# REQUIRED LIBRARIES
# =========================

from fastapi import params
import requests
import json
import time
from datetime import datetime

# =========================
# CONFIGURATION FUNCTIONS
# =========================
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()

    if choice == "n":
        token = input("Enter your Webex Access Token: ") #Asks the user to input their Webex Access Token if they choose not to use the hard-coded token
        print(f"---Debug: Using user-provided Webex token: {token}---")
        return f"Bearer {token}"
    else:
        with open("keys.json", "r") as file:
            keys = json.load(file)
        token = keys["keys"]["Webex"]
        print (f"---Debug: Using Hard-coded Webex token: {token}---")
        return f"Bearer {token}"



def get_api_key():
    choice = input("Use hard-coded Open-Weather key? (y/n): ").lower()

    if choice == "n":
        weatherKey = input("Enter your Open-Weather API key: ")
        print("---Debug: Using user-provided Open-Weather key---")
        return weatherKey
    else:
        with open("keys.json", "r") as file:
            keys = json.load(file)
    weatherKey = keys["keys"]["Open-Weather"]
    print("---Debug: Using key from keys.json---")
    return weatherKey


# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = ("https://webexapis.com/v1/rooms") #URL to fetch rooms from Webex API
    headers = {
    "Authorization": token,
    "Accept": "application/json" #headers dictionary to include the Authorization header with the token and Accept as application/json
    }
    payload = None
    response = requests.request('GET', url, headers=headers, data = payload) #request to fetch rooms from Webex API using the requests library with the GET method, passing in the URL, headers, and payload

    if response.status_code != 200: #Checks if the response status code is not 200 (OK), indicating an error in fetching rooms
        print("Error fetching rooms:", response.status_code)
        return []

    return response.json().get("items", []) #Returns the list of rooms from the JSON response, or an empty list if no rooms are found


def print_rooms(rooms): #Function to print the list of rooms with their titles and IDs
    for room in rooms:
        print(f"Room: {room['title']} | ID: {room['id']}") #Breaks down the room information into a formatted string displaying the room title and ID


def select_room(rooms): #Function to allow the user to select a room by name from the list of rooms
    while True:
        name = input("Enter the Webex room name: ") #Asks the user to input the name of the Webex room they want to select

        for room in rooms:
            if name.lower() in room["title"].lower(): #Checks if the input name is a valid room title to find a matching room
                print(f"Selected room: {room['title']}")
                return room["id"] #Returns the ID of the selected room if a match is found

        print("Room not found. Please try again.") #If no matching room is found, it prompts the user to try again


def get_latest_message(token, room_id): #Function to fetch the latest message from a specified Webex room using the Webex API
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": room_id, "max": 1}
    headers = {
        "Authorization": token,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params) #request to fetch the latest message from the specified Webex room using the requests library with the GET method, passing in the URL, headers, and parameters

    if response.status_code != 200: #Error handling to check if the response status code is not 200 (OK), indicating an error in fetching messages
        print("Error fetching messages:", response.status_code)
        return None, None

    data = response.json().get("items", [])

    if not data: #Checks if the data list is empty, indicating that there are no messages in the specified room
        return None, None

    latest = data[0] #Retrieves the latest message from the data list, which contains the messages fetched from the Webex API
    return latest.get("id"), latest.get("text", "")


def send_message(token, room_id, message): #Function to send a message to a specified Webex room using the Webex API
    url = "https://webexapis.com/v1/messages"
    headers = { #headers dictionary to include the Authorization header with the token and Content-Type as application/json
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = { #data dictionary to include the room ID and the message text to be sent to the specified Webex room
        "roomId": room_id,
        "text": message
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200: #Error handling to check if the response status code is not 200 (OK), indicating an error in sending the message
        print("Error sending message:", response.status_code)

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "limit": 1, "appid": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching city coordinates:", response.status_code)
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key) #Calls the get_city_coordinates function to retrieve the latitude and longitude of the specified city using the OpenWeatherMap API

    if not location:
        return f"City '{city}' not found." #If the location is not found, it returns a message indicating that the city was not found

    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = { #parameters dictionary to include the latitude, longitude, units, and the API key
        "lat": location["lat"],
        "lon": location["lon"],
        "units": "metric",
        "appid": api_key
    }

    response = requests.get(url, params=parameters) #request to fetch the weather data for the specified city using the OpenWeatherMap API with the GET method, passing in the URL and parameters

    if response.status_code != 200:
        print("Error fetching weather:", response.status_code)
        return "Unable to retrieve weather data."

    weather = response.json() #Parses the JSON response from the OpenWeatherMap API to extract the weather data for the specified city

    city_name = weather.get("name", city) #Retrieves the city name from the weather data, defaulting to the input city name if not found
    country = weather.get("sys", {}).get("country", "Unknown")
    temperature = weather.get("main", {}).get("temp", "Unknown")
    humidity = weather.get("main", {}).get("humidity", "Unknown")
    wind_speed = weather.get("wind", {}).get("speed", "Unknown")
    weather_data = weather.get("weather", []) #Retrieves the weather conditions from the weather data, defaulting to an empty list if not found

    if weather_data: #Checks if the weather_data list is not empty, indicating that weather conditions are available
        description = weather_data[0].get("description", "Unknown")
    else:
        description = "Unknown" #If the weather_data list is empty, it sets the description to "Unknown" to indicate that the weather conditions are not available

    return ( #Returns a formatted string containing the weather information for the specified city, including the city name, country, temperature, weather conditions, humidity, and wind speed
        f"Weather in {city_name}, {country}:\n"
        f"Temperature: {temperature} °C\n"
        f"Conditions: {description.capitalize()}\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind_speed} m/s"
    )

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = "https://api.openweathermap.org/geo/1.0/reverse" #URL to fetch reverse geocoding data from the OpenWeatherMap API using latitude and longitude coordinates

    parameters = { #parameters dictionary to include the latitude, longitude, limit, and the API key for reverse geocoding
        "lat": lat,
        "lon": lon,
        "limit": 1,
        "appid": api_key
    }

    response = requests.get(url, params=parameters)

    if response.status_code != 200:
        print("Error fetching reverse geocoding data:", response.status_code)
        return None

    data = response.json() #Parses the JSON response from the OpenWeatherMap API to extract the reverse geocoding data based on the provided latitude and longitude coordinates
    return data[0] if data else None #Returns the first result from the reverse geocoding data if available, or None if no results are found


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to retrieve ISS location."

    data = response.json()

    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location.get("name", place)

        if location.get("country"):
            place = place + ", " + location["country"]

    return (
        f"Current ISS Location:\n"
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
        f"Nearby location: {place}"
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main():

    token = get_webex_token()

    weather_key = get_api_key(
        "Weather API key",
        "YOUR_OPENWEATHER_API_KEY"
    )

    rooms = get_rooms(token)

    if not rooms:
        print(#complete the print statement )
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(#complete the print statement to display the received message text)

            if not message_text.startswith(#complete):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith(#complete):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
