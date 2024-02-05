import webbrowser
import requests


class CNetWork :
    def __init__(self):
        self.__etatInternet = bool
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            self.__etatInternet = True
        except requests.ConnectionError :
            self.__etatInternet = False
    
    def getEtatInternet(self):
        return self.__etatInternet
    
    def braveSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://search.brave.com/search?q='
                urllink = requests.get(url+query+"&source=web")
                lienBrave = urllink.url
                webbrowser.open(lienBrave)
            return True
        else:
            return False

    def AmazonSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.amazon.fr/s?k='
                urllink = requests.get(url+query)
                lienAmazon = urllink.url
                webbrowser.open(lienAmazon)
            return True
        else:
            return False

    def googleSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.google.com/search?q'
                query = {'q': query}
                urllink = requests.get(url, params=query)
                liengoogle = urllink.url
                webbrowser.open(liengoogle)
            return True
        else:
            return False

    def duckduckgoSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://duckduckgo.com/?q'
                query = {'q': query}
                urllink = requests.get(url, params=query)
                lienduck = urllink.url
                webbrowser.open(lienduck)
            return True
        else:
            return False


    def QwantSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.qwant.com/?l=fr&q'
                query = {'q': query}
                urllink = requests.get(url, params=query)
                lienQwant = urllink.url
                webbrowser.open(lienQwant)
            return True
        else:
            return False

    def EcosiaSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.ecosia.org/search'
                query = {'q': query}
                urllink = requests.get(url,query)
                lienEcosia = urllink.url
                webbrowser.open(lienEcosia)
            return True
        else:
            return False
    
    def bingSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = "https://www.bing.com/search"
                query = {'q': query}
                urllink = requests.get(url, params=query)
                lienbing = urllink.url
                webbrowser.open(lienbing)
            return True
        else:
            return False

    def WikipediaSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://fr.wikipedia.org/wiki/'
                lienWiki = url+query
                webbrowser.open(lienWiki)
            return True
        else:
            return False

    def ReversoSeacrch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.reverso.net/traduction-texte#sl=fra&tl=eng&text='
                urllink = requests.get(url+query)
                liengoogle = urllink.url
                webbrowser.open(liengoogle) 
            return True
        else:
            return False

    def WordreferenceSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://www.wordreference.com/fren/'
                lienWord = url+query
                webbrowser.open(lienWord)
            return True
        else:
            return False

    def YTmusicSearch(self,query:str)->bool:
        if (self.__etatInternet==True):
            with requests.session() as c:
                url = 'https://music.youtube.com/search'
                query = {'q': query}
                urllink = requests.get(url, params=query)
                lienYTmusic = urllink.url
                webbrowser.open(lienYTmusic)
            return True
        else:
            return False

    def GrandRecherche(self,query:str)->bool:
        if (self.__etatInternet==True):
            googleSearch(query)
            duckduckgoSearch(query)
            QwantSearch(query)
            EcosiaSearch(query)
            bingSearch(query) 
            braveSearch(query)
            return True
        else:
            return False
    
        
def TestInternet():
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        return True
    except requests.ConnectionError :
        return False
def braveSearch(query):
    with requests.session() as c:
        url = 'https://search.brave.com/search?q='
        urllink = requests.get(url+query+"&source=web")
        lienBrave = urllink.url
        webbrowser.open(lienBrave)
def AmazonSearch(query):
    with requests.session() as c:
        url = 'https://www.amazon.fr/s?k='
        urllink = requests.get(url+query)
        lienAmazon = urllink.url
        webbrowser.open(lienAmazon)
def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle)
def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.open(lienduck)
    
def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.open(lienQwant)

def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.open(lienEcosia)
  
def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.open(lienbing)
def WikipediaSearch(query):
    with requests.session() as c:
        url = 'https://fr.wikipedia.org/wiki/'
        lienWiki = url+query
        webbrowser.open(lienWiki)
def ReversoSeacrch(query):
    with requests.session() as c:
        url = 'https://www.reverso.net/traduction-texte#sl=fra&tl=eng&text='
        urllink = requests.get(url+query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle) 
def WordreferenceSearch(query):
    with requests.session() as c:
        url = 'https://www.wordreference.com/fren/'
        lienWord = url+query
        webbrowser.open(lienWord)

def YTmusicSearch(query):
    with requests.session() as c:
        url = 'https://music.youtube.com/search'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienYTmusic = urllink.url
        webbrowser.open(lienYTmusic)

def GrandRecherche(query):
    googleSearch(query)
    duckduckgoSearch(query)
    QwantSearch(query)
    EcosiaSearch(query)
    bingSearch(query) 
    braveSearch(query)

