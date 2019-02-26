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


vars = [
{'varname': 'access_to_electricity_pct_of_population_resid', 'long_name': 'Access to Electricity, % of Population, Residuals from Regression on GDP per Capita', 'short_name': 'Access to Electricity, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'access_to_electricity_pct_of_population', 'long_name': 'Access to Electricity, % of Population, 2015', 'short_name': 'Access to Electricity', 'source':'World Bank, World Development Indicators'},
{'varname': 'adolescent_fertility_rate_resid', 'long_name': 'Adolescent Fertility Rate (per 1,000 Women Age 15-19), Residuals', 'short_name': 'Adolescent Fertility Rate', Residuals', 'source':'World Bank, World Development Indicators'},
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
{'varname': 'female_employment_pct_of_total_resid', 'long_name': 'Female Employment, % of Total Employment, Residuals from Regression on GDP per Capita', 'short_name': 'Female Employment, % of Total Employment, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_employment_pct_of_total', 'long_name': 'Female Employment, % of Total Employment, 2015', 'short_name': 'Female Employment, %', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_literacy_pct_resid', 'long_name': 'Female Literacy, % of All Women, Residuals from Regression on GDP per Capita', 'short_name': 'Female Literacy, % of All Women, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'female_literacy_pct', 'long_name': 'Female Literacy, % of All Women, 2015', 'short_name': 'Female Literacy, % of All Women', 'source':'World Bank, World Development Indicators'},
{'varname': 'fertility_rate_resid', 'long_name': 'Fertility Rate, Residuals from Regression on GDP per Capita', 'short_name': 'Fertility Rate, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'fertility_rate', 'long_name': 'Fertility Rate', 'short_name': 'Fertility Rate, 2015', 'source':'World Bank, World Development Indicators'},
{'varname': 'govt_exp_educ_pct_gdp_resid', 'long_name': 'Government Expenditure on Education, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Government Expenditure on Education, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'govt_exp_educ_pct_gdp', 'long_name': 'Government Expenditure on Education, % of Gross Domestic Product, 2015', 'short_name': 'Government Expenditure on Education, % of GDP', 'source':'World Bank, World Development Indicators'},
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
{'varname': 'poverty_headcount_ratio_190_2011_ppp_resid', 'long_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 PPP, Residuals from Regression on GDP per Capita', 'short_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 PPP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'poverty_headcount_ratio_190_2011_ppp', 'long_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 USD PPP, 2015', 'short_name': 'Poverty Headcount Ratio, $1.90 per day in 2011 PPP', 'source':'World Bank, World Development Indicators'},
{'varname': 'recognition_rate_resid', 'long_name': 'Asylum Recognition Rate, Residuals from Regression on GDP per Capita', 'short_name': 'Asylum Recognition Rate, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'recognition_rate', 'long_name': 'Asylum Recognition Rate, %, 2015', 'short_name': 'Asylum Recognition Rate', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees_resid', 'long_name': 'Refugees, Residuals from Regression on GDP per Capita', 'short_name': 'Refugees, residuals', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'refugees', 'long_name': 'Refugees', 'short_name': 'Refugees, 2015', 'source':'United Nations High Commission for Refugees, Population Statistics'},
{'varname': 'remittances_resid', 'long_name': 'Personal remittances from abroad, USD, Residuals from Regression on GDP per Capita', 'short_name': 'Personal remittances from abroad, USD, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'remittances', 'long_name': 'Personal remittances from abroad, USD, 2015', 'short_name': 'Personal remittances', 'source':'World Bank, World Development Indicators'},
{'varname': 'renewable_freshwater_per_capita_resid', 'long_name': 'Renewable Freshwater Resources, cubic meters per capita, Residuals from Regression on GDP per Capita', 'short_name': 'Renewable Freshwater Resources, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'renewable_freshwater_per_capita', 'long_name': 'Renewable Freshwater Resources, cubic meters per capita, 2014', 'short_name': 'Renewable Freshwater Resources', 'source':'World Bank, World Development Indicators'},
{'varname': 'revenue_pct_gdp_resid', 'long_name': 'Government revenue, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Government revenue, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'revenue_pct_gdp', 'long_name': 'Government revenue, % of Gross Domestic Product, 2015', 'short_name': 'Government revenue, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'risk_premium_resid', 'long_name': 'Risk Premium (over US Treasury), Residuals from Regression on GDP per Capita', 'short_name': 'Risk Premium (over US Treasury), Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'risk_premium', 'long_name': 'Risk Premium (over US Treasury), 2015', 'short_name': 'Risk Premium (over US Treasury)', 'source':'World Bank, World Development Indicators'},
{'varname': 'slum_population_pct_urban_population_resid', 'long_name': 'Slum Population, % of Urban Population, Residuals from Regression on GDP per Capita', 'short_name': 'Slum Population, % of Urban Population, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'slum_population_pct_urban_population', 'long_name': 'Slum Population, % of Urban Population, 2014', 'short_name': 'Slum Population, % of Urban Population', 'source':'World Bank, World Development Indicators'},
{'varname': 'strength_legal_rights_0_12_resid', 'long_name': 'Strength of Legal Rights (0-12, 12 high), Residuals from Regression on GDP per Capita', 'short_name': 'Strength of Legal Rights (0-12, 12 high), Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'strength_legal_rights_0_12', 'long_name': 'Strength of Legal Rights (0-12, 12 high), 2015', 'short_name': 'Strength of Legal Rights (0-12, 12 high)', 'source':'World Bank, World Development Indicators'},
{'varname': 'tax_revenue_pct_gdp_resid', 'long_name': 'Tax Revenue, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Tax Revenue, % of Gross Domestic Product, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'tax_revenue_pct_gdp', 'long_name': 'Tax Revenue, % of Gross Domestic Product, 2015', 'short_name': 'Tax Revenue, % of Gross Domestic Product', 'source':'World Bank, World Development Indicators'},
{'varname': 'ti_cpi_resid', 'long_name': 'Corruption Perception Index (reversed), Residuals from Regression on GDP per Capita', 'short_name': 'Corruption Perception Index (reversed), residuals', 'source':'Transparency International'},
{'varname': 'ti_cpi', 'long_name': 'Corruption Perception Index (reversed), 2015', 'short_name': 'Corruption Perception Index (reversed)', 'source':'Transparency International'},
{'varname': 'trade_pct_gdp_resid', 'long_name': 'Trade, % of Gross Domestic Product, Residuals from Regression on GDP per Capita', 'short_name': 'Trade, % of GDP, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'trade_pct_gdp', 'long_name': 'Trade, % of Gross Domestic Product, 2015', 'short_name': 'Trade, % of GDP', 'source':'World Bank, World Development Indicators'},
{'varname': 'urbpop_resid', 'long_name': 'Urban Population, % of Total, Residuals from Regression on GDP per Capita', 'short_name': 'Urban Population, % of Total, Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'urbpop', 'long_name': 'Urban Population, % of Total, 2015', 'short_name': 'Urban Population', 'source':'World Bank, World Development Indicators'},
{'varname': 'use_internet_pct_pop_resid', 'long_name': 'Internet Use, % of Population,  Residuals from Regression on GDP per Capita', 'short_name': 'Internet Use, % of Population,  Residuals', 'source':'World Bank, World Development Indicators'},
{'varname': 'use_internet_pct_pop', 'long_name': 'Internet Use, % of Population, 2015', 'short_name': 'Internet Use', 'source':'World Bank, World Development Indicators'},
#{'varname': 'asylum_seekers_per_pop', 'long_name': 'Asylum Seekers per Population', 'short_name': 'Asylum Seekers per Population', 'source':'United Nations High Commission for Refugees, Population Statistics'},
#{'varname': 'asylum_seekers_per_pop', 'long_name': 'Asylum Seekers per Population', 'short_name': 'Asylum Seekers per Population', 'source':'United Nations High Commission for Refugees, Population Statistics'},
#{'varname': 'refugees_per_pop_resid', 'long_name': 'Refugees per Population, Residuals from Regression on GDP per Capita', 'short_name': 'Refugees per Population', 'source':'United Nations High Commission for Refugees, Population Statistics'},
#{'varname': 'refugees_per_pop', 'long_name': 'Refugees per Population', 'short_name': 'Refugees per Population', 'source':'United Nations High Commission for Refugees, Population Statistics'},

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
    plotly.offline.plot(fig, filename = '../maps/'+ vars[i]['varname'] +'.html', auto_open=False)
