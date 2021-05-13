# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:05:13 2021

@author: ASB
"""

#import pandas library
import pandas as pd

# import urllib library
from urllib.request import urlopen
  
# import json
import json

# store the URL in url as 
# parameter for urlopen
url_stats = "https://www.thesportsdb.com/api/v1/json/40130162/lookupeventstats.php?id="
url_events = "https://www.thesportsdb.com/api/v1/json/40130162/eventsseason.php?id=4328&s=2020-2021"

# store the response of URL - Events
response_events = urlopen(url_events)
  
# storing the JSON response 
# from url in data
data_json_events = json.loads(response_events.read())
  
#extract the Dict
datos_eventos = data_json_events.get("events")

#Create the DataFrame
df_eventos = pd.DataFrame(datos_eventos)

#Create the list of Events
lista_eventos = [evento for evento in df_eventos['idEvent']]

#Create the DataFrame with all the stats of the events
df_stats = pd.DataFrame()

for i in range(0,380):
    url_stats = "https://www.thesportsdb.com/api/v1/json/40130162/lookupeventstats.php?id=" + lista_eventos[i]
    response_stats = urlopen(url_stats)
    data_json_stats = json.loads(response_stats.read())
    datos_stats = data_json_stats.get("eventstats")
    df = pd.DataFrame(datos_stats)
    df_stats = pd.concat([df_stats,df], axis = 0)
    
df_stats.to_csv('stats_eventos.csv')
df_eventos.to_csv('eventos.csv')
    