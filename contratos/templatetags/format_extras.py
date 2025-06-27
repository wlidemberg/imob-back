from django import template
register = template.Library()
@register.filter()
def brl(valor):
    try:
        valor_float = float(valor)
        # Formata com o padrão americano ex: 1,500.00
        formatUsdt = f'{valor_float:,.2f}'
        # Troca o separador de milhar de ',' para '.' e decimal de '.' para ','
        formatBrl = formatUsdt.replace(',', 'v').replace('.', ',').replace('v', '.')
        return f'R$ {formatBrl}'
    except:
        return valor


