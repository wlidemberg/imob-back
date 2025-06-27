from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from .models import ContratoLocacao


# View para listar todos os contratos
@login_required
def lista_contratos(request):
    contratos = ContratoLocacao.objects.all() # Busca todos os contratos no banco
    return render(request, 'contratos/contratoLista.html', {'contratos':contratos})

# View para mostra detahes do contrato
@login_required
def detalhes_contrato(request, contrato_id):
    contrato = get_object_or_404(ContratoLocacao, id=contrato_id) # Busca contrato por id ou mostra 404
    return render(request, 'contratos/contratoDetalhe.html', {'contrato':contrato})



@login_required
def gerar_contrato_pdf(request, contrato_id):
    contrato = ContratoLocacao.objects.get(id=contrato_id)
    html = render_to_string('contratos/contratoPDF.html', {'contrato':contrato})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contrato.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
