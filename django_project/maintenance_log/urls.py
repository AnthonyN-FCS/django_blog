from django.urls import path
from . import views

urlpatterns = [
    path('maintenance-log', views.maintenance_home, name='maintenance-log-home'),
]