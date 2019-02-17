#!/usr/bin/env pygeo
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 07:09:57 2019

@author: rs
"""

import requests
import zipfile
import io
import os
import pandas as pd

os.chdir('/Users/rs/data/geo/multi-maps/data')

# download zip archives of csv data files
# unzip them
# write to csv for use in R

data_dictionary = {
# maternal mortality rate per 100000 live births
'maternal_mortality_rate' : 'http://api.worldbank.org/v2/en/indicator/SH.STA.MMRT?downloadformat=csv',

#life expectancy at birth
'life_expectancy' : 'http://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv',

# hiv prevalence
'hiv_prevalence' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.AIDS.ZS?downloadformat=csv',

# urban population, percent of population
'urbpop' : 'http://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv',

# gross domestic product per capita, current USD at PPP
'gdp_per_capita' : 'http://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv',

# share of income held by lowest 20% of population
'lowest_twenty_income_share' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.20?downloadformat=csv',

# net official development assistance as percent of gross national income
'oda_pct_of_gni' : 'http://api.worldbank.org/v2/en/indicator/DT.ODA.ODAT.GN.ZS?downloadformat=csv',

# net migration
'net_migration' : 'http://api.worldbank.org/v2/en/indicator/SM.POP.NETM?downloadformat=csv',

# poverty headcount ratio, $1.90 at 2011 PPP
'poverty_headcount_ratio_190_2011_ppp' : 'http://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv',

# access to electricity, % of population
'access_to_electricity_pct_of_population' : 'http://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv',

# CO2 emissions, metric tons per capita
'co2_tons_per_capita' : 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv',

# mortality rate under 5 per 1000 live births
'mortality_under_5_per_1000_live_births' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.MORT?downloadformat=csv',

# energy use per capita (kg equiv oil)
'energy_use_per_capita' : 'http://api.worldbank.org/v2/en/indicator/EG.USE.PCAP.KG.OE?downloadformat=csv',

# remittances received, current USD
'remittances' : 'http://api.worldbank.org/v2/en/indicator/BX.TRF.PWKR.CD.DT?downloadformat=csv',

# revenue, % of gdp
'revenue_pct_gdp' : 'http://api.worldbank.org/v2/en/indicator/GC.REV.XGRT.GD.ZS?downloadformat=csv',

# govt expenditure on education, % of GDP
'govt_exp_educ_pct_gdp' : 'http://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GD.ZS?downloadformat=csv',

# female literacy, over 15, %
'female_literacy_pct' : 'http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.FE.ZS?downloadformat=csv',

# external debt, % of GNI
'external_debt_pct_GNI' : 'http://api.worldbank.org/v2/en/indicator/DT.DOD.DECT.GN.ZS?downloadformat=csv',

# FDI, net, current USD
'fdi_net_current_usd' : 'http://api.worldbank.org/v2/en/indicator/BX.KLT.DINV.CD.WD?downloadformat=csv',

# strength of legal rights, 0=low, 12=high
'strength_legal_rights_0_12' : 'http://api.worldbank.org/v2/en/indicator/IC.LGL.CRED.XQ?downloadformat=csv',

# adolescent fertility rate, 15-19, per 1000 live births
'adolescent_fertility_rate' : 'http://api.worldbank.org/v2/en/indicator/SP.ADO.TFRT?downloadformat=csv',

# fertility rate, births per woman
'fertility_rate' : 'http://api.worldbank.org/v2/en/indicator/SP.DYN.TFRT.IN?downloadformat=csv',

# female employment, % of total labor force
'female_employment_pct_of_total' : 'http://api.worldbank.org/v2/en/indicator/SL.TLF.TOTL.FE.ZS?downloadformat=csv',

}

for k, v in data_dictionary.items():
    data = requests.get(v)
    zip = zipfile.ZipFile(io.BytesIO(data.content))
    names = zipfile.ZipFile.namelist(zip)
    csv = pd.read_csv(zipfile.ZipFile.extract(zip, names[1]), header=2)
    csv.to_csv(k+'.csv')