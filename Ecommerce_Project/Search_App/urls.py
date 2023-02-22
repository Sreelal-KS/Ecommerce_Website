from django.urls import path
from . import views

app_name = 'Search_App'
urlpatterns = [
    path('', views.searchResult, name='SearchResult')
]
