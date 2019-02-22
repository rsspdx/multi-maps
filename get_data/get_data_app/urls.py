
from django.urls import path
from . import views

app_name = 'get_data_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    path('chart/', views.chart, name='chart'),
]
