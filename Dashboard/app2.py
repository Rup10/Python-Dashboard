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
        dbc.Row(
            [
                html.Div(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Button([], className="fa fa-bar-chart", style={
                                                    'font-size': '25px',
                                                    'background-color': 'black', 'border-color': 'transparent',
                                                    'color': 'yellow', 'margin-right': '2px',
                                                }),
                                                dbc.Button([], className="fa fa-area-chart", style={
                                                    'font-size': '25px',
                                                    'background-color': 'black', 'border-color': 'transparent',
                                                    'color': '#8700ff', 'margin-right': '2px',
                                                    'margin-left': '1px'
                                                }),
                                                dbc.Button([], className="fa fa-line-chart", style={
                                                    'font-size': '25px',
                                                    'background-color': 'black', 'border-color': 'transparent',
                                                    'color': '#0dd092', 'margin-right': '2px',
                                                }),
                                                dbc.Button([], className="fa fa-pie-chart", style={
                                                    'font-size': '25px',
                                                    'background-color': 'black', 'border-color': 'transparent',
                                                    'color': '#ef0fa0', 'margin-right': '1px',
                                                }),
                                                # dbc.Button([], className="fa fa-bar-chart", style={
                                                #     'background-color': 'black',
                                                #     'border-color': 'transparent',
                                                #     'color': 'yellow',
                                                #     'margin-right': '2px',
                                                #     # 'hover': {
                                                #     #     'background-color': 'black'
                                                #     # }
                                                #
                                                # }),
                                                # html.Button(children=[], id='bt-1', className="fa fa-bar-chart"),
                                                # html.Span("Bar graph", className="bt1_hov"),
                                                # html.Button(children=[], id='bt-1', className="fa fa-area-chart"),
                                                # html.Span("Area graph", className="bt1_hov"),
                                                # html.Button(children=[], id='bt-1', className="fa fa-line-chart"),
                                                # html.Span("Line graph", className="bt1_hov"),
                                            ], className='btn_grp'
                                        ),
                                        # html.Div([
                                        #     html.Button(children=[], id='bt-1', className="fa fa-bar-chart"),
                                        #     html.Span("Bar graph", className="bt1_hover")
                                        # ]),
                                        # html.Div([
                                        #     html.Button(children=[], id='bt-1', className="fa fa-line-chart"),
                                        #     html.Span("Bar graph", className="bt1_hover")
                                        # ]),
                                        # html.Div([
                                        #     html.Button(children=[], id='bt-1', className="fa fa-pie-chart"),
                                        #     html.Span("Bar graph", className="bt1_hover")
                                        # ]),
                                        # html.Button(children=[],id='bt-1', className="fa fa-area-chart"),
                                        # html.Button(children="", id='bt-2', className="fa fa-bar-chart"),
                                        # html.Button(children="", id='bt-3', className="fa fa-line-chart"),
                                        # html.Button(children="", id='bt-3', className="fa fa-pie-chart")


                                    ]
                                )
                            ], className='cl-1', width=6, lg=4
                        )
                    ]
                )
            ], className='rw-1'
        )

        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 dbc.ButtonGroup(
        #                     [dbc.Button(name='pie', className='BG-1'),
        #                      dbc.Button("Line", className='BG-1'),
        #                      dbc.Button("Bar", className='BG-1'), ], size='md'
        #                 ),
        #                 dbc.ButtonGroup(
        #                     [dbc.Button("Pie", className='BG-1'),
        #                      dbc.Button("Line", className='BG-1'),
        #                      dbc.Button("Bar", className='BG-1'), ], size='md'
        #                 ),
        #                 dbc.ButtonGroup(
        #                     [dbc.Button("Pie", className='BG-1'),
        #                      dbc.Button("Line", className='BG-1'),
        #                      dbc.Button("Bar", className='BG-1'), ], size='md'
        #                 )
        #             ], id="col-1",  width=3, lg=2,
        #         ),
        #
        #         # dbc.Col(
        #         #     [
        #         #         dbc.ButtonGroup(
        #         #             [dbc.Button("Pie"), dbc.Button("Line"), dbc.Button("Bar"), ], size='md'
        #         #         )
        #         #     ], id='col-2', width=12
        #         # )
        #
        #     ], id='row-1'
        # )


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
