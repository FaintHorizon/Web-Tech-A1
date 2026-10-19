

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
| Sample full GET or POST request | `{
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
}` |
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
| Sample JSON response (formatted example) |
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
| Sample JSON response (formatted example) |
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
|
| Output (human-readable time) | 
`2029-10-25 17:17:48
2029-10-25` |
---
## Extended Feature API ( 3 marks)
| Criteria | Details |
|---------|---------|
| API Provider | '_________' |
| API Base URL | `_______________________________` |
| Endpoint | `_______________________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample JSON response (formatted example) |
```
```
|
---
## Evaluation – Web Architecture, MVC Design & Security
In this section, evaluate how web technologies, architecture, and design patterns
have been applied in your **AstroBot**. Your responses must relate directly to your
implementation and include reflection on your design decisions.
---
### Web Architecture – Client–Server Model (3 marks)
Explain how the client–server model applies to your AstroBot:
- Identify the **client**
- Identify the **server(s)**
- Describe how data flows between:
- User, AstroBot and APIs
Include a **simple block diagram** to illustrate this interaction.

In the scenario we have the users who are the clients they are messeging through webex our server to comunicate with the bot that pulls from the apis (open weather, webex and the ISS location). 

<img src=".\imgs\WebTechDiagOne.png" alt="Diagram One"><br>

#### Security Considerations: (3 marks )
Hardcoding keys ive done through a json file added to the gitignore list
keys.json in the main folder organaised as so 
{
    "keys":
    {
        "Webex":"Webex Dev Key",
        "Open-Weather":"Open Weather API Key"
    }
}
this makes it so the python code can read the json and get the appropriate keys while not uploading them to github
---
### RESTful API Usage in Your Application (3 marks )
Explain how REST APIs are used in your AstroBot:
- Describe how HTTP methods (GET, POST) are used
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)
- Describe how JSON responses are received and processed
Note: Relate your explanation directly to your code for higher grade.
#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses,
Avoiding excessive API calls
---
### MVC Design Pattern in AstroBot (3 Marks)
Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation
| Component | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model** | |
| **View** | |
| **Controller** | |
---
### 🚀 Reflection and Evaluation ( 8 marks )
Reflect on your AstroBot (400 words):
- How effective is your bot in meeting the Astronomy Club’s needs?
- What design decisions worked well?
- What challenges did you face when integrating APIs?
- What security risks did you identify and how were they handled?
- How could your solution be improved in the future?
---
**Tip:** Link your answers directly to your code and examples for higher marks.
### Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---
### Total: /40
