import pandas as pd
import os




# Cette fonction nous renvoie le nombre de vente par un axe analytique choisit (Pays, Age, Sexe...)
def nombre_de_vente_par_axe(df,axe):
    sales_by_axis = df.groupby('Country')[axe].count().reset_index()
    return sales_by_axis
