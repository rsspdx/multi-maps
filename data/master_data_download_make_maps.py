#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:01:16 2019

@author: rs
"""

#!/usr/bin/env pygeo
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 07:09:57 2019

@author: rs
"""

# download two UNHCR data sets (Persons of Concern and Asylum Seekers), which are byte objects
# decode them to strings and chop off extraneous stuff at the beginning
# split those strings into lines
# put those in a list -- first element is varnames
# zip them together to create DataFrames
# manipulate those and save:

    # asylum_seekers.csv
    # idps.csv
    # refugees.csv
    # recognition_rate.csv
    
import requests
import os
import pandas as pd

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)

# read country_code concordance
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv', index_col = False)

# download UNHCR data - Population Statistics - Persons of Concern
poc = requests.get('http://popstats.unhcr.org/en/persons_of_concern.csv')
# decode it to a string
poc_string = poc.content.decode('utf-8', errors='ignore')[188:]
# remove commas from two country names
poc_string = poc_string.replace('"China, Hong Kong SAR"', 'China HK')
poc_string = poc_string.replace('"China, Macao SAR"', 'China Macao')
# split it to a list, split rows by commas
poc_string = poc_string.split('\r\n')
poc_list = []
for i in range(len(poc_string)-1):
    poc_list.append(poc_string[i].split(','))
# get first row as varnames
header = poc_list[0]
# zip varnames together with the data to create a spreadsheet-like list of dicts
poc_dict_list = []
for i in range(len(poc_list)-1):
    poc_dict_list.append(dict(zip(header, poc_list[i])))
# turn it into a pandas data frame
poc_df = pd.DataFrame(poc_dict_list)
# keep year 2015 only
poc_df_2015 = poc_df[poc_df['Year'] == '2015']
poc_df_2015.to_csv('poc_2015.csv')
# give the variables usable names
poc_df_2015 = poc_df_2015.rename(index=str, columns={
        'Asylum-seekers (pending cases)' : 'asylum_seekers',
        'Country / territory of asylum/residence' : 'country',
        'Internally displaced persons (IDPs)' : 'idps',
        'Origin' : 'country_of_origin',
        'Others of concern' : 'others_of_concern',
        'Refugees (incl. refugee-like situations)' : 'refugees',
        'Returned IDPs' : 'returned_idps',
        'Returned refugees' : 'returned_refugees',
        'Stateless persons' : 'stateless_persons',
        'Total Population' : 'total_population',
        'Year' : 'year'
        })
    
# get sums of asylum_seekers, idps, refugees -- first need to convert these to ints
poc_df_2015.asylum_seekers = poc_df_2015.asylum_seekers[poc_df_2015.asylum_seekers != ''].astype('int32')
poc_df_2015.idps = poc_df_2015.idps[poc_df_2015.idps != ''].astype('int32')
poc_df_2015.refugees = poc_df_2015.refugees[poc_df_2015.refugees != ''].astype('int32')

asylum_seekers = pd.DataFrame(poc_df_2015.groupby('country').asylum_seekers.sum())
idps = pd.DataFrame(poc_df_2015.groupby('country').idps.sum())
refugees = pd.DataFrame(poc_df_2015.groupby('country').refugees.sum())

# merge to get country_codes
asylum_seekers = asylum_seekers.merge(country_iso_2_iso_3, on='country')
idps = idps.merge(country_iso_2_iso_3, on='country')
refugees =  refugees.merge(country_iso_2_iso_3, on='country')

# drop country names and extraneous vars
asylum_seekers = asylum_seekers.drop('country', 1)
asylum_seekers = asylum_seekers.drop('iso_2', 1)
asylum_seekers['country_code'] = asylum_seekers.iso_3
asylum_seekers = asylum_seekers.drop('iso_3', 1)

idps = idps.drop('country', 1)
idps = idps.drop('iso_2', 1)
idps['country_code'] = idps.iso_3
idps = idps.drop('iso_3', 1)

refugees = refugees.drop('country', 1)
refugees = refugees.drop('iso_2', 1)
refugees['country_code'] = refugees.iso_3
refugees = refugees.drop('iso_3', 1)

# save to csv
asylum_seekers.to_csv('asylum_seekers.csv')
idps.to_csv('idps.csv')
refugees.to_csv('refugees.csv')

# ------------------
# ------------------

# download UNHCR data - Population Statistics - Asylum Seekers
asylum = requests.get('http://popstats.unhcr.org/en/asylum_seekers.csv')
# decode it to a string
asylum_string = asylum.content.decode('utf-8', errors='ignore')[197:]
# remove commas from two country names
asylum_string = asylum_string.replace('"China, Hong Kong SAR"', 'China HK')
asylum_string = asylum_string.replace('"China, Macao SAR"', 'China Macao')
# split it to a list, split rows by commas
asylum_string = asylum_string.split('\r\n')
asylum_list = []
for i in range(len(asylum_string)-1):
    asylum_list.append(asylum_string[i].split(','))
# get first row as varnames
header = asylum_list[0]
# zip varnames together with data to create a spreadsheet-like list of dicts
asylum_dict_list = []
for i in range(len(asylum_list)-1):
    asylum_dict_list.append(dict(zip(header, asylum_list[i])))
# turn it into a pandas data frame
asylum_df = pd.DataFrame(asylum_dict_list)
# keep year 2015 only
asylum_df_2015 = asylum_df[asylum_df['Year'] == '2015']

asylum_df_2015.to_csv('asylum_csv_2015.csv')
# give the variables usable names
asylum_df_2015 = asylum_df_2015.rename(index=str, columns={
        'Applied during year' : 'applied_during_year',
        'Country / territory of asylum/residence' : 'country',
        'Origin' : 'country_of_origin',
        'Otherwise closed' : 'otherwise_closed',
        'RSD Procedure type / level' : 'rsd_procedure_type',
        'Rejected' : 'rejected',
        'Tota pending start-year' : 'total_pending_start_year',
        'Total decisions' : 'total_decisions',
        'Total pending end-year' : 'total_pending_end_year',
        'Year' : 'year',
        'of which UNHCR-assisted' : 'of_which_unhcr_assisted',
        'statistics.filter.decisions_other' : 'decisions_other',
        'statistics.filter.decisions_recognized' : 'recognized'
        })
# get sums of recognized and total_decisions -- first need to convert these to int
asylum_df_2015.total_decisions = asylum_df_2015.total_decisions[asylum_df_2015.total_decisions != ''].astype('int32')
asylum_df_2015.recognized = asylum_df_2015.recognized[asylum_df_2015.recognized != ''].astype('int32')

recognized_2015 = asylum_df_2015.groupby('country').recognized.sum()
total_decisions_2015 = asylum_df_2015.groupby('country').total_decisions.sum()

# merge recognzed with total decisions
recognized_2015 = pd.DataFrame(recognized_2015)
total_decisions_2015 = pd.DataFrame(total_decisions_2015)
recognized_total_decisions_2015 = recognized_2015.merge(total_decisions_2015, on='country')
recognized_total_decisions_2015['recognition_rate'] = 100 * recognized_total_decisions_2015.recognized / recognized_total_decisions_2015.total_decisions

# merge to get country_codes and drop extraneous vars to get recognition rate
recognized_total_decisions_2015 = recognized_total_decisions_2015.merge(country_iso_2_iso_3, on='country')
recognition_rate = recognized_total_decisions_2015.drop('country', 1)
recognition_rate = recognition_rate.drop('recognized', 1)
recognition_rate = recognition_rate.drop('total_decisions', 1)
recognition_rate['country_code'] = recognition_rate.iso_3
recognition_rate = recognition_rate.drop('iso_3', 1)
recognition_rate = recognition_rate.drop('iso_2', 1)

# save to csv
recognition_rate.to_csv('recognition_rate.csv')

#####################################################
#####################################################
#####################################################

# DOWNLOAD WDI DATA

# download zip archives of csv data files from World Bank, World Development Indicators
# unzip them
# manipulate them to keep relevant years, remove regions (leaving only countries)
# write to csv
# commented out data sets are left here to remind me not to retrieve them later; they are full of missing data


import zipfile
import io

regions = ['ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA', 'IDB', 'IDX', 'INX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST', 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA', 'TSS', 'UMC', 'WLD']

data_dictionary = [
      
        
# Population, total   
        
    {'name' : 'population',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv',
     'long_name' : 'Population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Population)'
     },
        
# International migrant stock (% of population    
        
    {'name' : 'migrant_stock',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SM.POP.TOTL.ZS?downloadformat=csv',
     'long_name' : 'International migrant stock (% of population), 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'International migrant stock (% of population)'
     },

        
# gross domestic product per capita, current USD at PPP

    {'name' : 'gdp_per_capita',
     'url' : 'http://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv',
     'long_name' : 'Gross Domestic Product per capita, Current USD at PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'GDP per capita'
     },
     
# maternal mortality rate per 100000 live births
    {'name' : 'maternal_mortality_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.STA.MMRT?downloadformat=csv',
     'long_name' : 'Maternal Mortality Rate: materal deaths per 100,000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Maternal Mortality Rate'
     },

#life expectancy at birth
    {'name' :'life_expectancy',
     'url': 'http://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv',
     'long_name' : 'Life Expectancy at Birth, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Life Expectancy'
     },
     
# hiv prevalence
    {'name' : 'hiv_prevalence',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.AIDS.ZS?downloadformat=csv',
     'long_name' : 'HIV prevalance, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'HIV Prevalence'
     },
     
# urban population, percent of population
    {'name' : 'urbpop',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv',
     'long_name' : 'Urban Population (% of Total), 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Urban Population'
     },

     
# share of income held by lowest 20% of population
    {'name' : 'lowest_twenty_income_share',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.20?downloadformat=csv',
     'long_name' : 'Share of income held by lowest 20% of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Income share'
     },
     
# net official development assistance as percent of gross national income
    {'name' :'oda_pct_of_gni',
     'url' : 'http://api.worldbank.org/v2/en/indicator/DT.ODA.ODAT.GN.ZS?downloadformat=csv',
     'long_name' : 'Official development assistance (net), % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'ODA as % of GNI'
     },

# net migration
    {'name' : 'net_migration',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SM.POP.NETM?downloadformat=csv',
     'long_name' : 'Net migration, 2017',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net migration'
     },

# poverty headcount ratio, $1.90 at 2011 PPP
    {'name' : 'poverty_headcount_ratio_190_2011_ppp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv',
     'long_name' : 'Poverty headcount ratio, USD $1.90 at 2011 PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Poverty headcount ratio'
     },

# access to electricity, % of population
    {'name' : 'access_to_electricity_pct_of_population',
     'url': 'http://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv',
     'long_name' : 'Access to electricity, % of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Access to electricity'
     },
         
# CO2 emissions, metric tons per capita -- 2014 is latest available
    {'name' : 'co2_tons_per_capita',
     'url' : 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv',
     'long_name' : 'C02 emissions, metric tons per capita, 2014',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'C02 emissions per capita'
     },
     
# mortality rate under 5 per 1000 live births
    {'name' : 'mortality_under_5_per_1000_live_births',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.MORT?downloadformat=csv',
     'long_name' : 'Mortality rate under age 5 per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Mortality rate under age 5'
     },

# energy use per capita (kg equiv oil) -- 2014 is the latest available
    {'name' : 'energy_use_per_capita',
     'url': 'http://api.worldbank.org/v2/en/indicator/EG.USE.PCAP.KG.OE?downloadformat=csv',
     'long_name' : 'Energy use per capita, kg equivalent of petroleum, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Energy use per capita'
     },


# remittances received, current USD
    {'name' : 'remittances',
     'url' : 'http://api.worldbank.org/v2/en/indicator/BX.TRF.PWKR.CD.DT?downloadformat=csv',
     'long_name' : 'Remittances received, current USD, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Remittances received'
     },

# revenue, % of gdp
    {'name' : 'revenue_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/GC.REV.XGRT.GD.ZS?downloadformat=csv',
     'long_name' : 'Government revenue, % of gross domestic product, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Revenue, % of GDP'
      },

# govt expenditure on education, % of GDP
    {'name' : 'govt_exp_educ_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GD.ZS?downloadformat=csv',
     'long_name' : 'Government expenditures on education, % of gross domestic product, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Education expenditure, % of GDP'
     },

# female literacy, over 15, %
    {'name' : 'female_literacy_pct',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.FE.ZS?downloadformat=csv',
     'long_name' : 'Female literacy over age 15, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female literacy'
     },

     
# external debt, % of GNI
    {'name' : 'external_debt_pct_GNI',
     'url' : 'http://api.worldbank.org/v2/en/indicator/DT.DOD.DECT.GN.ZS?downloadformat=csv',
     'long_name' : 'External debt, % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'External debt, % of GNI'
     },

# FDI, net, current USD
    {'name' : 'fdi_net_current_usd',
     'url' : 'http://api.worldbank.org/v2/en/indicator/BX.KLT.DINV.CD.WD?downloadformat=csv',
     'long_name' : 'Foreign direct investment, net, current USD, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net FDI, current USD'
     },

# strength of legal rights, 0=low, 12=high
    {'name' : 'strength_legal_rights_0_12',
     'url' : 'http://api.worldbank.org/v2/en/indicator/IC.LGL.CRED.XQ?downloadformat=csv',
     'long_name' : 'Strength of legal rights, 0-12 scale, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Strength of legal rights'
    },     

# adolescent fertility rate, 15-19, per 1000 live births
    {'name' : 'adolescent_fertility_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.ADO.TFRT?downloadformat=csv',
     'long_name' : 'Adolescent fertility rate (age 15-19), per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Adolescent fertility rate'
     },
     
# fertility rate, births per woman
    {'name' : 'fertility_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.DYN.TFRT.IN?downloadformat=csv',
     'long_name' : 'Fertility rate, births per woman, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Fertility rate'
     },

# female employment, % of total labor force
    {'name' :'female_employment_pct_of_total',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SL.TLF.TOTL.FE.ZS?downloadformat=csv',
     'long_name' : 'Female employment, % of total labor force, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female employment'
     },
# share of income held by lowest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'lowest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.10?downloadformat=csv',
      'long_name' : 'Share of income held by lowest 10% of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, lowest 10%'
      },
      
# share of income held by highest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'highest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.10TH.10?downloadformat=csv',
      'long_name' : 'Share of income held by highest 10% of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, highest 10%'
      },
      

# safety net (etc.) data commented out because data is almost all missing
     
## adequacy of unemployment and active labor market programs
#     {'name' : 'adequacy_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_lm_alllm.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of unemployment benefits and ALMP'
#      },
      
## coverage of unemployment and active labor market programs
#     {'name' : 'coverage_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_lm_alllm.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of unemployment benefits and ALMP'
#      },
      
## adequacy of social safety net programs
#     {'name' : 'adequacy_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_sa_allsa.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social safety net programs'
#      },
#      
## coverage of social safety net programs
#     {'name' : 'coverage_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_sa_allsa.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social safety net programs'
#      },
      
## adequacy of social protection and labor programs
#     {'name' : 'adequacy_social_protection',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_allsp.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social protection and labor programs'
#      },

## coverage of social protection and labor programs
#     {'name' : 'coverage_social_protection',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_allsp.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social protection and labor programs'
#      },

# trade (% of GDP)
     {'name' : 'trade_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/NE.TRD.GNFS.ZS?downloadformat=csv',
      'long_name' : 'Trade, % of gross domestic product, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Trade, % of GDP'
      },
      
# Individuals using the Internet (% of population)
     {'name' : 'use_internet_pct_pop',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IT.NET.USER.ZS?downloadformat=csv',
      'long_name' : 'Individuals using the Internet (% of population), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Internet users, & of population'
      },
     
# Mobile cellular subscriptions (per 100 people)
     {'name' : 'mobile_phone_subscriptions_pct_pop',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IT.CEL.SETS.P2?downloadformat=csv',
      'long_name' : 'Mobile cellular subscriptions, % of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Mobile phone subscriptions, & of population'
      },
     
# Time required to start a business (days)
     {'name' : 'days_required_to_start_business',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.REG.DURS?downloadformat=csv',
      'long_name' : 'Time required to start a business (days), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Time required to start a business (days)'
      },
   
# data mostly missing
## Firms with female participation in ownership (% of firms)
#     {'name' : 'firms_female_top_mgmt_pct',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.FEMO.ZS?downloadformat=csv',
#      'long_name' : 'Firms with female participation in ownership (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Firms with female participation in ownership (% of firms)'
#      },
     
# data mostly missing
## Informal payments to public officials (% of firms)
#     {'name' : 'informal_payments_to_officials_pct_firms',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.CORR.ZS?downloadformat=csv',
#      'long_name' : 'Informal payments to public officials (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Informal payments to public officials (% of firms)'
#      },
#      
## Bribery incidence (% of firms experiencing at least one bribe payment request)
#     {'name' : 'bribe_incidence_pct_firm',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.BRIB.ZS?downloadformat=csv',
#      'long_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)'
#      },
      
# Ease of doing business index (1=most business-friendly regulations)
# ------------> # NOTE: data from 2018
     {'name' : 'ease_doing_business',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.BUS.EASE.XQ?downloadformat=csv',
      'long_name' : 'Ease of doing business index (1=most business-friendly regulations), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Ease of doing business index (1=most business-friendly regulations)'
      },
      
# Tax revenue (% of GDP)
     {'name' : 'tax_revenue_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.TAX.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Tax revenue (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Tax revenue (% of GDP)'
      },
      
# Net lending (+) / net borrowing (-) (% of GDP)
     {'name' : 'net_lending_borrowing_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.NLD.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Net lending (+) / net borrowing (-) (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net lending (+) / net borrowing (-) (% of GDP)'
      },

# Central government debt, total (% of GDP)
     {'name' : 'central_govt_debt_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.DOD.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Central government debt, total (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Central government debt, total (% of GDP)'
      },  

# all data missing      
# Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)
#     {'name' : 'account_ownership_pct_population_15_plus',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/FX.OWN.TOTL.ZS?downloadformat=csv',
#      'long_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'
#      }, 

# Risk premium on lending (lending rate minus treasury bill rate, %)
     {'name' : 'risk_premium',
      'url' : 'http://api.worldbank.org/v2/en/indicator/FR.INR.RISK?downloadformat=csv',
      'long_name' : 'Risk premium on lending (lending rate minus treasury bill rate, %), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Risk premium on lending'
      },
       
# Terrestrial and marine protected areas (% of total territorial area)
     # data are from 2016
     {'name' : 'biodiversity_protected_areas',
      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.PTD.TOTL.ZS?downloadformat=csv',
      'long_name' : 'Terrestrial and marine protected areas (% of total territorial area), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Terrestrial and marine protected areas (% of total territorial area)'
      },
      
# Renewable internal freshwater resources per capita (cubic meters)
     {'name' : 'renewable_freshwater_per_capita',
      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.H2O.INTR.PC?downloadformat=csv',
      'long_name' : 'Renewable internal freshwater resources per capita (cubic meters), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Renewable internal freshwater resources per capita (cubic meters)'
      },
      
## all data missing
## Level of water stress: freshwater withdrawal as a proportion of available freshwater resources
#     {'name' : 'frewshwater_stress',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.H2O.FWST.ZS?downloadformat=csv',
#      'long_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources'
#      }, 

# Population living in slums (% of urban population)
# NOTE: data from 2014
     {'name' : 'slum_population_pct_urban_population',
      'url' : 'http://api.worldbank.org/v2/en/indicator/EN.POP.SLUM.UR.ZS?downloadformat=csv',
      'long_name' : 'Population living in slums (% of urban population), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Population living in slums (% of urban population)'
      }, 

# PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)
     {'name' : 'pm25_pct_population',
      'url' : 'http://api.worldbank.org/v2/en/indicator/EN.ATM.PM25.MC.ZS?downloadformat=csv',
      'long_name' : 'PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'PM2.5 air pollution exposure, % of population)'
      }, 

# Foreign direct investment, net (BoP, current US$
     {'name' : 'net_fdi',
      'url' : 'http://api.worldbank.org/v2/en/indicator/BN.KLT.DINV.CD?downloadformat=csv',
      'long_name' : 'Foreign direct investment, net (BoP, current US$), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net foreign direct investment)'
      } ,

# Literacy rate, adults
    {'name': 'literacy_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.ZS?downloadformat=csv',
     'long_name' : 'Adult Literacy Rate, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Adult Literacy Rate'
     },
     
# Gini coefficient     
     {'name' : 'gini_coefficient',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.POV.GINI?downloadformat=csv',
      'long_name' : 'Gini Coefficient',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Gini Coefficient'
      }
      
      
]

for i in range(len(data_dictionary)):
    data = requests.get(data_dictionary[i]['url'])
    zip = zipfile.ZipFile(io.BytesIO(data.content))
    names = zipfile.ZipFile.namelist(zip)
    csv = pd.read_csv(zipfile.ZipFile.extract(zip, names[1]), header=2)
    if data_dictionary[i]['name'] == 'co2_tons_per_capita' or data_dictionary[i]['name'] == 'energy_use_per_capita':
        csv = csv[['Country Name', 'Country Code', '2014']]
    elif data_dictionary[i]['name'] == 'net_migration':
        csv = csv[['Country Name', 'Country Code', '2017']]
    elif data_dictionary[i]['name'] == 'ease_doing_business':
        csv = csv[['Country Name', 'Country Code', '2018']]    
    elif data_dictionary[i]['name'] == 'biodiversity_protected_areas':
        csv = csv[['Country Name', 'Country Code', '2016']]    
    elif data_dictionary[i]['name'] == 'renewable_freshwater_per_capita':
        csv = csv[['Country Name', 'Country Code', '2014']]    
    elif data_dictionary[i]['name'] == 'slum_population_pct_urban_population':
        csv = csv[['Country Name', 'Country Code', '2014']]    
    else:
        csv = csv[['Country Name', 'Country Code', '2015']].copy()
        
    if data_dictionary[i]['name'] == 'co2_tons_per_capita' or data_dictionary[i]['name'] == 'energy_use_per_capita':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'net_migration':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2017': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'ease_doing_business':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2018': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'biodiversity_protected_areas':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2016': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'renewable_freshwater_per_capita':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'slum_population_pct_urban_population':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    else:
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2015': data_dictionary[i]['name']})
    
# we want only countries, not regions
    for reg in regions:
        csv = csv[csv.country_code != reg] 
    csv.to_csv(data_dictionary[i]['name']+'.csv', index=False)

varnames = []
for i in range(len(data_dictionary)):
    varnames.append(data_dictionary[i]['name'])
varnames = pd.DataFrame(varnames)
varnames.to_csv('varnames.csv')

##########################################
##########################################
##########################################


# LOWESS MODELS

# uses World Development Indicators data
# estimates lowess regressions of these vars on gdp per capita
# saves residuals from those regressions as csv files with suffix _resid.csv
# lowess models for UNHCR data are estimated separately

import statsmodels.api as sm

gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=False)
lowess = sm.nonparametric.lowess

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')
varnames.remove('population')

vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)):
    vars[i]['file'] = vars[i]['name'] + '.csv'

lowess = sm.nonparametric.lowess

for i in range(len(vars)):
    df = pd.read_csv(vars[i]['file'], index_col=False)
    df = df.merge(gdpcap, on=['country', 'country_code'])
    df = df.dropna()
    model = lowess(df[vars[i]['name']], df.gdp_per_capita, return_sorted=False)
    df[vars[i]['name'] + '_resid'] = df[vars[i]['name']] - model
    df = df.drop(columns = [vars[i]['name'], 'gdp_per_capita'])
    df = df.merge(gdpcap, on=['country', 'country_code'], how='outer')
    df = df.drop('gdp_per_capita', 1)
    df.to_csv(vars[i]['name'] + '_resid.csv')
    
varnames_resid = pd.DataFrame(varnames)
varnames_resid.to_csv('varnames_resid.csv')

#########################################
#########################################
#########################################


# MERGE WDI DATA

# merges World Development Indicators into a single file
# this file is not used directly, it is just for future use

# open gdp_per_capita, get other varnames
gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=0)

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')

vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)):
    vars[i]['file'] = vars[i]['name'] + '.csv'
    
varnames_resid = pd.read_csv('varnames_resid.csv')
varnames_resid = varnames_resid.iloc[:, 1].tolist()
for i in range(len(varnames_resid)):
    varnames_resid[i] = {'name': varnames_resid[i] + '_resid'}
    varnames_resid[i]['file'] = varnames_resid[i]['name'] + '.csv'
    
vars += varnames_resid

for i in range(len(vars)):
    gdpcap = gdpcap.merge(pd.read_csv(vars[i]['file']), on=['country', 'country_code'])
    
gdpcap.to_csv('wdi_vars.csv')

###########################################
###########################################
###########################################

# MERGE UNHCR DATA, HAPPINESS, CORRUPTION, CIVIL LIBERTIES, GET LOWESS RESIDS OF THOSE


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

asylum_seekers_pct_pop = pd.read_csv('asylum_seekers_pct_pop.csv', index_col=False)
asylum_seekers_pct_pop['country'] = asylum_seekers_pct_pop['country_x']
asylum_seekers_pct_pop.to_csv('asylum_seekers_pct_pop.csv')


asylum_seekers_pct_pop_resid = pd.read_csv('asylum_seekers_pct_pop_resid.csv', index_col=False)
asylum_seekers_pct_pop_resid['country'] = asylum_seekers_pct_pop_resid['country_x']
asylum_seekers_pct_pop_resid.to_csv('asylum_seekers_pct_pop_resid.csv')

fdi_net_pct_gdp = pd.read_csv('fdi_net_pct_gdp.csv', index_col=False)
fdi_net_pct_gdp['country'] = fdi_net_pct_gdp['country_x']
fdi_net_pct_gdp.to_csv('fdi_net_pct_gdp.csv')

fdi_net_pct_gdp_resid = pd.read_csv('fdi_net_pct_gdp_resid.csv', index_col=False)
fdi_net_pct_gdp_resid['country'] = fdi_net_pct_gdp_resid['country_x']
fdi_net_pct_gdp_resid.to_csv('fdi_net_pct_gdp_resid.csv')

idps = idps.merge(country_iso_2_iso_3, left_on='country_code', right_on='iso_3')
idps.to_csv('idps.csv')

#idps_resid = pd.read_csv('idps_resid.csv', index_col=False)
#idps_resid['country'] = idps_resid['country_x']
#idps_resid.to_csv('idps_resid.csv')

happiness = happiness.merge(country_iso_2_iso_3, left_on='country_code', right_on='iso_3')
happiness.to_csv('happiness.csv')

#happiness_resid = pd.read_csv('happiness_resid.csv', index_col=False)
#happiness_resid['country'] = happiness_resid['country_x']
#happiness_resid.to_csv('happiness_resid.csv')

recognition_rate = recognition_rate.merge(country_iso_2_iso_3, left_on='country_code', right_on='iso_3') 
recognition_rate.to_csv('recognition_rate.csv')

#recognition_rate_resid = pd.read_csv('recognition_rate_resid.csv', index_col=False)
#recognition_rate_resid['country'] = recognition_rate_resid['country_x']
#recognition_rate_resid.to_csv('recognition_rate_resid.csv')

refugees = refugees.merge(country_iso_2_iso_3, left_on='country_code', right_on='iso_3')
refugees.to_csv('refugees.csv')

refugees_pct_pop = pd.read_csv('refugees_pct_pop.csv', index_col=False)
refugees_pct_pop['country'] = refugees_pct_pop['country_x']
refugees_pct_pop.to_csv('refugees_pct_pop.csv')

refugees_pct_pop_resid = pd.read_csv('refugees_pct_pop_resid.csv', index_col=False)
refugees_pct_pop_resid['country'] = refugees_pct_pop_resid['country_x']
refugees_pct_pop_resid.to_csv('refugees_pct_pop_resid.csv')

ti_cpi = ti_cpi.merge(country_iso_2_iso_3, left_on='country_code', right_on='iso_3')
ti_cpi.to_csv('ti_cpi.csv')

#ti_cpi_resid = pd.read_csv('ti_cpi_resid.csv', index_col=False)
#ti_cpi_resid['country'] = ti_cpi_resid['country_x']
#ti_cpi_resid.to_csv('ti_cpi_resid.csv')

wdi_vars.to_csv('map_data.csv')
###########################################
###########################################
###########################################


# MAKE MAPS

# generates maps (as divs) to include in 'MapMinder' web app
# these divs need to be copied to /../mapminder/charts


import plotly

vars = [
{'varname': 'access_to_electricity_pct_of_population_resid', 'long_name': 'Access to Electricity, % of Population, Residuals from Regression on GDP per Capita', 'short_name': 'Access to Electricity, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'access_to_electricity_pct_of_population', 'long_name': 'Access to Electricity, % of Population, 2015', 'short_name': 'Access to Electricity', 'source':'World Bank, World Development Indicators'},
{'varname': 'adolescent_fertility_rate_resid', 'long_name': 'Adolescent Fertility Rate (per 1,000 Women Age 15-19), Residuals', 'short_name': 'Adolescent Fertility Rate, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'adolescent_fertility_rate', 'long_name': 'Adolescent Fertility Rate (per 1,000 Women Age 15-19), 2015)', 'short_name': 'Adolescent Fertility Rate', 'source':'World Bank, World Development Indicators'},
{'varname': 'asylum_seekers_resid', 'long_name': 'Asylum Seekers, 2015, Residuals', 'short_name': 'Asylum Seekers, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'asylum_seekers', 'long_name': 'Asylum Seekers, 2015', 'short_name': 'Asylum Seekers', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'biodiversity_protected_areas_resid', 'long_name': 'Biodiversity: Protected Areas, % of Land Area, Residuals', 'short_name': 'Protected Areas, % of Land Area, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'biodiversity_protected_areas', 'long_name': 'Biodiversity: Protected Areas, % of Land Area, 2016', 'short_name': 'Protected Areas, % of Land Area', 'source':'World Bank, World Development Indicators'},
{'varname': 'central_govt_debt_pct_gdp_resid', 'long_name': 'Central Government Debt, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Central Government Debt, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'central_govt_debt_pct_gdp', 'long_name': 'Central Government Debt, % of Gross Domestic Product, 2015', 'short_name': 'Central Government Debt, % of GGDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'co2_tons_per_capita_resid', 'long_name': 'C02 Emissions per Capita, Metric Tons, Residuals from Regression on GDP per Capita', 'short_name': 'C02 Emissions per Capita, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'co2_tons_per_capita', 'long_name': 'C02 Emissions per Capita, Metric Tons, 2014', 'short_name': 'C02 Emissions per Capita', 'source':'World Bank, World Development Indicators'},
{'varname': 'days_required_to_start_business_resid', 'long_name': 'Days Required to Start a Business, Residuals from Regression on GDP per Capita', 'short_name': 'Days to Start a Business, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'days_required_to_start_business', 'long_name': 'Days Required to Start a Business, 2015', 'short_name': 'Days Required to Start a Business', 'source':'World Bank, World Development Indicators'},
{'varname': 'ease_doing_business_resid', 'long_name': 'Ease of Doing Business (Ranking), Residuals from Regression on GDP per Capita', 'short_name': 'Ease of Doing Business (Ranking), Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'ease_doing_business', 'long_name': 'Ease of Doing Business (Ranking), 2018', 'short_name': 'Ease of Doing Business (Ranking)', 'source':'World Bank, World Development Indicators'},
{'varname': 'energy_use_per_capita_resid', 'long_name': 'Energy Use Per Capita, kg of Diesel Equivalent, Residuals from Regression on GDP per Capita', 'short_name': 'Energy Use Per Capita, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'energy_use_per_capita', 'long_name': 'Energy Use Per Capita, kg of Diesel Equivalent, 2015', 'short_name': 'Energy Use Per Capita', 'source':'World Bank, World Development Indicators'},
{'varname': 'external_debt_pct_GNI_resid', 'long_name': 'External Government Debt, % of Gross National Income, Residuals from Regression on GDP per Capita', 'short_name': 'External Government Debt, % of GNI, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'external_debt_pct_GNI', 'long_name': 'External Government Debt, % of Gross National Income, 2015', 'short_name': 'External Government Debt, % of GNI', 'source':'World Bank, World Development Indicators'},
{'varname': 'fdi_net_current_usd_resid', 'long_name': 'Foreign Direct Investment, USD, Residuals from Regression on GDP per Capita', 'short_name': 'Foreign Direct Investment, USD, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'fdi_net_current_usd', 'long_name': 'Foreign Direct Investment, USD, 2015', 'short_name': 'Foreign Direct Investment, USD', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_employment_pct_of_total_resid', 'long_name': 'Female Employment, % of Total Employment, Residuals from Regression on GDP per Capita', 'short_name': 'Female % of Total Employment, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_employment_pct_of_total', 'long_name': 'Female Employment, % of Total Employment, 2015', 'short_name': 'Female % of Total Employment', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_literacy_pct_resid', 'long_name': 'Female Literacy, % of All Women, Residuals from Regression on GDP per Capita', 'short_name': 'Female Literacy, % of All Women, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_literacy_pct', 'long_name': 'Female Literacy, % of All Women, 2015', 'short_name': 'Female Literacy, % of All Women', 'source':'World Bank, World Development Indicators'},
{'varname': 'fertility_rate_resid', 'long_name': 'Fertility Rate, Residuals from Regression on GDP per Capita', 'short_name': 'Fertility Rate, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'fertility_rate', 'long_name': 'Fertility Rate, Births per Woman, 2015', 'short_name': 'Fertility Rate', 'source':'World Bank, World Development Indicators'},
{'varname': 'govt_exp_educ_pct_gdp_resid', 'long_name': 'Government Expenditure on Education, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Gov\'t Exp. Education, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'govt_exp_educ_pct_gdp', 'long_name': 'Government Expenditure on Education, % of Gross Domestic Product, 2015', 'short_name': 'Gov\'t Exp. Education, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'happiness_resid', 'long_name': 'Self-Reported Happiness (1-10, 10 high), Residuals from Regression on GDP per Capita', 'short_name': 'Self-Reported Happiness, residuals', 'source':'World Happiness Report'},
{'varname': 'happiness', 'long_name': 'Self-Reported Happiness (1-10, 10 high), 2015', 'short_name': 'Self-Reported Happiness', 'source':'World Happiness Report'},
{'varname': 'highest_ten_income_share_resid', 'long_name': 'Income Share, Highest 10%, Residuals from Regression on GDP per Capita', 'short_name': 'Income Share, Highest 10%, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'highest_ten_income_share', 'long_name': 'Income Share, Highest 10%, 2015', 'short_name': 'Income Share, Highest 10%', 'source':'World Bank, World Development Indicators'},
{'varname': 'hiv_prevalence_resid', 'long_name': 'HIV Prevalance,  Residuals from Regression on GDP per Capita', 'short_name': 'HIV Prevalance,  Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'hiv_prevalence', 'long_name': 'HIV Prevalance, %, 2015', 'short_name': 'HIV Prevalance', 'source':'World Bank, World Development Indicators'},
{'varname': 'idps_resid', 'long_name': 'Internally Displaced Persons, Residuals from Regression on GDP per Capita', 'short_name': 'Internally Displaced Persons, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'idps', 'long_name': 'Internally Displaced Persons, 2015', 'short_name': 'Internally Displaced Persons', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'life_expectancy_resid', 'long_name': 'Life Expectancy, Residuals from Regression on GDP per Capita', 'short_name': 'Life Expectancy, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'life_expectancy', 'long_name': 'Life Expectancy, 2015', 'short_name': 'Life Expectancy', 'source':'World Bank, World Development Indicators'},
{'varname': 'lowest_ten_income_share_resid', 'long_name': 'Income Share, Lowest 10%, Residuals from Regression on GDP per Capita', 'short_name': 'Income Share, Lowest 10%, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'lowest_ten_income_share', 'long_name': 'Income Share, Lowest 10%, 2015', 'short_name': 'Income Share, Lowest 10%', 'source':'World Bank, World Development Indicators'},
{'varname': 'lowest_twenty_income_share_resid', 'long_name': 'Income Share, Lowest 20%, Residuals from Regression on GDP per Capita', 'short_name': 'Income Share, Lowest 20%, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'lowest_twenty_income_share', 'long_name': 'Income Share, Lowest 20%, 2015', 'short_name': 'Income Share, Lowest 20%', 'source':'World Bank, World Development Indicators'},
{'varname': 'maternal_mortality_rate_resid', 'long_name': 'Maternal Mortality Rate, Residuals from Regression on GDP per Capita', 'short_name': 'Maternal Mortality Rate, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'maternal_mortality_rate', 'long_name': 'Maternal Mortality Rate, 2015', 'short_name': 'Maternal Mortality Rate', 'source':'World Bank, World Development Indicators'},
{'varname': 'migrant_stock_resid', 'long_name': 'Migrant Stock, Residuals from Regression on GDP per Capita', 'short_name': 'Migrant Stock, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'migrant_stock', 'long_name': 'Migrant Stock, % of Population', 'short_name': 'Migrant Stock, %, 2015', 'source':'World Bank, World Development Indicators'},
{'varname': 'mobile_phone_subscriptions_pct_pop_resid', 'long_name': 'Mobile Phone Subscriptions, % of Population, Residuals from Regression on GDP per Capita', 'short_name': 'Mobile Phone Subscriptions, % of Population, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'mobile_phone_subscriptions_pct_pop', 'long_name': 'Mobile Phone Subscriptions, % of Population, 2015', 'short_name': 'Mobile Phone Subscriptions', 'source':'World Bank, World Development Indicators'},
{'varname': 'mortality_under_5_per_1000_live_births_resid', 'long_name': 'Mortality Under 5 Years, per 1000 Live Births, Residuals from Regression on GDP per Capita', 'short_name': 'Mortality Under 5 Years, per 1000 Live Births, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'mortality_under_5_per_1000_live_births', 'long_name': 'Mortality Under 5 Years, per 1000 Live Births, 2015', 'short_name': 'Mortality Under 5 Years, per 1000 Live Births', 'source':'World Bank, World Development Indicators'},
{'varname': 'net_lending_borrowing_pct_gdp_resid', 'long_name': 'Net Lending/Borrowing, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Net Lending/Borrowing, % of Gross Domestic Product, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'net_lending_borrowing_pct_gdp', 'long_name': 'Net Lending/Borrowing, % of Gross Domestic Product, 2015', 'short_name': 'Net Lending/Borrowing', 'source':'World Bank, World Development Indicators'},
{'varname': 'net_migration_resid', 'long_name': 'Net Migration, Residuals from Regression on GDP per Capita', 'short_name': 'Net Migration, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'net_migration', 'long_name': 'Net Migration, 2017', 'short_name': 'Net Migration', 'source':'World Bank, World Development Indicators'},
{'varname': 'oda_pct_of_gni_resid', 'long_name': 'Official Development Assistance, & of Gross National Income, Residuals from Regression on GDP per Capita', 'short_name': 'Official Development Assistance, & of Gross National Income, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'oda_pct_of_gni', 'long_name': 'Official Development Assistance, & of Gross National Income', 'short_name': 'Official Development Assistance', 'source':'World Bank, World Development Indicators'},
{'varname': 'pm25_pct_population_resid', 'long_name': 'PM25 Exposure, % of population, Residuals from Regression on GDP per Capita', 'short_name': 'PM25 Exposure, % of population, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'pm25_pct_population', 'long_name': 'PM25 Exposure, % of population, 2015', 'short_name': 'PM25 Exposure, % of population', 'source':'World Bank, World Development Indicators'},
{'varname': 'population', 'long_name': 'Population, 2015', 'short_name': 'Population', 'source':'World Bank, World Development Indicators'},
{'varname': 'poverty_headcount_ratio_190_2011_ppp_resid', 'long_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 PPP, Residuals from Regression on GDP per Capita', 'short_name': 'Poverty Headcount Ratio, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'poverty_headcount_ratio_190_2011_ppp', 'long_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 USD PPP, 2015', 'short_name': 'Poverty Headcount Ratio', 'source':'World Bank, World Development Indicators'},
{'varname': 'recognition_rate_resid', 'long_name': 'Asylum Recognition Rate, Residuals from Regression on GDP per Capita', 'short_name': 'Asylum Recognition Rate, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'recognition_rate', 'long_name': 'Asylum Recognition Rate, %, 2015', 'short_name': 'Asylum Recognition Rate', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees_resid', 'long_name': 'Refugees, Residuals from Regression on GDP per Capita', 'short_name': 'Refugees, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees', 'long_name': 'Refugees, 2015', 'short_name': 'Refugees, 2015', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'remittances_resid', 'long_name': 'Personal remittances from abroad, USD, Residuals from Regression on GDP per Capita', 'short_name': 'Personal remittances, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'remittances', 'long_name': 'Personal remittances from abroad, USD, 2015', 'short_name': 'Personal remittances', 'source':'World Bank, World Development Indicators'},
{'varname': 'renewable_freshwater_per_capita_resid', 'long_name': 'Renewable Freshwater Resources, cubic meters per capita, Residuals from Regression on GDP per Capita', 'short_name': 'Renewable Freshwater Resources, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'renewable_freshwater_per_capita', 'long_name': 'Renewable Freshwater Resources, cubic meters per capita, 2014', 'short_name': 'Renewable Freshwater Resources', 'source':'World Bank, World Development Indicators'},
{'varname': 'revenue_pct_gdp_resid', 'long_name': 'Government revenue, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Government revenue, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'revenue_pct_gdp', 'long_name': 'Government revenue, % of Gross Domestic Product, 2015', 'short_name': 'Government revenue, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'risk_premium_resid', 'long_name': 'Risk Premium (over US Treasury), Residuals from Regression on GDP per Capita', 'short_name': 'Risk Premium (over US Treasury), Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'risk_premium', 'long_name': 'Risk Premium (over US Treasury), 2015', 'short_name': 'Risk Premium (over US Treasury)', 'source':'World Bank, World Development Indicators'},
{'varname': 'slum_population_pct_urban_population_resid', 'long_name': 'Slum Population, % of Urban Population, Residuals from Regression on GDP per Capita', 'short_name': 'Slum Population, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'slum_population_pct_urban_population', 'long_name': 'Slum Population, % of Urban Population, 2014', 'short_name': 'Slum Population', 'source':'World Bank, World Development Indicators'},
{'varname': 'strength_legal_rights_0_12_resid', 'long_name': 'Strength of Legal Rights (0-12, 12 high), Residuals from Regression on GDP per Capita', 'short_name': 'Strength of Legal Rights, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'strength_legal_rights_0_12', 'long_name': 'Strength of Legal Rights (0-12, 12 high), 2015', 'short_name': 'Strength of Legal Rights', 'source':'World Bank, World Development Indicators'},
{'varname': 'tax_revenue_pct_gdp_resid', 'long_name': 'Tax Revenue, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Tax Revenue, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'tax_revenue_pct_gdp', 'long_name': 'Tax Revenue, % of Gross Domestic Product, 2015', 'short_name': 'Tax Revenue, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'ti_cpi_resid', 'long_name': 'Corruption Perception Index (reversed), Residuals from Regression on GDP per Capita', 'short_name': 'Corruption Perception Index (reversed), residuals', 'source':'Transparency International'},
{'varname': 'ti_cpi', 'long_name': 'Corruption Perception Index (reversed), 2015', 'short_name': 'Corruption Perception Index (reversed)', 'source':'Transparency International'},
{'varname': 'trade_pct_gdp_resid', 'long_name': 'Trade, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Trade, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'trade_pct_gdp', 'long_name': 'Trade, % of Gross Domestic Product, 2015', 'short_name': 'Trade, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'urbpop_resid', 'long_name': 'Urban Population, % of Total, Residuals from Regression on GDP per Capita', 'short_name': 'Urban Population, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'urbpop', 'long_name': 'Urban Population, % of Total, 2015', 'short_name': 'Urban Population', 'source':'World Bank, World Development Indicators'},
{'varname': 'use_internet_pct_pop_resid', 'long_name': 'Internet Use, % of Population,  Residuals from Regression on GDP per Capita', 'short_name': 'Internet Use, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'use_internet_pct_pop', 'long_name': 'Internet Use, % of Population, 2015', 'short_name': 'Internet Use', 'source':'World Bank, World Development Indicators'},
{'varname': 'asylum_seekers_pct_pop_resid', 'long_name': 'Asylum Seekers per Population, %, Residuals', 'short_name': 'Asylum Seekers, %, Residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'asylum_seekers_pct_pop', 'long_name': 'Asylum Seekers per Population, %, 2015', 'short_name': 'Asylum Seekers, %', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees_pct_pop_resid', 'long_name': 'Refugees per Population %, Residuals from Regression on GDP per Capita', 'short_name': 'Refugees, %, Residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees_pct_pop', 'long_name': 'Refugees per Population, %, 2015', 'short_name': 'Refugees per Population, %', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'civil_liberties', 'long_name': "Civil Liberties, Rank 1-7 (1 High), 2015", 'short_name': 'Civil Liberties', 'source': 'Freedom House, Freedom in the World Report'},
{'varname': 'civil_liberties_resid', 'long_name': "Civil Liberties, Rank 1-7 (1 High), Residuals from Regression on Gross Domestic Product per Capita", 'short_name': 'Civil Liberties, Residuals', 'source': 'Freedom House, Freedom in the World Report'},
{'varname': 'fdi_net_pct_gdp', 'long_name': 'Net Foreign Direct Investment as % of Gross Domestic Product, 2015', 'short_name': 'FDI, % of GDP', 'source': 'World Bank, World Development Indicators'},
{'varname': 'fdi_net_pct_gdp_resid', 'long_name': 'Net Foreign Direct Investment as % of GDP, Residuals from Regression on GDP per capita', 'short_name': 'FDI, % of GDP, Residuals', 'source': 'World Bank, World Development Indicators'},

 ]

for i in range(len(vars)):
    filename = vars[i]['varname'] + '.csv'
    df = pd.read_csv(filename)
    
    data = [ dict(
           type = 'choropleth',
           locations = df['country_code'],
           z = df[vars[i]['varname']],
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
               title = vars[i]['short_name']
           ),
       ) ]
    
    layout = dict(
       title = vars[i]['long_name'] + '<br>' + vars[i]['source'],
       geo = dict(
           showframe = False,
           showcoastlines = False,
           projection = dict(
               type = 'kavrayskiy7'
           )
       )
    )
    
    fig = dict( data=data, layout=layout )
    f = open(vars[i]['varname'] + '.div', 'w+')
    f.write(plotly.offline.plot(fig, output_type='div', include_plotlyjs=False, auto_open=False))
    f.close()
