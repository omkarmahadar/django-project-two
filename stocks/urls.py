from django.urls import path
from django.conf.urls import url
from . import views

app_name='stocks'

urlpatterns = [
	path('',views.home, name='home'),
	path('bar/', views.bar, name='bar'),
	path('doughnut/', views.doughnut, name='doughnut'),
	path('line/',views.line, name='line'),

	path('bar/get_data_bar/', views.get_data_bar, name='get_data_bar'),
	path('doughnut/get_data_doughnut/',views.get_data_doughnut, name='get_data_doughnut'),
	path('line/get_data_line/', views.get_data_line, name='get_data_line')

]

