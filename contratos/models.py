from django.db import models
from imoveis.models import Imovel, Locadores, Locatarios, Fiadores



# Create your models here.

# Modelo de Contrato de Locação
class ContratoLocacao(models.Model):
    STATUS_LOC = [
        ('A', 'Ativo'),
        ('E', 'Encerrado'),
        ('R', 'Rescidido')
    ]

    TIPO_LOCACAO = [
        ('RESIDENCIAL', 'Residencial'),
        ('NAO_RESIDENCIAL', 'Não Residencial'),
        ('COMERCIAL', 'Comercial')
    ]  

    # Umóvel que esta sendo o objeto da locação
    imovel = models.ForeignKey(
        Imovel, # Relacionameto com modelo Imóvel
        on_delete=models.PROTECT, # Impede a exclusão de um imóvel se existir um contrato
        help_text='Imóvel alugado por este contrato.'
    ) 

    tipo = models.CharField(
        max_length=30, 
        choices=TIPO_LOCACAO, 
        default='RESIDENCIAL',
        help_text='TIPO LOCAÇÃO: RESIDENCIAL(36 MESES) - NÃO RESIDENCIAL: (DE 12 A 60 MESES) - COMERCIAL: (60 MESES)') 

    # Locatario (Pessoa ou Empresa) que esta alugando o imóvel
    locatario = models.ForeignKey(
        Locatarios, # Relacionamenro com o modelo Locatário
        on_delete=models.PROTECT, # Imoede a exclusão do Locatário se houver um contrato ativo
        help_text='Pessoa ou empresa que esta alugando o imóvel'
    )

    # Fiador (Opcional ), pode ser nulo
    fiador = models.ForeignKey(
        Fiadores, # Relacionamento com modelo Fiadores
        on_delete=models.SET_NULL, # Se o fiador for excluido o campo fica vazio( onferir isso depois)
        null=True,
        blank=True,
        help_text='Fiador, responsavel pelo pagamento se nao houver(opcinal)'
    ) 

    # Data do inicio de vigencia do contrato
    data_inicio = models.DateField()

    # Data prevista para o fim da vigencia
    """
        Logica a ser implementada:
        calculo deve acontecer de acordo com o tipo de contrato:
        RESIDENCIAL: 36 MESES
        NÃO_RESIDENCIAL: ATE 36 MESES
        COMERCIAL: 60 MESES
    """
    data_fim = models.DateField()

    # Valor Mensal do aluguel (pode ser até 9999999,99)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def save(self, *args, **kwargs):
        # Se valor_aluguel não foi preenchido (None ou vazio), pegar do imovel.preco
        if self.valor_aluguel is None:
            self.valor_aluguel = self.imovel.preco
        super().save(*args, **kwargs)

    # Periodicidade de Reajuste do valor do aluguel
    periodo_reajuste = models.CharField(
        max_length=20,
        choices=[('ANUAL', 'Anual'), ('SEMESTRAL', 'Semestral'), ('TRIENAL', 'Trienal')],
        default='ANUAL'
    )

    # Status atual do contrato
    status = models.CharField(max_length=15, choices=STATUS_LOC, default='ATIVO')

    # Campo opcional para anotações adicionais
    observacoes = models.TextField(blank=True)

    # Data da criação do contrato
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Data da ultima atualização
    data_atualizacao = models.DateTimeField(auto_now=True)

    # Como o contrato sera exibido no admin e me representações
    def __str__(self):
        return f'{self.locatario} - {self.imovel}'

