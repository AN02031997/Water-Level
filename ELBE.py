from random import random
import requests
import pandas as pd
import time
import csv

while(True):

    r = requests.get('https://pegelonline.wsv.de/webservices/rest-api/v2/stations.json?includeTimeseries=true&includeCurrentMeasurement=true')

    parsed = r.json()

    longname=[]
    value=[]
    parsedindex=[]
    indexno=[]

    for i in range(len(parsed)):
        if parsed[i]["water"]["shortname"]=="ELBE":
            indexno.append(i)
            parsedindex.append(parsed[i]["water"]["shortname"])
            longname.append(parsed[i]["timeseries"][0]["longname"])
            value.append(parsed[i]["timeseries"][0]["currentMeasurement"]["value"])

    df=pd.DataFrame(list(zip(indexno,parsedindex,longname, value)),
                columns =['Station','PID','LONGNAME', 'VALUE'])


    print(df)
    header = ['Station','PID','LONGNAME', 'VALUE']
    data = [
        [df[5:8]]
        
    ]

    with open('water level.csv', 'w', encoding='UTF8', newline='') as f:

        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    time.sleep(5)

