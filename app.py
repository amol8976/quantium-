from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

data_path = "data/output.csv"
df = pd.read_csv(data_path)

df = df.sort_values(by="Date")

app = Dash(__name__)


fig = px.line(
    df, 
    x="Date", 
    y="Sales", 
    color="Region",
    title="Pink Morsel Sales by Region",
    labels={
        "Date": "Sale Date",
        "Sales": "Total Sales ($)",
        "Region": "Geographic Region"
    }
)

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualizer',
        style={'textAlign': 'center'}
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
