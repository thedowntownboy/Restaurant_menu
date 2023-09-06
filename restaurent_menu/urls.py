from django.urls import path
from . import views

urlpatterns =[
    path('', views.MenuList.as_view(), name='home')      # .as_view since MenuList is a class and class doesn't return
]