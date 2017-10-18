# Récupération via crawling de la liste des 256 top contributors sur cette 
# page https://gist.github.com/paulmillr/2657075
# En utilisant l'API github https://developer.github.com/v3/ récupérer pour 
# chacun de ces users le nombre moyens de stars des repositories qui leur 
# appartiennent. Pour finir classer ces 256 contributors par leur note moyenne.﻿
# voir la première fonction de françois (à prendre)


import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://gist.github.com/paulmillr/2657075'

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

#rows = soup.find_all("th", scope = "row")
#for row in rows:
#    print(row.parent.text + " " + row.parent.td.text)

def getUserNames(url):
    soup = getSoupFromURL(url)
    Usernames = []        
    for i in range(0,256):
        Usernames += [soup.find_all("th", scope = "row")[i].parent.a.text]
    return(Usernames)
        

Usernames = getUserNames(url)    
for i in range(0,256):
    print('#' + str(i+1) + ' ' + Usernames[i])

def getNomberMeanofStarUser(user):
    #url_search = "https://github.com/" + user
    url_search = "https://api.github.com/users/" + user + "/repos"
    res = requests.get(url_search) 
    if res.status_code == 200:
        mean = pd.Series([rep['stargazers_count'] for rep in res.json()]).mean()
        return print("Le nombre moyen de star des repositories de l user " + user +" est " + str(mean))   
    else:
        return 'url wrong response'
    
for user in Usernames:
    print(getNomberMeanofStarUser(user))   
 


