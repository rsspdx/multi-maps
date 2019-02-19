#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

import pandas as pd
import os

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)


asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv', index_col=0)
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv', index_col=0)
wdi_vars = pd.read_csv('wdi_vars.csv', index_col=0)
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv', index_col=0)
happiness = pd.read_csv('happiness.2015.csv', index_col=0)
ti_cpi = pd.read_csv('ti_cpi_2015.csv')

unhcr_vars = asylum_idps_refugees.merge(recognized_total_decisions, on='country')
unhcr_vars = unhcr_vars.merge(country_iso_2_iso_3, on='country')


wdi_vars = wdi_vars.merge(unhcr_vars, left_on='country_code', right_on='iso_3')


wdi_vars['refugees_per_pop'] = wdi_vars['refugees'] / wdi_vars['population']
wdi_vars['asylum_seekers_per_pop'] = wdi_vars['asylum_seekers'] / wdi_vars['population']
wdi_vars = wdi_vars.merge(happiness, on='country_code')
wdi_vars = wdi_vars.merge(ti_cpi, on='country_code')



wdi_vars.to_csv('map_data.csv')

filenames = pd.DataFrame(wdi_vars.columns.tolist())
filenames.to_csv('map_data_varnames.csv')


asylum_seekers = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.asylum_seekers)
asylum_seekers.rename(columns = {0: 'country', 1: 'country_code', 2: 'asylum_seekers'})
asylum_seekers.to_csv('asylum_seekers.csv')

idps = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.idps)
idps.csv = idps.to_csv('idps.csv')

refugees = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.refugees)
refugees.to_csv('refugees.csv')

recognition_rate = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.recognition_rate)
recognition_rate.to_csv('recognition_rate.csv')

refugees_per_pop = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.refugees_per_pop)
refugees_per_pop.to_csv('refugees_per_pop.csv')

asylum_seekers_per_pop = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.asylum_seekers_per_pop)
asylum_seekers_per_pop.to_csv('asylum_seekers_per_pop.csv')

happiness = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.happiness)
happiness.to_csv('happiness.csv')

ti_cpi  = pd.DataFrame(wdi_vars.country, wdi_vars.country_code, wdi_vars.ti_cpi)
ti_cpi.to_csv('ti_cpi.csv')

newvars = ['asylum_seekers', 'idps', 'refugees', 'recognition_rate', 'refugees_per_pop', 'asylum_seekers_per_pop', 'happiness']


for i in range(len(newvars)):
    df = pd.read_csv(newvars[i] + '.csv', index_col=0)
    df = df.merge(gdpcap, on=['country', 'country_code'])
    df = df.dropna()
    model = lowess(df[vars[i]['name']], df.gdp_per_capita, return_sorted=False)
    df[vars[i]['name'] + '_resid'] = df[vars[i]['name']] - model
    df = df.drop(columns = [vars[i]['name'], 'gdp_per_capita'])
    df.to_csv(vars[i]['name'] + '_resid.csv')
    