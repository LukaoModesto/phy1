# Exercício 1: Criar um Dicionário
# Criando um dicionário para armazenar informações de um aluno
# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }
# Exibindo o dicionário
# Saida Dicionário do aluno: [aluno]


# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }

# print(f'Dicionário do aluno: {aluno}')

##################################################

# Exercício 2: Acessar Valores do Dicionário
# Acessando e exibindo o nome do aluno
# Saida: Nome do aluno: [aluno["nome"]]

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }

# print(f'Nome do aluno: {aluno["nome"]}')


##################################################

# Exercício 3: Adicionar um Novo Item ao Dicionário
# Adicionando a nota do aluno ao dicionário
# nota = 9.5
# Saida: Dicionário do aluno após adição: [aluno]

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }
# print(aluno)
# aluno['nota'] = 9.5
# print(aluno)


# print(f'Dicionário do aluno após adição: {aluno}')



##################################################

# Exercício 4: Atualizar um Valor no Dicionário
# Atualizando a idade do aluno (atualize idade para 21)
# Saida: Dicionário do aluno após atualização: [aluno]

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }
# print(aluno)
# aluno["idade"] = 21

# print(aluno)

# print(f'Dicionário do aluno após atualização: {aluno}')

##################################################

# Exercício 5: Remover um Item do Dicionário
# Remova a nota do aluno usando .pop() para remover 
# Exibindo o dicionário após a remoção
# Saida: Dicionário do aluno após remoção da nota: [aluno]

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }
# print(aluno)

# aluno['nota'] = 9.5

# print(aluno)

# aluno.pop('nota')

# print(aluno)

# print(f'Dicionário do aluno após remoção da nota: {aluno}')


##################################################

# Exercício 6: Verificar a Existência de uma Chave
# Verificando se a chave 'curso' existe no dicionário
# usando a condicional if e else
# Saida verdadeira: O aluno está matriculado em um curso.
# Saida falsa: O aluno não está matriculado em um curso.

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }

# if 'curso' in aluno:
#     print(f'O aluno está matriculado em um curso.')
# else:
#     print(f'O aluno não está matriculado em um curso.')


##################################################


# Exercício 8: Dicionário Aninhado
# Criando um dicionário aninhado para armazenar informações de alunos
# nome do dicionario = alunos
# aluno1 nome:João,idade:20
# aluno2 nome:Maria,idade:22
# Acessando o nome do segundo aluno
# Saida: Nome do segundo aluno: [alunos[?][?]]

# alunos = {
#     'aluno1':{
#         "nome": "João",
#         "idade": 20
#     },
#     'aluno2':{
#         "nome": "Maria",
#         "idade": 22
#     }
# }

# print(f'Nome do segundo aluno: {alunos['aluno2']["nome"]}')



##################################################
# Exercício 9: Criar um Dicionário a Partir de Listas
# lista 1: chaves = "nome", "idade", "curso"
# lista 2: valores = "Carlos", 23, "Matemática"
# Criar um dicionário a partir das listas usando dist() e o zip()
# Saida: Dicionário criado a partir de listas: [dicionario_aluno]

# chaves = ["nome", "idade", "curso"]
# valores = ["Carlos", 23, "Matemática"]


# dicionario_aluno = dict(zip(chaves,valores))

# print(dicionario_aluno)

##################################################

# Exercício 10: Obter o Tamanho do Dicionário
# Obtendo o tamanho do dicionário de alunos usando o len
# Saida: O tamanho do dicionário do aluno é: [tamanho_aluno]

# aluno = {
#     "nome": "João",
#     "idade": 20,
#     "curso": "Engenharia"
# }

# tamanho_aluno = len(aluno)

# print(f'O tamanho do dicionário do aluno é: {tamanho_aluno}')