import requests,json
from time import gmtime, strftime
import time

#Temperature is available in Fahrenheit, Celsius and Kelvin units.

#	For temperature in Fahrenheit use units=imperial
#	For temperature in Celsius use units=metric
#	Temperature in Kelvin is used by default, no need to use units parameter in API call

url="http://api.openweathermap.org/data/2.5/weather?zip=<zip here>,us&APPID=<key here>&units=imperial"

response=requests.post(url)


#print json.loads(response.text)

resp=json.loads(response.text)

print "#####################"
#print resp["coord"]["lat"]
print resp["weather"][0]["description"]
print "Current temperature is ",resp["main"]["temp"], " Farenheit"

print "Pressure ",resp["main"]["pressure"]," hpa"

print "Humidity ",resp["main"]["humidity"],"%"

print "Temperature from ", resp["main"]["temp_min"], " to ", resp["main"]["temp_max"], " Farenheit"

v=1
while v==1:
	print strftime("%Y-%m-%d %H:%M:%S")
	time.sleep(1)

	
#http://api.openweathermap.org/data/2.5/weather?zip=94040,us&APPID=<key>
#http://api.openweathermap.org/data/2.5/forecast/city?zip=94040,us&APPID=<key>
#http://api.openweathermap.org/data/2.5/weather?zip=94040,us&APPID=<key>&units=metric
#url="http://api.openweathermap.org/data/2.5/forecast/city?zip=94040,us&APPID=<key>&units=metric"
