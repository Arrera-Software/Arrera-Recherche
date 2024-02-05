from tkinter import*
from ModuleInternet import*
import os
from time import*
from tkinter.messagebox import*
class ArreraRecherche :
    def __init__(self):
        self.__objRecherche = CNetWork()
        self.__color = "#3c0f14"
        self.__textColor = "white"
        self.__tailleText =  "15"
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
        cadreSearch = Frame(self.__windows,bg=self.__color,width=500,height=100)
        cadreLeft = Frame(self.__windows,bg=self.__color,width=175,height=550)
        cadreRight = Frame(self.__windows,bg=self.__color,width=330,height=550)
        #Zone de texte
        self.__zoneEntrer = Entry(cadreSearch,bg="white",bd=0,font=("arial","13"))
        #Bouton
        BoutonValider = Button(cadreSearch,bg=self.__color,command=lambda : self.__valider(self.__getRecherche()))
        BoutonWordReference = Button(cadreLeft,bg=self.__color,command=lambda : self.__searchWordReference(self.__getRecherche()))
        BoutonWikipedia = Button(cadreLeft,bg=self.__color,command=lambda :self.__searchWikipedia(self.__getRecherche()))
        boutonReverso = Button(cadreLeft,bg=self.__color,command=lambda :self.__searchReverso(self.__getRecherche()))   
        BoutonMusic = Button(cadreLeft,bg=self.__color,command=lambda :self.__searchYtMusic(self.__getRecherche()))
        #var image 
        iconValider = PhotoImage(file="image/iconRecherche.png",master=BoutonValider)
        iconMusic =  PhotoImage(file="image/Music.png",master=BoutonMusic)
        iconWikipedia = PhotoImage(file="image/iconWikipedia.png",master=BoutonWikipedia)
        iconWordreference = PhotoImage(file="image/iconWordreference.png",master=boutonReverso)
        iconReverso=PhotoImage(file="image/iconReverso.png",master=BoutonMusic)
        #Application des image
        BoutonValider.image_names=iconValider
        BoutonWordReference.image_names=iconWordreference
        BoutonWikipedia.image_names=iconWikipedia
        boutonReverso.image_names=iconReverso  
        BoutonMusic.image_names=iconMusic
        BoutonValider.configure(image=iconValider)
        BoutonWordReference.configure(image=iconWordreference)
        BoutonWikipedia.configure(image=iconWikipedia)
        boutonReverso.configure(image=iconReverso)   
        BoutonMusic.configure(image=iconMusic)
        #label
        labelText=Label(cadreRight,
                        text="Drapeau pour lancer une recherche :\n\n-google : @gg\n\n-Ecosia : @ec\n\n-Qwant : @qw\n\n-Brave : @br\n\n-Bing : @bg\n\n-Grand Recherche : @gr\n\n-Amazon : @am"
                        ,bg=self.__color,font=("arial","15"),fg=self.__textColor)
        #affichage
        #cadre
        cadreSearch.pack(side="top")
        cadreLeft.pack(side="left")
        cadreRight.pack(side="right")
        #zone de texte
        self.__zoneEntrer.place(x=10,y=30,width=395,height=30)
        #bouton
        BoutonValider.place(x=420,y=15)
        BoutonMusic.place(x=50,y=25)
        BoutonWordReference.place(x=50,y=125)
        BoutonWikipedia.place(x=50,y=225)
        boutonReverso.place(x=50,y=325)
        #label
        labelText.place(x=0,y=0)
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