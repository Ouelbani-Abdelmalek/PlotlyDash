
#supprimer les lignes ou on a des vides
def clean_data(df):
    df.dropna(inplace=True)
    return df