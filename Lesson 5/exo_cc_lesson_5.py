# Connaitre les distances en voiture villes √  villes 
# dans le but d'implanter des bureaux commerciaux en france
# r√©cu√©rer la liste des 100 plus grandes villes
# puis sortir la matrice des distances
# API √  utiliser: google distance matrice API
# https://developers.google.com/maps/documentation/distance-matrix/?hl=fr
# Cyril Nguyen
# joseph asouline

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import multiprocessing as mp
import numpy as np

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
    

def getListOfUrlCar(statu,page):
    url_search = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?o="+ str(page) +"&q=Renault%20Zo%E9&f=" + statu
    soup = getSoupFromURL(url_search)
    class_result = "list_item clearfix trackable"
    results_search = []
    results_search += [a['href'] for a in soup.find_all("a", class_= class_result)]
    return results_search



url = "https://open-medicaments.fr/api/v1/medicaments?query=ibuprofene"
soup = requests.get(url)
for elt in soup.json():
    print(elt["denomination"])

"https://open-medicaments.fr/api/v1/medicaments/66801493"
"https://www.open-medicaments.fr/api/v1/medicaments/64565560"





