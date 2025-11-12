from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list,name='contact_list'),
    path('contact/<int:pk>/',views.contact_details,name='contact_details'),
    path('contact/new/', views.contact_create, name='contact_create'),
    ]