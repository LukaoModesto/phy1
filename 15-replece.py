numero = float(input("Digite um valor em moeda: "))

print(numero)


numero_formatado = f"{numero:,.2f}".replace('.','X').replace(',','.').replace('X',',')

print(f"R$ {numero_formatado}")