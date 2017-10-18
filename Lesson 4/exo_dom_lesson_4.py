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

# url_zoe = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?th=1&q=Renault%20Zo%E9"
# url_prof = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?q=Renault%20Zo%E9&f=c"
# url_particul = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?q=Renault%20Zo%E9&f=p"


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
    data = []
    # insertion de la version
    data.append(soup.find_all("h1", class_="no-border")[0].text.strip())
    #insertion de l'année
    data.append(val[4].text.strip())
    #insertion du kilometrage
    Kilometrage = val[5].text.strip()
    data.append(val[5].text.strip())
    #insertion du prix
    data.append(val[0].text.strip())
    #insertion du statu
    return data
    
statu = ["c", "p"]
df_Ile_de_france = pd.DataFrame(columns=["version", "année", "kilométrage", "prix", "statu_propri"])

version = []
Year= []
kilo= []
price = []
statu_prop = []

for elt in statu:
    if elt == "c":
        n = getPageNumber(elt)
        for i in range(1,n):
            urlList = getListOfUrlCar(elt,i)
            for url1 in urlList:
                m = "https:" + url1
                don = getVariablesValues(m)
                version.append(don[0])
                Year.append(don[1])
                kilo.append(don[2])
                price.append(don[3])
                statu_prop.append(elt)
    else:
        url3 = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?q=Renault%20Zo%E9&f=p" 
        soup = getSoupFromURL(url3)
        class_result = "list_item clearfix trackable"
        results_search = []
        results_search += [a['href'] for a in soup.find_all("a", class_= class_result)]
        urlList = results_search
        for url1 in urlList:
            m = "https:" + url1
            don = getVariablesValues(m)
            version.append(don[0])
            Year.append(don[1])
            kilo.append(don[2])
            price.append(don[3])
            statu_prop.append(elt)
    
df_Ile_de_france["version"] = version    
df_Ile_de_france["année"] = Year
df_Ile_de_france["kilométrage"] = kilo
df_Ile_de_france["prix"] = price
df_Ile_de_france["statu_propri"] = statu_prop













def getPrice(url):
    soup = getSoupFromURL(url)
    return soup.find_all("span", class_="value")[0].text.strip()

def getYear(url):
    soup = getSoupFromURL(url)
    return soup.find_all("span", class_="value")[4].text.strip()

def getKilometrage(url):
    soup = getSoupFromURL(url)
    Kilometrage = soup.find_all("span", class_="value")[5].text.strip()
    return re.findall("\d+", Kilometrage)


def getVersion(url):
    soup = getSoupFromURL(url)
    return soup.find_all("h1", class_="no-border")[0].text.strip()


age = re.findall("\d{2}", "Ariane a 22 ans")


#re.findall("\d+", '15 254 KM')


url = "https://www.leboncoin.fr/voitures/offres/ile_de_france/?o=1&q=Renault%20Zo%E9&f=c"
soup = getSoupFromURL(url)
soup.find_all("a", class_="element page static")[1]["href"]
soup.find_all("a", {"id": "last"}, class_="element page static")[0]["href"]
u = soup.find_all("a", class_="element page")


soup.find_all("a", {"id": "last"})

<a href="//www.leboncoin.fr/voitures/offres/ile_de_france/?o=3&amp;q=Renault%20Zo%E9&amp;f=c" class="element page static" id="last"><i class="icon-chevron-double-right nomargin"></i></a>


https://www.lacentrale.fr/cote-voitures-renault-zoe--2013-.html
https://www.lacentrale.fr/cote-auto-renault-zoe-intens+charge+rapide-2014.html
https://www.lacentrale.fr/cote-auto-renault-zoe-zen+charge+rapide-2014.html
https://www.lacentrale.fr/cote-auto-renault-zoe-zen+charge+rapide-2014.html

#############################################################################à
url = 'https://gist.github.com/paulmillr/2657075'



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
 


