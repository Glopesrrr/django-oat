from django.urls import path
from app_gestao_financeira import views


urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.home, name='home'),

    path('usuarios/', views.usuarios, name='financeiro')
]
