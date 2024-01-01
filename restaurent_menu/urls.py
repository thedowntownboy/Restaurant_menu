from django.urls import path
from . import views

urlpatterns =[
    path('', views.MenuList.as_view(), name='home'),   # .as_view since MenuList is a class and class doesn't return
    path('item/<int:pk>', views.MenuItemDetail.as_view(), name='menu_item'),
    path('about', views.about, name="about"),
    path('mybag', views.mybag, name="mybag"),
    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('submit/', views.send, name='send'),
    path('order_confirmed/', views.order_confirmation, name='order_confirmed'),

]