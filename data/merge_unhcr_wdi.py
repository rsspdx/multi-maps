#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

# merges proper country codes into happiness.csv file
# generates per-capita asylum seekers and refugees
# generates net fdi as percent of GDP
# estimates lowess regressions, saves residuals in '*_resid.csv' files
# merges these and wdi_vars, saves map_data.csv


# three important kludges:
    # happiness (World Database of Happiness self-reported happiness, 1-10, 10 high)
    # ti_cpi (Transparency International corruption perception index)
    # civil_liberties (Freedom House civil liberties, 1-7, 1 high)
# all those are downloaded separately and manipulated outside of python

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

happiness = pd.read_csv('happiness.csv', index_col=False)

ti_cpi = pd.read_csv('ti_cpi.csv', index_col=False)

asylum_seekers = pd.read_csv('asylum_seekers.csv', index_col=False)

idps = pd.read_csv('idps.csv', index_col=False)

refugees = pd.read_csv('refugees.csv', index_col=False)

recognition_rate = pd.read_csv('recognition_rate.csv', index_col=False)

civil_liberties = pd.read_csv('civil_liberties.csv', index_col=False)


# create a couple of vars scaled by population

asylum_seekers_pct_pop = asylum_seekers.merge(population, on='country_code')
asylum_seekers_pct_pop['asylum_seekers_pct_pop'] = 100 * asylum_seekers_pct_pop['asylum_seekers'] / asylum_seekers_pct_pop['population']
asylum_seekers_pct_pop = asylum_seekers_pct_pop.drop('population', 1)
asylum_seekers_pct_pop.to_csv('asylum_seekers_pct_pop.csv')

refugees_pct_pop = refugees.merge(population, on='country_code')
refugees_pct_pop['refugees_pct_pop'] = 100 * refugees_pct_pop['refugees'] / refugees_pct_pop['population']
refugees_pct_pop = refugees_pct_pop.drop('population', 1)
refugees_pct_pop.to_csv('refugees_pct_pop.csv')

# create fdi as pct of gdp
fdi_net_current_usd = pd.read_csv('fdi_net_current_usd.csv')
fdi_net_pct_gdp = fdi_net_current_usd.merge(gdpcap, on=['country', 'country_code'])
fdi_net_pct_gdp = fdi_net_pct_gdp.merge(population, on=['country', 'country_code'])
fdi_net_pct_gdp['gdp'] = fdi_net_pct_gdp.gdp_per_capita * fdi_net_pct_gdp.population
fdi_net_pct_gdp['fdi_net_pct_gdp'] = 100 * fdi_net_pct_gdp.fdi_net_current_usd / fdi_net_pct_gdp.gdp
fdi_net_pct_gdp = fdi_net_pct_gdp.drop('gdp', 1)
fdi_net_pct_gdp = fdi_net_pct_gdp.drop('population', 1)
fdi_net_pct_gdp = fdi_net_pct_gdp.drop('fdi_net_current_usd', 1)
fdi_net_pct_gdp = fdi_net_pct_gdp.drop('gdp_per_capita', 1)
fdi_net_pct_gdp.to_csv('fdi_net_pct_gdp.csv')

# merge non-WDI vars into wdi_vars

wdi_vars = wdi_vars.merge(asylum_seekers_pct_pop, on='country_code')
wdi_vars = wdi_vars.merge(refugees_pct_pop, on='country_code')
wdi_vars = wdi_vars.merge(idps, on='country_code')
wdi_vars = wdi_vars.merge(recognition_rate, on='country_code')
#wdi_vars - wdi_vars.merge(civil_liberties, on='country_code')
wdi_vars = wdi_vars.merge(happiness, on='country_code')
wdi_vars = wdi_vars.merge(ti_cpi, on='country_code')
wdi_vars = wdi_vars.merge(fdi_net_pct_gdp, on=['country_code', 'country'])

filenames = pd.DataFrame(wdi_vars.columns.tolist())
filenames.to_csv('map_data_varnames.csv')

# run loess regressions
# note: merging with gdp per capita and then dropping gdp per capita is
# for the purpose of bringing back in the country_codes that were dropped
# in order to do the loess regressions and merge data with residuals
newvars = ['asylum_seekers', 'idps', 'refugees', 'recognition_rate', 'happiness', 'ti_cpi', 'civil_liberties', 'asylum_seekers_pct_pop', 'refugees_pct_pop' , 'fdi_net_pct_gdp']

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


wdi_vars.to_csv('map_data.csv')
