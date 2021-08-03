import requests as re
from smtplib import SMTP
import os

server = SMTP('smtp.gmail.com')
server.starttls()
fromaddr = 'nguyentangthaihoa21011999@gmail.com'
toaddrs = 'hoa.ntt5224@sinhvien.hoasen.edu.vn'
msg = 'The weather is going to be rained in 12 hours, so please bring your  umbrella together'
# username = os.environ['user_name']
# password = os.environ['password']
username = os.environ.get('OWN_username')
password = os.environ.get('OWN_password')
server.login(user=username, password=password)

#from openweather api
api_endpoints = 'https://api.openweathermap.org/data/2.5/onecall'
api_param = {
    'lat': 22.572645,
    'lon': 88.363892,
    'exclude': 'current,daily,minutely',
    'appid': '049a01df48b18478e6dac02dffc67503'
}

will_rain = False
rq = re.get(api_endpoints, api_param)
weather_data = rq.json()['hourly'][:13]
for i in weather_data:
    condition_code = i['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
