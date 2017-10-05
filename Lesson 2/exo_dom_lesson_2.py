# crawler le résultat des comptes de la ville de Paris pour les exercices 2010 à 2015. 
# récupération des données A,B,C et D sur les colonnes Euros par habitant et par strate.


import requests
from bs4 import BeautifulSoup

years = range(2010,2016)

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


for j in years:
    url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='+ str(j)
    soup = getSoupFromURL(url)
    libele = soup.find_all("td", class_="libellepetit G")
    amount = soup.find_all("td", class_="montantpetit G")    
    print('                                                ')
    print('Comptes ville de Paris pour les exercices de ' + str(j))
    for i in [0, 1, 3, 4]:
        print(libele[i].text)
        print(amount[3*i].text + 'milliers d euro')
        print(amount[3*i + 1].text + 'euros par habitants')
        print(amount[3*i + 2].text + 'en moyenne de la strate')


