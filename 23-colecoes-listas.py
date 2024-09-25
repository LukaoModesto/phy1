pessoas = ['Diego','Jhenny','Nina','Mevis','Cleusa']
#             0       1       2       3
#             -4     -3      -2       -1

# print(type(pessoas))

# print(len(pessoas)) 

# print(pessoas[0]) # retorna um indice

# print(pessoas[-2]) # retorna um indice de traz para frente

# print(pessoas[1:]) # retorna a partir do indice

# print(pessoas[1:3]) # retorna a partir do indice 1 até o 4, excluido o 4

print(pessoas)
pessoas[2] = "Celeste" # altera o indice
print(pessoas)

pessoas.extend(['Mauro','Cleusa','Marina']) #função .extend inclui outra lista na lista atual 

print(pessoas)


pessoas.append('Charlie') # inclui um registro no final da lista

print(pessoas)

pessoas.insert(3, "Lucy") # inclui um registro, no indice indicado 
# primeiro argumento = indice
# segundo argumento = registro (dados)

print(pessoas)

pessoas.pop() # exclui o ultimo valor

print(pessoas)

pessoas.pop(4) # exclui o dado com o indice passado

print(pessoas)

pessoas.remove('Celeste') # exclui o dado com o valor passado

print(pessoas)

# pessoas.clear() # exclui a lista

print(pessoas.index('Cleusa')) # retorna em qual indice o registro está (Sendo o primeiro registro)

print(pessoas.count('Cleusa')) # conta quantos registro tem passo como argumento


#aaaaaa




# pessoas.sort()
# print(pessoas)
