from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('exportjson',views.exportjson,name="exportjson"),
    path('exportcsv',views.exportcsv,name="exportcsv"),

]
