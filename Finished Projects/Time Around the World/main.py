from datetime import datetime

import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

while True:
    userInput = input(
        "Would You Like To Get The Time Of A Location By 1. Entering The Name 2. Entering The Location Address: "
    ).strip()
    if userInput == "1":
        while True:
            userInput = input(
                "Enter Where You Would Like To See The Current Time [Enter ? For Help]: "
            ).strip()
            while userInput == "?":
                for timeZone in pytz.all_timezones:
                    print(timeZone)
                userInput = input(
                    "Enter Where You Would Like To See The Current Time [Enter ? For Help]: "
                ).strip()
            try:
                currentTime = pytz.timezone(userInput.strip())
                newTime = datetime.now(currentTime)
                print(newTime.strftime("%H:%M"))
            except:
                print(f"pytz.exceptions.UnknownTimeZoneError: '{userInput}'")
    elif userInput == "2":
        geolocator = Nominatim(user_agent="geoapiExercises")
        while True:
            locationId = input("Enter The Location Address: ")
            try:
                location = geolocator.geocode(locationId)
                print("Latitude/Longitude Of Address")
                print((location.latitude, location.longitude))
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
                print("Time Zone:", result)
                currentTime = pytz.timezone(result)
                newTime = datetime.now(currentTime)
                print(newTime.strftime("%H:%M"))
            except:
                print("Invalid Input")
    else:
        print("Invalid Input")
