import requests
apiKey = "your key here"
baseUrl = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter City Name: ")
requestsUrl = f"{baseUrl}?appid={apiKey}&q={city}"
response = requests.get(requestsUrl)
if response.status_code == 200:
    data = response.json()
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {round(data['main']['temp'] - 271.15, 2)} C {round((data['main']['temp'] - 271.15) * 1.8 + 32, 2)} F")
else: print(f"Error {response.status_code}")
