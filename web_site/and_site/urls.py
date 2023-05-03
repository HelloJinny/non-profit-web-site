from django.urls import path
from . import views

app_name = 'and_site'

urlpatterns = [
    path('', views.home_page_main, name='home_page_main')
]
