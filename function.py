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


def create_habit(name):

    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    return Habits(name,[],[day,month,year])

#Fonction vérifiant si un fichier est vide
def est_fichier_vide(nom_fichier):
    return stat(nom_fichier).st_size == 0





#fonctions liées à l'interface

#création des fonctions de page



def fonction_page2():
    global page1,page2,page3,window,on_off_var,habits_name_entry,habits_name_label,numbers,first_try, x,stock
    
    global blind2_en_cours,blind1_en_cours
    global troll4
    
    #Création du premier ecran


    window = ctk.CTk()
    window.title('Projet_de_groupe_askip')
    window.geometry("800x500")



    #choix du style + scaling
    ctk.set_default_color_theme("themes/NightTrain.json")

    ctk.deactivate_automatic_dpi_awareness()



    #création des pages
    page1 = Page(window)

    page1.configure(border_color = 'white',border_width = 1)
    page1.place(relheight = 1, relwidth = 1)
    
    
    
    page2 = Page(window)
    page2.configure(border_color = 'white',border_width = 1)
    
    
    
    page3 = Page(window)
    page3.configure(border_color = 'white',border_width = 1)
    
    page4 = Page(window)
    page4.configure(border_color = 'white',border_width = 1)
    
    
    #Création des widjets

    button_create_habit = ctk.CTkButton(page1, text = "Create habits", width = 150, height = 75, 
                                        font=("calibri",20),bg_color=window.cget('fg_color'),command=change_window)

    button_create_habit.place(relx=0.5,rely=0.5,anchor = "center")
    
    
    
    
    habits_name_label = ctk.CTkLabel(page2, text = 'Name it', font=('calibri',20,'bold'))
    
    habits_name_entry = ctk.CTkEntry(page2,placeholder_text = "Brush my teeth",justify = "center")
    
    validation_time_label = ctk.CTkLabel(page3, text = 'Validation time', font = ('calibri',20,'bold'))
    
    
    
    
    def fonction_troll():
        troll4.place(relx=0.5 ,rely = 0.2, anchor = 'center')
        troll5.place(relx=0.5 ,rely = 0.94, anchor = 'center')
        
    
    troll1 = ctk.CTkLabel(master = page4,text = 'un avis de cette expérience immersive?', 
                          font=('calibri',20,'bold'))
    troll2 = ctk.CTkTextbox(page4,border_color = 'white',border_width= 1)
    
    troll3 = ctk.CTkButton(page4, text = "Envoyer",command = fonction_troll)
    
    troll4 = ctk.CTkLabel(page4,text="nan jrigole jmen fou et ça envoie rien BEHHH",
                          font=('calibri',20,'bold'))
    troll5 = ctk.CTkLabel(page4,text="t'as test le prototype d'un futur chef-d'oeuvre",
                          font=('calibri',14,'bold'))
    
    troll1.place(relx = 0.5,rely = 0.3, anchor = 'center')
    troll2.place(relx = 0.5,rely = 0.6, anchor = 'center')
    troll3.place(relx = 0.85,rely = 0.3, anchor = 'center')
    
   
    
    def move_widgets2(widget):
            
            global window
            
            h = 0
            
            window.update()

            x_pos = widget.winfo_x()
            y_pos = widget.winfo_y()
            
            initial_placement = widget.place_info()
            
            widget.place_forget()
            window.after(200)
            while h < 1:
                x_bis = random.uniform(-2, 2)
                y_bis = random.uniform(-2, 2)
               
                
                widget.place_configure(x = x_pos + x_bis, y = y_pos + y_bis)
                
                window.after(50)
                window.update()
                widget.place_configure(x = x_pos , y = y_pos )
                
                h += 0.1
            
            
            widget.place_configure(**initial_placement)
            habits_name_entry.bind("<KeyPress-Return>",lambda event: enter_event())
    
    
    
    
    def maj_pressed(event):    ##savoir si la  touche maj est activée
        if event.state == 2  :  
            print('la touche maj est activé')
    
    
    
    #events
    
    habits_name_entry.bind("<KeyPress-Return>" ,lambda event: enter_event())
    
    
    
    
    
    
    
    
    
    
    #placement page 2
    
    habits_name_label.place(relx = 0.5,rely = 0.3, anchor = 'center')
    
    habits_name_entry.place(relx = 0.5,rely = 0.4, anchor = 'center')
    
    
    #placement page 3
    
    validation_time_label.place(relx = 0.5,rely = 0.3, anchor = 'center')
    
    
    
    hours_1 = '0'
    hours_0 = '0'
    minutes_3 = '0'
    minutes_2 = '0'
    
    
    time_disp = ctk.CTkLabel(page3, text = str(hours_1) + str(hours_0) + ' : ' +
                             str(minutes_3) + str(minutes_2),font = ('calibri',36),
                             fg_color = 'transparent')
    time_disp.place(relx = 0.5,rely = 0.4,anchor = "center")
    
    
    
    blink = "  "
    
    numbers = [str(x) for x in range(10)]
    stock=['0','  ','0','0']
    x=0
    
    first_try = True
    
    blind1_en_cours="on"
    blind2_en_cours = "off"
    
    def checker():
        global x, window, stock, first_try
        if on_off_var == "off":
            window.after(100,checker)
        elif on_off_var == 'on':
            
            if stock[0] in ["0","1","2"] and x == 0:
                
                x += 1
            elif not stock[0] in ["0","1","2"] and x == 0 and first_try:
                stock[1]="0"
                x+=2
            elif x == 1 and first_try == True: 
                x += 1
                
                
                blink_function()
                
            elif 1 < x and x < 3 and first_try == True:
                x += 1
                blink_function()
                
                
            elif (x == 3 or x == 2) and first_try == False:
                
                x = 2
                blink_function2()
           
            else:
                blink_function()
            
            
    def checker2():
        global x, window, stock
        if on_off_var == "off":
            window.after(100,checker)
        
            
            
            
    
        
        
        
        
    
    def enter_page2_1(event=None):
        global stock,numbers,x,on_off_var,first_try
        window.bind('<KeyPress>', lambda event: enter_page2_1(event))
        
        if event != None :
                           
            
            if event.keysym in numbers:
                    
                if first_try == True: 
                    
                    if x == 4:
                        return 'salut'
                    
                    if x == 1:
                        swaper = stock[0]  
                        stock[0] = event.keysym
                        stock[1] = swaper
                    
                        
                
                        
                    elif x == 3 and stock[2] in numbers[:6]:
                        swaper = stock[2]  
                        stock[2] = event.keysym
                        stock[3] = swaper
                        first_try = False
                        
                        
                        
    
                        
                      
                    
                    
                    elif x == 3 and stock[2] in numbers[6:]:
                        
                        
                        
                        
                        
                        first_try = False
                        
                  
                    
                    
                    else:
                        
                        stock[x]=event.keysym
                        
                    window.after(100,checker)
                
                elif first_try == False :
                    
                    if event.keysym in numbers[6:] and x == 3:
                        blink_function2()
                    
                    
                    
                    stock[x]=event.keysym
                    blink_function2()
            elif event.keysym == "Left" and not first_try:
                if x != 1:
                    checker2()
                    if x == 0 or x == 2:
                        x += 1
                    elif x == 3 : 
                        x = 0
            elif event.keysym == "Right" and not first_try:
                if x != 2:
                    checker2()
                    if x == 1 or x == 3:
                        x -= 1
                    elif x == 0:
                        x = 3
            elif event.keysym == 'Return' and stock[0] in ["0","1","2"] and stock[1]in ["  ","0"]:
                checker2()
                x = 2
                stock[1]="0"
                time.sleep(0.3)
                
            elif event.keysym == 'Return' and x >= 2:
                enter_page2_2()
        
    
    
    def enter_page2_2():
        global x
        
        if x == 2 or x == 3:
            x=4
            
            window.after(200,troll())
            
            
    
    def troll():
        start_transition(page3, page4)
        
        
        
    def blink_function():
        global x, stock, on_off_var,blind2_en_cours,blind1_en_cours
        
        
        if blind2_en_cours == "on":
            window.after(100,checker)
        
        
        elif blind2_en_cours == 'off':
            
            if on_off_var == "on":
                    
                    time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                             str(stock[3]) + str(stock[2]))
            elif on_off_var == 'off':
                
                
                if x < 2 :
                    time_disp.configure(text=str(blink) + str(blink) + ' : ' +
                                             str(stock[3]) + str(stock[2]))
                
                else :
                    window.bind('<KeyPress-Return>', lambda event: enter_page2_2())
                    time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                             str(blink) + str(blink))
            
            window.after(300,blink_function)
    
    
    def blink_function2():
        global x, stock, on_off_var,blind2_en_cours,blind1_en_cours
        blind2_en_cours = "on"
        
        if on_off_var == "on":
            
                time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                         str(stock[3]) + str(stock[2]))
        elif on_off_var == 'off':
            
            if x == 0 :
                time_disp.configure(text=str(stock[1]) + str(blink) + ' : ' +
                                         str(stock[3]) + str(stock[2]))
            
            elif x == 1 :
                time_disp.configure(text=str(blink) + str(stock[0]) + ' : ' +
                                         str(stock[3]) + str(stock[2]))
            
            elif x == 2 :
                time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                         str(stock[3]) + str(blink))
            elif x == 3 :
                time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                         str(blink) + str(stock[2]))
        
        window.after(300,blink_function2)
        
            
            
            
    
        
        
    def enter_event():
        global habits_name,habits_name_label
        
        habits_name = habits_name_entry.get()
       
        if len(habits_name)!=0:
            habits_name_entry.unbind("<KeyPress-Return>")
            habits_name_entry.configure(state = 'disabled')
            window.after(300,lambda: start_transition(page2, page3))
            blink_function()
            enter_page2_1()
        else:
            habits_name_entry.unbind("<KeyPress-Return>")
            move_widgets2(habits_name_label)
    
    on_off_var="on"
    def on_off():
        global on_off_var, window
        if on_off_var == "on":
            on_off_var="off"
            window.after(630,on_off)
        elif on_off_var == "off" :
            on_off_var='on'
            window.after(1600,on_off)
            
    on_off()
    
    window.mainloop()


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






        
        

def start_transition(page1, page2, direction='o'):
    
    

    # Lancer la transition dans la direction donnée
    transition_progress = 0
    transition_direction = 1
    transition_step(page1, page2, direction, transition_progress, transition_direction)

def transition_step(page1, page2, direction, transition_progress, transition_direction):
    # Calculer les nouvelles positions des pages en fonction de la direction
    if direction == "n":
        page1_y = -transition_progress * 500
        page2_y = 500 - transition_progress * 500
        page1_x = 0
        page2_x = 0
    elif direction == "s":
        page1_y = transition_progress * 500
        page2_y = -500 + transition_progress * 500
        page1_x = 0
        page2_x = 0
    elif direction == "o":
        page1_y = 0
        page2_y = 0
        page1_x = -transition_progress * 800
        page2_x = 800 - transition_progress * 800   
    elif direction == "e":
        page1_y = 0
        page2_y = 0
        page1_x = transition_progress * 800
        page2_x = -800 + transition_progress * 800
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
    
      

    

def change_window(): #fonction activé avec boutton page1
   
    global window
   
    """for widget in page1.winfo_children():
        if widget.winfo_name() != 'Frame':
            widget.place_forget()""" #pour masquer les widgets
            
            
    window.after(100,start_transition(page1, page2))



#fonction pour récupérer des variables se trouvant ici
variable_page_2 = []
def get_variables_page_2():
    return variable_page_2