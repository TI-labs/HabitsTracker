# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import customtkinter as ctk
from Class import *
import pandas as pd
import datetime
from function import *
import customtkinter as ctk
import tkinter as tk

#Ouverture du fichier

if est_fichier_vide('data.csv'):
    working_df = pd.DataFrame()
else :
    working_df = pd.read_csv('data.csv')
    


#fonction de sauvegarde du df dans le fichier data
def save_habits():
    working_df.to_csv('data.csv')









        


fonction_page2()
    
 
    





