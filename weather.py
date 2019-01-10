import requests, smtplib, datetime, time

server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login('***@gmail.com', '***')

# Send text message through SMS gateway of destination number
while True:

    now = datetime.datetime.now()
    time_now = now.hour, now.minute, now.second
    time.sleep(1)
    print(time_now)

    if time_now == (8, 30, 0):
       
        api_address = "http://api.openweathermap.org/data/2.5/weather?lat=34.73&lon=-87.7&appid=c3d2817674f897ffbb82c1f317e8329b&units=imperial"

        json_data = requests.get(api_address).json()

        weather = json_data["weather"][0]["main"]
        temp = str(round(json_data["main"]["temp"]))
        wind = str(round(json_data['wind']['speed']))
        max_temp = str(round(json_data["main"]["temp_max"]))
        min_temp = str(round(json_data["main"]["temp_min"]))

        server.sendmail( '***@gmail.com', '***@mms.att.net', "It is " + temp + " degrees and " + weather + " outside right now with a max of " + max_temp + " and a low of " + min_temp + ". The wind is blowing at " + wind + " MPH.")
       
        time.sleep(5)
        
        print("sent!")


