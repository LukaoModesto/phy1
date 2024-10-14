meses = {
    1 : "Janeiro",
    2 : "Fevereiro",
    3 : "Março",
    4 : "Abril",
    5 : "Maio",
    6 : "Junho"
}

# print(meses)
# print(type(meses))

# print(meses[4])

meses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Abr" : "Abril",
    "Mai" : "Maio",
    "Jun" : "Junho"
}

# print(meses)
# print(type(meses))

# print(meses['Mai'])

# meses['Jun'] = 'JUNHO' # alterar
# meses['Jul'] = 'Julho' # adicionar

# print(meses)

# meses.pop("Jan")

# print(meses)



frutas = {
    'fruta1': {

        'nome' : 'Maça',
        'preco' : 5.60

    },
    'fruta2': {

        'nome' : 'Banana',
        'preco' : 10.10

    }
}



print(frutas)
print(type(frutas))

print(frutas['fruta1']['nome'])
print(frutas['fruta2']['preco'])


chaves = ['nome','idade','curso']
valores = ['Maria',23,'Python']

print(type(chaves))
print(type(valores))


pessoas = dict(zip(chaves,valores))

print(pessoas)


print(type(pessoas))

