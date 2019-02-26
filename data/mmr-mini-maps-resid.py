#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:41:02 2019

@author: rs
"""

import os
import plotly
import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

os.chdir('/Users/rs/multi-maps/data')

filename = 'maternal_mortality_rate_resid.csv'
df = pd.read_csv(filename)

data = [ dict(
       type = 'choropleth',
       locations = df['country_code'],
       z = df['maternal_mortality_rate_resid'],
       text = df['country'],
       colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
           [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
#        colorscale = 'Blues',
       autocolorscale = False,
       reversescale = True,
       showscale = False,
       marker = dict(
           line = dict (
               color = 'rgb(180,180,180)',
               width = 0.5
           )
       ),
#        tick0 = 0,
       zmin = 0,
#        dtick = 1000,
#       colorbar = dict(
##            autotick = False,
##            tickprefix = '$',
#           title = vars[i]['short_name']
#       ),
   ) ]

layout = dict(
   title = 'Maternal Mortality Rate, Residuals' + '<br>' + 'World Bank, World Development Indicators',
   geo = dict(
       showframe = False,
       showcoastlines = False,
       projection = dict(
           type = 'kavrayskiy7'
       )
   )
)

fig = dict( data=data, layout=layout )
f = open('mmr-mini-map-resid.div', 'w+')
f.write(plotly.offline.plot(fig, output_type='div', include_plotlyjs=False, auto_open=False))
f.close()
