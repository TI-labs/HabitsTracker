# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Class import *
import pandas as pd
import numpy as np
from os import stat
import datetime
import customtkinter as ctk




def create_habit(name):

    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    return Habits(name,[],[day,month,year])

#Fonction vérifiant si un fichier est vide
def est_fichier_vide(nom_fichier):
    return stat(nom_fichier).st_size == 0





#fonctions liées à l'interface



#fonction get_widgets_and_frames
#pour recuperer sous forme de liste les frames d'un top level et les widget inclu
#dans chacun des frame     frames = [frame1,frame2]  Widgets = [[widget1_frame1 , widget2_frame1],
                                                             #  [wiget1_frame2,  widget2_frame2]]  
def get_widgets_and_frames(top_level):
    widgets = []
    frames = []

    for x in top_level.winfo_children():
        if isinstance(x, ctk.CTkFrame):
            frames.append(x)
            for widget in x.winfo_children():
                widgets.append(widget)
    
        

    return widgets, frames








#fonction new_screen_disp
#qui permet d'afficher un target_screen (préfait) sur une fenetre vide
#target_screen est un ctk.CTkToplevel object

           
def new_screen_disp(window,target_screen):
    widgets_target, frames_target = get_widgets_and_frames(target_screen)
    print(widgets_target, frames_target)
      
            
