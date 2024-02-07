from tkinter import*
from ModuleInternet import*
import os
from time import*
from tkinter.messagebox import*
class ArreraRecherche :
    def __init__(self):
        self.__objRecherche = CNetWork()
        self.__color = "white"
        self.__textColor = "black"
        self.__windows = Tk()
        self.__windows.iconphoto(False,PhotoImage(file="image/ArreraRecherche.png"))
        self.__windows.title("Arrera Recherche")
        self.__windows.config(bg=self.__color)
    
    def __guiSearch(self):
        #Fenetre
        self.__windows.iconphoto(False,PhotoImage(file="image/ArreraRecherche.png"))
        self.__windows.title("Arrera Recherche")
        self.__windows.maxsize(550,680)
        self.__windows.minsize(550,680)
        self.__windows.config(bg=self.__color)
        #Cadre
        cadreSearch = Frame(self.__windows,bg="red",width=500,height=70)
        cadreLeft = Frame(self.__windows,bg="yellow",width=50,height=680)
        cadreRight = Frame(self.__windows,bg="green",width=500,height=610)
        #bouton
        #cadreLeft
        btnHistorique = Button(cadreLeft,width="5",height="2")
        btnParametre = Button(cadreLeft,width="5",height="2")
        btnApropos = Button(cadreLeft,width="5",height="2")
        #cadreRight
        btnResult = [
            Button(cadreRight,width=40,font=("arial","15")),#duck
            Button(cadreRight,width=40,font=("arial","15")),#google
            Button(cadreRight,width=40,font=("arial","15")),#Bing
            Button(cadreRight,width=40,font=("arial","15")),#Brave
            Button(cadreRight,width=40,font=("arial","15")),#Ecosia
            Button(cadreRight,width=40,font=("arial","15")),#Qwant
            Button(cadreRight,width=40,font=("arial","15")),#bigSearch
            Button(cadreRight,width=40,font=("arial","15")),#Wikipedia
            Button(cadreRight,width=40,font=("arial","15")),#Amazon
            Button(cadreRight,width=40,font=("arial","15")),#WordReference
            Button(cadreRight,width=40,font=("arial","15")),#YtMusic
            Button(cadreRight,width=40,font=("arial","15"))#Reverso
        ]
        #Zone de texte
        self.__zoneEntrer = Entry(cadreSearch,bg="white",bd=0,font=("arial","13"),width=50,relief="solid", borderwidth=2)
        
        #Calcule de passement
        largeurCadreLeft = cadreLeft.winfo_reqwidth()
        largeurcadreRight = cadreRight.winfo_reqwidth()
        largeurBTN = (btnResult[1].winfo_reqheight()/2)
        #affichage
        #cadre
        cadreSearch.place(x=50,y=0)
        cadreLeft.place(x=0,y=0)
        cadreRight.place(x=50,y=70)
        #btnCadreLeft
        btnHistorique.place(x=((largeurCadreLeft-btnHistorique.winfo_reqwidth())//2),y=45)
        btnParametre.place(x=((largeurCadreLeft-btnParametre.winfo_reqwidth())//2),y=105)
        btnApropos.place(x=((largeurCadreLeft-btnApropos.winfo_reqwidth())//2),y=620)
        #btncadreRight
        btnResult[0].place(x=((largeurcadreRight-btnResult[0].winfo_reqwidth())//2),y=15)
        btnResult[1].place(x=((largeurcadreRight-btnResult[1].winfo_reqwidth())//2),y=60)
        btnResult[2].place(x=((largeurcadreRight-btnResult[2].winfo_reqwidth())//2),y=105)
        btnResult[3].place(x=((largeurcadreRight-btnResult[3].winfo_reqwidth())//2),y=150)
        btnResult[4].place(x=((largeurcadreRight-btnResult[4].winfo_reqwidth())//2),y=195)
        btnResult[5].place(x=((largeurcadreRight-btnResult[5].winfo_reqwidth())//2),y=240)
        btnResult[6].place(x=((largeurcadreRight-btnResult[6].winfo_reqwidth())//2),y=285)
        btnResult[7].place(x=((largeurcadreRight-btnResult[7].winfo_reqwidth())//2),y=330)
        btnResult[8].place(x=((largeurcadreRight-btnResult[8].winfo_reqwidth())//2),y=375)
        btnResult[9].place(x=((largeurcadreRight-btnResult[0].winfo_reqwidth())//2),y=420)
        btnResult[10].place(x=((largeurcadreRight-btnResult[10].winfo_reqwidth())//2),y=465)
        btnResult[11].place(x=((largeurcadreRight-btnResult[11].winfo_reqwidth())//2),y=510)
        #zone de texte
        self.__zoneEntrer.place(relx=0.5,rely=0.5,anchor="center")
        self.__getTouches(13)

    def __searchWordReference(self,requette:str):
        if requette :
            self.__objRecherche.WordreferenceSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")

    def __searchWikipedia(self,requette:str):
        if requette :
            self.__objRecherche.WikipediaSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")

    def __searchReverso(self,requette:str):
        if requette :
            self.__objRecherche.ReversoSeacrch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")

    def __searchYtMusic(self,requette:str):
        if requette :
            self.__objRecherche.YTmusicSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchgoogle(self,requette:str):
        if requette :
            self.__objRecherche.googleSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchEcosia(self,requette:str):
        if requette :
            self.__objRecherche.EcosiaSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchQwant(self,requette:str):
        if requette :
            self.__objRecherche.QwantSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchBing(self,requette:str):
        if requette :
            self.__objRecherche.bingSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchBrave(self,requette:str):
        if requette :
            self.__objRecherche.braveSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchAmazon(self,requette:str):
        if requette :
            self.__objRecherche.AmazonSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __searchDuckduckgo(self,requette:str):
        if requette :
            self.__objRecherche.duckduckgoSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __bigSearch(self,requette:str):
        if requette :
            self.__objRecherche.GrandRecherche(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __guiNoInternet(self):
        self.__windows.maxsize(525,70)
        self.__windows.minsize(525,70)
        label=Label(self.__windows,text="Pas d'acces a internet",font=("arial",30),bg="black",fg="white").pack()

    def __valider(self,requette:str):
        if requette :
            test = requette[:1]
            if test == "@":
                flag =  requette[:3]
                recherche = requette[3:]
                if flag == "@gg":
                    self.__searchgoogle(recherche)
                else :
                    if flag == "@ec":
                        self.__searchEcosia(recherche)
                    else:
                        if flag == "@qw":
                            self.__searchQwant(recherche)
                        else :
                            if flag == "@bg":
                                self.__searchBing(recherche)
                            else :
                                if flag == "@br":
                                    self.__searchBrave(recherche)
                                else :
                                    if flag == "@gr":
                                        self.__bigSearch(recherche)
                                    else:
                                        if flag == "@am":
                                            self.__searchAmazon(recherche)
            else :
                self.__objRecherche.duckduckgoSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __getRecherche(self)->str:
        sortie = self.__zoneEntrer.get()
        self.__zoneEntrer.delete(0,END)
        return sortie

    def __getTouches(self,touche1):
        def anychar(event):
            if event.keycode == touche1:
                self.__valider(self.__getRecherche())
        self.__windows.bind("<Key>", anychar)

    def boot(self):
        if (self.__objRecherche.getEtatInternet()==True):
            self.__guiSearch()
        else :
            self.__guiSearch()   
        self.__windows.mainloop()

ArreraRecherche().boot()