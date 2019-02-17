#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:45:26 2019

@author: rs
"""

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

os.chdir('/Users/rs/data/geo/multi-maps/maps')

df = pd.read_csv('~/data/geo/multi-maps/data//cleaned_2015/adolescent_fertility_rate.csv')



data = [ dict(
       type = 'choropleth',
       locations = df['country_code'],
       z = df['adolescent_fertility_rate'],
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
           title = 'Adolescent fertilitu'
       ),
   ) ]

layout = dict(
   title = 'Adolescent fertility rate, births per 1,000 women age 15-19<br>World Bank, World Development Indicators',
   geo = dict(
       showframe = False,
       showcoastlines = False,
       projection = dict(
           type = 'kavrayskiy7'
       )
   )
)

fig = dict( data=data, layout=layout )
plotly.offline.plot(fig, filename='adolescent_fertility_rate.html')

    

