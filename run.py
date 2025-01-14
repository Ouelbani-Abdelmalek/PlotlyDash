from dash import Dash
from app.data_loading import load_data
from app.data_cleaning import clean_data
from app.data_processing import nombre_de_vente_par_axe
from app.callbacks import register_callbacks
from app.layouts import serve_layout

app = Dash(__name__, suppress_callback_exceptions=True)
app = Dash(__name__)

# Charger et traiter les données
df = load_data('data/','new_retail_data.csv')
df = clean_data(df)
df = nombre_de_vente_par_axe(df,'Customer_ID')

# Définir la mise en page
app.layout = serve_layout()

# Enregistrer les callbacks
register_callbacks(app, df)

if __name__ == '__main__':
    app.run_server(debug=True)

