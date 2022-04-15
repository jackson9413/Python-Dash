# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:12:06 2022

@author: jqche
"""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import packages
# !pip install dash
from dash import Dash, html, dcc, dash_table # dash
import plotly.graph_objects as go ## Python Plotly
import pandas as pd
import openpyxl
import tkinter as tk  # tkinter GUI
from tkinter import ttk
from tkinter import filedialog as fd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)                                
app = Dash(__name__)   
# Root window
root = tk.Tk()
filename = fd.askopenfilename()  ## SELECT YOUR EXCEL FILE ##
root.destroy()

df = pd.read_excel(filename, header=0, nrows=129) ## ONLY READ TOP 129 ROWS ##


fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=df.index.values, y=df["Average/run"].values, 
                         error_y_array = df["STDEV/run"].values, error_y_visible = True,
                         marker_symbol="square-open", marker_line_width = 2, 
                         marker_size=10, marker_opacity = 1, mode="markers", 
                         name = "Average/run"))

fig.add_trace(go.Scatter(x=df.index.values, y=df["% Recovery"].values,
                    mode='lines+markers',
                    name='% Recovery'))

fig.add_hline(y=df.iloc[0]["Average"], line_color = "green", line_dash = "dash", annotation_text="Average")
fig.add_hline(y=df.iloc[0]["UCL"], line_color = "red", line_dash = "dash", annotation_text="UCL")
fig.add_hline(y=df.iloc[0]["LCL"], line_color = "red", line_dash = "dash", annotation_text="LCL")
fig.update_layout(
    yaxis_range=[85, 120],
    title="Normal BSA",
    xaxis_title="date",
    yaxis_title="% Recovery",
    legend=dict(
    yanchor="top",
    xanchor="right")
)

app.layout = html.Div(children=[
    #dcc.Upload(html.Button('Upload File')),
    #html.Hr(),
    #dcc.Upload(html.A('Upload File')),
    html.Hr(),    
    html.H1(children='Normal BSA X-bar Contorl Chart'),
    html.Hr(),
    dcc.Upload([
        'Drag and Drop or ',
        html.A('Select a File')
    ], style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center'
    }),
    html.Hr(),
    html.Div(
        children= [
            dash_table.DataTable(
                id ='Table',
                data = df.to_dict('records'),
                columns = [{'name': i, 'id': i} for i in df.columns]
        )
            ]  
        ),
    html.Hr(),    
    html.Div(children='''
        A Web App By Using Dash and Plotly.
    '''),
    html.Hr(),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)