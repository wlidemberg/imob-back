from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Imovel, Locadores, Locatarios, Fiadores, LocadorImovel
from .forms import LocadorForm, LocatarioForm, FiadorForm

# Register your models here.


class ImovelLocadorInline(admin.TabularInline):
    model = LocadorImovel
    extra = 1

    def get_formset(self, request, obj = None,  **kwargs):
        formset =  super().get_formset(request, obj, **kwargs)  

        # Validação personalizada dentro do inline
        class ValidatedFormSet(formset):
            def clean(self_inner):
                super().clean()
                total = 0
                for form in self_inner.forms:
                    if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                        total += form.cleaned_data.get('participacao', 0)  
                if total != 100:
                    raise ValidationError(
                        f'A soma dos percentuais dos locadores deve ser 100%. Total atual: {total}%.'
                    )
        return ValidatedFormSet                 

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImovelLocadorInline]
    list_display = ('id', 'titulo', 'tipo', 'preco', 'disponivel', 'data_cadastro', 'locatario', 'fiador')
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

@admin.register(Fiadores)
class FiadoresAdmin(admin.ModelAdmin):
    form = FiadorForm
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone','data_cadastro')
    search_fields = ('nome', 'cpf')
    ordering = ('-data_cadastro',)

class ImovelLocadorInline(admin.TabularInline):
    model = LocadorImovel
    extra = 1

    def get_formset(self, request, obj = None,  **kwargs):
        formset =  super().get_formset(request, obj, **kwargs)  

        # Validação personalizada dentro do inline
        class ValidatedFormSet(formset):
            def clean(self_inner):
                super().clean()
                total = 0
                for form in self_inner.forms:
                    if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                        total += form.cleaned_data.get('participacao', 0)  
                if total != 100:
                    raise ValidationError(
                        f'A soma dos percentuais dos locadores deve ser 100%. Total atual: {total}%.'
                    )
        return ValidatedFormSet                 