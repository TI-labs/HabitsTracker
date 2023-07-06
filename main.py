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





#Création du premier ecran


window = ctk.CTk()
window.title('first screen')
window.geometry("800x500")



#choix du style + scaling
ctk.set_default_color_theme("themes/NightTrain.json")

ctk.deactivate_automatic_dpi_awareness()





#creation des frames
frame_main = ctk.CTkFrame(screen2_0)
frame_main.pack(expand = True)


#création des pages







#la fonction liée au boutton doit forcément être dans ce fichier

def change_window(): #fonction qui efface le contenu de la fenetre et affiche la page 2
   
    global window
    
    for widget in frame_main.winfo_children(): #on efface la premiere fenetre
        widget.pack_forget()
        
    #pour que le frame prenne la couleur de la fenetre lorsque le boutton disparait
    frame_main.configure(fg_color = window.cget('fg_color') )
        
    
        
    #on affiche la page 2
    
    

    
#Création des screens

screen2_0 = Page(window,text_label='')
screen2_1 = Page(window,text_label='')




#screen2_0.place(x=0, y=0)





#Création des widjets

button_create_habit = ctk.CTkButton(frame_main, text = "Create habits", width = 150, height = 75, 
                                    font=("calibri",20),bg_color=window.cget('fg_color'),command=change_window)

button_create_habit.pack()





window.mainloop()
