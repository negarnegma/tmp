from django.urls import path
from api import views

name = 'api'

urlpatterns = [
    path('pidetail/<str:name>', views.PointDetail.as_view(), name='point_detail'),
    path('macLocations', views.MapLocations.as_view(), name='point_detail'),
]
