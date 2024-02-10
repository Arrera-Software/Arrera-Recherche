from tkinter import*
from ModuleInternet import*
import platform
from time import*
from tkinter.messagebox import*
from PIL import Image, ImageTk 
import json

class jsonWork : 
    def __init__(self,file):
        self.fichier = file
    
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)

    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict,writeFile,indent=2)

class historique:
    def __init__(self, nameFile:str):
        self.__fileName = nameFile

    def write(self, contenu):
        with open(self.__fileName, 'a') as fichier:
            fichier.write(contenu + '\n')

    def read(self)->list:
        with open(self.__fileName, 'r') as fichier:
            lignes = fichier.readlines()
            return lignes

    def suppr(self):
        with open(self.__fileName, 'w') as fichier:
            fichier.truncate(0)

class OS :
    def __init__(self) :
        self.os = platform.system()
        
    def osWindows(self):
        if self.os == "Windows":
           return True
        else :
            return False
    
    def osLinux(self):
        if self.os == "Linux":
            return True
        else :
            return False
class ArreraRecherche :
    def __init__(self):
        self.__objRecherche = CNetWork()
        self.__color = str
        self.__textColor = str
        self.__secondColor = str
        self.__listSecondColor = ["#9e9e9e","#595959"]
        self.__listColor = ["white","black"]
        self.__listTextColor = ["black","white"]
        
        self.__listMoteur = ["Google","Duckduckgo","Ecosia","Qwant","Bing","Brave"]
        self.__listTheme = ["Light","Dark"]
        self.__windows = Tk()
        self.__objPara = jsonWork("UserFile/config.json")
        self.__objOS = OS()
        self.__objHistorique = historique("UserFile/historique.txt")
        self.__windows.iconphoto(False,PhotoImage(file="image/ArreraRecherche.png"))
        self.__windows.title("Arrera Recherche")
        
        self.__nameApp = "Arrera Recherche"
        self.__versionApp = "I2024-1.00"
        self.__imagePath = "image/ArreraRecherche.png"
        self.__copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        self.__varMoteur = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        #Creation de cardre
        self.__cadreSearch = Frame(self.__windows,width=500,height=70)
        self.__cadreLeft = Frame(self.__windows,width=50,height=680)
        self.__cadreRight = Frame(self.__windows,width=500,height=610)
        self.__cadreParametre = Frame(self.__windows,width=550,height=680)
        self.__cardeHistorique = Frame(self.__windows,width=550,height=680)
    
    def __setTheme(self):
        if (self.__objPara.lectureJSON("theme")==self.__listTheme[0]):
            self.__color = self.__listColor[0]
            self.__textColor = self.__listTextColor[0]
            self.__secondColor = self.__listSecondColor[0]
        else :
            if (self.__objPara.lectureJSON("theme")==self.__listTheme[1]):
                self.__color = self.__listColor[1]
                self.__textColor = self.__listTextColor[1]
                self.__secondColor = self.__listSecondColor[1]
        self.__windows.config(bg=self.__color)
        self.__cadreSearch.configure(bg=self.__color)
        self.__cadreLeft.configure(bg=self.__secondColor)
        self.__cadreRight.configure(bg=self.__color)
        self.__cadreParametre.configure(bg=self.__color)
        self.__cardeHistorique.configure(bg=self.__color)

    def __guiSearch(self):
        #Fenetre
        self.__windows.iconphoto(False,PhotoImage(file=self.__imagePath))
        self.__windows.title(self.__nameApp)
        self.__windows.maxsize(550,680)
        self.__windows.minsize(550,680)
        #Cadre
        #bouton
        self.__setTheme()
        #cadreLeft
        btnHistorique = Button(self.__cadreLeft,bg=self.__secondColor,command=self.__historiqueGui)
        btnParametre = Button(self.__cadreLeft,bg=self.__secondColor,command=self.__settingGui)
        btnApropos = Button(self.__cadreLeft,bg=self.__secondColor,command=self.Apropop)
        #cardeHistorique
        self.__labelHisto = Label(self.__cardeHistorique,bg=self.__color,fg=self.__textColor,font=("arial","13"), justify="left")
        btnQuitterHistorique = Button(self.__cardeHistorique,text="Retour",bg=self.__color,fg=self.__textColor,command=self.__mainGUI,font=("Arial","15"))    
        #Image BTN
        imageAbout = Image.open("image/IconAbout.png")
        imageSetting = Image.open("image/para.png")
        imageHistorique = Image.open("image/historique.png")
        iconAbout = ImageTk.PhotoImage(imageAbout.resize((40,40)))
        btnApropos.image_names = iconAbout
        btnApropos.configure(image=iconAbout)
        iconSetting = ImageTk.PhotoImage(imageSetting.resize((40,40)))
        btnParametre.image_names = iconSetting
        btnParametre.configure(image=iconSetting)
        iconHistorique = ImageTk.PhotoImage(imageHistorique.resize((40,40)))
        btnHistorique.image_names = iconHistorique
        btnHistorique.configure(image=iconHistorique)
        #cadreRight
        btnResult = [
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Duckduckgo",command=lambda : self.__searchDuckduckgo(self.__getRecherche())),#duck
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Google",command=lambda : self.__searchgoogle(self.__getRecherche())),#google
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Bing",command=lambda : self.__searchBing(self.__getRecherche())),#Bing
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Brave",command=lambda : self.__searchBrave(self.__getRecherche())),#Brave
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Ecosia",command=lambda : self.__searchEcosia(self.__getRecherche())),#Ecosia
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Qwant",command=lambda : self.__searchQwant(self.__getRecherche())),#Qwant
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Grande Recherche",command=lambda : self.__bigSearch(self.__getRecherche())),#bigSearch
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Wikipedia",command=lambda : self.__searchWikipedia(self.__getRecherche())),#Wikipedia
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Amazon",command=lambda : self.__searchAmazon(self.__getRecherche())),#Amazon
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur WordReference",command=lambda : self.__searchWordReference(self.__getRecherche())),#WordReference
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Youtube Music",command=lambda : self.__searchYtMusic(self.__getRecherche())),#YtMusic
            Button(self.__cadreRight,width=40,font=("arial","15"),bg=self.__color,fg=self.__textColor,text="Resultat sur Reverso",command=lambda : self.__searchReverso(self.__getRecherche()))#Reverso
        ]
        #Zone de texte
        self.__zoneEntrer = Entry(self.__cadreSearch,bg="white",bd=0,font=("arial","13"),width=50,relief="solid", borderwidth=2)
        
        #Calcule de passement
        largeurCadreLeft = self.__cadreLeft.winfo_reqwidth()
        largeurcadreRight = self.__cadreRight.winfo_reqwidth()


        largeurcardeHistorique = self.__cardeHistorique.winfo_reqwidth()
        hauteurcardeHistorique= self.__cardeHistorique.winfo_reqheight()
        #affichage
        #cadre
        
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
        
        #cardeHistorique
        btnQuitterHistorique.place(x=(largeurcardeHistorique-btnQuitterHistorique.winfo_reqwidth()),y=(hauteurcardeHistorique-btnQuitterHistorique.winfo_reqheight()))
        #zone de texte
        self.__zoneEntrer.place(relx=0.5,rely=0.5,anchor="center")
        self.__mainGUI()
        if ((self.__objOS.osLinux() == False)and(self.__objOS.osWindows()== True)):
            self.__getTouches(13)
        else :
            if ((self.__objOS.osLinux() == True)and(self.__objOS.osWindows() == False)):
                self.__getTouches(36)

    def __guiParametre(self):
        #cadreParametre
        cadreAffichageSetting = [
            Frame(self.__cadreParametre,bg=self.__color),
            Frame(self.__cadreParametre,bg=self.__color)
        ]
        labelIndicationSetting =  [
            Label(cadreAffichageSetting[0],text="Moteur de recherche par default : ",bg=self.__color,fg=self.__textColor,font=("Arial","15")),
            Label(cadreAffichageSetting[1],text="Theme de l'application : ",bg=self.__color,fg=self.__textColor,font=("Arial","15"))
        ]
        menuListMoteur = OptionMenu(cadreAffichageSetting[0],self.__varMoteur,*self.__listMoteur)
        menuListTheme = OptionMenu(cadreAffichageSetting[1],self.__varTheme,*self.__listTheme)
        btnResetHist = Button(self.__cadreParametre,text="Reset",bg=self.__color,fg=self.__textColor,font=("Arial","15"),width=20,command=self.__resetHistorqueSetting)
        btnValiderSetting = Button(self.__cadreParametre,text="Valider",bg=self.__color,fg=self.__textColor,font=("Arial","15"),width=20,command=self.__validerSetting)
        btnQuitterSetting = Button(self.__cadreParametre,text="Retour",bg=self.__color,fg=self.__textColor,command=self.__mainGUI,font=("Arial","15"))
        #Recuperation dimension
        largeurcadreParametre = self.__cadreParametre.winfo_reqwidth()
        hauteurcadreParametre = self.__cadreParametre.winfo_reqheight()
        #btncadreParametre
        labelIndicationSetting[0].pack(side="left")
        labelIndicationSetting[1].pack(side="left")
        menuListMoteur.pack(side="right")
        menuListTheme.pack(side="right")
        cadreAffichageSetting[0].place(x=15,y=100)
        cadreAffichageSetting[1].place(x=15,y=200)
        btnResetHist.place(x=((largeurcadreParametre-btnValiderSetting.winfo_reqwidth())//2),y=400)
        btnValiderSetting.place(x=((largeurcadreParametre-btnValiderSetting.winfo_reqwidth())//2),y=450)
        btnQuitterSetting.place(x=(largeurcadreParametre-btnQuitterSetting.winfo_reqwidth()),y=(hauteurcadreParametre-btnQuitterSetting.winfo_reqheight()))

    def __mainGUI(self):
        self.__cadreParametre.place_forget()
        self.__cardeHistorique.place_forget()
        self.__cadreSearch.place(x=50,y=0)
        self.__cadreLeft.place(x=0,y=0)
        self.__cadreRight.place(x=50,y=70)
    
    def __settingGui(self):
        self.__guiParametre()
        self.__cadreParametre.place(x=0,y=0)
        self.__cardeHistorique.place_forget()
        self.__cadreSearch.place_forget()
        self.__cadreLeft.place_forget()
        self.__cadreRight.place_forget()
    
    def __historiqueGui(self):
        listHistorique = self.__objHistorique.read()
        longeur = len(listHistorique)
        if (longeur>16):
            debut = longeur-16
        else:
            debut = 0
        self.__labelHisto.configure(text="Historique : \n")
        for i in range(debut,longeur):
            contenu = self.__labelHisto.cget("text")
            newText = contenu + " - "+listHistorique[i]+"\n"
            self.__labelHisto.configure(text=newText)
        self.__cadreParametre.place_forget()
        self.__cardeHistorique.place(x=0,y=0)
        self.__labelHisto.place(x=0,y=0)
        self.__cadreSearch.place_forget()
        self.__cadreLeft.place_forget()
        self.__cadreRight.place_forget()
    
    def __validerSetting(self):
        self.__objPara.EcritureJSON("moteur",self.__varMoteur.get())
        self.__objPara.EcritureJSON("theme",self.__varTheme.get())
        self.__guiSearch()
        self.__mainGUI()
    
    def __resetHistorqueSetting(self):
        self.__objHistorique.suppr()
        self.__mainGUI()
        showinfo("Historique effacer","Votre historique a ete efacer")

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
        if (self.__objPara.lectureJSON("theme")==self.__listTheme[0]):
            Label(self.__windows,text="Pas d'acces a internet",font=("arial",30),bg=self.__listColor[0],fg=self.__listTextColor[0]).pack()
            self.__windows.configure(bg=self.__listColor[0])
        else :
            if (self.__objPara.lectureJSON("theme")==self.__listTheme[1]):
                Label(self.__windows,text="Pas d'acces a internet",font=("arial",30),bg=self.__listColor[1],fg=self.__listTextColor[1]).pack()
                self.__windows.configure(bg=self.__listColor[1])
        

    def __valider(self,requette:str):
        #self.__listMoteur = ["Google","Duckduckgo","Ecosia","Qwant","Bing","Brave"]
        parametre = self.__objPara.lectureJSON("moteur")
        if requette :
            if parametre == self.__listMoteur[0]:
                self.__objRecherche.googleSearch(requette)
            else :
                if parametre == self.__listMoteur[1]:
                    self.__objRecherche.duckduckgoSearch(requette)
                else :
                    if parametre == self.__listMoteur[2]:
                        self.__objRecherche.EcosiaSearch(requette)
                    else :
                        if parametre == self.__listMoteur[3]:
                            self.__objRecherche.QwantSearch(requette)
                        else :
                            if parametre == self.__listMoteur[4]:
                                self.__objRecherche.bingSearch(requette)
                            else :
                                if parametre == self.__listMoteur[5]:
                                    self.__objRecherche.braveSearch(requette)
        else :
            showerror("Erreur","Aucune recherche n'a ete taper")
    
    def __getRecherche(self)->str:
        sortie = self.__zoneEntrer.get()
        if sortie :
            self.__objHistorique.write(sortie)
        self.__zoneEntrer.delete(0,END)
        return sortie

    def __getTouches(self,touche1):
        def anychar(event):
            if event.keycode == touche1:
                self.__valider(self.__getRecherche())
        self.__windows.bind("<Key>", anychar)
    
    def Apropop(self):
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Toplevel()
        about.title("A propos : "+self.__nameApp)
        about.iconphoto(False,PhotoImage(file=self.__imagePath))
        about.configure(bg=self.__color)
        about.maxsize(400,300)
        about.minsize(400,300)
        #Traitement Image
        imageOrigine = Image.open(self.__imagePath)    
        imageRedim = imageOrigine.resize(tailleIMG)
        #Label
        labelIcon = Label(about,bg=self.__color)
        icon = ImageTk.PhotoImage(imageRedim,master=labelIcon)
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+self.__nameApp+"\n",font=("arial","12"),bg=self.__color,fg=self.__textColor)
        labelVersion = Label(about,text=self.__versionApp+"\n",font=("arial","11"),bg=self.__color,fg=self.__textColor)
        labelCopyright = Label(about,text=self.__copyrightApp,font=("arial","9"),bg=self.__color,fg=self.__textColor)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()

    def boot(self):
        if (self.__objRecherche.getEtatInternet()==True):
            self.__guiSearch()
        else :
            self.__guiNoInternet()  
        self.__windows.mainloop()

ArreraRecherche().boot()
"""
file = historique("UserFile/historique.txt")
for i in range(0,100):
    file.write(str(i))
"""