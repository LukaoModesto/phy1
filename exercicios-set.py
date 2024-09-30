# Exercício 1: Criar um Conjunto
# Criando um conjunto chamado frutas = "maçã", "banana", "laranja"
# Saida Conjunto de frutas: [frutas]

# frutas = {"maçã", "banana", "laranja"}
# print(f'Conjunto de frutas: {frutas}')


# #############################################

# Exercício 2: Adicionar Elementos ao Conjunto
# Saida: Conjunto de frutas após adição: [frutas]

# frutas = {"maçã", "banana", "laranja"}
# frutas.add ('uva')
# print(frutas)
##########################################################

# Exercício 3: Remover Elementos do Conjunto
# Removendo uma fruta do conjunto usando remove
# Saida: Conjunto de frutas após remoção: [frutas]

# frutas = {"maçã", "banana", "laranja"}
# frutas.remove('maçã')
# print(frutas)

###############################################################33

# Exercício 4: Verificar a Existência de um Elemento
# Verificando se a fruta 'laranja' está no conjunto
# Use a condicional if e else
# Saida verdadeira A fruta 'laranja' está no conjunto.
# Saida Falsa A fruta 'laranja' está no conjunto.

# frutas = {"maçã", "banana", "laranja"}

# if "laranjas" in frutas:
#     print(f'a fruta \'laranja\' esta em frutas')
# else: print(f"a fruta \'laranja\' nao esta em frutas")

###########################################

# Exercício 5: Operações de União
# Criando outro conjunto de frutas 
# frutas_citricas = "laranja", "limão", "tangerina"
# Saida: Todas as frutas: [todas_as_frutas]

# frutas = {"maçã", "banana", "laranja"}
# frutas_citricas = {"laranja", "limão", "tangerina"}

# frutas_todas = frutas | frutas_citricas
# print(f'Todas as frutas: {list(frutas_todas)}')

###########################################

# Exercício 6: Operações de Interseção
# Criando um conjunto de frutas tropicais
# frutas_tropicais = "maçã", "banana", "coco"
# Encontrando a interseção entre os dois conjuntos usando .intersection 
# Saida Frutas comuns: [frutas_comuns]

# frutas = {"maçã", "banana", "laranja"}
# frutas_tropicais = {"maçã", "banana", "coco"}

# frutas_comuns = frutas.intersection(frutas_tropicais)
# print(frutas_comuns)
# ########################################################

# Exercício 7: Diferença de Conjuntos
# Crie um conjunto de frutas de inverno
# frutas_inverno = "kiwi", "maçã", "pêra"
# Encontrando a diferença entre 'frutas' e 'frutas_inverno' usando .difference
# Saida Frutas que não estão no inverno: [frutas_diferentes]

# frutas_inverno = {"kiwi", "maçã", "pêra"}
# frutas = {"maçã", "banana", "laranja"}

# diferenca = frutas.difference(frutas_inverno) | frutas_inverno.difference(frutas)
# print(diferenca)
######################################################################

# Exercício 8: Conjunto de Elementos Únicos
# Crie uma lista com frutas repetidas
# lista_frutas = "maçã", "banana", "laranja", "maçã", "uva", "banana"
# Convertendo a lista em um conjunto para obter elementos únicos, usando o set()
# Saida: Frutas únicas: [frutas_unicas]

# lista_frutas = {"maçã", "banana", "laranja", "maçã", "uva", "banana"}
# print(type(lista_frutas))
# frutas_unicas = set(lista_frutas)
# print(type(frutas_unicas))
# print(frutas_unicas)
# print(f'frutas unicas{frutas_unicas}')
################################################################

# Exercício 9: Tamanho do Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva"
# Obtendo o tamanho do conjunto de frutas, usando o len()
# Saida: O tamanho do conjunto de frutas é: [tamanho_frutas]

# frutas = {"maçã", "banana", "laranja", "maçã", "uva"}

# tamanho_frutas =len(frutas)
# print(tamanho_frutas)
# print(f'o tamanho do conjunto de frutas é: {tamanho_frutas}')
##############################################################

# Exercício 10: Limpar um Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva" 
# Limpando todos os elementos do conjunto, usando .clear()
# Saida: Conjunto de frutas após limpeza: frutas


frutas = {"maçã", "banana", "laranja", "maçã", "uva"}

frutas.clear()

print(f'Conjunto de frutas após limpeza: {frutas}')
