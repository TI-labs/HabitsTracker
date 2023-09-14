# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from Class import *
import customtkinter as ctk
import pandas as pd
import datetime
from function import *




#Ouverture du fichier

if est_fichier_vide('data.csv'):
    working_df = pd.DataFrame()
else :
    working_df = pd.read_csv('data.csv')
    


#fonction de sauvegarde du df dans le fichier data
def save_habits():
    working_df.to_csv('data.csv')









# Création du premier ecran
window = ctk.CTk()
window.resizable(False,False)



create_tool = ctk.CTkToplevel(window)

create_tool.geometry('800x500')
create_tool.title('Create tool')

create_tool.resizable(False,False)

window.title('Habits Tracker')
window.geometry("800x500")

themes = ["themes/Anthracite.json", "themes/DaynNight.json", "themes/GhostTrain.json",
          "themes/Greengage.json", "themes/GreyGhost.json", "Hades.json",
          "themes/Harleyquin.json", "themes/MoonlitSky.json", "themes/NightTrain.json",
          "themes/Oceanix.json", "themes/TestCard.json", "themes/TrojanBlue.json"]
 
# Choix du style + scaling
#ctk.set_default_color_theme(themes[9])
ctk.set_appearance_mode('dark')

ctk.deactivate_automatic_dpi_awareness()




# Création des pages
page1 = Page(create_tool)

page1.configure(border_color='white', border_width=1)
page1.place(relheight=1, relwidth=1)

page2 = Page(create_tool)
page2.configure(border_color='white', border_width=1)

page3 = Page(create_tool)
page3.configure(border_color='white', border_width=1)

page4 = Page(create_tool)
page4.configure(border_color='white', border_width=1)

page5 = Page(create_tool)
page5.configure(border_color='white', border_width=1)

pages = [page1, page2, page3, page4, page5]



def change_window(): #fonction activé avec boutton page1
   
    global window
   
    """for widget in page1.winfo_children():
        if widget.winfo_name() != 'Frame':
            widget.place_forget()""" #pour masquer les widgets
            
            
    create_tool.after(100,start_transition(create_tool,page1, page2,"o"))

w = True

def resizer():
    global pages, w
    largeur_init = 800

    if w == True:
        if window.winfo_width() != largeur_init:

            for page in pages:
                page.configure(width=window.winfo_width(), height=window.winfo_height())

            largeur_init = window.winfo_width()
            w = False

        window.after(2000, resizer)
    elif w == False:
        for page in pages:
            page.configure(width=window.winfo_width(), height=window.winfo_height())



color1 = "gray17"
color2 = "#212121"
# page principale


def enter_main():
    global sub_frame1,sub_frame2,sub_frame3,frame_main
    global sub2_statue,sub3_statue,habit_number
    window.state('zoomed')
    window.resizable(False, False)
    
    habit1 = create_habit(habits_name_entry.get(),tmp,stock[1] + stock[0] + 'h' + stock[3] + stock[2])
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_height()
    
    
    
    margin_x = 20
    margin_y = 20
    
    frame_width = screen_width //4 - 2 * margin_x
    frame_height = screen_height - 2 * margin_y
    
    
    frame_main = Page(window)
    
    
    frame = Page(frame_main)
    frame.configure(width=frame_width, height=frame_height,
                   border_width = 1 , fg_color = 'gray14')
    frame.pack_propagate(False)
    
    frame.place(x=margin_x, y=margin_y)
    
    
    
    frame2 = Page(frame_main)
    frame2.configure(width=screen_width - frame_width - 3 * margin_x
                     , height=frame_height//1.4 - margin_y,
                   border_width = 1)
    frame2.pack_propagate(False)
    
    frame2.place(x=2*margin_x + frame_width, y=margin_y)
    
    
    frame2_1 = Page(frame_main)
    frame2_1.configure(width = screen_width - frame_width - 3 * margin_x,
                       height = frame_height-frame_height//1.4,
                     border_width = 1
                       )
    frame2_1.place(x=2*margin_x + frame_width,y=2*margin_y + frame2.cget('height') -4.5
                   )
    
    
    
    
    
    
    sub_frame1= ctk.CTkFrame(frame_main,height = frame_height//3 - 20,width = frame_width-20,
                            border_width=1, corner_radius = 200 ,
                            background_corner_colors=("gray14",'gray14',"gray14",'gray14')
                            ,bg_color = 'gray14'
                            )
       
    
    sub_frame1.place(x = margin_x + 10, y = 1.65*margin_y + 10)
    
    
    
    
    sub_frame2= ctk.CTkFrame(frame_main,height = frame_height//3 - 20,width = frame_width-20,
                            border_width=1, corner_radius = 200,
                            background_corner_colors=("gray14",'gray14',"gray14",'gray14'))
    
    sub_frame2.place(x = margin_x + 10, y = 1.65*margin_y + 221 + 10)
    
    
    
    
    sub2_statue = "unlocked"
    
    
    sub_frame3= ctk.CTkFrame(frame_main,height = frame_height//3 - 20,width = frame_width-20,
                            border_width=1, corner_radius = 200,
                            background_corner_colors=("gray14",'gray14',"gray14",'gray14'))
    
    sub_frame3.place(x = margin_x + 10, y = 1.65*margin_y + 442 + 10)
    
    
    sub3_statue = "unlocked"
    
    
    

    
    
    label_frame1 = ctk.CTkLabel(sub_frame1,text = habit1.name,font = ('calibri',20))
    label_frame1.place(relx = 0.5, rely = 0.5,anchor = "center")
    
    
    
    
    
    
    
    
    progressbar1 = ctk.CTkProgressBar(sub_frame1, orientation="horizontal",height = 6,
                                      progress_color="green",width = 100)
    progressbar1.place(relx = 0.5, rely = 0.68,anchor = "center")
    progressbar1.set(0)
    
    
    
    
    label_frame2 = ctk.CTkLabel(sub_frame2,text = "",font = ('calibri',20))
    label_frame2.place(relx = 0.5, rely = 0.5,anchor = "center")
    
    
    
    progressbar2 = ctk.CTkProgressBar(sub_frame2, orientation="horizontal",height = 6,
                                      progress_color="green",width = 100)
    
    
    add_icon_pil_image = Image.open('img/plus_icon.png')
    add_icon_pil_image = add_icon_pil_image.convert("RGBA")
    add_icon_label_image = ctk.CTkImage(add_icon_pil_image, size=(50,50))
    
 
    
    
    add_label2 = ctk.CTkLabel(sub_frame2,image = add_icon_label_image, text = "")
    add_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    
    
    
    
    
      
    label_frame3 = ctk.CTkLabel(sub_frame3,text = "",font = ('calibri',20))
    label_frame3.place(relx = 0.5, rely = 0.5,anchor = "center")
    
    add_label3 = ctk.CTkLabel(sub_frame3,image = add_icon_label_image, text = "")
    add_label3.place(relx = 0.5, rely = 0.5, anchor = "center")
    
    progressbar3 = ctk.CTkProgressBar(sub_frame3, orientation="horizontal",height = 6,
                                      progress_color="green",width = 100)
    
    
    
    
    
    

    window.after(1000,start_transition(window, page5, frame_main))
    
    
    
    
    
    #events
    
    sub_frame1.bind("<Enter>",lambda event : change_color(event,"frame_1","on"))

    sub_frame1.bind("<Leave>",lambda event : change_color(event,"frame_1","out"))
    
    progressbar1.bind("<Enter>",lambda event : change_color(event,"frame_1","on"))
    label_frame1.bind("<Enter>",lambda event : change_color(event,"frame_1","on"))



    sub_frame2.bind("<Enter>",lambda event : change_color(event,"frame_2","on"))

    sub_frame2.bind("<Leave>",lambda event : change_color(event,"frame_2","out"))
    
    progressbar2.bind("<Enter>",lambda event : change_color(event,"frame_2","on"))
    label_frame2.bind("<Enter>",lambda event : change_color(event,"frame_2","on"))

    
    add_label2.bind("<Enter>",lambda event : change_color(event,"frame_2","on"))




    sub_frame3.bind("<Enter>",lambda event : change_color(event,"frame_3","on"))

    sub_frame3.bind("<Leave>",lambda event : change_color(event,"frame_3","out"))
    
    progressbar3.bind("<Enter>",lambda event : change_color(event,"frame_3","on"))
    label_frame3.bind("<Enter>",lambda event : change_color(event,"frame_3","on"))
    
    add_label3.bind("<Enter>",lambda event : change_color(event,"frame_3","on"))
    

    #cadre du haut 
    
    up_left_skip_frame = Page(frame2)
    up_left_skip_frame.configure(width = 65,
                       height=frame_height//1.4 - margin_y,
                     border_width = 1, fg_color = '#1e1e1e' )
    up_left_skip_frame.place(x = 0,y = 0)
    
    
    up_right_skip_frame = Page(frame2)
    up_right_skip_frame.configure(width = 65,
                       height=frame_height//1.4 - margin_y,
                     border_width = 1, fg_color = '#1e1e1e'  )
    up_right_skip_frame.place(relx = 1,y = 0, anchor = "ne")
    
    
    


    # cadre du bas 
    
    ''' On peut glisser en placant sur le frame2_1_bis qui lui est sur le frame2_1'''
    

    left_skip_frame = Page(frame2_1)
    left_skip_frame.configure(width = 65,
                       height = frame_height-frame_height//1.4,
                     border_width = 1, fg_color = '#1e1e1e' )
    left_skip_frame.place(x = 0,y = 0)
    left_skip_frame.pack_propagate(False)
    
    
    arrow_icon_pil_image = Image.open('img/arrow.png')
    
    arrow_icon_label_image = ctk.CTkImage(arrow_icon_pil_image, size=(40,200))
    
    
   
    arrow_icon_pil_image2 = arrow_icon_pil_image.transpose(Image.FLIP_LEFT_RIGHT)
    arrow_icon_label_image2 = ctk.CTkImage(arrow_icon_pil_image2, size=(40,200))
    
    del arrow_icon_pil_image2
    
    
    left_skip_label = ctk.CTkLabel(left_skip_frame,image = arrow_icon_label_image2 , text ='' )
    
    left_skip_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
    
    
    
    
    
    right_skip_frame = Page(frame2_1)
    right_skip_frame.configure(width = 65,
                       height = frame_height-frame_height//1.4,
                     border_width = 1, fg_color = '#1e1e1e' )
    right_skip_frame.place(relx = 1,y = 0, anchor = "ne")
    right_skip_frame.pack_propagate(False)
    
    
    
    right_skip_label = ctk.CTkLabel(right_skip_frame,image = arrow_icon_label_image , text ='' )
    
    right_skip_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
    
    
    
    
    

    frame2_1_bis = Page(frame2_1)
    frame2_1_bis.configure(corner_radius = 0,
        width = screen_width - frame_width - 3 * margin_x - 128 ,
                       height = frame_height-frame_height//1.4,
                     border_width = 1
                       )
    
    frame2_1_bis.place(x = 64,y = 0
                   )
     
    
    week_number = 1
    week_str = "week" + " " + str(week_number)
    
    week_label = ctk.CTkLabel(frame2_1_bis,text = week_str,font = ('calibri',23))
    week_label.place(relx = 0.5, y = 2 * margin_y, anchor = "center")
    
    
    LARGEUR = frame2_1_bis.cget('width')//2 
    
    
    cb_0 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_0.place(x = 38 + LARGEUR - 9 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
   
    cb_1 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_1.place(x = 38.5 + LARGEUR - 6 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
    
    
    cb_2 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_2.place(x = 38.5 + LARGEUR - 3 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
    
    
    cb_3 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_3.place(x = 38.5 + LARGEUR , y = 5.5 * margin_y , anchor = 'center') 
    
    
    cb_4 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_4.place(x = 38.5 + LARGEUR + 3 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
   
    cb_5 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_5.place(x = 38.5 + LARGEUR + 6 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
    
    
    cb_6 = ctk.CTkCheckBox(frame2_1_bis,border_color = 'grey28', width = 100,height = 100,
                           text = None ,hover_color = color1,state='disabled')
    cb_6.place(x = 38.5 + LARGEUR + 9 * margin_x , y = 5.5 * margin_y , anchor = 'center') 
    
    
    
    
    
    
    frame_main.configure(fg_color = "#1c1c1c")
    
   
    
    
    def week_update():
        global week_str
        
        week_str = "week" + str(week_number)
        week_label.configure(text = week_str)






def change_color(event,frame_name,state):
    global color1, color2
    if frame_name == "frame_1":
        if state == 'on':
            sub_frame1.configure(fg_color = color2)
        else:
            sub_frame1.configure(fg_color = color1)
    
    elif frame_name == "frame_2" and sub2_statue == "unlocked" :
        if state == 'on':
            sub_frame2.configure(fg_color = color2)
        else:
            sub_frame2.configure(fg_color = color1)
   
    elif frame_name == "frame_3" and sub3_statue == "unlocked" :
        if state == 'on':
            sub_frame3.configure(fg_color = color2)
        else:
            sub_frame3.configure(fg_color = color1)






    
# Création des widjets

button_create_habit = ctk.CTkButton(page1, text="Create habits", width=150, height=75,
                                    font=("calibri", 20), bg_color=window.cget('fg_color'), command=change_window,
                                    fg_color='#111111',hover_color='#040404')

button_create_habit.place(relx=0.5, rely=0.5, anchor="center")

habits_name_label = ctk.CTkLabel(page2, text='Name it', font=('calibri', 20, 'bold'))

habits_name_entry = ctk.CTkEntry(page2, placeholder_text="Brush my teeth", justify="center")

validation_time_label = ctk.CTkLabel(page3, text='Validation time', font=('calibri', 20, 'bold'))
 
    

how_long_label = ctk.CTkLabel(page4, text='How long ?', font=('calibri', 20, 'bold'))

how_long_entry = ctk.CTkEntry(page4, placeholder_text="How many months ?", justify="center")

or_label = ctk.CTkLabel(page4, text='or', font=('calibri', 20, 'bold'))

infinite_pil_image = Image.open('img/infinite_button.png')
infinite_pil_image = infinite_pil_image.convert("RGBA")
infinite_button_image = ctk.CTkImage(infinite_pil_image)

info_icon_pil_image = Image.open('img/info-icon.png')
info_icon_pil_image = info_icon_pil_image.convert("RGBA")
info_icon_label_image = ctk.CTkImage(info_icon_pil_image)

modify_icon_pil_image = Image.open('img/modify_icon.png')
modify_icon_pil_image = modify_icon_pil_image.convert("RGBA")
modify_icon_label_image = ctk.CTkImage(modify_icon_pil_image, size=(55, 55))

modify_icon_pil_image2 = Image.open('img/modify_icon2.png')
modify_icon_pil_image2 = modify_icon_pil_image2.convert("RGBA")
modify_icon_label_image2 = ctk.CTkImage(modify_icon_pil_image2, size=(55, 55))

tooltip_label = ctk.CTkLabel(page3, text="Time before you have to check if you did the habit", width=150, height=25,
                             corner_radius=7, fg_color="#4e6889", text_color="white",
                             font=("calibri", 10), anchor="center", padx=1, pady=1)

info_icon_label = ctk.CTkLabel(page3, image=info_icon_label_image, text='',
                               width=20, height=20)

modify_icon_label = ctk.CTkLabel(page5, image=modify_icon_label_image, text='',
                                 width=50, height=50, )







# page 5
page5_label1 = ctk.CTkLabel(page5, text="Habit's name", font=("calibri", 20))
page5_label1.place(relx=0.2, rely=0.3, anchor="center")

page5_label2 = ctk.CTkLabel(page5, text="Validation time", font=("calibri", 20))
page5_label2.place(relx=0.5, rely=0.3, anchor="center")

page5_label3 = ctk.CTkLabel(page5, text="How long", font=("calibri", 20))
page5_label3.place(relx=0.8, rely=0.3, anchor="center")

page5_entry1 = ctk.CTkEntry(page5, justify="center")
page5_entry1.place(relx=0.2, rely=0.4, anchor="center")

page5_entry2 = ctk.CTkEntry(page5, justify="center")
page5_entry2.place(relx=0.5, rely=0.4, anchor="center")

page5_entry3 = ctk.CTkEntry(page5, justify="center")
page5_entry3.place(relx=0.8, rely=0.4, anchor="center")

page5_button = ctk.CTkButton(page5, text="OK", width=50,command = enter_main,
                             fg_color='#111111',hover_color='#040404')
page5_button.place(relx=0.5, rely=0.6, anchor='center')

modify_icon_label.place(relx=0.925, rely=0.04, anchor='nw')

tmp = ''
def modify_entries(event):
    global tmp

    page5_entry1.configure(state='normal')
    page5_entry2.configure(state='normal')
    page5_entry3.configure(state='normal')

    page5_entry1.configure(placeholder_text='')
    page5_entry1.insert(0, habits_name_entry.get())

    page5_entry2.configure(placeholder_text='')
    page5_entry2.insert(0, stock[1] + stock[0] + 'h' + stock[3] + stock[2])

    page5_entry3.configure(placeholder_text='')
    page5_entry3.insert(0, tmp)

    modify_icon_label.configure(image=modify_icon_label_image2)

    modify_icon_label.unbind("<Enter>")
    modify_icon_label.unbind("<Leave>")
    modify_icon_label.unbind("<Button-1>")





def enter_page5(event='button_pressed'):
    global tmp

    modify_icon_label.bind('<Button-1>', lambda event: modify_entries(event))

    page5_entry1.configure(placeholder_text=habits_name_entry.get())
    page5_entry1.configure(state='disabled')

    page5_entry2.configure(placeholder_text=stock[1] + stock[0] + 'h' + stock[3] + stock[2])
    page5_entry2.configure(state='disabled')

    if event != 'button_pressed':
        tmp = how_long_entry.get() + ' months'
    else:
        tmp = 'limitless'

    page5_entry3.configure(placeholder_text=tmp)
    page5_entry3.configure(state='disabled')
    how_long_entry.unbind("<KeyPress-Return>")
    start_transition(create_tool,page4, page5)

infinity_button = ctk.CTkButton(page4, image=infinite_button_image, text="", width=50,
                                command=enter_page5,fg_color='#111111',hover_color='#040404')


def move_widgets2(widget):
    global create_tool

    h = 0

    create_tool.update()

    x_pos = widget.winfo_x()
    y_pos = widget.winfo_y()

    initial_placement = widget.place_info()

    widget.place_forget()
    create_tool.after(200)
    while h < 1:
        x_bis = random.uniform(-2, 2)
        y_bis = random.uniform(-2, 2)

        widget.place_configure(x=x_pos + x_bis, y=y_pos + y_bis)

        create_tool.after(50)
        create_tool.update()
        widget.place_configure(x=x_pos, y=y_pos)

        h += 0.1

    widget.place_configure(**initial_placement)
    habits_name_entry.bind("<KeyPress-Return>", lambda event: enter_event())

def maj_pressed(event):
    # savoir si la touche maj est activée
    if event.state == 2:
        print('la touche maj est activée')

def show_tooltip(event):
    tooltip_label.place(relx=0.75, rely=0.305, anchor='center')

def hide_tooltip(event):
    tooltip_label.place_forget()

def modify_selected(event):
    modify_icon_label.configure(image=modify_icon_label_image2)

def modify_unselected(event):
    modify_icon_label.configure(image=modify_icon_label_image)

# events
habits_name_entry.bind("<KeyPress-Return>", lambda event: enter_event())

info_icon_label.bind("<Enter>", show_tooltip)
info_icon_label.bind("<Leave>", hide_tooltip)

modify_icon_label.bind("<Enter>", modify_selected)
modify_icon_label.bind("<Leave>", modify_unselected)

# placement page 2
habits_name_label.place(relx=0.5, rely=0.3, anchor='center')
habits_name_entry.place(relx=0.5, rely=0.4, anchor='center')

# placement page 3
validation_time_label.place(relx=0.5, rely=0.3, anchor='center')
info_icon_label.place(relx=0.61, rely=0.305, anchor='center')

# placement page 4
how_long_label.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.3)
how_long_entry.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.18)
or_label.place(relx=0.43, rely=0.5, anchor='center', relwidth=0.05)
infinity_button.place(relx=0.5, rely=0.5, anchor='center')

hours_1 = '0'
hours_0 = '0'
minutes_3 = '0'
minutes_2 = '0'

time_disp = ctk.CTkLabel(page3, text=str(hours_1) + str(hours_0) + ' : ' +
                         str(minutes_3) + str(minutes_2), font=('calibri', 36),
                         fg_color='transparent')
time_disp.place(relx=0.5, rely=0.4, anchor="center")

blink = "  "
blink2 = "_"

numbers = [str(x) for x in range(10)]
stock = ['0', '  ', '0', '0']
x = 0

first_try = True
blind1_en_cours = "on"
blind2_en_cours = "off"

running = True

def checker():
    global x, create_tool, stock, first_try, running
    if not running:
        return
    else:
        if on_off_var == "off":
            create_tool.after(100, checker)
        elif on_off_var == 'on':
            if stock[0] in ["0", "1", "2"] and x == 0:
                x += 1
            elif not stock[0] in ["0", "1", "2"] and x == 0 and first_try:
                stock[1] = "0"
                x += 2
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
    global x, create_tool, stock
    if on_off_var == "off":
        create_tool.after(100, checker)

def enter_page2_1(event=None):
    global stock, numbers, x, on_off_var, first_try
    create_tool.bind('<KeyPress>', lambda event: enter_page2_1(event))

    if event != None:
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
                    stock[x] = event.keysym
                create_tool.after(100, checker)
            elif first_try == False:
                if event.keysym in numbers[6:] and x == 3:
                    blink_function2()
                stock[x] = event.keysym
                blink_function2()
        elif event.keysym == "Left" and not first_try:
            if x != 1:
                checker2()
                if x == 0 or x == 2:
                    x += 1
                elif x == 3:
                    x = 0
        elif event.keysym == "Right" and not first_try:
            if x != 2:
                checker2()
                if x == 1 or x == 3:
                    x -= 1
                elif x == 0:
                    x = 3
        elif event.keysym == 'Return' and x >= 2:
            enter_page2_2()
        elif event.keysym == 'Return' and stock[0] in ["0", "1", "2"] and stock[1] in ["  ", "0"]:
            checker2()
            x = 2
            stock[1] = "0"
            time.sleep(0.3)

def enter_page2_2():
    global x, running
    running = False
    if x == 2 or x == 3:
        x = 4
        create_tool.unbind("<KeyPress>")
        create_tool.after(100, enter_page4())

def enter_page4():
    start_transition(create_tool,page3, page4)
    how_long_entry.bind("<KeyPress-Return>", lambda event: enter_page5(event))


def blink_function():
    global x, stock, on_off_var, blind2_en_cours, blind1_en_cours

    if blind2_en_cours == "on":
        create_tool.after(100, checker)
    elif blind2_en_cours == 'off':
        if on_off_var == "on":
            time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                 str(stock[3]) + str(stock[2]))
        elif on_off_var == 'off':
            if x < 2:
                time_disp.configure(text=str(blink) + str(blink) + ' : ' +
                                     str(stock[3]) + str(stock[2]))
            else:
                create_tool.bind('<KeyPress-Return>', lambda event: enter_page2_2())
                time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                     str(blink) + str(blink))
        create_tool.after(300, blink_function)

def blink_function2():
    global x, stock, on_off_var, blind2_en_cours, blind1_en_cours
    blind2_en_cours = "on"
    if on_off_var == "on":
        time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                             str(stock[3]) + str(stock[2]))
    elif on_off_var == 'off':
        if x == 0:
            time_disp.configure(text=str(stock[1]) + str(blink2) + ' : ' +
                                 str(stock[3]) + str(stock[2]))
        elif x == 1:
            time_disp.configure(text=str(blink2) + str(stock[0]) + ' : ' +
                                 str(stock[3]) + str(stock[2]))
        elif x == 2:
            time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                 str(stock[3]) + str(blink2))
        elif x == 3:
            time_disp.configure(text=str(stock[1]) + str(stock[0]) + ' : ' +
                                 str(blink2) + str(stock[2]))
    create_tool.after(300, blink_function2)

def enter_event():
    global habits_name, habits_name_label
    habits_name = habits_name_entry.get()
    if len(habits_name) != 0:
        habits_name_entry.unbind("<KeyPress-Return>")
        habits_name_entry.configure(state='disabled')
        create_tool.after(300, lambda: start_transition(create_tool,page2, page3))
        blink_function()
        enter_page2_1()
    else:
        habits_name_entry.unbind("<KeyPress-Return>")
        move_widgets2(habits_name_label)

on_off_var = "on"
running_on_off = True

def on_off():
    global on_off_var, create_tool, running_on_off
    if on_off_var == "on":
        on_off_var = "off"
        create_tool.after(470, on_off)
    elif on_off_var == "off":
        on_off_var = 'on'
        create_tool.after(2600, on_off)

on_off()

habit_number = 0







window.mainloop()
