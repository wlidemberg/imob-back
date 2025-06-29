# Generated by Django 5.2.3 on 2025-06-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_locadores_delete_locador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locatarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], default='F', help_text='Tipo de Pessoa: Física ou Jurídica.', max_length=1)),
                ('nome', models.CharField(help_text='Nome do Locatário se pessoa física.', max_length=100)),
                ('cpf', models.CharField(help_text='Digite o CPF do Locador.', max_length=13, unique=True)),
                ('identidade', models.CharField(blank=True, help_text='Documento de Identificação com foto', max_length=20, null=True)),
                ('nome_fantasia', models.CharField(blank=True, help_text='Nome fantasia, caso não possua, deixar em branco.', max_length=100, null=True)),
                ('cnpj', models.CharField(help_text='Digite o CNPJ da empresa.', max_length=18, unique=True)),
                ('inscricao_estadual', models.CharField(blank=True, help_text='Número de inscrição estadual.', max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('endereco', models.CharField(blank=True, max_length=200)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
