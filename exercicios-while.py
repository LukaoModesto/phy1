# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.

## for c in range(1,10+1):


# c = 1

# while c <= 10:

#     print(c)

#     c += 1

#########################################################################

# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.


# contador = 1
# soma = 0
# while contador <= 100:

#     soma += contador

#     contador += 1

# print(f'soma = {soma}')



#########################################################################

# Exercício 3: Tabuada do 5
# Imprima a tabuada do 5.

# contador = 0
# while contador <= 10:
#     tabuada = 5 * contador
#     print(f'5 x {contador} = {tabuada}')
#     contador += 1
#     # contador = contador + 1

#########################################################################

# Exercício 4: Números Pares
# Imprima todos os números pares de 1 a 20.

# contador = 1
# while contador <= 20:
#     if contador % 2 == 0:
#         print(contador)
#     contador += 1


#########################################################################

# Exercício 5: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.

# contador = 1
# while contador <= 10:
#     calculo = contador ** 2
#     print(f'{contador}^2 = {calculo}')

#     contador += 1

#########################################################################

# Exercício 6: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.

# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1


#########################################################################

# Exercício 7: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.

# numero = 5
# contador = 1
# fatorial = 1

# while contador <= numero:

#     fatorial *= contador
   
#     contador += 1
  
# print(f'Fatorial de {numero} = {fatorial}')


#########################################################################

# Exercício 8: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.

# contador = 1
# while contador <= 20:
#     if contador % 2 != 0:
#         print(contador)
#     contador += 1

#########################################################################

# Exercício 9: Contar Vogais
# Conte e imprima o número de vogais em uma string.
# string = "Hello, World!"
# vogais = "aeiouAEIOU"

# string = "Hello, World!"
# vogais = "aeiouAEIOU"
# contador = 0
# indice = 0

# # print(string[7])
# # print(len(string))

# while indice < len(string): 
#     if string[indice] in vogais:
#         contador += 1
#     indice += 1

# print(f"Número de vogais: {contador}")       
    


#########################################################################

# Exercício 10: Gerenciador de Lista de Compras
# Peça ao usuário para adicionar itens à sua lista de compras até que ele digite "sair".
# Inicializa a lista de compras vazia 
# Loop para adicionar itens
# Exibe a lista de compras com o loop FOR

lista_compras = []

# print(type(lista_compras))

while True:
    item = input('Digite um item para a lista de compras (ou "sair" para finalizar): ')

    if item.upper() == 'SAIR':
        break

    lista_compras.append(item)

    print(lista_compras)
    
for i, item in enumerate(lista_compras, start=1):

    print(f'{i}: {item}')

