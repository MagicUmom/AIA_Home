from django.urls import path, include

from . import views

app_name = 'AIA'

urlpatterns = [
    path( '', views.index, name='index'),

]
