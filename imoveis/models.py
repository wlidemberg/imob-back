from django.db import models

# Create your models here.


# Modelo Imovel
class Imovel(models.Model):
    # Campos básicos do imóvel
    titulo = models.CharField(
        max_length=100,
        help_text='Título ou nome do imóvel(Ex: Casa em Paraty)'
    )

    descricao = models.TextField(
        blank=True,
        help_text='Descrição detalhada do imóvel'
    )

    endereco = models.CharField(
        max_length=200,
        help_text='Endereço completo do imóvel'
    )

    # Definindo tipos de imóves
    tipo_imovel = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('SA', 'Sala'),
        ('LJ', 'Loja'),
        ('SBJ', 'Sobreloja'),
        ('GP', 'Galpão'),
        ('TE', 'Terreno'),
        ('PT', 'Parte'), # quando é somente parte de um imovel
    ]

    tipo = models.CharField(
        max_length=3,
        choices=tipo_imovel,
        default='CA',
        help_text='Tipo do Imóvel'
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Valor do imóvel (Ex.: 1000000,00).'
    )

    disponivel = models.BooleanField(
        default=True,
        help_text='Se está disponível para venda ou locação.'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        help_text='Data em que o imóvel foi cadastrado.'
    )

    data_atualizacao = models.DateTimeField(
        auto_now=True,
        help_text='Data da ultima atualização.'
    )

    # Representação do objeto no admin e nos logs
    def __str__(self):
        return f'{self.titulo} - {self.get_tipo_display()}'
    
# Modelo Locadores (quem aluga o imóvel)
class Locadores(models.Model):
    TIPO_PESSOA = [
        ('F', 'Pessoa Fisíca'),
        ('J', 'Pessoa Jurídica')
    ]

    tipo = models.CharField(
        max_length=1,
        choices=TIPO_PESSOA,
        default='F',
        help_text='Tipo de Pessoa: Fisíca ou Jurídica'
    )

    nome = models.CharField(
        max_length=100,
        help_text='Nome completo do Locador'
    )
    cpf = models.CharField(
        max_length=13,
        unique=True,
        help_text='Digite o CPF do Locador'
    )

    identidade = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Documento de Identificação com Foto'
    )

    cnpj = models.CharField(
        max_length=18,
        unique=True,
        help_text='Digite o CNPJ da Empresa'
    )

    inscricao_estadual = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Inscrição estadual empresa'
    )

    email = models.EmailField(
        blank=True,
        help_text='Email para contato'
    )
    telefone = models.CharField(
        max_length=20,
        blank=True,
        help_text='Telefone para contato'
    )
    endereco = models.CharField(
        max_length=200,
        blank=True,
        help_text='Endereço Locador'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        help_text='Data que o locador fo cadastrado'
    )

    def __str__(self):
        return f'{self.nome} - {self.get_tipo_display()}'    