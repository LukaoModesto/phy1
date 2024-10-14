# Uma tupla (tuple) em Python é uma sequência imutável de valores de qualquer tipo

# coordenadas = (-49,200,-20,80,200)

# print(coordenadas)
# print(type(coordenadas))

# # coordenadas[2] = 100000
# # coordenadas.pop()

# print(coordenadas[2])
# print(coordenadas.count(200))

# print(len(coordenadas))


# coordenadas2 = (50,-30,-60,10)

# tupla_concatenada = coordenadas + coordenadas2

# print(tupla_concatenada)


# Popular tuplas com repetições


# tupla_repetida = ("Python",) * 5

# print(tupla_repetida)


# # print("testes", tupla_repetida)

# pessoas_lista = ['Diego','Jhenny','Nina','Mevis','Cleusa','Diego']
# print(pessoas_lista)
# pessoas_tupla = tuple(pessoas_lista)
# print(pessoas_tupla)

# print(type(pessoas_lista))
# print(type(pessoas_tupla))



pessoa = ('Diego', 20, 'Desenvolvedor')

print(pessoa[2])

nome, idade, profissao = pessoa


print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}")


tupla_aninhada = (
    ("Maça",1),
    ("Banana",2),
    ("Laranja",3)
)


print(tupla_aninhada[2][0])


