# ibuprofene

import pandas as pd
import requests
from bs4 import BeautifulSoup


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


url = "https://open-medicaments.fr/api/v1/medicaments?limit=100&query=ibuprofene"
soup = requests.get(url)
labels = ['Name','Prix','Annee','Mois']
Medivament = []
for i in range(0,100):
    code = soup.json()[i]['codeCIS']
    name = soup.json()[i]['denomination']
    url1 = "https://open-medicaments.fr/api/v1/medicaments/" + code
    res1 = requests.get(url1)
    price = res1.json()['presentations'][0]['prix']
    date = res1.json()['dateAMM']
    date = date.split('-')
    year = date[0]
    month  = date[1]
    Medivament.append([name,price,year,month])
df = pd.DataFrame.from_records(Medivament, columns=labels)
df.to_csv('ibuprofene.csv')





