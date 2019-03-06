#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:34:23 2019

@author: rs
"""

import os
import plotly
import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

os.chdir('/Users/rs/data/geo/multi-maps')

df = pd.read_csv('~/data/geo/multi-maps/mmr.2015.csv')


data = [ dict(
       type = 'choropleth',
       locations = df['country.code'],
       z = df['mmr'],
       text = df['country'],
       colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
           [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
#        colorscale = 'Blues',
       autocolorscale = False,
       reversescale = True,
       marker = dict(
           line = dict (
               color = 'rgb(180,180,180)',
               width = 0.5
           )
       ),
#        tick0 = 0,
       zmin = 0,
#        dtick = 1000,
       colorbar = dict(
#            autotick = False,
#            tickprefix = '$',
           title = 'Maternal deaths per 100,000 live births'
       ),
   ) ]

layout = dict(
   title = 'Maternal mortality<br>World Bank, World Development Indicators',
   geo = dict(
       showframe = False,
       showcoastlines = False,
       projection = dict(
           type = 'kavrayskiy7'
       )
   )
)

fig = dict( data=data, layout=layout )
plotly.offline.plot(fig)
#url = py.plot(fig, filename='d3-world-map')