from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('filter', views.filter, name='filter'),
    path('do_search', views.do_search, name='do_search'),
]
