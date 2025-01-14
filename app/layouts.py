import dash_core_components as dcc
import dash_html_components as html

def serve_layout():
    return html.Div([
        html.Header('Retail analytics', className='container-fluid'),
        
        html.Div([
            html.Nav([
                html.Ul([
                    html.Li(html.A('Accueil', href='#', className='nav-link')),
                    html.Li(html.A('Graphique', href='#', className='nav-link')),
                    html.Li(html.A('Contact', href='#', className='nav-link'))
                ], className='nav flex-column')
            ], className='col-2 sidebar'),

            html.Main([
                dcc.Graph(id='sales-by-country-graph'),
                html.Button('Mettre à jour', id='update-button', n_clicks=0)
            ], className='col-10')
        ], className='row no-gutters'),

        html.Footer('© 2025 Lynxia', className='container-fluid')
    ])

