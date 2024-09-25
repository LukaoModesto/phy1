frutas = {"Maça", "laranja", "Abacaxi", "Maça"}

frutas.add("Uva") #adicionamos a UVA

frutas.pop()

outras_frutas = ('banana', 'pera')
#frutas.remove("Maça") #removemos a Maça
frutas.update(outras_frutas)

frutas = {"Maça", "Laranja", "Banana"}
Frutas_citricas = ('Laranja', 'Limao', 'Tangerina')

todas_frutas = frutas.union(Frutas_citricas)

frutas_comuns = frutas.intersection(Frutas_citricas)
#print(frutas_comuns)

#frozensets
#Usando frozensets em sets
#Os frozensets pode ser usado dentro de sets, pois sao imutaveis, o significa que nao podem ser alteradis apos a criaçao;
#Isso é importante para que o set principal mantenha a propriedade de elemento unico.

grupo_estudante = {
    frozenset({"Joao","Maria"}),
    frozenset({"Romeu","Julieta"})
}

#print(grupo_estudante)
grupo_estudante.add(frozenset({"Tiago","Fernanda"}))

#for grupo in grupo_estudante:
    #print(f"Grupo: {grupo}")


#Operadores de conjunto
grupo_a = frozenset({"Diego", "Jhenny"})
grupo_b = frozenset({"Maria"})

#Uniao

uniao = grupo_a | grupo_b
#print(uniao)

#interseçao

intersecao = grupo_a & grupo_b
print(intersecao)
