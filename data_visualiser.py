import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

DATA = './formatted_data.csv'

data = pd.read_csv(DATA)
data = data.sort_values(by='Date')

app = Dash(__name__)

line_chart = px.line(data, x='Date', y='Sales', title='Pink Morsel Sales')
visualization = dcc.Graph(figure=line_chart, id='line_chart')

header = html.H1('Pink Morsel Sales', id='header')

app.layout = html.Div([header, visualization])

if __name__ == '__main__':
    app.run_server(debug=True)