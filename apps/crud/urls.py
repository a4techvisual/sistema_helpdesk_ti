from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('novoChamado/', views.novo_chamado, name='novo-chamado'),
    path('novoChamadoSucesso/<int:codigo_chamado>', views.novo_chamado_sucesso, name='novo_chamado_sucesso'),
    path('alterarChamado/<int:codigo_chamado>', views.alterar_chamado, name='alterar_chamado'),
    path('excluirChamado/<int:codigo_chamado>', views.excluir_chamado, name='excluir_chamado'),
    path('buscar/', views.buscar_chamado, name='buscar_chamado'),
]
