from django.contrib import admin
from .models import ContratoLocacao

# Register your models here.
@admin.register(ContratoLocacao)
class ContratoLocacaoAdmin(admin.ModelAdmin):
    # Define os campos que aparecerão na listagem principal do admin
    list_display = ('id', 'imovel', 'locatario', 'fiador', 'data_inicio', 'data_fim', 'valor_aluguel', 'status')
    
    # Permite buscar contratos por nome do imovel, nome do locatario e nome do fiador
    search_fields = ('imovel__titulo', 'locatario__nome', 'fiador__nome')

    # Filtros laterais para facilitar navegação
    list_filter = ('tipo', 'status', 'periodo_reajuste', 'data_inicio')

    # Ordenação pode data de inicio
    ordering = ('-data_inicio',) 

    # Torna campos os campos de datas automaticas somente leitura
    readonly_fields = ('data_criacao', 'data_atualizacao')  

    # Organiza os campos do formulário em seções
    fieldsets = (
        ('Informações de Contrato', {
            'fields':(
                'imovel',
                'tipo',
                'locatario',
                'fiador',
                'status',
                'valor_aluguel',
                'data_inicio',
                'data_fim',
                'observacoes',
            )
        }),
        ('Controle Interno',{
            'fields':('data_criacao', 'data_atualizacao')
        })
    )              
