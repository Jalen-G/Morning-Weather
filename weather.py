import requests, smtplib, datetime, time

while True:

    now = datetime.datetime.now()
    time_now = now.hour, now.minute, now.second
    time.sleep(1)
    print(time_now)

    if time_now == (8, 0, 0):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('***@gmail.com', '***')

        api_address = "***"
        current_api = "***"

        json_data = requests.get(api_address).json()
        current_data = requests.get(current_api).json()

        weather = json_data['Headline']['Text']
        max_temp = str(int(json_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']))
        min_temp = str(int(json_data['DailyForecasts'][0]['Temperature']['Minimum']['Value']))
        temp = str(int(current_data[0]['Temperature']['Imperial']['Value']))


        server.sendmail( '***@gmail.com', '***@mms.att.net', weather + ". Currently it's " + temp + " degrees outside with a high of " + max_temp + " and a low of " + min_temp +".")
        time.sleep(5)
        print("sent!")


