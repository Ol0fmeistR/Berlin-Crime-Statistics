import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

#Connect to main app.py file
from app import app
from app import server

#Connect to your app pages
from apps import assault, robbery, arson, narcotics, graffiti, home

#Navbar
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/apps/home")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Assault Cases", href="/apps/assault"),
                    dbc.DropdownMenuItem("Robbery Cases", href="/apps/robbery"),
                    dbc.DropdownMenuItem("Narcotics Cases", href="/apps/narcotics"),
                    dbc.DropdownMenuItem("Arson Cases", href="/apps/arson"),
                    dbc.DropdownMenuItem("Graffiti Cases", href="/apps/graffiti"),
                ],
                nav=True,
                in_navbar=True,
                label="Crime Statistics",
            ),
            dbc.NavItem(dbc.NavLink("About", href="#"))
        ],
    brand="Berlin Crime Statistics",
    brand_href="/apps/home",
    style={"margin-bottom":5},
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[])
])

#Not making a 404 page, routing it directly to home
default_template = home.layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/assault':
        return assault.layout
    elif pathname == '/apps/robbery':
        return robbery.layout
    elif pathname == '/apps/arson':
        return arson.layout
    elif pathname == '/apps/narcotics':
        return narcotics.layout
    elif pathname == '/apps/graffiti':
        return graffiti.layout
    elif pathname == '/apps/home':
        return home.layout
    else:
        return default_template


if __name__ == '__main__':
    app.run_server(debug=False)
