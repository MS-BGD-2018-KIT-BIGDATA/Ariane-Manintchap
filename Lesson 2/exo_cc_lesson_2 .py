# Calculer le pourcentage de réduction des pc Acer et pc Dell sur Cdiscount

import requests
from bs4 import BeautifulSoup
import numpy as np


# url = "https://www.cdiscount.com/search/10/dell.html#_his_"

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

pc = ["acer", "dell"]

for computer in pc:
    url = "https://www.cdiscount.com/search/10/" + computer + ".html#_his_"
    soup = getSoupFromURL(url)
    for bloc in soup.find_all("div", class_="prdtBloc"):
        print (bloc.find_all("div", class_="prdtBTit")[0].text)
        lastprice = bloc.find_all("div", class_="prdtPrSt")
        if lastprice != []:
            pmax = int(lastprice[0].text.split(",")[0])
            cmax = int(lastprice[0].text.split(",")[1])
            pmin = int(bloc.find_all("span", class_="price")[0].text.split("€")[0])
            cmin = int(bloc.find_all("span", class_="price")[0].text.split("€")[1])            
            print ("The previous price was " + lastprice[0].text.replace(",","€"))
            print ("The new price is " + bloc.find_all("span", class_="price")[0].text)
            print ("the reduction is " + str(pmax - pmin) + "€"+ str(np.abs(cmax - cmin)) + "\n")
        else:
            print ("The price is " + bloc.find_all("span", class_="price")[0].text)
            print ("Il n'existe pas de réduction"+ "\n")
            

