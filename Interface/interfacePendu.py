#Importation des bibliothèques
import tkinter as tk
from tkinter import *
from tkinter import Tk, Label, StringVar, Entry, Button
import random
from random import randint



def getMot():
    with open("pendu.txt") as f:
        listeMot = f.read().splitlines()
        f.close()
    indice=randint(0,len(listeMot)-1)
    mot=listeMot[indice]
    return[listeMot,indice,mot]

def affichageMot():
    
    memeLettre=""
    [listeMot,indice,mot]=getMot()
    motCaché=""
    lettreDéjàJouées=[]
    
    global nouveauJeu
    
    for i,val in enumerate(mot):
        while i==0:
            i+=1
            memeLettre+=val
            lettreDéjàJouées+=val
        if memeLettre==val:
            motCaché+=val
        else:
            motCaché+=str("_")
    print(motCaché)
    
    return[motCaché,lettreDéjàJouées,mot]

def intoTheWhile():
    global motCaché, tour, score, lettreDéjàJouées
    global listePhoto
    global compteurPhoto
    global nbrCoups
    #compteurPhoto=0
    if "_" in motCaché and nbrCoups>0 :
        test=0
        tour+=1
        homme=0
        
        lettreJoueur=lettreSaisie.get()
        lettreSaisie.set("")
        print("lettreJoueur", lettreJoueur)
        score+=1
        if lettreJoueur in lettreDéjàJouées :
            print("Cette lettre a déjà été jouée")
        else:
            lettreDéjàJouées+=lettreJoueur
            print("lettreDéjàJouées : ",lettreDéjàJouées)
            
            for i,val in enumerate(mot):
                if lettreJoueur==val:
                    test=1
                    motCachéTk = zonegraphique.create_text(115, 40, anchor="nw", font=("Arial", -22 ,"bold"), text = motCaché, fill="#808080")
                    motCaché=motCaché[:i]+val+motCaché[i+1:]
                    print(val)
            if test==0:
                compteurPhoto+=1
                bonhomme=listePhoto[compteurPhoto]
                affichagePendu=zonegraphique.create_image(900, 10, anchor="nw", image = bonhomme)
                print("compteurPhoto",compteurPhoto)
                print("nbrCoups :",nbrCoups)
                CoupsAffichage = zonegraphique.create_text(400, 100, anchor="nw", font=("Arial", -22 ,"bold"), text = nbrCoups, fill="#808080")
                nbrCoups-=1

                if nbrCoups==0:
                    defaite = zonegraphique.create_text(200, 200, anchor="nw", font=("Arial", -22 ,"bold"), text = "Vous avez perdu !!!")
                    


        CoupsAffichage = zonegraphique.create_text(400, 100, anchor="nw", font=("Arial", -22 ,"bold"), text = nbrCoups)            
        print(motCaché)
        
        motCachéTk = zonegraphique.create_text(115, 40, anchor="nw", font=("Arial", -22 ,"bold"), text = motCaché)

    else :
        print("Votre score est de : ",score)
        affichageScorePhrase = zonegraphique.create_text(215, 200, anchor="nw", font=("Arial", -22 ,"bold"), text = "Score : ")
        affichageScore = zonegraphique.create_text(295, 200, anchor="nw", font=("Arial", -22 ,"bold"), text = score)
        listeScore.append(score)
        return listeScore

def nvJeu():
    nouveauJeu='oui'
    return nouveauJeu
        
    
    
def reinitialiser():
    [listeMot,indice,mot]=getMot()
    indice=randint(0,len(listeMot)-1)
    mot=listeMot[indice]
    motCaché=""
    memeLettre=""
    lettreDéjàJouées=[]
    tour=0
    score=0

def nouvellePartie():
    nouveauJeu='oui'
    while nouveauJeu=='oui':
        listeScore=intoTheWhile()
        nouveauJeu=nvJeu()
        
        reinitialiser()
        
    meilleurScore=min(listeScore)
    print(listeScore,"liste score")
    print("Votre meilleur score est : ",meilleurScore)
    

def start():
    global motCaché, nbrCoups, tour, lettreSaisie, score, lettreDéjàJouées, mot, compteurPhoto, listePhoto, zonegraphique

    tour=0
    score=0
    meilleurScore=0
    [motCaché,lettreDéjàJouées,mot]=affichageMot()
    listeScore=[]
        
    pnd = tk.Tk()
    imageFond = tk.PhotoImage(file = "fondGris.gif")
    imageHomme7 = tk.PhotoImage(file = "bonhomme1.gif")
    imageHomme6 = tk.PhotoImage(file = "bonhomme2.gif")
    imageHomme5 = tk.PhotoImage(file = "bonhomme3.gif")
    imageHomme4 = tk.PhotoImage(file = "bonhomme4.gif")
    imageHomme3 = tk.PhotoImage(file = "bonhomme5.gif")
    imageHomme2 = tk.PhotoImage(file = "bonhomme6.gif")
    imageHomme1 = tk.PhotoImage(file = "bonhomme7.gif")
    

    listePhoto=["0", imageHomme1,imageHomme2,imageHomme3,imageHomme4,imageHomme5,imageHomme6,imageHomme7]

    compteurPhoto=0
    nbrCoups=7


    pnd.title("Jeu de Pendu")           
    pnd.geometry("1500x1300")

    # Création d'une zone graphique canvas
    zonegraphique = tk.Canvas(pnd, height = 700, width = 1500)

    zonegraphique.grid(row=0, column=0, rowspan=100, columnspan=100)

    Fond = zonegraphique.create_image(0, 0, anchor="nw", image = imageFond)


    Label1= Label(pnd, text='Saisissez votre lettre')
    Label1.grid(row=50, column=25, padx=5, pady=5)

    lettreSaisie=StringVar()
    Champ=Entry(pnd, textvariable=lettreSaisie, show="", bg='bisque', fg='maroon')
    Champ.focus_set()
    Champ.grid(row=50, column=26, padx=5, pady=5)

    #Affichage texte
    motCachéTk = zonegraphique.create_text(115, 40, anchor="nw", font=("Arial", -22 ,"bold"), text = motCaché)
    nbrCoupsAffichage = zonegraphique.create_text(115, 100, anchor="nw", font=("Arial", -22 ,"bold"), text = "Nombre de coups restant :")
    CoupsAffichage = zonegraphique.create_text(400, 100, anchor="nw", font=("Arial", -22 ,"bold"), text = nbrCoups)

    Bouton=Button(pnd, text='Proposer', command=intoTheWhile)
    Bouton.grid(row=50, column=27, padx=5, pady=5)

    boutonRejouer=tk.Button(pnd,text="REJOUER", command=start)
    boutonRejouer.grid(row=80, column=45)

    boutonQuitter=tk.Button(pnd,text="QUITTER", command=pnd.destroy)
    boutonQuitter.grid(row=100, column=45)


    pnd.mainloop()




start()





















