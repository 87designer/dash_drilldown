import dash
from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('https://theunitedstates.io/congress-legislators/legislators-current.csv')

state_df = df[['state', 'type', 'full_name']].groupby(by=["state", "type"]).count()
state_df.rename(columns={'full_name': 'count'}, inplace=True)
state_df.reset_index(inplace=True)

app = dash.Dash(__name__)

# TODO: Build out a simple Plotly Dash App and create a Custom DataTable Drill Down feature
app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in state_df.columns],
    data=state_df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)