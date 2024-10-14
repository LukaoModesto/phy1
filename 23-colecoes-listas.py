# pessoas = ['Diego','Jhenny','Nina','Mevis','Cleusa','Diego']
pessoas = ['Diego', 32]

nome, idade = pessoas

print(nome)
print(idade)

#             0       1       2       3        4       5
#             -5        -4     -3      -2       -1

# print(type(pessoas))

# print(len(pessoas)) 

# print(pessoas[0]) # retorna um indice

# print(pessoas[-2]) # retorna um indice de traz para frente

# print(pessoas[1:]) # retorna a partir do indice

# print(pessoas[:3]) # retorna a partir do indice

# print(pessoas[1:3]) # retorna a partir do indice 1 até o 4, excluido o 4

# print(pessoas[1:-1])


# print(pessoas)
pessoas[2] = "Celeste" # altera o indice
# print(pessoas)

# pessoas.extend(['Mauro','Cleusa','Marina']) #função .extend inclui outra lista na lista atual 

# print(pessoas)


pessoas.append('Charlie') # inclui um registro no final da lista

# print(pessoas)

pessoas.insert(3, "Lucy") # inclui um registro, no indice indicado 
# primeiro argumento = indice
# segundo argumento = registro (dados)

# print(pessoas)

# pessoas.pop() # exclui o ultimo valor

# print(pessoas)

# pessoas.pop(4) # exclui o dado com o indice passado

# print(pessoas)

# pessoas.remove('Celeste') 
# exclui o dado com o valor passado

# print(pessoas)

# pessoas.clear() # exclui a lista

# print(pessoas.index('Cleusa')) # retorna em qual indice o registro está (Sendo o primeiro registro)

# print(pessoas)

# print(pessoas.count('Charlie')) # conta quantos registro tem passo como argumento

# print(pessoas)





# print(pessoas)

# pessoas.sort() # função .sort() ordena a lista em ordem ascendente

# print(pessoas)


numeros = [33,25,60,10,20]



# print(numeros)

numeros.sort()

# print(numeros)

numeros.reverse()

# print(numeros)


pessoas2 = pessoas 

# print(pessoas)

# pessoas.remove('Lucy')

# print(pessoas2)



# pessoas3 = pessoas.copy()

# print(pessoas)
# print(pessoas2)
# print(pessoas3)

# pessoas3.remove('Lucy')

# print(pessoas)
# print(pessoas2)
# print(pessoas3)


# numeros = [3,1,4,1,5,9,2,6,5]

# maior_numero = max(numeros)
# menor_numero = min(numeros)

# print(maior_numero)
# print(menor_numero)

turma = [
    ["João" , 20 , "Desenvolvedor web"],
    ["Maria" , 22 , "Python"],
    ["Diego" , 32 , "PHP"]
]

print(turma[1][2])
print(turma[1][0])
print(turma[2][2])