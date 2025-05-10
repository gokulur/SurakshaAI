from django.urls import path 
from Home.views import indexPage

urlpatterns = [
    path('index/', indexPage,name='indexPage')
]