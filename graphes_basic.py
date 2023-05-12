#version basic
# Using express
import plotly.express as px
import pandas as pd
df = pd.read_csv('sensor-data-p2.csv',sep=';')
# Use directly Columns as argument. You can use tab completion for this!
fig = px.line( x=df.time,y=df.temp, title='Mesures temperature')

fig.show()


'''
#version basic
# Using graph_objects 
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('sensor-data-p2.csv',sep=';')

#fig = go.Figure(data=[go.Scatter(x=df['time'], y=df['temp'], mode = 'markers',)])
fig = go.Figure([go.Scatter(x=df['time'], y=df['temp'],)])  

fig.show()
'''

'''
#version basic
#version matplot lib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sensor-data-p2.csv',sep=';')

plt.plot(df['time'],df['temp'])

plt.show()
'''