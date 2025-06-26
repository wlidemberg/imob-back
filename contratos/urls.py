from django.urls import path
from .views import gerar_contrato_pdf

urlpatterns = [
    path('pdf/<int:contrato_id>/', gerar_contrato_pdf, name='gerar_pdf_contrato'),
]