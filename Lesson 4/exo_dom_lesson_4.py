# L'objectif est de générer un fichier de données sur le prix des Renault Zoé 
# sur le marché de l'occasion en Ile de France, PACA et Aquitaine. 

# Vous utiliserez leboncoin.fr comme source. Le fichier doit être propre et 
# contenir les infos suivantes : version ( il y en a 3), année, kilométrage, 
# prix, téléphone du propriétaire, est ce que la voiture est vendue par un 
# professionnel ou un particulier.

# Vous ajouterez une colonne sur le prix de l'Argus du modèle que vous récupérez 
# sur ce site http://www.lacentrale.fr/cote-voitures-renault-zoe--2013-.html.

# Les données quanti (prix, km notamment) devront être manipulables (pas de string, pas d'unité).
# Vous ajouterez une colonne si la voiture est plus chere ou moins chere que sa cote moyenne.

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

def getPageNumber(statu):
    url = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?q=Renault%20Zo%E9&f=" + statu
    soup = getSoupFromURL(url)
    url_pageMax = soup.find_all("a", {"id": "last"}, class_="element page static")[0]["href"]
    return int(re.findall("\d+", url_pageMax)[0])

def getVariablesValues(url):
    soup = getSoupFromURL(url)
    val = soup.find_all("span", class_="value")
    data = {}
    # insertion de la version
    data["version"] = soup.find_all("h1", class_="no-border")[0].text.strip()
    #insertion de l'année
    data["Year"] = val[4].text.strip()
    #insertion du kilometrage
    Kilometrage = "".join(re.findall("\d+", val[5].text.strip()))
    data["Kilometrage"] = int(Kilometrage)
    #insertion du prix
    price = "".join(re.findall("\d+", val[0].text.strip()))
    data["price"] = int(price)
    #insertion du statu
    return data
    
statu = ["c", "p"]
result = []

def ExtratVariablesParticulier(url):
    m = "https:" + url
    don = getVariablesValues(m)
    don["statu_propi"] = "c"
    return don

def ExtratVariablesProffessionel(url):
    m = "https:" + url
    don = getVariablesValues(m)
    don["statu_propi"] = "p"
    return don   

for elt in statu:
    if elt == "c":
        n = getPageNumber(elt)
        for i in range(1,n):
            urlList = getListOfUrlCar(elt,i)    
            pool = mp.Pool(processes =10)
            don = pool.map(ExtratVariablesParticulier, urlList)#renvoit un tableau d'elements
            result.extend(don)
    else:
        url3 = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?q=Renault%20Zo%E9&f=p" 
        soup = getSoupFromURL(url3)
        class_result = "list_item clearfix trackable"
        urlList = []
        urlList += [a['href'] for a in soup.find_all("a", class_= class_result)]
        pool = mp.Pool(processes =10)
        don = pool.map(ExtratVariablesProffessionel, urlList)#renvoit un tableau d'elements
        result.extend(don)
            
df_Ile_de_france = pd.DataFrame(result)
df_Ile_de_france["version"] = df_Ile_de_france.version.str.lower()

def split_it(u):
    result = re.findall("(fuence|zoé|zoe|zen|intens|life){1}", u)
    result.reverse()
    return result[0]

df_Ile_de_france["version"] = df_Ile_de_france["version"].apply(split_it) 
df_Ile_de_france = df_Ile_de_france.replace(to_replace= 'ze', value='zen').replace(to_replace= 'zoé', value='zen').replace(to_replace= 'fuence', value='zen').replace(to_replace= 'zoe', value='zen')
d = df_Ile_de_france.groupby("Year").first()  
n = df_Ile_de_france.shape[0]
df_Ile_de_france["Argus"] = np.zeros(n)

for year in d.index:
    df2 = df_Ile_de_france[df_Ile_de_france.Year == year]
    df2 = df2.groupby("version").first()
    for vers in df2.index:
        url6 = "https://www.lacentrale.fr/cote-auto-renault-zoe-" + vers + "+charge+rapide-" + year + ".html"
        soup6 = getSoupFromURL(url6)
        Argus = soup6.find_all("span", class_= "jsRefinedQuot")[0].text
        Argus = int("".join(re.findall("\d+", Argus)))
        df_Ile_de_france["Argus"][(df_Ile_de_france.Year == year) & (df_Ile_de_france.version == vers)] = Argus

df_Ile_de_france.to_csv('df_Ile_de_france.csv')

