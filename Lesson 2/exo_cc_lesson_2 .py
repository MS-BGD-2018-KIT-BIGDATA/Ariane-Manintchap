# Calculer le pourcentage de réduction des pc Acer et pc Dell sur Cdiscount

import requests
from bs4 import BeautifulSoup


url = 'http://www.purepeople.com/article/caroline-de-maigret-ce-jour-ou-yarol-poupaud-a-quitte-sa-copine-pour-elle_a251827/1'
share_class_pp = "c-sharebox__stats-number"

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




