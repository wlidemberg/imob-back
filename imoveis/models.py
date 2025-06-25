from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

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

    locadores = models.ManyToManyField('Locadores', through='LocadorImovel', related_name='imoveis', help_text='Locadores Vinculados a esse imóvel')

    # Locatário atual do imóvel (opcional, por que nem todo imovel está alugado)
    """
        Logica a ser implementada:
        Se não houver Locatário automaticamente imóvel será considerado disponível
    """
    locatario = models.ForeignKey(
        'Locatarios', 
        on_delete=models.SET_NULL, # Mesmo que o Locatario seja excluido o imóvel permanece
        null=True,
        blank=True,
        help_text='Locatário atual do imóvel(se alugado)'
    )

    # Fiador atual (opcional)
    """
        Logica a ser implementada:
        Se não houver Fiador automaticamente sera considerado 03 meses deposito garantia (valor aluguel)
    """
    fiador = models.ForeignKey(
        'Fiadores',
        on_delete=models.SET_NULL, # Mesmo que o fiador seja excluido o locatário permanece
        null=True,
        blank=True,
        help_text='Fiador do Locatario se houver'
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
    
    # Validação do percentual do imovel
    """def clean(self):
        total = sum(
            li.participa for li in LocadorImovel.objects.filter(imovel=self)
        )
        if total != 100:
            raise ValidationError(
                f'A soma dos percentuais dos locadores deve ser exatamente 100%. Atualmente {total}%.'
            )"""
    
# Modelo ImovelLocador responsavel por criar a relaçao imovel / locador e seu percentual de participação
class LocadorImovel(models.Model):
    imovel = models.ForeignKey('Imovel', on_delete=models.CASCADE)
    locador = models.ForeignKey('Locadores', on_delete=models.CASCADE)
    participacao = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Percentual de Participação de Locação do Imóvel.'
    )

    class Meta:
        unique_together = ('imovel', 'locador')

    def __str__(self):
        return f'{self.locador.nome} - {self.participacao}% do {self.imovel.titulo}'      
    
# Modelo Locadores (quem disponibiliza o imóvel)
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
        null=True,
        blank=True,
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
        null=True,
        blank=True,
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
    
# Modelo Locatário (quem aluga o imovel)
class Locatarios(models.Model):
    TIPO_PESSOA = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica')
    ]

    tipo = models.CharField(
        max_length=1,
        choices=TIPO_PESSOA,
        default='F',
        help_text='Tipo de Pessoa: Física ou Jurídica.'
    )

    nome = models.CharField(
        max_length=100,
        help_text='Nome do Locatário se pessoa física.'
    )

    cpf = models.CharField(
        max_length=13,
        unique=True,
        null=True,
        blank=True,
        help_text='Digite o CPF do Locador.'
    )

    identidade = models.CharField(
        max_length=20,
        help_text='Documento de Identificação com foto',
        null=True,
        blank=True
    )

    nome_fantasia = models.CharField(
        max_length=100,
        help_text='Nome fantasia, caso não possua, deixar em branco.',
        null=True,
        blank=True
    )

    cnpj = models.CharField(
        max_length=18,
        unique=True,
        null=True,
        blank=True,
        help_text='Digite o CNPJ da empresa.'
    )

    inscricao_estadual = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='Número de inscrição estadual.'
    )

    email = models.EmailField(
        blank=True
    )

    telefone = models.CharField(
        max_length=20, 
        blank=True
    )

    endereco = models.CharField(
        max_length=200,
        blank=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.nome} - {self.get_tipo_display()}'
    
    def clean(self):
        """ Valida o CPF ou CNPJ de acordo com o tipo """
        if self.tipo == 'F':
            if not self.cpf:
                raise ValidationError({'cpf' : 'CPF é obrigatório para pessoa física.'})
            
            if not CPF().validate(self.cpf):
                raise ValidationError({'cpf':'CPF inválido'})

        elif self.tipo == 'J':
            if not self.cnpj:
                raise ValidationError({'cnpj':'CNPJ é obrigatório para pessoa jurídica.'})
            if not CNPJ().validate(self.cnpj):
                raise ValidationError({'cnpj':'CNPJ inválido.'})

# Modelo Fiador (garantidor do pagamento do aluguel)
class Fiadores(models.Model):
    nome = models.CharField(
        max_length=100,
        help_text='Nome do Fiador'
    )                

    cpf = models.CharField(
        max_length=13,
        unique=True,
        help_text='Digite o CPF do Fiador.'
    )

    identidade = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='Documento de identificação com foto.'
    )

    email = models.EmailField(
        blank=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
    )
    
    endereco = models.CharField(
        max_length=200,
        blank=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.nome} - {self.cpf}'
    
    def clean(self):
        if not CPF().validate(self.cpf):
            raise ValidationError({'cpf':'CPF inválido.'})