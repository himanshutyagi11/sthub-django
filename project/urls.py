from django.contrib import admin
from django.urls import path
from . import views
from .views import export_contacts_to_excel

urlpatterns = [
path ("",views.index, name = "index"),
path("about", views.about, name = "about"),
path("contact", views.contact, name = "contact"),
path('', views.index, name='submit_form'),
path('export-contacts/', export_contacts_to_excel, name='export_contacts'),


]