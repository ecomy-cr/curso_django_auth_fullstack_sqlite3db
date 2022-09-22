from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciarSesion, name='iniciarSesion'),
    
    path('logout/', views.logOut, name='logout'),
    
]