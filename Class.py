
class Habits :

    def __init__(self, name, iteration, starting_date):

        self.name = name
        self.iteration = iteration

        #Data JJMMAAA
        self.starting_date = starting_date
        self.attributs_ls = [name, iteration, starting_date]
        pass

    def add_iteration(self,booleen_value):
        #iteration est un tableau

        self.iteration.append(booleen_value)
