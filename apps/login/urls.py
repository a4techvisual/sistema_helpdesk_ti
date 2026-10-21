from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('novoUsuario/', views.novo_usuario, name='novo_usuario'),
]