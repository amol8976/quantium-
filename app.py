from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

data_path = "data/output.csv"
df = pd.read_csv(data_path)

df = df.sort_values(by="Date")

app = Dash(__name__)

# Define the layout
app.layout = html.Div(
    className="app-container",
    children=[
        html.Div(
            className="glass-header",
            children=[
                html.H1(
                    children='Sales Visualizer',
                    className="title"
                ),
            ]
        ),
        
        html.Div(
            className="glass-container controls",
            children=[
                # Radio button with 5 options
                dcc.RadioItems(
                    id='region-filter',
                    options=[
                        {'label': 'North', 'value': 'north'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'West', 'value': 'west'},
                        {'label': 'All Regions', 'value': 'all'}
                    ],
                    value='all',  
                    inline=True,
                    className="radio-group"
                )
            ]
        ),
        
        html.Div(
            className="glass-container graph-container",
            children=[
                dcc.Graph(
                    id='sales-line-chart'
                )
            ]
        )
    ]
)

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
        title_text = "Pink Morsel Sales - All Regions"
    else:
        filtered_df = df[df['Region'] == selected_region]
        title_text = f"Pink Morsel Sales - {selected_region.capitalize()} Region"

    region_colors = {
        "north": "#00f2fe", 
        "south": "#ff0844",  
        "east":  "#b02bf4", 
        "west":  "#00e676"   
    }

    fig = px.line(
        filtered_df, 
        x="Date", 
        y="Sales", 
        color="Region",
        color_discrete_map=region_colors,
        title=title_text,
        labels={
            "Date": "Sale Date",
            "Sales": "Total Sales ($)",
            "Region": "Geographic Region"
        },
        template="plotly_dark"  
    )
    
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#e0e0e0",
        margin=dict(l=40, r=40, t=80, b=80),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
