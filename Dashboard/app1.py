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

# print("hello world")
x = bar_gph.Barclass('a', 'b')
print((bar_gph.long_df["nation"]))
# x.name = "rup"
# print(x.method1())

app = Dash(__name__)


app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            bar_gph.nations,
            id="drop_1",
            maxHeight=100,
            style={'width': '200px'},

        )
    ]),



    dcc.Graph(
        figure=x.method1()
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)