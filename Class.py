
import customtkinter as ctk

class Habits :

    def __init__(self, name, iteration, starting_date):

        self.name = name
        self.iteration = iteration

        #Data JJMMAAA
        self.starting_date = starting_date
        self.attributs_ls = [name, iteration, starting_date]


    def add_iteration(self,booleen_value):
        #iteration est un tableau

        self.iteration.append(booleen_value)

class Page(ctk.CTkFrame) : 
    def __init__(self, master,title=''):
        master.update()
        ctk.CTkFrame.__init__(self, master, height = master.winfo_height(), width = master.winfo_width())
        self.label = ctk.CTkLabel(self, text=title)
        self.label.place(relx=0.5, rely=0.5, anchor='center')