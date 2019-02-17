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

# maternal mortality rate per 100000 live births
maternal_mortality_rate = requests.get('http://api.worldbank.org/v2/en/indicator/SH.STA.MMRT?downloadformat=csv')
maternal_mortality_rate_zip = zipfile.ZipFile(io.BytesIO(maternal_mortality_rate.content))
names = zipfile.ZipFile.namelist(maternal_mortality_rate_zip)
maternal_mortality_rate_csv = pd.read_csv(zipfile.ZipFile.extract(maternal_mortality_rate_zip, names[1]), header=2)
maternal_mortality_rate_csv.to_csv('maternal_mortality_rate.csv')

#life expectancy at birth
life_expectancy = requests.get('http://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv')
life_expectancy_zip = zipfile.ZipFile(io.BytesIO(life_expectancy.content))
names = zipfile.ZipFile.namelist(life_expectancy_zip)
life_expectancy_csv = pd.read_csv(zipfile.ZipFile.extract(life_expectancy_zip, names[1]), header=2)
life_expectancy_csv.to_csv('life_expectancy.csv')

# hiv prevalence
hiv_prevalence = requests.get('http://api.worldbank.org/v2/en/indicator/SH.DYN.AIDS.ZS?downloadformat=csv')
hiv_prevalence_zip = zipfile.ZipFile(io.BytesIO(hiv_prevalence.content))
names = zipfile.ZipFile.namelist(hiv_prevalence_zip)
hiv_prevalence_csv = pd.read_csv(zipfile.ZipFile.extract(hiv_prevalence_zip, names[1]), header=2)
hiv_prevalence_csv.to_csv('hiv_prevalence.csv')


# urban population, percent of population
urbpop = requests.get('http://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv')
urbpop_zip = zipfile.ZipFile(io.BytesIO(urbpop.content))
names = zipfile.ZipFile.namelist(urbpop_zip)
urbpop_csv = pd.read_csv(zipfile.ZipFile.extract(urbpop_zip, names[1]), header=2)
urbpop_csv.to_csv('urbpop.csv')


# gross domestic product per capita, current USD at PPP
gdp_per_capita = requests.get('http://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv')
gdp_per_capita_zip = zipfile.ZipFile(io.BytesIO(gdp_per_capita.content))
names = zipfile.ZipFile.namelist(gdp_per_capita_zip)
gdp_per_capita_csv = pd.read_csv(zipfile.ZipFile.extract(gdp_per_capita_zip, names[1]), header=2)
gdp_per_capita_csv.to_csv('gdp_per_capita.csv')

# share of income held by lowest 20% of population
lowest_twenty_income_share = requests.get('http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.20?downloadformat=csv')
lowest_twenty_income_share_zip = zipfile.ZipFile(io.BytesIO(lowest_twenty_income_share.content))
names = zipfile.ZipFile.namelist(lowest_twenty_income_share_zip)
lowest_twenty_income_share_csv = pd.read_csv(zipfile.ZipFile.extract(lowest_twenty_income_share_zip, names[1]), header=2)
lowest_twenty_income_share_csv.to_csv('lowest_twenty_income_share.csv')

# net official development assistance as percent of gross national income
oda_pct_of_gni = requests.get('http://api.worldbank.org/v2/en/indicator/DT.ODA.ODAT.GN.ZS?downloadformat=csv')
oda_pct_of_gni_zip = zipfile.ZipFile(io.BytesIO(oda_pct_of_gni.content))
names = zipfile.ZipFile.namelist(oda_pct_of_gni_zip)
oda_pct_of_gni_csv = pd.read_csv(zipfile.ZipFile.extract(oda_pct_of_gni_zip, names[1]), header=2)
oda_pct_of_gni_csv.to_csv('oda_pct_of_gni.csv')

# net migration
net_migration = requests.get('http://api.worldbank.org/v2/en/indicator/SM.POP.NETM?downloadformat=csv')
net_migration_zip = zipfile.ZipFile(io.BytesIO(net_migration.content))
names = zipfile.ZipFile.namelist(net_migration_zip)
net_migration_csv = pd.read_csv(zipfile.ZipFile.extract(net_migration_zip, names[1]), header=2)
net_migration_csv.to_csv('net_migration.csv')

# poverty headcount ratio, $1.90 at 2011 PPP
poverty_headcount_ratio_190_2011_ppp = requests.get('http://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv')
poverty_headcount_ratio_190_2011_ppp_zip = zipfile.ZipFile(io.BytesIO(poverty_headcount_ratio_190_2011_ppp.content))
names = zipfile.ZipFile.namelist(poverty_headcount_ratio_190_2011_ppp_zip)
poverty_headcount_ratio_190_2011_ppp_csv = pd.read_csv(zipfile.ZipFile.extract(poverty_headcount_ratio_190_2011_ppp_zip, names[1]), header=2)
poverty_headcount_ratio_190_2011_ppp_csv.to_csv('poverty_headcount_ratio_190_2011_ppp.csv')

# access to electricity, % of population
access_to_electricity_pct_of_population = requests.get('http://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv')
access_to_electricity_pct_of_population_zip = zipfile.ZipFile(io.BytesIO(access_to_electricity_pct_of_population.content))
names = zipfile.ZipFile.namelist(access_to_electricity_pct_of_population_zip)
access_to_electricity_pct_of_population_csv = pd.read_csv(zipfile.ZipFile.extract(access_to_electricity_pct_of_population_zip, names[1]), header=2)
access_to_electricity_pct_of_population_csv.to_csv('access_to_electricity_pct_of_population.csv')

# CO2 emissions, metric tons per capita
co2_tons_per_capita = requests.get('http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv')
co2_tons_per_capita_zip = zipfile.ZipFile(io.BytesIO(co2_tons_per_capita.content))
names = zipfile.ZipFile.namelist(co2_tons_per_capita_zip)
co2_tons_per_capita_csv = pd.read_csv(zipfile.ZipFile.extract(co2_tons_per_capita_zip, names[1]), header=2)
co2_tons_per_capita_csv.to_csv('co2_tons_per_capita.csv')

# mortality rate under 5 per 1000 live births
mortality_under_5_per_1000_live_births = requests.get('http://api.worldbank.org/v2/en/indicator/SH.DYN.MORT?downloadformat=csv')
mortality_under_5_per_1000_live_births_zip = zipfile.ZipFile(io.BytesIO(mortality_under_5_per_1000_live_births.content))
names = zipfile.ZipFile.namelist(mortality_under_5_per_1000_live_births_zip)
mortality_under_5_per_1000_live_births_csv = pd.read_csv(zipfile.ZipFile.extract(mortality_under_5_per_1000_live_births_zip, names[1]), header=2)
mortality_under_5_per_1000_live_births_csv.to_csv('mortality_under_5_per_1000_live_births.csv')

# energy use per capita (kg equiv oil)
energy_use_per_capita = requests.get('http://api.worldbank.org/v2/en/indicator/EG.USE.PCAP.KG.OE?downloadformat=csv')
energy_use_per_capita_zip = zipfile.ZipFile(io.BytesIO(energy_use_per_capita.content))
names = zipfile.ZipFile.namelist(energy_use_per_capita_zip)
energy_use_per_capita_csv = pd.read_csv(zipfile.ZipFile.extract(energy_use_per_capita_zip, names[1]), header=2)
energy_use_per_capita_csv.to_csv('energy_use_per_capita.csv')

# remittances received, current USD
remittances = requests.get('http://api.worldbank.org/v2/en/indicator/BX.TRF.PWKR.CD.DT?downloadformat=csv')
remittances_zip = zipfile.ZipFile(io.BytesIO(remittances.content))
names = zipfile.ZipFile.namelist(remittances_zip)
remittances_csv = pd.read_csv(zipfile.ZipFile.extract(remittances_zip, names[1]), header=2)
remittances_csv.to_csv('remittances.csv')

# revenue, % of gdp
revenue_pct_gdp = requests.get('http://api.worldbank.org/v2/en/indicator/GC.REV.XGRT.GD.ZS?downloadformat=csv')
revenue_pct_gdp_zip = zipfile.ZipFile(io.BytesIO(revenue_pct_gdp.content))
names = zipfile.ZipFile.namelist(revenue_pct_gdp_zip)
revenue_pct_gdp_csv = pd.read_csv(zipfile.ZipFile.extract(revenue_pct_gdp_zip, names[1]), header=2)
revenue_pct_gdp_csv.to_csv('revenue_pct_gdp.csv')

# govt expenditure on education, % of GDP
govt_exp_educ_pct_gdp = requests.get('http://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GD.ZS?downloadformat=csv')
govt_exp_educ_pct_gdp_zip = zipfile.ZipFile(io.BytesIO(govt_exp_educ_pct_gdp.content))
names = zipfile.ZipFile.namelist(govt_exp_educ_pct_gdp_zip)
govt_exp_educ_pct_gdp_csv = pd.read_csv(zipfile.ZipFile.extract(govt_exp_educ_pct_gdp_zip, names[1]), header=2)
govt_exp_educ_pct_gdp_csv.to_csv('govt_exp_educ_pct_gdp.csv')

# female literacy, over 15, %
female_literacy_pct = requests.get('http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.FE.ZS?downloadformat=csv')
female_literacy_pct_zip = zipfile.ZipFile(io.BytesIO(female_literacy_pct.content))
names = zipfile.ZipFile.namelist(female_literacy_pct_zip)
female_literacy_pct_csv = pd.read_csv(zipfile.ZipFile.extract(female_literacy_pct_zip, names[1]), header=2)
female_literacy_pct_csv.to_csv('female_literacy_pct.csv')

# external debt, % of GNI
external_debt_pct_GNI = requests.get('http://api.worldbank.org/v2/en/indicator/DT.DOD.DECT.GN.ZS?downloadformat=csv')
external_debt_pct_GNI_zip = zipfile.ZipFile(io.BytesIO(external_debt_pct_GNI.content))
names = zipfile.ZipFile.namelist(external_debt_pct_GNI_zip)
external_debt_pct_GNI_csv = pd.read_csv(zipfile.ZipFile.extract(external_debt_pct_GNI_zip, names[1]), header=2)
external_debt_pct_GNI_csv.to_csv('external_debt_pct_GNI.csv')

# FDI, net, current USD
fdi_net_current_usd = requests.get('http://api.worldbank.org/v2/en/indicator/BX.KLT.DINV.CD.WD?downloadformat=csv')
fdi_net_current_usd_zip = zipfile.ZipFile(io.BytesIO(fdi_net_current_usd.content))
names = zipfile.ZipFile.namelist(fdi_net_current_usd_zip)
fdi_net_current_usd_csv = pd.read_csv(zipfile.ZipFile.extract(fdi_net_current_usd_zip, names[1]), header=2)
fdi_net_current_usd_csv.to_csv('fdi_net_current_usd.csv')

# strength of legal rights, 0=low, 12=high
strength_legal_rights_0_12 = requests.get('http://api.worldbank.org/v2/en/indicator/IC.LGL.CRED.XQ?downloadformat=csv')
strength_legal_rights_0_12_zip = zipfile.ZipFile(io.BytesIO(strength_legal_rights_0_12.content))
names = zipfile.ZipFile.namelist(strength_legal_rights_0_12_zip)
strength_legal_rights_0_12_csv = pd.read_csv(zipfile.ZipFile.extract(strength_legal_rights_0_12_zip, names[1]), header=2)
strength_legal_rights_0_12_csv.to_csv('strength_legal_rights_0_12.csv')

# adolescent fertility rate, 15-19, per 1000 live births
adolescent_fertility_rate = requests.get('http://api.worldbank.org/v2/en/indicator/SP.ADO.TFRT?downloadformat=csv')
adolescent_fertility_rate_zip = zipfile.ZipFile(io.BytesIO(adolescent_fertility_rate.content))
names = zipfile.ZipFile.namelist(adolescent_fertility_rate_zip)
adolescent_fertility_rate_csv = pd.read_csv(zipfile.ZipFile.extract(adolescent_fertility_rate_zip, names[1]), header=2)
adolescent_fertility_rate_csv.to_csv('adolescent_fertility_rate.csv')

# fertility rate, births per woman
fertility_rate = requests.get('http://api.worldbank.org/v2/en/indicator/SP.DYN.TFRT.IN?downloadformat=csv')
fertility_rate_zip = zipfile.ZipFile(io.BytesIO(fertility_rate.content))
names = zipfile.ZipFile.namelist(fertility_rate_zip)
fertility_rate_csv = pd.read_csv(zipfile.ZipFile.extract(fertility_rate_zip, names[1]), header=2)
fertility_rate_csv.to_csv('fertility_rate.csv')

# female employment, % of total labor force
female_employment_pct_of_total = requests.get('http://api.worldbank.org/v2/en/indicator/SL.TLF.TOTL.FE.ZS?downloadformat=csv')
female_employment_pct_of_total_zip = zipfile.ZipFile(io.BytesIO(female_employment_pct_of_total.content))
names = zipfile.ZipFile.namelist(female_employment_pct_of_total_zip)
female_employment_pct_of_total_csv = pd.read_csv(zipfile.ZipFile.extract(female_employment_pct_of_total_zip, names[1]), header=2)
female_employment_pct_of_total_csv.to_csv('female_employment_pct_of_total.csv')

