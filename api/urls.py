from django.urls import path 
from Home.views import IndexPageView

urlpatterns = [
    path('index/', IndexPageView.as_view(),name='indexPage')
]