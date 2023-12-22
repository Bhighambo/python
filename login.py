#Les bibliotheques a imprter
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox



#Fonction se connecter

def seconnecter():
    surnom = textnomUtilisateur.get()
    mdp = textMotdepasse.get()

    if surnom == "" and mdp == "":
        messagebox.showinfo("","Tous les champs sont obligatoires")
        textMotdepasse.delete("0", "end")
        textnomUtilisateur.delete("0", "end")
    elif surnom == "admin" and mdp == "admin":
        messagebox.showinfo("", "Connexion réussit")
        textMotdepasse.delete("0", "end")
        textnomUtilisateur.delete("0", "end")
        root.destroy()
        call(["python", "enregistrement.py"])
    else:
        messagebox.showwarning("", "Echec de la connexion")
        textMotdepasse.delete("0", "end")
        textnomUtilisateur.delete("0", "end")


#La fenetre de connexion
root = Tk()

root.title("Fenetre de connexion")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter les titres

lbltitre = Label(root, borderwidth=3, relief= SUNKEN, text="Formulaire de connexion ", font=("sans serif", 25), background="#091821", fg="white")
lbltitre.place(x=0, y=0, width=400)

lblnomutilisateur = Label(root, text="Nom Utilisateur", font=("Arial", 14), bg="#091021", fg="white")
lblnomutilisateur.place(x = 5, y = 100, width=150)
textnomUtilisateur = Entry(root, bd=2, font=("Arial", 13))
textnomUtilisateur.place(x=150, y=100, width=200, height=30)

lblmotdepasse = Label(root, text="Mot de passe", font=("Arial", 13), bg="#091821", fg="white")
lblmotdepasse.place(x= 15, y=150, width=100)
textMotdepasse = Entry(root, show="*", bd=2, font=("Arial", 10))
textMotdepasse.place(x=150, y=150, width=200, height=30)

#Traitement du bouton
btnEnregistrement = Button(root, text="Se connecter", font=("Arial", 16), bg="#FF4500", fg="white", command=seconnecter)
btnEnregistrement.place(x = 150, y = 200, width=200)




#Executer
root.mainloop()