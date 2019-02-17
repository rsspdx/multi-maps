setwd("~/data/geo/multi-maps")
poc <- read.csv("unhcr_popstats_export_persons_of_concern_all_data.csv", skip=3, stringsAsFactors = FALSE)
# names(poc)
names(poc) <- c('year', 'country', 'origin', 'refugees', 'asylum.seekers', 'returned.refugees', 'idps', 'returned.idps', 'stateless', 'others', 'total')
poc.2015 <- poc[poc$year == 2015,]
idps.2015 <- aggregate(idps ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
unhcr.country.to.iso3 <- read.csv("unhcr-country-to-iso3.csv", stringsAsFactors = FALSE)
idps <- merge(idps.2015, unhcr.country.to.iso3, by='country')
write.csv(idps, file="idps.2015.csv")

poc.2015$total <- as.integer(poc.2015$total)
poc.total.2015 <- aggregate(total ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
poc.total <- merge(poc.total.2015, unhcr.country.to.iso3, by='country')
write.csv(poc.total, file="poc.total.2015.csv")

poc.2015$asylum.seekers <- as.integer(poc.2015$asylum.seekers)
asylum.seekers <- aggregate(asylum.seekers ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
poc.asylum.seekers <- merge(asylum.seekers, unhcr.country.to.iso3, by="country")
write.csv(poc.asylum.seekers, file="poc.asylum.seekers.2015.csv")

poc.2015$refugees <- as.integer(poc.2015$refugees)
refugees <- aggregate(refugees ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
poc.refugees <- merge(refugees, unhcr.country.to.iso3, by="country")
write.csv(poc.refugees, file="poc.refugees.2015.csv")

pop <- read.csv("API_SP.POP.TOTL_DS2_en_csv_v2_10383678.csv", skip=3, stringsAsFactors = FALSE)
pop.2015 <- as.data.frame(cbind(pop$Country.Name, pop$Country.Code, pop$X2015), stringsAsFactors = FALSE)
names(pop.2015) <- c('country', 'country.code', 'population')
pop.2015$population <- as.integer(pop.2015$population)
pop.2015$pop.million <- pop.2015$population / 1e6


poc.2015$refugees <- as.integer(poc.2015$refugees)
refugees <- aggregate(refugees ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
poc.refugees <- merge(refugees, unhcr.country.to.iso3, by="country")
poc.refugees <- merge(poc.refugees, pop.2015, by.x="country.code", by.y="country.code")
poc.refugees$refugees.per.million.pop <- round(poc.refugees$refugees / poc.refugees$pop.million, 0)
poc.refugees$country <- poc.refugees$country.x
write.csv(poc.refugees, file="poc.refugees.2015.csv")
