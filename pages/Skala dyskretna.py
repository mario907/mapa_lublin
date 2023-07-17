import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

map_parafie = pd.read_excel(r'clear.xlsx')

map_col = {"Extreme-": "#ee202a", 
            "Anomalous-": "#f48929", 
            "Very-": "#f7e829", 
            "Normal": "#ffffff", 
            "Very+": "#2fbebb", 
            "Anomalous+": "#006eb8", 
            "Extreme+": "#2d3795"}

customdata = np.dstack((map_parafie['Parafia'], map_parafie['SDDR']))

fig = px.scatter_mapbox(
    map_parafie[map_parafie['year'] > 1810],
    lat="lat",
    lon="lon",
    hover_name="Parafia",
    color = 'cat_SDDR',
    size = 'size',
    hover_data={'SDDR': True, 'lat': False, 'year': False, 'lon': False, 'size': False},
    #color_discrete_sequence=["#ee202a", "#f48929","#f7e829","#ffffff","#2fbebb", "#006eb8","#2d3795"],
    color_discrete_map=map_col,
    category_orders={"cat_SDDR": ["Extreme-", "Anomalous-", "Very-", "Normal", "Very+", "Anomalous+", "Extreme+"]},
    zoom=8,
    height=800,
    animation_frame="year",
    animation_group = 'Parafia',
    title="year"
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
