from django.urls import path
from helloapp import views

urlpatterns = [
    path('', views.index, name='home'),
]