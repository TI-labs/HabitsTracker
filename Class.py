
import customtkinter as ctk

class Habits() :

    def __init__(self, name, iteration, starting_date,how_long ,validation_time):

        self.name = name
        self.iteration = iteration
        self.how_long = how_long
        self.validation_time = validation_time
        
        #Data JJMMAAA
        self.starting_date = starting_date
        self.all_attributs = [name, iteration, starting_date, how_long ,validation_time]


    def add_iteration(self,booleen_value):
        #iteration est une liste

        self.iteration.append(booleen_value)

class Page(ctk.CTkFrame) : 
    def __init__(self, master,title=''):
        master.update()
        ctk.CTkFrame.__init__(self, master,
                              height = master.winfo_height(), 
                              width = master.winfo_width(),
                              bg_color = master.cget("fg_color"),
                              fg_color = master.cget("fg_color" ))
        
        self.label = ctk.CTkLabel(self, text=title)
        self.label.place(relx=0.5, rely=0.5, anchor='center')