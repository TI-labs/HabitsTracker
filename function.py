# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Class import *
import pandas as pd
import numpy as np
from os import stat
import datetime
import customtkinter as ctk

import time
import random
from PIL import Image, ImageTk

def create_habit(name,how_long="limitless",validation_time='00h00'):

    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    return Habits(name,[],[day,month,year],how_long,validation_time)

#Fonction vérifiant si un fichier est vide
def est_fichier_vide(nom_fichier):
    return stat(nom_fichier).st_size == 0





#fonctions liées à l'interface

#création des fonctions de page







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





#fonction clone_widget
#permet de cloner un widget sur le master = fenetre_cible

def clone_widget(widget,fenetre_cible):
    # Obtenir le type de widget
    widget_type = type(widget)
    
    
    options = widget.config()
    
    options = {key: widget.cget(key) for key in options.keys() if widget.cget(key)}
    
    clone_widget = widget_type(fenetre_cible.master, **options)
    
    return clone_widget




def start_transition(master,page1, page2, direction='o'):
    
    global master_bis
    master_bis=master
    
    # Lancer la transition dans la direction donnée
    transition_progress = 0
    transition_direction = 1
    transition_step(page1, page2, direction, transition_progress, transition_direction)


def transition_step(page1, page2, direction, transition_progress, transition_direction):
    global master_bis
    # Calculer les nouvelles positions des pages en fonction de la direction
    w,h = master_bis.winfo_width(),master_bis.winfo_height()
    
    if direction == "n":
        page1_y = -transition_progress * h
        page2_y = h - transition_progress * h
        page1_x = 0
        page2_x = 0
    elif direction == "s":
        page1_y = transition_progress * h
        page2_y = -h + transition_progress * h
        page1_x = 0
        page2_x = 0
    elif direction == "o":
        page1_y = 0
        page2_y = 0
        page1_x = -transition_progress * w
        page2_x = w - transition_progress * w  
    elif direction == "e":
        page1_y = 0
        page2_y = 0
        page1_x = transition_progress * w
        page2_x = -w + transition_progress * w
    else:
        return

    # Déplacer les pages
    page1.place(x=page1_x, y=page1_y)
    page2.place(x=page2_x, y=page2_y)

    # Mettre à jour la transition
    transition_progress += 0.04

    # Vérifier si la transition est terminée
    if transition_progress <= 1:
        # La transition n'est pas terminée
        page1.after(20, lambda: transition_step(page1, page2, direction, transition_progress, transition_direction))
    else:
        # La transition est terminée, afficher page 2 et réinitialiser les paramètres
        page1.place_forget()
        page2.place(x=0, y=0)
        page2.label.place(relx=0.5, rely=0.5, anchor='center')
        page2.place_configure(relwidth=1,relheight=1)
        transition_progress = 0
        transition_direction = -1   
    
      

    





