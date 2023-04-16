from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home,name="home"),
    path('login',views.log,name="log"),
    path('reg',views.reg,name="reg"),
    path('logo',views.logo,name="logo")
]