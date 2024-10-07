# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.

# for i in range(1, 11):
#     print(i)

#########################################################################

# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.


# soma = 0
# numero = 1

# while numero <= 100:
#     soma += numero
#     numero += 1

# print(f"A soma dos números de 1 a 100 é: {soma}")


#########################################################################

# Exercício 3: Tabuada do 5
# Imprima a tabuada do 5.
# Tabuada do 5 usando while

# i = 1
# while i <= 10:
#     resultado = 5 * i
#     print(f"5 x {i} = {resultado}")
#     i += 1


#########################################################################

# Exercício 4: Números Pares
# Imprima todos os números pares de 1 a 20.

# i = 1
# while i <= 20:
#     if i % 2 == 0:  # Verifica se o número é par
#         print(i)
#     i += 1

#########################################################################

# Exercício 5: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.

# for i in range(1, 11):
#     quadrado = i ** 2
#     print(f"O quadrado de {i} é {quadrado}")

#########################################################################

# Exercício 6: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.


# i = 10
# while i > 0:
#     print(i)
#     i -= 1


#########################################################################

# Exercício 7: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.

# numero = 5
# fatorial = 1
# i = 1

# while i <= numero:
#     fatorial *= i
#     i += 1

# print(f"O fatorial de {numero} é {fatorial}")


#########################################################################

# Exercício 8: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.

# i = 1
# while i <= 20:
#     if i % 2 != 0:  # Verifica se o número é ímpar
#         print(i)
#     i += 1


#########################################################################

# Exercício 9: Contar Vogais
# Conte e imprima o número de vogais em uma string.
# string = "Hello, World!"
# vogais = "aeiouAEIOU"

# string = "Hello, World!"
# vogais = "aeiouAEIOU"


# contador = 0
# i = 0


# while i < len(string):
#     if string[i] in vogais:
#         contador += 1
#     i += 1

# # Imprimir o resultado
# print(f"O número de vogais na string é: {contador}")



#########################################################################

# Exercício 10: Gerenciador de Lista de Compras
# Peça ao usuário para adicionar itens à sua lista de compras até que ele digite "sair".
# Inicializa a lista de compras vazia 
# Loop para adicionar itens
# Exibe a lista de compras com o loop FOR

lista_compras = []

while True:
    item = input('Digite um item da lista de compras (ou "sair" pra finalizar)')
    if item.upper() == 'SAIR':
        break
    lista_compras.append(item)

    print(lista_compras)

for i, item in enumerate(lista_compras, start=1):
    print(f'{i}: {item}')