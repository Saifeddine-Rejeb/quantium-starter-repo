import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DATA = "./formatted_data.csv"
COLORS = {
    "bg": "#4C585B", 
    "bg2": "#7E99A3", 
    "pprbg": "#A5BFCC", 
    "bckg": "#F4EDD3"
}

data = pd.read_csv(DATA)
data = data.sort_values(by="Date")

color_map = {
    "north": "#3B6790",
    "east": "#77B254",
    "south": "#BE3144",
    "west": "#A888B5",
}

app = Dash(__name__)

def generate_figure(data):
    figure = px.line(
        data, x="Date", y="Sales", color="Region", color_discrete_map=color_map
    )
    figure.update_layout(
        plot_bgcolor=COLORS["bckg"],
        paper_bgcolor=COLORS["pprbg"],
        font_color=COLORS["bg"],
    )
    return figure

visualization = dcc.Graph(figure=generate_figure(data), id="line_chart")

header = html.H1(
    "Pink Morsel Sales",
    id="header",
    style={
        "textAlign": "center",
        "backgroundColor": COLORS["bg"],
        "color": COLORS["bckg"],
        "padding": "10px",
        "margin": "10px",
    },
)

region = dcc.RadioItems(
    ["north", "east", "south", "west", "all"], "north", id="region", inline=True
)

region_wrapper = html.Div(
    [region],
    style={
        "padding": "10px",
        "margin": "10px",
        "border": "1px solid black",
        "font-size": "200%",
    },
)

@app.callback(
    Output(visualization, "figure"),
    Input(region, "value"),
)
def update_graph(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["Region"] == region]
    figure = generate_figure(filtered_data)
    return figure

app.layout = html.Div(
    [header, visualization, region],
    style={
        "textAlign": "center",
        "backgroundColor": COLORS["bg"],
        "color": COLORS["bckg"],
    },
)

if __name__ == "__main__":
    app.run_server(debug=True)
