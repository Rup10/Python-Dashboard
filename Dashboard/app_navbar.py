import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output


nav1 = dbc.Nav(
    [
        dbc.NavItem(
            [
                html.H6("Columns"),
                dcc.Dropdown(
                    ["1", "2", "3"],
                    id="drop1",
                    multi=True

                )
            ],
            className="nav_item1"
        )
        # dbc.DropdownMenu(
        #     [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
        #     label="Dropdown",
        #     nav=True,
        # )
        # dcc.Dropdown(
        #         ["1", "2", "3"],
        #         id="drop1",
        #
        #     )
    ],
    id="nav-1"
    # vertical='md'
)

