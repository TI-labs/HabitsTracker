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




##Création des widjets

button_create_habit = ctk.CTkButton(window, text = "create a habit", width = 100, height = 50)
button_create_habit.place(relx=0.5, rely=0.4)



button_create_habit.place()


window.mainloop()
