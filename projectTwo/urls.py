from django.contrib import admin
from django.urls import path, include
from stocks.views import ClubChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    path('charts/',ClubChartView.as_view(),name='club-chart-view')
]
