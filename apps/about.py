import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from app import app

card_main = dbc.Card(
    [
        dbc.CardImg(src="/assets/crime_scene.jpg", top=True, bottom=False,
                    title="Crime Scene Investigation"),
        dbc.CardBody(
            [
                html.H4("Learn more about Dash", className="card-title"),
                html.P(
                    "Dash is a Python framework created by Plotly for building interactive web applications. Dash is written on top of Flask, Plotly.js and React.js." + " " +
                    "With Dash, you don't have to learn HTML, CSS and Javascript in order to create interactive dashboards, you only need Python." + " " +
                    "Read more about Dash from it's documentation at dash.plotly.com",
                    className="card-text",
                ),
                html.Br(),
                html.H4("Scope of the Dashboard", className="card-title"),
                html.P("Feel free to add your own spin to the dashboard. For instance, you can try scraping housing data of Berlin so that future residents can" + " " +
                     "plan according to their budget. Additional data based on recreational facilities, healthcare, transportation etc. can also be collected," + " " +
                     "and we can use different clustering algorithms on that data to recommend the perfect district in Berlin for a new user to stay, based on their preferences.",
                     className="card-text",
                ),
            ]
        ),
    ],
    color="dark",
    inverse=True,   
    outline=False,  
)

layout = html.Div([
    dbc.Row([dbc.Col(card_main, width=6)], justify="center"),
])

