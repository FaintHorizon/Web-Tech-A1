

# 🚀 ASTRO Bot API Investigation Sheet
**Total Marks: 40**
**TASK 1: Collect Required API Documentation**
This investigation sheet helps you gather key technical information from the three
APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current
Location API**, **Weather API** and a **Geocoding API** , plus the Python time
module. Also furhter investigate the application of Web Architecture and MVC design
pattern in development of the Bot
---
## Webex Messaging API (4 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `https://webexapis.com` |
| Authentication Method | `Authorization: Bearer THE_BOTS_ACCESS_TOKEN` |
| Endpoint to list rooms | `/v1/rooms` |
| Endpoint to get messages | `/v1/messages` |
| Endpoint to send message | `/v1/messages` |
| Required headers | `"Authorization": "Bearer API Key",
    "Accept": "application/json"` |
| Sample full GET or POST request || `<br>
{
    "items": [
        {
            "id": "IDKey",
            "title": "Brandon's space",
            "type": "group",
            "lastActivity": "2026-09-23T09:36:12.802Z",
            "creatorId": "CreatorIDKey",
            "created": "2026-09-23T09:36:12.802Z",
            "ownerId": "OwnerIDKey",
            "isPublic": false,
            "isReadOnly": false,
            "isLocked": false
        }
    ]
}` <br>
---
## ISS Current Location API (2 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | http://api.open-notify.org/iss-now.json` |
| Endpoint for current ISS location | `http://api.open-notify.org/` |
| Sample response format (example JSON) |
{
    "iss_position": {
        "latitude": "40.3008",
        "longitude": "121.2208"
    },
    "timestamp": 1790761317,
    "message": "success"
}
```
```
|
---
## Geocoding API (4 marks)
| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other -provide -- Remove {} for requests
detail** |
| API Base URL | `http://api.openweathermap.org/geo/1.0/zip?zip=WD25,GB&appid={API Key}` |
| Endpoint for geocoding | `http://api.openweathermap.org/geo/1.0/direct>` |
| Endpoint for reverse geocoding | `http://api.openweathermap.org/geo/1.0/reverse?` |
| Authentication method | `N/A` |
| Required query parameters | `PostCode,CoutryCode,APIKEY` |
| Sample request with latitude/longitude | `lat={lat}&lon={lon}&limit={limit}&appid={API key}` |
| Sample JSON response (formatted example) ||
{
    "zip": "WD25",
    "name": "Watford",
    "lat": 51.6553,
    "lon": -0.396,
    "country": "GB"
}
```
```
|
---
## Weather API (3 marks)
| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | **OpenWeather, OpenWeatherMap (or other – provide
details)** |
| API Base URL | `https://api.openweathermap.org/data/2.5/weather?lat={51.5074}&lon={0.1278}&appid={APIKEY}&units={metric}` |
| Endpoint for current weather | `https://api.openweathermap.org/data/2.5/weather?` |
| Authentication method | `{appid}` | -- remove {} brackets
| Required query parameters | `lat,long,appid,units` |
| Sample JSON response (formatted example) ||
{
    "coord": {
        "lon": 0.1278,
        "lat": 51.5074
    },
    "weather": [
        {
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 9.54,
        "feels_like": 9.54,
        "temp_min": 8.62,
        "temp_max": 10.76,
        "pressure": 1028,
        "humidity": 86,
        "sea_level": 1028,
        "grnd_level": 1027
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.23,
        "deg": 210,
        "gust": 2.48
    },
    "clouds": {
        "all": 37
    },
    "dt": 1791959272,
    "sys": {
        "type": 2,
        "id": 2011528,
        "country": "GB",
        "sunrise": 1791958872,
        "sunset": 1791997772
    },
    "timezone": 3600,
    "id": 7302135,
    "name": "Abbey Wood",
    "cod": 200
}
```
```
|       
---
## Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `datetime` |
| Function used to convert epoch | `datetime.fromtimestamp` |
| Sample code to convert timestamp |
https://www.geeksforgeeks.org/python/python-datetime-module/
from datetime import datetime
date_time = datetime.fromtimestamp(1887639468)
print(date_time)
print(date_time.date())
```
```

Output (human-readable time)  
`2029-10-25 17:17:48
2029-10-25` 
---
## Extended Feature API ( 3 marks)
| Criteria | Details |
|---------|---------|
| API Provider | 'Nasa' |
| API Base URL | `https://science.nasa.gov/wp-json/wp/v2/` |
| Endpoint | `apod-basic/` |
| Authentication method | `API Key` |
| Required query parameters | `API Key` |
| Sample JSON response (formatted example) ||

{
    "date": "2026-10-19",
    "title": "Treble Clef: Unusual X-ray Hot Radio Source",
    "media_type": "image",
    "explanation": "This unusual radio structure extends over 2 million light-years and resembles a musical symbol. Recent observations suggest it may have originated from a supermassive black hole.",
    "credit": "NASA/CXC/INAF-IRA and other contributors",
    "url": "https://science.nasa.gov/image-article/apod-2026-october-19-treble-clef-unusual-x-ray-hot-radio-source/",
    "hdurl": "https://assets.science.nasa.gov/dynamicimage/assets/science/cds/apod/apod/2026/october/trebleclef.jpg"
}


```
```

---
## Evaluation – Web Architecture, MVC Design & Security
In this section, evaluate how web technologies, architecture, and design patterns
have been applied in your **AstroBot**. Your responses must relate directly to your
implementation and include reflection on your design decisions.
---
### Web Architecture – Client–Server Model (3 marks)

In the scenario we have the users who are the clients they are messeging through webex our server to comunicate with the bot that pulls from the apis (open weather, webex and the ISS location). 

<img src=".\imgs\WebTechDiagOne.png" alt="Diagram One"><br>

#### Security Considerations: (3 marks )
Hardcoding keys ive done through a json file added to the gitignore list.
keys.json in the main folder organaised as so 
</br>
{
    "keys":
    {
        "Webex":"Webex Dev Key",
        "Open-Weather":"Open Weather API Key",
        "Nasa":"Nasa Open API key"
    }
}
</br>
This makes it so the python code can read the json and get the appropriate keys while not uploading them to github

---
### RESTful API Usage in Your Application (3 marks )

The bot uses **POST** and **GET** requests to read and reply to the messeges through Webex using Get to read new messeges and post to send the response.

We utilize the requests libary to send the post and get requests and the JSON libary to read the fields from the api responses such as items, id, and text from webex or lat and lon from geocoding.

#### Security Considerations: (2 marks)

We can check status codes with the responses and compare them to a value of 200 with 200 meaning ok anything else we can mark as a fail and report that to the terminal or the user.

---
### MVC Design Pattern in AstroBot (3 Marks)

Astro bot has the model side the different functions to retrive data, the view side where it posts messeges to terminal or the chatroom and the controler side where it allows the user to use slash commands to opperate its different functions.

| Component | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model** | | we have numerus functions to retive data get_rooms(), get_city_coordinates() etc can all be viewed as the model
| **View** | | print_rooms() shows the rooms in terminal to allow the user to set the bot to join, send_message() is what allows the bot to post inside of the room
| **Controller** | | The / Commands such as help, quit and the api specific ones such as /weather (location)

---
### 🚀 Reflection and Evaluation ( 8 marks )
Reflect on your AstroBot (400 words):
## Reflection and Evaluation


The AstroBot works well within the scope of the project and provides the main features required for the Astronomy Club. Users can interact with the bot through Webex and use commands to retrieve weather information for a chosen city, check the current location of the International Space Station, view the available commands and shut down the bot. While there are additional features that could be added, the current implementation covers the main requirements without making the program unnecessarily complicated.

One design decision that worked well was keeping the program modular. By separating the different tasks into functions, it was easier to test individual elements outside of the main program. For example, the functions for retrieving weather information, getting city coordinates and finding a location from latitude and longitude can be handled separately. This also makes the code easier to read and means that changes can be made to one part without needing to rewrite the entire program.

One of the main challenges I faced when integrating the APIs was finding the correct information in the documentation. The Webex documentation is very expansive and covers far more than what was required for this project. As a result, finding the specific endpoints, parameters and information needed for the bot was sometimes troublesome because it was buried among other documentation. Another challenge was understanding how the different APIs worked together, particularly how geocoding could be used to find coordinates before retrieving weather information, or to identify a nearby location for the ISS.

A security risk I identified was the possibility of exposing API keys publicly. To reduce this risk, I used a keys.json file to store the Webex and OpenWeather keys separately from the main Python code. I also added the file to .gitignore so it would not be uploaded to GitHub with the rest of the project. This is a more secure approach than directly hardcoding the keys into the program, although care still needs to be taken to ensure the file is not shared or committed accidentally.

In the future, the bot could be improved by adding a startup screen or some form of loading indicator when API requests take longer to complete. At the moment, a user could assume the program has crashed if it takes a while to respond. The bot could also be expanded with additional astronomy-related features, such as NASA's Astronomy Picture of the Day API. These changes would make the bot more useful and improve the user experience while keeping the existing modular structure.


---
**Tip:** Link your answers directly to your code and examples for higher marks.
### Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---
### Total: /40
