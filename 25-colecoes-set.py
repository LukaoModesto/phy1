# # set = conjunto
# # set funciona como uma lista desornada 
# # Não aceita valores duplicados
# # dados não podem ser alterados para outra dado
# # podemos incluir e excluir dados

# frutas = {'Maça','Laranja','Abacaxi','Maça'}

# print(frutas)
# print(type(frutas))

# frutas.add("Uva")
# frutas.remove('Maça')
# frutas.pop()


# print(frutas)

# outras_frutas = {'banana','Pera'}

# frutas.update(outras_frutas)

# print(frutas)

# frutas = {'Maça','Banana','Laranja','Tangerina'}
# frutas_citricas = {'Laranja','Limão','Tangerina'}

# todas_frutas = frutas.union(frutas_citricas)

# print(todas_frutas)

# frutas_comuns = frutas.intersection(frutas_citricas)

# print(frutas_comuns)

# Frozensets
# Usando Frozensets em sets
# Os frozensets pode ser usados dentro de sets, pois são imutáveis, o que significa que não podem se alterados apos a criação. Isso é importante para que o set principal mantenha a propriedade de elemento único.

grupo_estudante = {
    frozenset({"João","Maria"}),
    frozenset({"Romeu","Julieta"})
}

print(grupo_estudante)

grupo_estudante.add(frozenset({"Tiago","Fernanda"}))

print(grupo_estudante)


for grupo in grupo_estudante:
    print(f"Grupo: {grupo}")



# Operadores de conjunto

grupo_a = frozenset({"Diego","Jhenny"})
grupo_b = frozenset({"Maria",})


# União

uniao = grupo_a | grupo_b
print(uniao)

# Interseção 

intersecao = grupo_a & grupo_b
print(intersecao)


# Diferença

diferenca = grupo_b - grupo_a
print(diferenca)
