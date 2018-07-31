#pip install requests
import requests
import pprint

BaseURL = "http://api.openweathermap.org/data/2.5/weather" # location

#City = "Hong Kong" #table_name 

AppId = "abfa55e62ad2f34f61750264d2db2281" #appid => $_SESSION["username"]





while(True):
	Input = input("Input the city")
	if(Input == "Quit"):
		break
	else:
		SQL = BaseURL + "?q=" + Input + "&appid=" + AppId #sql 
		req = requests.get(SQL)
		stuff = req.json()
		pprint.pprint(stuff)
		