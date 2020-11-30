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
    
    #print(mot)
    for i,val in enumerate(mot):
        #print(i,val)
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

def jeu():
    tour=0
    score=0
    listeScore=[]
    meilleurScore=0
    [motCaché,lettreDéjàJouées,mot]=affichageMot()
    while "_" in motCaché and tour<8 :
        tour+=1
        lettreJoueur=str(input("Saisissez une lettre : "))
        score+=1
        if lettreJoueur in lettreDéjàJouées :
            print("Cette lettre a déjà été jouée")
        else:
            lettreDéjàJouées+=lettreJoueur
            
            for i,val in enumerate(mot):
                #print(i,val)
                if lettreJoueur==val:
                    motCaché=motCaché[:i]+val+motCaché[i+1:]
                    print(val)
        print(motCaché)
    print("Votre score est de : ",score)
    listeScore.append(score)
    nouveauJeu=str(input("Souhaitez-vous rejouer ? (oui ou non) : "))
    return[nouveauJeu,listeScore]
    
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
    #global nouveauJeu
    nouveauJeu='oui'
    while nouveauJeu=='oui':
        [nouveauJeu,listeScore]=jeu()
        reinitialiser()
        
    meilleurScore=min(listeScore)
    print("Votre meilleur score est : ",meilleurScore)
        
nouvellePartie()
