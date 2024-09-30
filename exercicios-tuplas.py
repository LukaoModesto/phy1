# Exercício 1: Criar e Exibir uma Tupla de cores "vermelho", "verde", "azul", "amarelo", "roxo"
# Saida: Tupla de cores: [cores]

#######################################

# Exercício 2: Acessar e Exibir Elementos da Tupla (acesse o primero e o último elemento)
# Saida 1: Primeira cor: [primeira_cor]
# Saida 2: Última cor: [ultima_cor]

# cores = ("vermelho", "verde", "azul", "amarelo", "roxo")

# primeira_cor = cores[0]
# ultima_cor = cores[-1]

# print(f"primeira cor: {primeira cor}")
# prit(f"ultima cor:{ultima_cor}")

#####################################################

# Exercício 3: Verificar a Existência de um Elemento 
# Verificando se a cor 'azul' está na tupla 'cores'
# usando as condicionais if e else 
# para verdadeiro: saida "A cor 'azul' está na tupla."
# para falso: saida "A cor 'azul' não está na tupla."

# cores = ("vermelho", "verde", "azul", "amarelo", "roxo")

# if "azul" in cores:
#     print("A cor azul esta na tupla")
# else :
#     print("a cor azul nao esta tupla")

##########################################

# Exercício 4: Contar Elementos e Encontrar o Índice
# Criando uma nova tupla chamada 'numeros' 1, 2, 3, 4, 5, 2, 3
# Contar quantas vezes o número 2 aparece na tupla, usando o .count()
# Encontrando o índice da primeira ocorrência do número 3, usuando o .index()
# Saida 1 : O número 2 aparece, [contagem_dois] vezes na tupla.
# Saida 2: O índice do primeiro número 3 é: [indice_tres]

# numeros = (1, 2, 3, 4, 5, 2, 3)

# contagem_dois = numeros.count(2)

# # print(f"O numero dois aparece {contagem_dois} vezes na tupla")
# indice_tres = numeros.index(3)
# print(f'o indice do primeiro numero 3 e: {indice_tres}')
# ##################################

# Exercício 5: Concatenar Tuplas
# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)

# saida "Tupla concatenada: [tupla_concatenada]

# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)

# tupla_concatenada = tupla1 + tupla2

# print(f"Tupla concatenada:{tupla_concatenada}")
       
##########################################
# Exercício 6: Repetir Elementos em uma Tupla
# Criando uma tupla com um elemento repetido 
# tupla = ("a")
# Saida: Tupla repetida: [tupla_repetida]

# tupla_repetida = ("a",) * 5

# print(tupla_repetida)
# ###########################################

# Exercício 7: Converter uma Lista em Tupla
# Criando uma lista de frutas
# lista_frutas = ["maçã", "banana", "laranja"]
# Converta a lista em uma tupla, usando o tuple()
# saida: Tupla de frutas: [tupla_frutas]

# lista_frutas = ["maçã", "banana", "laranja"]
# #print(type(lista_frutas))
# tupla_frutas = tuple(lista_frutas)
# # print(type(tupla_frutas))
# print(f"tupla frutas{tupla_frutas}")
################################

# Exercício 8: Desempacotar uma Tupla
# Criando uma tupla com informações de uma pessoa
# pessoa = ("João", 30, "Programador")
# Saida = Nome: [nome], Idade: [idade], Profissão: [profissao]

# pessoa = ("João", 30, "Programador")
# nome, idade, profissao  = pessoa
# print(f'nome: {nome}, Idade: {idade}, profissao: {profissao}')

#################################

# Exercício 9: Tuplas Aninhadas  ver
# Criando uma tupla com tuplas dentro
# tupla_aninhada = (("maçã", 1), ("banana", 2), ("laranja", 3))
# Acessando e exibindo o valor associado à 'banana'
# Saida: O valor da banana é [valor_banana] 

# tupla_aninhada = (("maçã", 1), ("banana", 2), ("laranja", 3))

# valor_banana = tupla_aninhada[2][1]
# print(valor_banana)
################################

# Exercício 10: Tamanho da Tupla
# Criando uma tupla de letras
# letras = ('a', 'b', 'c', 'd', 'e')
# saida = O tamanho da tupla é: [tamanho_tupla]

# letras = ('a', 'b,' 'c', 'd', 'e')
# tamanho_tupla = len(letras)
# print(f'o tamanho da tupla é {tamanho_tupla}')