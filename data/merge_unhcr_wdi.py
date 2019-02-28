#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

import pandas as pd
import os
import statsmodels.api as sm

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)

# read the csv files of unhcr data corruption perceptions, civil liberties 
# along with gdp per capita, population, and a country_code concordance
gdpcap = pd.read_csv('gdp_per_capita.csv')
population = pd.read_csv('population.csv')
wdi_vars = pd.read_csv('wdi_vars.csv')
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv')
happiness = pd.read_csv('happiness.2015.csv', index_col=0)
happiness = happiness.merge(country_iso_2_iso_3, on = 'country')
happiness.to_csv('happiness.csv')
ti_cpi = pd.read_csv('ti_cpi_2015.csv', index_col=0)
ti_cpi = ti_cpi.drop('country', 1)
ti_cpi.to_csv('ti_cpi.csv')
asylum_seekers = pd.read_csv('asylum_seekers.csv', index_col=0)
idps = pd.read_csv('idps.csv')
refugees = pd.read_csv('refugees.csv', index_col=0)
recognition_rate = pd.read_csv('recognition_rate.csv', index_col=0)
civil_liberties = pd.read_csv('civil_liberties.csv', index_col=False)
civil_liberties = civil_liberties.drop('country_y', 1)



# create a couple of vars scaled by population

asylum_seekers_pct_pop = asylum_seekers.merge(population, on='country_code')
asylum_seekers_pct_pop['asylum_seekers_pct_pop'] = 100 * asylum_seekers_pct_pop['asylum_seekers'] / asylum_seekers_pct_pop['population']
asylum_seekers_pct_pop = asylum_seekers_pct_pop.drop('population', 1)
asylum_seekers_pct_pop.to_csv('asylum_seekers_pct_pop.csv')

refugees_pct_pop = refugees.merge(population, on='country_code')
refugees_pct_pop['refugees_pct_pop'] = 100 * refugees_pct_pop['refugees'] / refugees_pct_pop['population']
refugees_pct_pop = refugees_pct_pop.drop('population', 1)
refugees_pct_pop.to_csv('refugees_pct_pop.csv')

# merge non-WDI vars into wdi_vars

wdi_vars = wdi_vars.merge(asylum_seekers_pct_pop, on='country_code')
wdi_vars = wdi_vars.merge(refugees_pct_pop, on='country_code')
wdi_vars = wdi_vars.merge(idps, on='country_code')
wdi_vars = wdi_vars.merge(recognition_rate, on='country_code')
#wdi_vars - wdi_vars.merge(civil_liberties, on='country_code')
wdi_vars = wdi_vars.merge(happiness, on='country_code')
wdi_vars = wdi_vars.merge(ti_cpi, on='country_code')


filenames = pd.DataFrame(wdi_vars.columns.tolist())
filenames.to_csv('map_data_varnames.csv')

# run loess regressions
# note: merging with gdp per capita and then dropping gdp per capita is
# for the purpose of bringing back in the country_codes that were dropped
# in order to do the loess regressions and merge data with residuals
newvars = ['asylum_seekers', 'idps', 'refugees', 'recognition_rate', 'happiness', 'ti_cpi', 'civil_liberties', 'asylum_seekers_pct_pop', 'refugees_pct_pop' ]

lowess = sm.nonparametric.lowess

for var in newvars:
    df = pd.read_csv(var + '.csv', index_col=False)
    df = df.merge(gdpcap, on='country_code')
    model = lowess(df[var], df['gdp_per_capita'], return_sorted=False)
    df = df.drop('gdp_per_capita', 1)
    df.to_csv(var + '.csv')
    df[var + '_resid'] = df[var] - model
    wdi_vars = wdi_vars.merge(df, on='country_code')
    df.to_csv(var + '_resid.csv')

# an afterthought : make net fdi as % of gdp

netfdi = pd.read_csv('net_fdi.csv')
gdpcap = pd.read_csv('gdp_per_capita.csv')
pop = pd.read_csv('population.csv')
df = netfdi.merge(gdpcap, on='country_code')
df = df.merge(pop, on='country_code')
df['gdp'] = df.gdp_per_capita * df.population
df['net_fdi_pct_gdp'] = 100 * df.net_fdi / df.gdp
df = df.drop('population', 1)
df = df.drop('gdp', 1)
df = df.drop('gdp_per_capita', 1)
df = df.drop('country_x', 1)
df = df.drop('country_y', 1)
df = df.drop('net_fdi', 1)
df.to_csv('net_fdi_pct_gdp.csv')

wdi_vars = wdi_vars.merge(df, on='country_code')
wdi_vars.to_csv('map_data.csv')

    

    





















