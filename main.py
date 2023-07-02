# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import customtkinter as ctk
from Class import *
import pandas as pd
import datetime
from function import *
import customtkinter as ctk


#Ouverture du fichier

if est_fichier_vide('data.csv'):
    working_df = pd.DataFrame()
else :
    working_df = pd.read_csv('data.csv')
    


#fonction de sauvegarde du df dans le fichier data
def save_habits():
    working_df.to_csv('data.csv')



#Création du premier ecran


window1 = ctk.CTk()
window1.title('first screen')
window1.geometry("800x500")


#choix du style + scaling
ctk.set_default_color_theme("themes/NightTrain.json")
ctk.deactivate_automatic_dpi_awareness()


#Création des frames

frame_main = ctk.CTkFrame(window1)
frame_main.pack(expand = True)


frame_child = ctk.CTkFrame(frame_main)
frame_child.pack(expand=True)


frame_main.grid_rowconfigure(0, weight = 1)    # Centre le cadre verticalement
frame_main.grid_columnconfigure(0, weight = 1) # Centre le cadre honrizontalement ta capté




#la fonction liée au boutton doit forcément être dans ce fichier

def change_window(): #fonction permettant d'update une fenetre pour arriver sur une nouvelle fenetre
    global window1
    window1.after(ms=100)
    window1.destroy()
    window2.after(ms=300)
    window2.mainloop()
    ctk.deactivate_automatic_dpi_awareness()
    
##je vais modifier cette fonction en faisant disparaitre les items du frame plutot que de créer une nouvelle fenetre,
#ca sera plus fluide et il y aura moin de soucis je l'espère    
    

    
#je n'ai pas reussi à faire une fonction générale fonctionnant pour n'importe qu'elle fenetre a cause du comportement du boutton


#si tu veux pour demain avant que j'arrive tu peux commencer à faire la fenetre 2 et j'améliorerais mon code si possible ou bien on peut faire l'inverse


#Création fenetre 2

window2=ctk.CTk()
window2.title('2nd screen')
window2.geometry("800x500")




#Création des widjets

button_create_habit = ctk.CTkButton(frame_child , text = "create a habit", width = 100, height = 50, 
                                    command = change_window)
button_create_habit.pack()

'''
button_create_habit.place(relx=0.5, rely=0.4)


Cela ne fonctionne pas chez moi, ce n'est pas centré, en gros c'est pas ouf mais ne t'inquiète pas, 
j'ai la solution. Ah et dailleur je n ai eu aucun soucis pour pull, pense à utiliser stash au cas ou
et stash pop pour retirer completement de la liste en gros stash joue le role d une corbeille mais 
j'imagine que tu connais déjà. 

Cordialement

Un débutant de git
'''




window1.mainloop()
