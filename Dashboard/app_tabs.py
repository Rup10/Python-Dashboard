import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import app_navbar as nb
# bot_style = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"

tab1 = dbc.Card(
    dbc.CardBody([
        html.P(id="tab1_output", children="this is tab 1", className="card-text"),
        html.Div(nb.nav1)

    ]), className="mt-3"
)


tab2 = dbc.Card(
    dbc.CardBody([
        html.P("this is tab 2", className="card-text")

    ]), className="mt-3"
)

