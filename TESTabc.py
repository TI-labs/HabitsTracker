import customtkinter as ctk
import random
import time
from Class import *
from function import *


window = ctk.CTk()
window.title('create a habit')
window.geometry('800x500')


ctk.deactivate_automatic_dpi_awareness()



#fontions

def enter_event():
    global habits_name
    
    habits_name = create_habit_entry.get()
    if len(habits_name)!=0:
        create_habit_entry.configure(state = 'disabled')
        window.after(300,lambda: start_transition(page, page2))


def move_widgets():
    # Fonction pour déplacer le label de manière animée
    window.after(250)
    button_test = ctk.CTkButton()
    def animate():
        nonlocal y, direction, animation_step
        
        
        # Calculer la nouvelle position verticale
        y += direction * animation_step
        
        # Mettre à jour la position du label
        create_habit_label.place(x=364, y=30 + y)
        
        # Inverser la direction si on atteint les limites
        if y <= -20 or y >= 0:
            direction *= -1
            if y >= 0:
                # Arreter l'animation et reactiver le bouton
                button_test.configure(state=ctk.NORMAL)
                return
        
        # Répéter l'animation apres un certain delai (en millisecondes)
        window.after(50, animate)
    
    # Variables pour l'animation
    y = 0
    direction = -1  # -1 pour monter, 1 pour descendre
    animation_step = 3 # Déplacement vertical par increments
    
    # Desactiver le bouton pendant l'animation
    button_test.configure(state=ctk.DISABLED)
    
   
    animate()


    


#page

page= Page(window,text_label='')
page.configure(bg_color=window.cget('fg_color'))

page2= Page(window,text_label='page 2')
page2.configure(bg_color='red')
page2.configure(fg_color='red')

page.grid(row=1,column=1,sticky="nswe")
#widgets


create_habit_label = ctk.CTkLabel(page, text = 'Name it', font=('calibri',20,'bold'))


create_habit_entry = ctk.CTkEntry(page,placeholder_text = "Brush my teeth",justify = "center")



 
#entry event
create_habit_entry.bind("<KeyPress-Return>" ,lambda event: enter_event())


#creating grid

for i in range (3):
    window.grid_rowconfigure(i,weight = 1)
    window.grid_columnconfigure(i,weight = 1)



for i in range (499):
    page.grid_rowconfigure(i,weight = 1)


page.grid_columnconfigure(0, weight = 1)
page.grid_columnconfigure(1, weight = 1)
page.grid_columnconfigure(2, weight = 1)


#placement

create_habit_label.grid(row =1 ,column = 1, )

create_habit_entry.grid(row =200 ,column = 1, sticky = "ns")



window.mainloop()