from django.shortcuts import render

from .models import Imovel

# Create your views here.

# View pública para listar imóveis
def lista_imoveis(request):
    imoveis = Imovel.objects.filter(disponivel=True).order_by('-data_cadastro')
    return render(request, 'imoveis/lista_imoveis.html', {'imoveis':imoveis})
