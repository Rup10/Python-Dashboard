import pandas as pd
import plotly
import plotly.express as px
import bar_graph as bar_gph
import dash_bootstrap_components as dbc

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

from dash import Dash, dcc, html, Input, Output


x = bar_gph.Barclass('a', 'b')
print((bar_gph.long_df["nation"]))
# x.name = "rup"
# print(x.method1())


# =========================================================
# style for sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


# ===================================================

app = Dash(__name__)


app.layout =html.Div([

    html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P(
                "A simple sidebar layout with navigation links", className="lead"
            ),
            dbc.Nav(
                [
                    # html.Div([dbc.NavLink("Home", href="/", active="exact")]),
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Page 1", href="/page-1", active="exact"),
                    dbc.NavLink("Page 2", href="/page-2", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style={
            # "border": "20 20 20 20",
            # "border-color": "coral",
            "position": "fixed",
            "top": 0,
            "left": 0,
            "width": "150px",
            "height": "100%",
            "padding": "20px 10px",
            "background-color": "rgb(151 171 194)",
        },
    ),

    # html.Div([
    #     dcc.Dropdown(
    #         bar_gph.nations,
    #         id="drop_1",
    #         maxHeight=100,
    #         style={'width': '200px'},
    #
    #     )
    # ]),



    # dcc.Graph(
    #     figure=x.method1()
    # )

])


if __name__ == '__main__':
    app.run_server(debug=True)