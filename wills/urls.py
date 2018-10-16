from django.urls import path
from . import views

urlpatterns = [
    path('', views.allwills, name="allwills"),

]