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
    global habits_name,habits_name_label
    
    habits_name = habits_name_entry.get()
   
    if len(habits_name)!=0:
        habits_name_entry.unbind("<KeyPress-Return>")
        habits_name_entry.configure(state = 'disabled')
        window.after(300,lambda: start_transition(page, page2))
        enter_page2_1()
    else:
        
        move_widgets2(habits_name_label)
        

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
        
        
        
        
#page

page = Page(window)
page.configure(bg_color = window.cget('fg_color'))
page.configure(border_color = 'white',border_width = 1)


page2 = Page(window)
page2.configure(border_color = 'white',border_width = 1)



page3 = Page(window)
page3.configure(border_color = 'white',border_width = 1)




page.place(relheight = 1, relwidth = 1)






#widgets


habits_name_label = ctk.CTkLabel(page, text = 'Name it', font=('calibri',20,'bold'))

habits_name_entry = ctk.CTkEntry(page,placeholder_text = "Brush my teeth",justify = "center")



validation_time_label = ctk.CTkLabel(page2, text = 'Validation time', font = ('calibri',20,'bold'))






def maj_pressed(event):    ##savoir si la  touche maj est activée
    if event.state == 2  :  
        print('la touche maj est activé')

#entry event
habits_name_entry.bind("<KeyPress-Return>" ,lambda event: enter_event())










#placement page 1

habits_name_label.place(relx = 0.5,rely = 0.3, anchor = 'center')

habits_name_entry.place(relx = 0.5,rely = 0.4, anchor = 'center')


#placement page 2

validation_time_label.place(relx = 0.5,rely = 0.3, anchor = 'center')



hours_1 = '0'
hours_2 = '0'
minutes_1 = '0'
minutes_2 = '0'


time_disp = ctk.CTkLabel(page2, text = str(hours_1) + str(hours_2) + ' : ' +
                         str(minutes_1) + str(minutes_2),font = ('calibri',36))
time_disp.place(relx = 0.5,rely = 0.4,anchor = "center")


x_hours = 0 #cette variable pour savoir quel nombbre on modifie

def check_entry(event): #event assoc à la modif de l heure 
    global hours_1 , hours_2 , minutes_1 , minutes_2,x_hours
    
    
    numbers = [str(x) for x in range(10)]
    
    if event.keysym in numbers :
        
        if x_hours == 0:
            
                
            hours_2 = event.keysym
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            x_hours += 1 
            window.unbind("<Keypress>")
            enter_page2_1()
            
        elif x_hours == 1:
            
            hours_1 = event.keysym
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            x_hours += 1 
            enter_page2_1()
            
        elif x_hours == 2:
            
            minutes_2 = event.keysym
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            x_hours += 1 
            enter_page2_1() 
            
        elif x_hours == 3:
            
            minutes_1 = event.keysym
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                     str(minutes_1) + str(minutes_2))
            
            enter_page2_1() 
        window.unbind("<Keypress>")
            
    elif event.keysym == "BackSpace":
        
        
        if x_hours == 0:
            
            hours_2='0'
            
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            window.unbind("<Keypress>")
            enter_page2_1()
            
        elif x_hours == 1:
            
            hours_1 = "0"
            x_hours -= 1
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            window.unbind("<Keypress>")
            enter_page2_1()
            
        elif x_hours == 2:
            
            minutes_2 = '0'
            x_hours -= 1
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            window.unbind("<Keypress>")
            enter_page2_1()
            
        elif x_hours == 3:
            
            minutes_1 = '0'
            x_hours -= 1
            time_disp.configure(text = str(hours_1) + str(hours_2) + ' : ' + 
                                    str(minutes_1) + str(minutes_2))
            window.unbind("<Keypress>")
            enter_page2_1()    
    elif event.keysym == 'Return':
       
        if x_hours == 0 or x_hours == 1:
            x_hours = 2
            window.unbind("<Keypress>")
            enter_page2_1()
        
        
        
        
def enter_page2_1(): #quand on est dans la page 2 (fonction inutile mais on la garde)
    if x_hours == 2 or x_hours == 3:
        
        window.bind('<KeyPress-Return>',enter_page2_2)



    else:
        window.bind("<KeyPress>", check_entry)

def enter_page2_2(event):
    window.unbind("<KeyPress>")
    window.unbind('<KeyPress-Return>')
    start_transition(page2, page3)
    
window.mainloop()