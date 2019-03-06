#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:56:04 2019

@author: rs
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


os.chdir('/Users/rs/data/geo/multi-maps')

datafile = os.path.expanduser('~/data/geo/multi-maps/poc.asylum.seekers.2015.csv')
shapefile = os.path.expanduser('~/data/geo//mmr/TM_WORLD_BORDERS/')

colors = 9
cmap = 'Blues'
figsize = (16, 10)
year = '2015'
cols = ['Country Name', 'Country Code', year]
title = f'Asylum seekers, {year}'

description = '''Asylum seekers. Source: unhcr.org, Population Statistics'''

gdf = gpd.read_file(shapefile)[['ISO3', 'geometry']].to_crs('+proj=robin')
gdf.sample(5)

df = pd.read_csv(datafile)
df.sample(5)
merged = gdf.merge(df, left_on='ISO3', right_on='country.code')
merged.describe()

ax = merged.dropna().plot(column='asylum.seekers', cmap=cmap, figsize=figsize, scheme='fisher_jenks', k=colors, legend=True)

merged[merged.isna().any(axis=1)].plot(ax=ax, color='#fafafa', hatch='///')

ax.set_title(title, fontdict={'fontsize': 20}, loc='center')
ax.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')

ax.set_axis_off()
ax.set_xlim([-1.5e7, 1.7e7])
ax.get_legend().set_bbox_to_anchor((.12, .4))
ax.get_figure()

