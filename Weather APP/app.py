import requests

api_key = 'd5205fb2c5bc2ae18385e121e7014a5b'     # This was obtained in order to get the data we will need for the weather app

input_of_User = input("Enter City or State:")             # Type in what city or state you want

 # Gets the data we want and plugs in into that function
Data_Weather = requests.get(                              
    f"https://api.openweathermap.org/data/2.5/weather?q={input_of_User}&units=imperial&APPID={api_key}")

 #If City/State is not Existent it will shoot back out an Error. If not it will run the code
if Data_Weather.json()['cod'] == '404':
    print("The City you have Provided not found.")
else:
    Weather = Data_Weather.json()['weather'][0]['main']
    temp = Data_Weather.json()['main']['temp']
    weather_advice = ""
    temp_advice = ""

    # These if else statements are use to check what the Weather is for that City and will detemrine which advice to give
    if Weather == 'Clear':
        weather_advice = f"The Weather in {input_of_User} is Clear and looking amazing."
    elif Weather == 'Rain':
        weather_advice = f"The Weather in {input_of_User} is Rainy and looking refreshing."
    elif Weather == 'Mist':
        weather_advice = f"The Weather in {input_of_User} is Misty and enchanting"
    elif Weather == 'Clouds':
        weather_advice = f"The Weather in {input_of_User} is Cloudy and looking dull."
    elif Weather == 'Snow':
        weather_advice = f"The Weather in {input_of_User} is Snowy and looks beautiful."
    else:
        # This is general advice in case weather doesn't meet the other cases.
        weather_advice = f"The weather in {input_of_User} is currently {Weather}. Stay prepared for anything."

    # These if else statements are use to check what the temp is for that City and will detemrine which advice to give
    if temp <= 32:
        temp_advice = "It's very cold outside. Make sure to dress warmly."
    elif 32 < temp <= 50: 
        temp_advice = "It's cold outside. Consider wearing a sweater."
    elif 50 < temp <= 68:
        temp_advice = "It's a bit chilly. A light jacket would be wise."
    elif 68 < temp <= 77:
        temp_advice = "The temperature is comfortable. A t-shirt should be fine."
    else:
        temp_advice = "It's quite warm. Light clothing is recommended."
    
    # Print weather advice and temperature advice
    print(weather_advice)
    print(temp_advice)
