from django.urls import include, path
from rest_framework import routers
from myproject.core import views as v
from .views import list_func, create_func, update_func, delete_func, info_func, SearchResultsView
from . import views


app_name = 'core'


urlpatterns = [
    path('', list_func, name='list_func'),
    path('new/', create_func, name='create_func'),
    path('update/<int:id>/', update_func, name='update_func'),
    path('delete/<int:id>/', delete_func, name='delete_func'),
    path('list_func/', list_func, name='list_func'),
    path('info/<int:id>/', info_func, name='info_func'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
