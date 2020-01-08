from django.urls import path

from . import views

app_name = 'AIA'

urlpatterns = [
    path( '', views.index, name='index'),
]
