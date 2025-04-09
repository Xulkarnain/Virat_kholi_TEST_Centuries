import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
df = pd.read_csv('Virat_Centuries_Final.csv')

print(df.head())



print(df.columns)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


df['year'] = df['Date'].dt.year

centuries_per_year = df['year'].value_counts().sort_index()

fig = px.bar(
    x=centuries_per_year.index,
    y=centuries_per_year.values,
    labels={'x': 'Year', 'y': 'Number of Centuries'},
    title="Virat Kohli's Centuries Per Year",
    color=centuries_per_year.values,
    text=centuries_per_year.values,
    color_continuous_scale='Viridis',
)


fig.show()


df.columns = df.columns.str.strip()       
df['Against'] = df['Against'].str.strip() 
df.columns = df.columns.str.strip()
df['Against'] = df['Against'].str.strip()



centuries_by_team = df['Against'].value_counts()

fig = px.bar(
    x=centuries_by_team.index,
    y=centuries_by_team.values,
    labels={'x': 'Opponent Team', 'y': 'Number of Centuries'},
    title="Virat Kohli's Centuries Against Each Country",
    color=centuries_by_team.values,
    text=centuries_by_team.values,
    color_continuous_scale='twilight',
)
   
fig.show()   

df.coulmns = df.columns.str.strip()
df['H/A'] = df['H/A'].str.strip()

centuries_HA= df['H/A'].value_counts()

fig = px.pie(
    values=centuries_HA.values,
    names=centuries_HA.index,
    color=centuries_HA.index,
    color_discrete_map={
        "Home": "darkblue",
        "Away": "cyan",
        "Neutral": "green"
    }
)

fig.update_traces(
    textinfo='label+percent',
    texttemplate='%{label} (%{percent})',
    textposition='inside'
)

# 🎯 Custom Title Styling
fig.update_layout(
    title={
        'text': "Virat Kohli's Centuries by Venue",
        'font': {'size': 24, 'color': 'black'},
        'x': 0.5,
        'xanchor': 'center'
    }
)

fig.show()

df['Result'] = df['Result'].replace(['Drawn', 'draw', 'tied', 'Tied'], 'Draw')


df['Result'] = df['Result'].str.strip()

result = df['Result'].value_counts()

fig = px.pie(
    values=result.values,
    names=result.index,
    color=result.index,  # This is the KEY to trigger color_discrete_map!
    color_discrete_map={
        "Won": "darkblue",
        "Lost": "royalblue",
        "Draw": "cyan",
        'Lost(D/L)': 'lightgreen',
        "Won(D/L)" : "lightred",
    }
)

fig.update_layout(
    title={
        'text': "Virat Kohli's Centuries by Result",
        'font': {'size': 24, 'color': 'black'},
        'x': 0.5,
        'xanchor': 'center'
    }
)
fig.update_traces(
    textinfo='label+percent',
    texttemplate='%{label} (%{percent})',
    textposition='inside',  # or 'outside' if you want them outside
    insidetextorientation='radial'
)
fig.show()

df['Format'] = df['Format'].str.strip()

format = df['Format'].value_counts()
fig = px.pie(
    values=format.values,
    names=format.index,
    color=format.index,  # This is the KEY to trigger color_discrete_map!
    title="Virat Kohli's Centuries by Format",
    color_discrete_map={
        "ODI": "darkblue",
        "T20I": "cyan",
        "Test": "lightgreen"
    }
)

fig.update_layout(
    title={
        'text': "Virat Kohli's Centuries by Format",
        'font': {'size': 24, 'color': 'black'},
        'x': 0.5,
        'xanchor': 'center'
    }
)

fig.update_traces(
    textinfo='label+percent',
    texttemplate='%{label} (%{percent})',
    textposition='inside',  # or 'outside' if you want them outside
    insidetextorientation='radial'
)
fig.show()

