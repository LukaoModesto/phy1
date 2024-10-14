lista_letras = ['A','B','C']

contador = 0

while contador < 5:
    print(f'Repetição: {contador}')
    contador += 1

    for letra in lista_letras:
        print(letra)

    # contador = contador + 1

print('fim')