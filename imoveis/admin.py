from django.contrib import admin
from .models import Imovel, Locadores

# Register your models here.

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'preco', 'disponivel', 'data_cadastro')
    list_filter = ('tipo', 'disponivel')
    search_fields = ('titulo', 'endereco')
    ordering = ('-data_cadastro',)

@admin.register(Locadores)
class LocadoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone', 'data_cadastro')    
    search_fields = ('nome', 'cpf')
    ordering = ('-data_cadastro', )
