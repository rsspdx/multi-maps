from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import plotly


from .models import Country, Chart, DataRow

def index(request):
    charts = Chart.objects.all()
    return render(request, 'get_data_app/index.html', {'charts': charts})


def get_chart_data(request):
    # get the chart id as a query parameter
    # get all the chart data associated with that chart
    # put it into a list
    # return a jsonresponse
    # chart = Chart.objects.filter(pk=chart_id)
    pass
   



def chart(request):
    chart_html = ''
    with open('get_data_app/charts/chart.html', 'r') as f:
        chart_html = f.read()
    return render(request, 'get_data_app/chart.html', {'chart_html': chart_html})


