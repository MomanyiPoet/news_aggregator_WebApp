from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('scrape/', views.scrape, name='scrape'),
]