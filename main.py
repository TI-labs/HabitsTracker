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


#Création des frames premier ecran

frame_main = ctk.CTkFrame(window,width = 800,height = 500)
frame_main.pack(expand = True)





#la fonction liée au boutton doit forcément être dans ce fichier

def change_window(): #fonction qui efface le contenu de la fenetre et affiche la page 2
   
    global window
    
    for widget in frame_main.winfo_children(): #on efface la premiere fenetre
        widget.pack_forget()
        
        #pour que le frame prenne la couleur de la fenetre lorsque le boutton disparait
        frame_main.configure(fg_color = window.cget('fg_color') )
        window.title('2nd screen')
        
    #on utilise la fonction new_screen_disp(premiere_page,page_cible) pour afficher la page cible
    new_screen_disp(window,screen2)
        
    
    
    

    
#Création des screens

#attention, on utilise des toplevels et non des windows, les toplevels se comportent pareil

screen2=ctk.CTkToplevel(window)
screen2.withdraw()
screen2.geometry("800x500")
screen2.title('2nd screen')


frame_bis = ctk.CTkFrame(screen2,width = 800, height = 500)
frame_bis.pack()
button_bis = ctk.CTkButton(frame_bis)
button_bis.pack()





#Création des widjets

button_create_habit = ctk.CTkButton(frame_main , text = "create a habit", width = 100, height = 50, 
                                    command = change_window)

button_create_habit.pack()





window.mainloop()
