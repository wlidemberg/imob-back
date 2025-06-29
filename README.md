# 🏠 Sistema Imobiliário Modular

Sistema de gestão imobiliária, com funcinalidades de cadastros, listagem e administração imóveis, Locadores, Locatários, Fiadores, Contratos e Corretores

## Tecnologias Utilizadas

- ✅ [Python 3.10+](https://www.python.org/)
- ✅ [Django 4.x](https://www.djangoproject.com/)
- ✅ SQLite (fase inicial)
- ✅ Django Admin
- ✅ Git e GitHub para versionamento

## Como rodar o projeto localmente
1. Clone o repositório:
```
    bash
    git clone git@github.com:wlidemberg/imob-back.git
    cd imob-back
```
2. Crie um ambiente virtual:
```
bash
python -m venv venv
venv\Scripts\activate (windows)
source venv\bin\activate (mac e linux)
```

3. Instale as dependências:
```
bash
pip install django
```

4. Execute as migrações do banco:
```
bash
python manage.py migrate
```

5. Crie um superusuário:
```
bash
python manage.py createsuperuser
```

6. Rode o servidor:
```
bash
python manage.py runserver
```

7. Acesse:

- Sistema: http://127.0.0.1:8000/

 - Admin: http://127.0.0.1:8000/admin
___
# ✅ Funcionalidades 
- [x] Criação do Projeto
- [x] Configuração do ambiente virtual
- [x] Modelo Imovel com:- 
    - Titulo
    - Descrição
    - Endereço
    - Tipo
    - Preço
    - Disponibilidade
- [x] Integração com Django Admin
- [x] Controle de versão com Git e Github
- [x] Templates públicos para listagem de imóveis
    - Página acessivel em `/`
    - Exibição dos imoveis disponíveis
    - HTML com estilização basica
    - Exibição de título, descrição, tipo, endereço, preço
- [x] Cadastro de Locadores
    - Por tipo de pessoa: Física ou Jurídica
    - Dados especificos por tipo de pessoa
    - Nome, email, telefone, endereço
    - Integração com Django Admin
- [x] Cadastro de Locatários
    - Seleção por tipo pessoa: Física ou Jurídica
    - Validação CPF/CNPJ usando a biblioteca [validate-docbr](https://pypi.org/project/validate-docbr/)
    - Formulário Admin Locatarios com campos dinâmicos
- [x] Cadastro de Fiadores
    - Validação CPF usando a biblioteca [validate-docbr](https://pypi.org/project/validate-docbr/)

- [x] Modelo Intermediario LocadorImovel
    - Relacionamento N:N entre `Imovel` e `Locadores`
    - Validação de 100% da soma
    - Admin inline para adcionar Locadores ao imovel diretamente

- [x] Relacionamento `Imóvel` com: 
    - `Locatarios`(um para muitos, opcional)
    - `Fiador` (opcional)
- [x] Criar Modelo Contrato de Locação 
    - Imóvel, Locatário e Fiador(opcional)
    - Datas de inicio e Fim
    - valor do aluguel
    - Reajuste Anual, Semestral e Trienal
    - Situação: Ativo, Encerrado e Rescidido
- [x] Admin personalizada com busca, filtros e ordenação
- [x] Implementação do Contrato em PDF
    - Implementação dos templates de Lista de Contratos e Detalhes do Contrato
    - Configuração das views
    - formatação de data e moeda
    - Tela de Login para a as views de contrato
    


___

# 🙋‍♂️ Autor
Desenvolvido por Berg Sousa \

📧 Contato [[Instagram](https://www.instagram.com/sousa.berg.80/)]
___
# 📄 Licença
Este projeto está sob a licença MIT.


 



