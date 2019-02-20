from django.db import models



class Chart(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    longname = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)

    def __str__(self):
        return self.shortname

class DataRow(models.Model):
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    varname = models.ForeignKey(Chart, on_delete=models.PROTECT)
    value = models.FloatField(null=True, blank=True)
    year = models.IntegerField()
    indicator = models.CharField(max_length=100)
    longname = models.CharField(max_length = 500)
    shortname = models.CharField(max_length=100)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name