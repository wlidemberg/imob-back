from django.urls import path
from . import views
from .views import gerar_contrato_pdf

urlpatterns = [
    path('', views.lista_contratos, name='lista_contratos'), # Listas todos os contratos
    path('<int:contrato_id>/', views.detalhes_contrato, name='detalhes_contrato'), # Detalhes
    path('pdf/<int:contrato_id>/', gerar_contrato_pdf, name='gerar_pdf_contrato'), # PDF downloads
]