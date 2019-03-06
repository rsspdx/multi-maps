setwd("~/data/geo/multi-maps")
poc <- read.csv("unhcr_popstats_export_persons_of_concern_all_data.csv", skip=3, stringsAsFactors = FALSE)
names(poc)
names(poc) <- c('year', 'country', 'origin', 'refugees', 'asylum,seekers', 'returned.refugees', 'idps', 'returned.idps', 'stateless', 'others', 'total')
poc.2015 <- poc[poc$year == 2015,]
idps.2015 <- aggregate(idps ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
unhcr.country.to.iso3 <- read.csv("unhcr-country-to-iso3.csv", stringsAsFactors = FALSE)
idps <- merge(idps.2015, unhcr.country.to.iso3, by='country')
write.csv(idps, file="idps.2015.csv")

poc.2015$total <- as.integer(poc.2015$total)
poc.total.2015 <- aggregate(total ~ country, poc.2015, function(x) sum(x, na.rm=TRUE), na.action=na.pass)
poc.total <- merge(poc.total.2015, unhcr.country.to.iso3, by='country')
write.csv(poc.total, file="poc.total.2015.csv")
