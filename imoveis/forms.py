from django import forms
from .models import Locadores, Locatarios, Fiadores

class LocadorForm(forms.ModelForm):
    class Meta:
        model = Locadores
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Quando o tipo estiver definido oculta os campos que nao interessam
        tipo = self.initial.get('tipo') or self.data.get('tipo')
        if tipo == 'F':
            self.fields['cnpj'].widget = forms.HiddenInput()
            self.fields['inscricao_estadual'].widget = forms.HiddenInput()
        elif tipo == 'J':
            self.fields['cpf'].widget = forms.HiddenInput()
            self.fields['identidade'].widget = forms.HiddenInput()    

class LocatarioForm(forms.ModelForm):
    class Meta:
        model = Locatarios 
        fields = '__all__'           

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tipo = self.initial.get('tipo') or self.data.get('tipo')
        if tipo == 'F':
            self.fields['nome_fantasia'].widget = forms.HiddenInput()
            self.fields['cnpj'].widget = forms.HiddenInput()
            self.fields['inscricao_estadual'].widget = forms.HiddenInput()
        elif tipo == 'J':
            self.fields['cpf'].widget = forms.HiddenInput()
            self.fields['identidade'].widget = forms.HiddenInput()

class FiadorForm(forms.ModelForm):
    class Meta:
        model = Fiadores
        fields = '__all__'