from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly
import plotly.express as px
import dash_bootstrap_components as dbc

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

import bar_graph as bar_gph
import app_tabs as tp
import app_navbar as nb

x = bar_gph.Barclass('a', 'b')
external_stylesheet = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[external_stylesheet])


app.layout = html.Div([

        dbc.Row(
            [
                dbc.Col(
                    [

                    ], width=6
                ),

            ]
        )


])
# @app.callback(
#     Output('tab1_output', "children"),
#     [Input("drop1", "value")]
# )
# def show_output(n):
#     if n:
#         return f'selected values is {n}'

if __name__ == '__main__':
    app.run_server(debug=True)
