# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Class import *
import pandas as pd
import numpy as np
from os import stat



def create_habit(name):

    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    return Habits(name,[],[day,month,year])

#Fonction vérifiant si un fichier est vide
def est_fichier_vide(nom_fichier):
    return stat(nom_fichier).st_size == 0


