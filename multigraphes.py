#multi graphes
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load dataset
df = pd.read_csv('sensor-data-p2.csv',sep=';')

# Initialize figure
fig = go.Figure()
#fig = px.line( x=df.time,y=df.TCOV) #time,temp,humidity,CO2,TCOV

# Add Traces
fig.add_trace(
    go.Scatter(x=list(df.time),
               y=list(df.temp),
               name="Temperature",
               line=dict(color="#F2BB05"),
               mode = 'lines'))  

fig.add_trace(
    go.Scatter(x=list(df.time),
               y=list(df.humidity),
               name="Humidité",
               line=dict(color="#6E0E0A"),
               mode = 'lines'))

fig.add_trace(
    go.Scatter(x=list(df.time),
               y=list(df.TCOV),
               name="TCOV",
               line=dict(color="#124E78"),
               mode = 'lines'))

fig.update_layout(
    updatemenus=[
        dict(
            active=3,
            buttons=list([
                dict(label="Température",
                     method="update",
                     args=[{"visible": [True, False,False ]},
                           {"title": "Mesures températures"},
                           {"yaxes_title":"°C"},]),
                dict(label="Humidité",
                     method="update",
                     args=[{"visible": [False, True,False]},
                           {"title": "Mesures Humidité"},
                           {"yaxes_title":"%"},]),
                dict(label="TCOV",
                     method="update",
                     args=[{"visible": [False,False ,True]},
                           {"title": "Mesures TCOV"},
                           {"yaxes_title":"X Axis Title"},]),
                dict(label="Tout",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {"title": "Mesures globales"},
                           {"yaxis_title":"X Axis Title"},]),
            ]),
        )
    ])


fig.update_xaxes(
        title_text = "<b>Mars 2023</b>",
        title_font = {"size": 20},
        title_standoff = 25,
        tickfont = {"size" : 15,'color' : 'black', 'family' : "Times New Roman"},
        tickangle = -90,
        showticklabels=True,
        nticks=31)

fig.update_yaxes(        
        title_standoff = 25,
        title_font = {"size": 20},
        rangemode="tozero")


# Set title
fig.update_layout(title_text="Mesures globales",
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="#D74E09",
    title_font ={"size": 35},
    title_x=0.5,)

fig.show()


