# Connaitre les distances en voiture villes à villes 
# dans le but d'implanter des bureaux commerciaux en france
# récuérer la liste des 100 plus grandes villes
# puis sortir la matrice des distances
# API à utiliser: google distance matrice API
# https://developers.google.com/maps/documentation/distance-matrix/?hl=fr
# Cyril Nguyen

import requests
from bs4 import BeautifulSoup

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
    for i in range(1,102):
        Towns += [soup.find_all("td", class_ ="xl65")[3*i-2].text.strip()]
    return(Towns)
    
towns = getTowns(url)



