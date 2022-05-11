import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import pandas as pd
from app import app

#Image Card for the home page
image_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Accu Stats", className="card-title", style={"padding":20, "text-align": "center"}),
                dbc.CardImg(src="../assets/dart.jpg")
            ]
        ),
    ],
    className="h-100",
    color="light",
)

#Text body for the home page
graph_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("The Criminal History Of Berlin", className="card-title", style={"text-align": "center",
                                                                                         "color": "black", "padding":20}),
                html.P("Berlin's long history as a European capital has left it with a rich legacy of museums. Amongst them is the Berlin Police Museum, which records the constant struggle between the Berlin Police Force and it's substantial criminal underworld."),
                html.P("The exhibits in the museum make it clear that the wealth of Berlin is what attracts the criminal underclass of Germany and beyond. Unfortunately, most of the museum's contents were destroyed during the Allied bombing raids of 1945. The museum reopened in 1973, with historical documents found in the intervening years, as well as materials on the Post War Federal Republic."),
                html.P("Today it attracts over 10,000 visitors a year. Among the most interesting exhibits is a collection of flags and other material on the criminal societies of '20's. These may not be as well known as their Chicago counterparts based on which they were modelled, but nonetheless, they posed an equal threat to police authority.")
            ],
        ),
    ],
    className="h-100",
    color="light",
)

#Layout of home page
layout = html.Div([
                dbc.Row([dbc.Col(image_card, width=3, style={"height": "100%"}),
                         dbc.Col(graph_card, width=8, style={"height": "100%"})],
                        align="stretch", justify="around", style={"height": "100vh"})
                ])
