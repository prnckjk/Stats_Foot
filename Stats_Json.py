# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:05:13 2021

@author: ASB
"""

#import pandas library
import pandas as pd

"""# import urllib library
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
df_eventos.to_csv('eventos.csv')"""

df_stats = pd.read_csv("stats_eventos.csv")
df_eventos = pd.read_csv("eventos_clean.csv")
df_stats_clean = pd.read_csv("stats_clean.csv")

df_stats_event = pd.DataFrame()



lista_home = []*300
lista_away = []*300
count1 = 0
count2= 16

while count2 <= 4576:
    lista_home.append([df_stats['intHome'][count1:count2].tolist()])
    lista_away.append([df_stats['intAway'][count1:count2].tolist()])
    count1 = count2
    count2 +=16
        
titulos = df_stats_clean.columns.tolist()   
   

count3 = 0

"""df_stats_clean['Ball Possession Home'][1] = lista_home[1][0][0]
df_stats_clean['Blocked Shots Home'][1] = lista_home[1][0][1]
       
while count3 <=286:
      count4 =1
      count_titulo = 2 
      while count4 < 16 and count_titulo < 18:
          df_stats_clean[titulos[count_titulo]][count3] = lista_home[count3][0][count4]
          count4 +=1
          count_titulo +=1
     count3 +=1"""

for i in range(0,286):
    count4 =0
    count_titulo = 2
    while count4 < 16 and count_titulo < 18:
        df_stats_clean[titulos[count_titulo]][i] = lista_home[i][0][count4]
        count4 +=1
        count_titulo +=1

for i in range(0,286):
    count4 =0
    count_titulo = 18
    while count4 < 16 and count_titulo < 34:
        df_stats_clean[titulos[count_titulo]][i] = lista_away[i][0][count4]
        count4 +=1
        count_titulo +=1        

df_stats_clean.to_csv('df_stats_clean.csv')