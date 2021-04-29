from tkinter import *
import random

phraseAccueil = 'Bienvenue sur le célèbre jeu du juste prix.\nTu dois deviner le prix auquel je pense.\nIl se situe entre 1 et 100.'
secondes = 0
tempsMax = 60
tentatives = 0
tentativesMax = 5
proposition = None
n = random.randint(1,100)
gagne = False

def temps():
    global secondes
    if not gagne:
        secondes += 1
    if secondes < tempsMax-10:
        affichageTemps['text'] = "Temps restant: {}s".format(tempsMax-secondes)
    elif secondes <= tempsMax:
        if secondes % 2 == 0:
            affichageTemps['bg'] = "red"
        else:
            affichageTemps['bg'] = "#abff91"
        affichageTemps['text'] = "Temps restant: {}s".format(tempsMax-secondes)
    else:
        affichageTemps['text'] = "Temps restant: 0s"
    affichageTemps.after(1000, temps)

def jeu():
    global tentatives
    global proposition
    global gagne
    proposition = entreeTexte.get()
    if proposition.isdigit() and not gagne:
        proposition = int(proposition)
        tentatives +=1
        if tentatives < tentativesMax:
            affichageTentatives['text'] = "Tentatives restantes: {}".format(tentativesMax-tentatives)
        else:
            affichageTentatives['text'] = "Tentatives restantes: 0"
        if secondes < tempsMax and tentatives <= tentativesMax:
            if proposition < n:
                affichageResultat['text'] = "C'est plus."
            elif proposition > n:
                affichageResultat['text'] = "C'est moins."
            else:
                affichageResultat['text'] = "C'est gagné !"
                gagne = True
        else:
            if tentatives <= tentativesMax:
                affichageResultat['text'] = "C'est perdu.\nTemps écoulé."
            else:
                affichageResultat['text'] = "C'est perdu.\nVous avez utilisé toutes vos tentatives."


root = Tk()
root.title('Juste prix')
root.minsize(750, 350)
root.maxsize(750, 350)
root.configure(bg="#abff91")

Label(root,text=phraseAccueil, fg='white', bg="#abff91", font=('Arial', 15)).place(x=190, y=50)
affichageTemps = Label(root,text="Temps restant: {}s".format(tempsMax), fg='white', bg="#abff91", font=('Arial', 12))
affichageTemps.place(x=10, y=10)
affichageTentatives = Label(root,text="Tentatives restantes: {}".format(tentativesMax) ,fg='white', bg="#abff91", font=('Arial', 12))
affichageTentatives.place(x=575, y=10)
entreeTexte = Entry(root, width=30)
entreeTexte.place(x=275, y=150)
Button(root, text='Valider', command=jeu, width=15).place(x=305, y=200)
affichageResultat = Label(root, fg='white', bg="#abff91", font=('Arial', 30), width=30, anchor=CENTER)
affichageResultat.place(x=20, y=250)

temps()
root.mainloop()