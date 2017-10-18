# Connaitre les distances en voiture villes √  villes 
# dans le but d'implanter des bureaux commerciaux en france
# r√©cu√©rer la liste des 100 plus grandes villes
# puis sortir la matrice des distances
# API √  utiliser: google distance matrice API
# https://developers.google.com/maps/documentation/distance-matrix/?hl=fr
# Cyril Nguyen
# joseph asouline

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = "https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/"
url1 = "https://developers.google.com/maps/documentation/distance-matrix/?hl=fr"

def getSoupFromURL(url, method='get', data={}):

  if method == 'get':
    res = requests.get(url)
  elif method == 'post':
    res = requests.post(url, data=data)
  else:
    return None

  if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
  else:
    return None

soup = getSoupFromURL(url)

#Api = getSoupFromURL(url1)

def getTowns(url):
    soup = getSoupFromURL(url)
    Towns = []        
    for i in range(1,10):
        Towns += [soup.find_all("td", class_ ="xl65")[3*i-2].text.strip()]
    return(Towns)
    
towns = getTowns(url)

distanceTown = pd.DataFrame(index = towns, columns=towns)

key = "AIzaSyBdEWDYTFKG0MsKxpY13uNt3QyV-YCe620"

for town1 in towns:
    for town2 in towns:
        url3 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + town1 + ",FR&destinations=" + town2 +",FR&key=" + key 
        dist = requests.get(url3)
        distanceTown.loc[town1,town2] = dist.json()['rows'][0]['elements'][0]['distance']['text']


https://maps.googleapis.com/maps/api/distancematrix/json?origins=Paris&destinations=Nancy






