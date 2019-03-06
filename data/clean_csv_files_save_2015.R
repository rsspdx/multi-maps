setwd("~/data/geo/multi-maps/data")

access_to_electricity_pct_of_population <- read.csv("access_to_electricity_pct_of_population.csv", stringsAsFactors = FALSE)
access_to_electricity_pct_of_population <- as.data.frame(cbind(access_to_electricity_pct_of_population$Country.Name, access_to_electricity_pct_of_population$Country.Code, access_to_electricity_pct_of_population$X2015), stringsAsFactors = FALSE) 
names(access_to_electricity_pct_of_population) <- c('country', 'country_code', 'access_to_electricity_pct_of_population')
write.csv(access_to_electricity_pct_of_population, file = 'cleaned_2015/access_to_electricity_pct_of_population.csv')

adolescent_fertility_rate <- read.csv("adolescent_fertility_rate.csv", stringsAsFactors = FALSE)
adolescent_fertility_rate <- as.data.frame(cbind(adolescent_fertility_rate$Country.Name, adolescent_fertility_rate$Country.Code, adolescent_fertility_rate$X2015), stringsAsFactors = FALSE) 
names(adolescent_fertility_rate) <- c('country', 'country_code', 'adolescent_fertility_rate')
write.csv(adolescent_fertility_rate, file = 'cleaned_2015/adolescent_fertility_rate.csv')

co2_tons_per_capita <- read.csv("co2_tons_per_capita.csv", stringsAsFactors = FALSE)
co2_tons_per_capita <- as.data.frame(cbind(co2_tons_per_capita$Country.Name, co2_tons_per_capita$Country.Code, co2_tons_per_capita$X2014), stringsAsFactors = FALSE)
names(co2_tons_per_capita) <- c("country", "country_code", "co2_tons_per_capita")
write.csv(co2_tons_per_capita, file = "cleaned_2015/co2_tons_per_capita.csv")

energy_use_per_capita <- read.csv("energy_use_per_capita.csv", stringsAsFactors = FALSE)
energy_use_per_capita <- as.data.frame(cbind(energy_use_per_capita$Country.Name, energy_use_per_capita$Country.Code, energy_use_per_capita$X2014), stringsAsFactors = FALSE)
names(energy_use_per_capita) <- c("country", "country_code", "energy_use_per_capita")
write.csv(energy_use_per_capita, file = "cleaned_2015/energy_use_per_capita.csv")

external_debt_pct_GNI <- read.csv("external_debt_pct_GNI.csv", stringsAsFactors = FALSE)
external_debt_pct_GNI <- as.data.frame(cbind(external_debt_pct_GNI$Country.Name, external_debt_pct_GNI$Country.Code, external_debt_pct_GNI$X2014), stringsAsFactors = FALSE)
names(external_debt_pct_GNI) <- c("country", "country_code", "external_debt_pct_GNI")
write.csv(external_debt_pct_GNI, file = "cleaned_2015/external_debt_pct_GNI.csv")

fdi_net_current_usd <- read.csv("fdi_net_current_usd.csv", stringsAsFactors = FALSE)
fdi_net_current_usd <- as.data.frame(cbind(fdi_net_current_usd$Country.Name, fdi_net_current_usd$Country.Code, fdi_net_current_usd$X2014), stringsAsFactors = FALSE)
names(fdi_net_current_usd) <- c("country", "country_code", "fdi_net_current_usd")
write.csv(fdi_net_current_usd, file = "cleaned_2015/fdi_net_current_usd.csv")

female_employment_pct_of_total <- read.csv("female_employment_pct_of_total.csv", stringsAsFactors = FALSE)
female_employment_pct_of_total <- as.data.frame(cbind(female_employment_pct_of_total$Country.Name, female_employment_pct_of_total$Country.Code, female_employment_pct_of_total$X2014), stringsAsFactors = FALSE)
names(female_employment_pct_of_total) <- c("country", "country_code", "female_employment_pct_of_total")
write.csv(female_employment_pct_of_total, file = "cleaned_2015/female_employment_pct_of_total.csv")

female_literacy_pct <- read.csv("female_literacy_pct.csv", stringsAsFactors = FALSE)
female_literacy_pct <- as.data.frame(cbind(female_literacy_pct$Country.Name, female_literacy_pct$Country.Code, female_literacy_pct$X2014), stringsAsFactors = FALSE)
names(female_literacy_pct) <- c("country", "country_code", "female_literacy_pct")
write.csv(female_literacy_pct, file = "cleaned_2015/female_literacy_pct.csv")

fertility_rate <- read.csv("fertility_rate.csv", stringsAsFactors = FALSE)
fertility_rate <- as.data.frame(cbind(fertility_rate$Country.Name, fertility_rate$Country.Code, fertility_rate$X2014), stringsAsFactors = FALSE)
names(fertility_rate) <- c("country", "country_code", "fertility_rate")
write.csv(fertility_rate, file = "cleaned_2015/fertility_rate.csv")

gdp_per_capita <- read.csv("gdp_per_capita.csv", stringsAsFactors = FALSE)
gdp_per_capita <- as.data.frame(cbind(gdp_per_capita$Country.Name, gdp_per_capita$Country.Code, gdp_per_capita$X2014), stringsAsFactors = FALSE)
names(gdp_per_capita) <- c("country", "country_code", "gdp_per_capita")
write.csv(gdp_per_capita, file = "cleaned_2015/gdp_per_capita.csv")

govt_exp_educ_pct_gdp <- read.csv("govt_exp_educ_pct_gdp.csv", stringsAsFactors = FALSE)
govt_exp_educ_pct_gdp <- as.data.frame(cbind(govt_exp_educ_pct_gdp$Country.Name, govt_exp_educ_pct_gdp$Country.Code, govt_exp_educ_pct_gdp$X2014), stringsAsFactors = FALSE)
names(govt_exp_educ_pct_gdp) <- c("country", "country_code", "govt_exp_educ_pct_gdp")
write.csv(govt_exp_educ_pct_gdp, file = "cleaned_2015/govt_exp_educ_pct_gdp.csv")

hiv_prevalence <- read.csv("hiv_prevalence.csv", stringsAsFactors = FALSE)
hiv_prevalence <- as.data.frame(cbind(hiv_prevalence$Country.Name, hiv_prevalence$Country.Code, hiv_prevalence$X2014), stringsAsFactors = FALSE)
names(hiv_prevalence) <- c("country", "country_code", "hiv_prevalence")
write.csv(hiv_prevalence, file = "cleaned_2015/hiv_prevalence.csv")

life_expectancy <- read.csv("life_expectancy.csv", stringsAsFactors = FALSE)
life_expectancy <- as.data.frame(cbind(life_expectancy$Country.Name, life_expectancy$Country.Code, life_expectancy$X2014), stringsAsFactors = FALSE)
names(life_expectancy) <- c("country", "country_code", "life_expectancy")
write.csv(life_expectancy, file = "cleaned_2015/life_expectancy.csv")

lowest_twenty_income_share <- read.csv("lowest_twenty_income_share.csv", stringsAsFactors = FALSE)
lowest_twenty_income_share <- as.data.frame(cbind(lowest_twenty_income_share$Country.Name, lowest_twenty_income_share$Country.Code, lowest_twenty_income_share$X2014), stringsAsFactors = FALSE)
names(lowest_twenty_income_share) <- c("country", "country_code", "lowest_twenty_income_share")
write.csv(lowest_twenty_income_share, file = "cleaned_2015/lowest_twenty_income_share.csv")

maternal_mortality_rate <- read.csv("maternal_mortality_rate.csv", stringsAsFactors = FALSE)
maternal_mortality_rate <- as.data.frame(cbind(maternal_mortality_rate$Country.Name, maternal_mortality_rate$Country.Code, maternal_mortality_rate$X2014), stringsAsFactors = FALSE)
names(maternal_mortality_rate) <- c("country", "country_code", "maternal_mortality_rate")
write.csv(maternal_mortality_rate, file = "cleaned_2015/maternal_mortality_rate.csv")

mortality_under_5_per_1000_live_births <- read.csv("mortality_under_5_per_1000_live_births.csv", stringsAsFactors = FALSE)
mortality_under_5_per_1000_live_births <- as.data.frame(cbind(mortality_under_5_per_1000_live_births$Country.Name, mortality_under_5_per_1000_live_births$Country.Code, mortality_under_5_per_1000_live_births$X2014), stringsAsFactors = FALSE)
names(mortality_under_5_per_1000_live_births) <- c("country", "country_code", "mortality_under_5_per_1000_live_births")
write.csv(mortality_under_5_per_1000_live_births, file = "cleaned_2015/mortality_under_5_per_1000_live_births.csv")

net_migration <- read.csv("net_migration.csv", stringsAsFactors = FALSE)
net_migration <- as.data.frame(cbind(net_migration$Country.Name, net_migration$Country.Code, net_migration$X2014), stringsAsFactors = FALSE)
names(net_migration) <- c("country", "country_code", "net_migration")
write.csv(net_migration, file = "cleaned_2015/net_migration.csv")

oda_pct_of_gni <- read.csv("oda_pct_of_gni.csv", stringsAsFactors = FALSE)
oda_pct_of_gni <- as.data.frame(cbind(oda_pct_of_gni$Country.Name, oda_pct_of_gni$Country.Code, oda_pct_of_gni$X2014), stringsAsFactors = FALSE)
names(oda_pct_of_gni) <- c("country", "country_code", "oda_pct_of_gni")
write.csv(oda_pct_of_gni, file = "cleaned_2015/oda_pct_of_gni.csv")

poverty_headcount_ratio_190_2011_ppp <- read.csv("poverty_headcount_ratio_190_2011_ppp.csv", stringsAsFactors = FALSE)
poverty_headcount_ratio_190_2011_ppp <- as.data.frame(cbind(poverty_headcount_ratio_190_2011_ppp$Country.Name, poverty_headcount_ratio_190_2011_ppp$Country.Code, poverty_headcount_ratio_190_2011_ppp$X2014), stringsAsFactors = FALSE)
names(poverty_headcount_ratio_190_2011_ppp) <- c("country", "country_code", "poverty_headcount_ratio_190_2011_ppp")
write.csv(poverty_headcount_ratio_190_2011_ppp, file = "cleaned_2015/poverty_headcount_ratio_190_2011_ppp.csv")

remittances <- read.csv("remittances.csv", stringsAsFactors = FALSE)
remittances <- as.data.frame(cbind(remittances$Country.Name, remittances$Country.Code, remittances$X2014), stringsAsFactors = FALSE)
names(remittances) <- c("country", "country_code", "remittances")
write.csv(remittances, file = "cleaned_2015/remittances.csv")

revenue_pct_gdp <- read.csv("revenue_pct_gdp.csv", stringsAsFactors = FALSE)
revenue_pct_gdp <- as.data.frame(cbind(revenue_pct_gdp$Country.Name, revenue_pct_gdp$Country.Code, revenue_pct_gdp$X2014), stringsAsFactors = FALSE)
names(revenue_pct_gdp) <- c("country", "country_code", "revenue_pct_gdp")
write.csv(revenue_pct_gdp, file = "cleaned_2015/revenue_pct_gdp.csv")

strength_legal_rights_0_12 <- read.csv("strength_legal_rights_0_12.csv", stringsAsFactors = FALSE)
strength_legal_rights_0_12 <- as.data.frame(cbind(strength_legal_rights_0_12$Country.Name, strength_legal_rights_0_12$Country.Code, strength_legal_rights_0_12$X2014), stringsAsFactors = FALSE)
names(strength_legal_rights_0_12) <- c("country", "country_code", "strength_legal_rights_0_12")
write.csv(strength_legal_rights_0_12, file = "cleaned_2015/strength_legal_rights_0_12.csv")

urbpop <- read.csv("urbpop.csv", stringsAsFactors = FALSE)
urbpop <- as.data.frame(cbind(urbpop$Country.Name, urbpop$Country.Code, urbpop$X2014), stringsAsFactors = FALSE)
names(urbpop) <- c("country", "country_code", "urbpop")
write.csv(urbpop, file = "cleaned_2015/urbpop.csv")