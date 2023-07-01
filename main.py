# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Class import *
import pandas as pd
import numpy as np
import datetime
import tkinter as tk
from function import *


#Ouverture du fichier

if est_fichier_vide('data.csv'):
    working_df = pd.DataFrame()
else:
    working_df = pd.read_csv('data.csv')



#fonction de sauvegarde du df dans le fichier data
def save_habits():
    working_df.to_csv('data.csv')



#Création de la fenetre

fenetre = tk.Tk()
fenetre.config(background='#403F3F')
fenetre.title('HabitTracker')
fenetre.geometry("800x500")

btn_creation1 = tk.Button(fenetre, text= "Create habits" )

btn_creation1.pack(anchor='center' )




fenetre.mainloop()

