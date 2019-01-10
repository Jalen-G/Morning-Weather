import requests, smtplib, datetime, time, pytemperature

# Send text message through SMS gateway of destination number
while True:

    now = datetime.datetime.now()
    time_now = now.hour, now.minute, now.second
    time.sleep(1)
    print(time_now)

    if time_now == (9, 9, 25):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('***@gmail.com', '***')

        api_address = "http://api.openweathermap.org/data/2.5/weather?lat=***&lon=***&appid=***"
        json_data = requests.get(api_address).json()

        weather = json_data["weather"][0]["main"]
        temp = json_data["main"]["temp"]
        wind = str(round(json_data['wind']['speed']))
        max_temp = json_data["main"]["temp_max"]
        min_temp = json_data["main"]["temp_min"]

        temp_f = str(round(pytemperature.k2f(temp)))
        max_f = str(round(pytemperature.k2f(max_temp)))
        min_f = str(round(pytemperature.k2f(min_temp)))

        server.sendmail( '***@gmail.com', '***@mms.att.net', "It is " + temp_f + " degrees and " + weather + " outside right now with a max of " + max_f + " and a low of " + min_f + ". The wind is blowing at " + wind + " MPH.")
        time.sleep(5)
        print("sent!")


