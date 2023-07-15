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
        blink_function()
        enter_page2_1()
    else:
        habits_name_entry.unbind("<KeyPress-Return>")
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
        habits_name_entry.bind("<KeyPress-Return>",lambda event: enter_event())
        
        
        
#page

page = Page(window)
page.configure(bg_color = window.cget('fg_color'))
page.configure(border_color = 'white',border_width = 1)

    
def fonction_page2():
    
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
    
    
    
    #events
    
    habits_name_entry.bind("<KeyPress-Return>" ,lambda event: enter_event())
    
    
    
    
    
    
    
    
    
    
    #placement page 1
    
    habits_name_label.place(relx = 0.5,rely = 0.3, anchor = 'center')
    
    habits_name_entry.place(relx = 0.5,rely = 0.4, anchor = 'center')
    
    
    #placement page 2
    
    validation_time_label.place(relx = 0.5,rely = 0.3, anchor = 'center')
    
    
    
    hours_1 = '0'
    hours_0 = '0'
    minutes_3 = '0'
    minutes_2 = '0'
    
    
    time_disp = ctk.CTkLabel(page2, text = str(hours_1) + str(hours_0) + ' : ' +
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
        z = "no"
        if event != None :
                           
            
            if event.keysym in numbers:
                    
                if first_try == True: 
                    
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
        
            
            
            
        def enter_page2_2(event):
            window.unbind("<KeyPress>")
            window.unbind('<KeyPress-Return>')
            start_transition(page2, page3)
        
    
    
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
        

fonction_page2()

window.mainloop()