from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('/Search/<str:query>',views.Filter,name="filter"),
    
]
