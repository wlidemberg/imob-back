from django.contrib import admin
from .models import Imovel, Locadores, Locatarios
from .forms import LocadorForm, LocatarioForm

# Register your models here.

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'preco', 'disponivel', 'data_cadastro')
    list_filter = ('tipo', 'disponivel')
    search_fields = ('titulo', 'endereco')
    ordering = ('-data_cadastro',)

@admin.register(Locadores)
class LocadoresAdmin(admin.ModelAdmin):
    form = LocadorForm
    list_display = ('id', 'nome', 'cpf', 'cnpj','email', 'telefone', 'data_cadastro') 
    list_filter = ('tipo',)   
    search_fields = ('nome', 'cpf', 'cnpj')
    ordering = ('-data_cadastro', )

    class Media:
        js = ('imoveis/admin.js',)


@admin.register(Locatarios)
class LocatariosAdmin(admin.ModelAdmin):
    form = LocatarioForm
    list_display = ('id', 'nome', 'cpf', 'cnpj', 'email', 'telefone', 'endereco', 'data_cadastro')
    list_filter = ('tipo',)
    search_fields = ('nome', 'cpf', 'cnpj')
    ordering = ('-data_cadastro',)

    class Media:
        js = ('imoveis/admin.js',)