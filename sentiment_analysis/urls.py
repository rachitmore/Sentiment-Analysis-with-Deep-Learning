from django.urls import path
from . import views

app_name = 'sentiment_analysis'

urlpatterns = [
    path('', views.home, name='home'),

]
