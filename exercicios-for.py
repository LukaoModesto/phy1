# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.

# for c in range(1, 10+1): ##[1,2,3,4,5,6,7,8,9,10]
    # print(c)

##########################################################################

# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.

# soma = 0

# for c in range(1, 100 + 1):
#     # print(c)
#     soma += c

# print(soma)

##########################################################################

# Exercício 3: Lista de Nomes
# Crie uma lista de nomes e imprima cada um deles.
# nomes = ["Alice", "Bob", "Carlos"]

# nomes = ["Alice", "Bob", "Carlos"]

# for nome in nomes:
#     print(nome)



##########################################################################

# Exercício 4: Tabuada do 5
# Imprima a tabuada do 5.


# for c in range(0, 10 + 1):
#     tabuada = 5 * c
#     print(f'5 x {c} = {tabuada}')


# numero = int(input('Digite um numero'))

# for c in range(0, 10 + 1):
#     tabuada = numero * c
#     print(f'{numero} x {c} = {tabuada}')


##########################################################################

# Exercício 5: Números Pares
# Imprima todos os números pares de 1 a 20.

# for c in range(1, 20 + 1):
#     if c % 2 == 0:
#         print(c)


##########################################################################

# Exercício 6: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.

# for c in range(1, 10 + 1):

#     calculo = c ** 2

#     print(f'{c}^2 = {calculo}')

##########################################################################

# Exercício 7: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.

# for c in range(10, 0, -1):
#     print(c)

##########################################################################

# Exercício 8: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.
# 5!=5×4×3×2×1=120
# 5!=1×2×3×4×5=120

# numero = 5
# fatorial = 1

# for c in range(1, numero + 1):
#     fatorial *= c


# print(f'Fatorial de {numero} = {fatorial}')


##########################################################################

# Exercício 9: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.

# for c in range(1, 20 + 1):
#     if c % 2 != 0:
#         print(c)


##########################################################################

# Exercício 10: Contar Vogais
# crie duas variaveis pra realizar o exercício
# string = "Hello, World!"
# vogais = "aeiouAEIOU"
# Conte e imprima o número de vogais em uma string.

string = "Hello, World!"
vogais = "aeiouAEIOU"

contador = 0

for letra in string:
    
    if letra in vogais:
        contador += 1

print(contador)


