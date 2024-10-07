frutas = ['maça', 'uva', 'laranja', 'banana']

#print(frutas)

# for fruta in frutas:
# for indice, fruta in enumerate(frutas,start=1):
#     print(indice)
#     print(fruta)

lista_frutas_list = list(enumerate(frutas))
lista_frutas_tupla = tuple(enumerate(frutas))
lista_frutas_set = set(enumerate(frutas))
lista_frutas_dict = dict(enumerate(frutas))

print(lista_frutas_list)
print(lista_frutas_tupla)
print(lista_frutas_set)
print(lista_frutas_dict)