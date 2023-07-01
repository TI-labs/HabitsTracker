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


window = ctk.CTk()
window.title('first screen')
window.geometry("800x500")


##choix du style + scaling
ctk.set_default_color_theme("themes/NightTrain.json")
ctk.deactivate_automatic_dpi_awareness()


#Création des frames

frame_useless = ctk.CTkFrame(window)
frame_useless.pack(expand = True)





frame_useless.grid_rowconfigure(0, weight = 1)    # Centre le cadre verticalement
frame_useless.grid_columnconfigure(0, weight = 1) # Centre le cadre honrizontalement ta capté



##Création des widjets

button_create_habit = ctk.CTkButton(frame_useless , text = "create a habit", width = 100, height = 50)
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




window.mainloop()
