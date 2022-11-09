from tkinter import*
from ModuleInternet import*
import os
from time import*

#Constante
Color = "#3c0f14"
TextColor = "white"
TailleText =  "15"
def Touches(fenetre,fonc1,touche1):
    def anychar(event):
        if event.keycode == touche1:
            fonc1()
    fenetre.bind("<Key>", anychar)

def NoInternet():
    ScreenSearch = Tk()
    ScreenSearch.title("Arrera Recherche")
    ScreenSearch.maxsize(525,70)
    ScreenSearch.minsize(525,70)
    ScreenSearch.config(bg="black")
    label=Label(ScreenSearch,text="Pas d'acces a internet",font=("arial",30),bg="black",fg="white").pack()
    ScreenSearch.mainloop()

def InterafaceSearch():
    ScreenSearch = Tk()
    #var image 
    iconRecherche = PhotoImage(file="image/iconRecherche.png")
    iconMusic =  PhotoImage(file="image/Music.png")
    iconWikipedia = PhotoImage(file="image/iconWikipedia.png")
    iconWordreference = PhotoImage(file="image/iconWordreference.png")
    iconReverso=PhotoImage(file="image/iconReverso.png")
    #Fenetre
    ScreenSearch.iconphoto(False,PhotoImage(file="image/ArreraRecherche.png"))
    ScreenSearch.title("Arrera Recherche")
    ScreenSearch.maxsize(550,680)
    ScreenSearch.minsize(550,680)
    ScreenSearch.config(bg=Color)
    #Cadre
    cadreSearch = Frame(ScreenSearch,bg=Color,width=500,height=100)
    cadreLeft = Frame(ScreenSearch,bg=Color,width=175,height=550)
    cadreRight = Frame(ScreenSearch,bg=Color,width=330,height=550)
    #Zone de texte
    ZoneEntrer = Entry(cadreSearch,bg="white",bd=0,font=("arial","13"))
    #fonction
    def Valider():
        requette = ZoneEntrer.get()
        test = requette[:1]
        if test == "@":
            char =  requette[:3]
            text = requette[3:]
            if char == "@gg":
                googleSearch(text)
            if char == "@ec":
                EcosiaSearch(text)
            if char == "@qw":
                QwantSearch(text)
            if char == "@bg":
                bingSearch(text)
            if char == "@br":
                braveSearch(text)
            if char == "@gr":
                GrandRecherche(text)
            if char == "@am":
                AmazonSearch(text)
        else :
            duckduckgoSearch(requette)
    def WordReference():
        requette = ZoneEntrer.get()
        WordreferenceSearch(requette)
    def Wikipedia():
        requette = ZoneEntrer.get()
        WikipediaSearch(requette)
    def Reverso():
        requette = ZoneEntrer.get()
        ReversoSeacrch(requette)
    def music():
        requette = ZoneEntrer.get()
        YTmusicSearch(requette)
    #Bouton
    BoutonValider = Button(cadreSearch,command=Valider,image=iconRecherche,bg=Color)
    BoutonWordReference = Button(cadreLeft,bg=Color,image=iconWordreference,command=WordReference)
    BoutonWikipedia = Button(cadreLeft,bg=Color,image=iconWikipedia,command=Wikipedia)
    boutonReverso = Button(cadreLeft,image=iconReverso,bg=Color,command=Reverso)   
    BoutonMusic = Button(cadreLeft,bg=Color,image=iconMusic,command=music)
    #label
    labelText=Label(cadreRight,text="Drapeau pour lancer une recherche :\n\n-google : @gg\n\n-Ecosia : @ec\n\n-Qwant : @qw\n\n-Brave : @br\n\n-Bing : @bg\n\n-Grand Recherche : @gr\n\n-Amazon : @am",bg=Color,font=("arial","15"),fg=TextColor)
    #affichage
    #cadre
    cadreSearch.pack(side="top")
    cadreLeft.pack(side="left")
    cadreRight.pack(side="right")
    #zone de texte
    ZoneEntrer.place(x=10,y=30,width=395,height=30)
    #bouton
    BoutonValider.place(x=420,y=15)
    BoutonMusic.place(x=50,y=25)
    BoutonWordReference.place(x=50,y=125)
    BoutonWikipedia.place(x=50,y=225)
    boutonReverso.place(x=50,y=325)
    #label
    labelText.place(x=0,y=0)
    #boucle tkinter
    ScreenSearch.mainloop()   


EtatInternet = TestInternet()
if EtatInternet == True:
    InterafaceSearch()
if EtatInternet == False :
    NoInternet()