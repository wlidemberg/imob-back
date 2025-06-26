from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from .models import ContratoLocacao



# Create your views here.
def gerar_contrato_pdf(request, contrato_id):
    contrato = ContratoLocacao.objects.get(id=contrato_id)
    html = render_to_string('contratos/contratoPDF.html', {'contrato':contrato})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contrato.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
