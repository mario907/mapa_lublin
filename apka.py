#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

map_parafie = pd.read_excel('clear.xlsx')
map_parafie['size'] = np.repeat(15, len(map_parafie['year']))

customdata = np.dstack((map_parafie['Parafia'], map_parafie['SDDR']))

fig = px.scatter_mapbox(
    map_parafie,
    lat="lat",
    lon="lon",
    hover_name="Parafia",
    hover_data={'SDDR': True, 'lat': False, 'year': False, 'lon': False, 'size': False},
    color='SDDR',
    size='size',
    color_continuous_scale='RdYlGn',
    zoom=8,
    height=800,
    width=800,
    animation_frame="year",
    animation_group='Parafia', 
    range_color=[map_parafie[map_parafie['year'] > 1810]['SDDR'].min(),map_parafie[map_parafie['year'] > 1810]['SDDR'].max()]
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5000
fig.show()

st.plotly_chart(fig, use_container_width = True)

