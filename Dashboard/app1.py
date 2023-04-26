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
external_stylesheet1 = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
external_stylesheet2 = "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.13.1/build/styles/tomorrow-night-eighties.min.css"
external_stylesheet3 = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
external_stylesheet4 = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
app = Dash(__name__, external_stylesheets=[external_stylesheet1, external_stylesheet2, external_stylesheet3,
                                           external_stylesheet4])

app.layout = html.Div([
    dbc.Row([
        # html.Div([

        dbc.Col([

            dbc.Button([], id='btn-1', className="fa fa-bar-chart", n_clicks=0,
                       style={
                           'margin-left': '0px', 'font-size': '20px',
                           'background-color': 'black', 'border-color': 'transparent',
                           'color': 'yellow', 'margin-right': '2px',
                       }),
            dbc.Button([], className="fa fa-area-chart", style={
                'font-size': '20px',
                'background-color': 'black', 'border-color': 'transparent',
                'color': '#8700ff', 'margin-right': '2px',
                'margin-left': '1px'
            }),
            dbc.Button([], className="fa fa-line-chart", style={
                'font-size': '20px',
                'background-color': 'black', 'border-color': 'transparent',
                'color': '#0dd092', 'margin-right': '2px',
            }),
            dbc.Button([], className="fa fa-pie-chart", style={
                'font-size': '20px',
                'background-color': 'black', 'border-color': 'transparent',
                'color': '#ef0fa0', 'margin-right': '1px',
            }),
        ], width=2, style={'height': '150px', 'border': '2px solid',
                           'padding-top': '2px', 'padding-bottom': '2px'}),

        dbc.Col([
            html.P(id='out-id', children=['output-'])

        ], width=3, style={'border': '2px solid'}),

    ], style={'margin-left': '1px'})

    # ])

])


@app.callback(
    Output("out-id", "children"), [Input("btn-1", "n_clicks")]
)
def show_output(n):
    if n is None:
        return "none"
    else:
        return f'output-{n}'


if __name__ == '__main__':
    app.run_server(debug=True)
