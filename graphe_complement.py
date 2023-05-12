# graphe complet
# Using plotly express
import plotly.express as px

import pandas as pd
df = pd.read_csv('sensor-data-p2.csv',sep=';')

#fig = go.Figure([go.Scatter( mode = "lines",x=df['time'], y=df['CO2'])])  
fig = px.scatter( x=df.time,y=df.CO2) #time,temp,humidity,CO2,TCOV

fig.update_xaxes(
        title_text = "<b>Mars 2023</b>",
        title_font = {"size": 20},
        title_standoff = 50,
        tickfont = {"size" : 15,'color' : 'black', 'family' : "Times New Roman"},
        tickangle = -90,
        showticklabels=True,
        nticks=31)
fig.update_yaxes(
        title_text = "<b>Niveau CO2</b>",
        title_standoff = 25,
        title_font = {"size": 20},
        rangemode="tozero")

fig.update_layout(
    title_text="<b>Mesures <i>Niveau CO2</i></b>",
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="red",
    title_font ={"size": 35},
     title_x=0.5,
    legend_title_font_color="green",
    xaxis=dict(type = "category")
    )
fig.show()
