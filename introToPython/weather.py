import requests
import json
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
authorization = "CWB-4E884048-6F63-4D56-AA33-D37CD194C120"
url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-053"
res = requests.get(url, {"Authorization": authorization}).json()
locations = res["records"]["locations"][0]["location"]
for location in locations:
    if location["locationName"]=="東區":
        print(location["locationName"])
        weatherElements = location["weatherElement"]
        for weatherElement in weatherElements:
            #print("weather element ={}".format(weatherElement))
            if weatherElement["elementName"] == "WeatherDescription":
                timeDicts = weatherElement["time"]
                for timeDict in timeDicts:
                    date , time = timeDict["startTime"].split()
                    print(time, timeDict["elementValue"][0]["value"])