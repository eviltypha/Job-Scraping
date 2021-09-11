from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('internshala', views.internshala, name='internshala'),
    path('iimjobs', views.iimjobs, name='iimjobs'),
    path('talentracker', views.talentracker, name='talentracker'),
    path('interesting_urls', views.interesting_urls, name='interesting_urls'),
    path('non_interesting_urls', views.non_interesting_urls,
         name='non_interesting_urls')
]
