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
asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv')
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv')
wdi_vars = pd.read_csv('wdi_vars.csv')
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv')
happiness = pd.read_csv('happiness.2015.csv', index_col=False)
happiness.to_csv('happiness.csv')
ti_cpi = pd.read_csv('ti_cpi_2015.csv', index_col=False)
ti_cpi = ti_cpi.drop('country', 1)
ti_cpi.to_csv('ti_cpi.csv')
asylum_seekers = pd.read_csv('asylum_seekers.csv', index_col=False)
idps = pd.read_csv('idps.csv')
refugees = pd.read_csv('refugees.csv', index_col=False)
recognition_rate = pd.read_csv('recognition_rate.csv', index_col=False)
civil_liberties = pd.read_csv('civil_liberties.csv', index_col=False)


# merge in country codes

unhcr_vars = asylum_idps_refugees.merge(recognized_total_decisions, on='country')
unhcr_vars = unhcr_vars.merge(country_iso_2_iso_3, on='country')
unhcr_vars['country_code'] = unhcr_vars['iso_3']

refugees = refugees.merge(country_iso_2_iso_3, on='country')
refugees = refugees.drop('country', 1)
refugees['country_code'] = refugees['iso_3']
refugees.to_csv('refugees.csv')

asylum_seekers = asylum_seekers.merge(country_iso_2_iso_3, on='country')
asylum_seekers = asylum_seekers.drop('country', 1)
asylum_seekers['country_code'] = asylum_seekers['iso_3']
asylum_seekers.to_csv('asylum_seekers.csv')

idps = idps.merge(country_iso_2_iso_3, on='country')
idps = idps.drop('country', 1)
idps['country_code'] = idps['iso_3']
idps.to_csv('idps.csv')

recognition_rate = recognition_rate.merge(country_iso_2_iso_3, on='country')
recognition_rate['country_code'] = recognition_rate['iso_3']
recognition_rate = recognition_rate.drop('country', 1)
recognition_rate.to_csv('recognition_rate.csv')

# create a couple of vars scaled by population

asylum_seekers_pct_pop = asylum_seekers.merge(population, on='country_code')
asylum_seekers_pct_pop['asylum_seekers_pct_pop'] = 100 * asylum_seekers_pct_pop['asylum_seekers'] / asylum_seekers_pct_pop['population']
asylum_seekers_pct_pop = asylum_seekers_pct_pop.drop('population', 1)
asylum_seekers_pct_pop.to_csv('asylum_seekers_pct_pop.csv')

refugees_pct_pop = refugees.merge(population, on='country_code')
refugees_pct_pop['refugees_pct_pop'] = 100 * refugees_pct_pop['refugees'] / refugees_pct_pop['population']
refugees_pct_pop = refugees_pct_pop.drop('population', 1)
refugees_pct_pop.to_csv('refugees_pct_pop.csv')

wdi_vars = wdi_vars.merge(unhcr_vars, on='country_code')
wdi_vars = wdi_vars.merge(asylum_seekers_pct_pop, on='country_code')
wdi_vars = wdi_vars.merge(refugees_pct_pop, on='country_code')


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
#    wdi_vars.merge(df_resid, on='country_code')
    df.to_csv(var + '_resid.csv')
    
# a kludge to fix the 'country' variable in asylum_seekers, ti_cpi, and happiness
#asylum_seekers = pd.read_csv('asylum_seekers.csv')
#asylum_seekers['country'] = asylum_seekers['country_x']
#asylum_seekers.to_csv('asylum_seekers.csv')
#
#happiness = pd.read_csv('happiness.csv')
#happiness['country'] = happiness['country_x']
#happiness.to_csv('happiness.csv')
#
#asylum_seekers_resid = pd.read_csv('asylum_seekers_resid.csv')
#asylum_seekers_resid['country'] = asylum_seekers_resid['country_x']
#asylum_seekers_resid.to_csv('asylum_seekers_resid.csv')
#
#happiness_resid = pd.read_csv('happiness_resid.csv')
#happiness_resid['country'] = happiness_resid['country_x']
#happiness_resid.to_csv('happiness_resid.csv')
#
#ti_cpi = ti_cpi.merge(gdpcap, on='country_code')
#ti_cpi = ti_cpi.drop('gdp_per_capita')
#ti_cpi.to_csv('ti_cpi.csv')

wdi_vars.to_csv('map_data.csv')

    

    





















