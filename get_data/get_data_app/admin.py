from django.contrib import admin

# Register your models here.
from .models import Chart, DataRow

admin.site.register(Chart)
admin.site.register(DataRow)