import locale

# Define o locale para o formato do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor = 10000.20

# formatando o número como moeda
valor_formatado = locale.currency(valor, grouping = True)


print(valor)
print(valor_formatado)