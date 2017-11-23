# Connaitre les distances en voiture villes à  villes 
# dans le but d'implanter des bureaux commerciaux en france
# récupérer la liste des 100 plus grandes villes
# puis sortir la matrice des distances
# API à  utiliser: google distance matrice API
# https://developers.google.com/maps/documentation/distance-matrix/?hl=fr

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/"

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

def getTowns(url):
    soup = getSoupFromURL(url)
    Towns = []        
    for i in range(1,10):
        Towns += [soup.find_all("td", class_ ="xl65")[3*i-2].text.strip()]
    return(Towns)
    
towns = getTowns(url)

distanceTown = pd.DataFrame(index = towns, columns=towns)

key = "AIzaSyBdEWDYTFKG0MsKxpY13uNt3QyV-YCe620"

# je détermine la matrice distance entre les 8 premières villes
for town1 in towns[:7]:
    for town2 in towns[:7]:
        url3 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + town1 + ",FR&destinations=" + town2 +",FR&key=" + key 
        dist = requests.get(url3)
        distance = dist.json()["rows"][0]['elements'][0]
        if distance["status"] == "OK":
            distanceTown.loc[town1,town2] = distance['distance']['text'].split(" ")[0]

print(distanceTown)
