# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import customtkinter as ctk
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


