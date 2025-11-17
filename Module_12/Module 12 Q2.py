import requests

api_key = "AAA333"
city = input("Enter municipality name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']} Celsius")
    else:
        print("Error !!;")
except:
    print(" Request fail")