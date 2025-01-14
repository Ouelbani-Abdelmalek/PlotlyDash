from dash.dependencies import Input, Output
import plotly.graph_objs as go

def register_callbacks(app, df):

    @app.callback(
        Output('sales-by-country-graph', 'figure'),
        [Input('update-button', 'n_clicks')]
    )
    def update_graph(n_clicks):
        data = [
            go.Bar(
                x=df['Country'],
                y=df['Customer_ID'],
                marker=dict(
                    color='rgba(0, 173, 181, 0.6)',
                    line=dict(color='rgba(0, 173, 181, 1.0)', width=2)
                )
            )
        ]

        layout = go.Layout(
            title='Nombre de Ventes par Pays',
            xaxis=dict(title='Pays'),
            yaxis=dict(title='Ventes'),
            paper_bgcolor='rgba(30, 30, 30, 1)',
            plot_bgcolor='rgba(30, 30, 30, 1)',
            font=dict(color='#E0E0E0')
        )

        return {'data': data, 'layout': layout}
