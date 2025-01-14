import pandas as pd
import os 

## Cette fonction nous permet de lire les differents fichiers csv qu'on utilisera par la suite comme source de données 
def load_data(full_path, file): 
    file_path = os.path.join(full_path, file) 
    df = pd.read_csv(file_path) 
    return df